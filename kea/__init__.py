
# kea runner

import argparse
import logging
import os
import subprocess as sp
import sys

import leip
import fantail

import mad2.util as mad2util

lg = logging.getLogger(__name__)
#lg.setLevel(logging.DEBUG)

conf = leip.get_config('kea')

#leiplog = logging.getLogger('leip')
#leiplog.setLevel(logging.DEBUG)


class Kea(leip.app):

    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            name = os.path.split(sys.argv[0])[1]
            if name[:3] == 'kea_':
                name = name[3:]

        # Call Leip - we do not need the Leip argparser:
        super(Kea, self).__init__('kea', disable_commands=True)

        # hack - if kea verbose is set - do that early:
        verbose_flag = self.conf['arg_prefix'] + '-v'
        if verbose_flag in sys.argv:
            lg.setLevel(logging.DEBUG)

        lg.debug("start kea initialization")

        # different hooks!
        self.hook_order = [
            'pre_argparse',
            'argparse',
            'post_argparse',
            'prepare',
            'pre_run',
            'run',
            'post_run',
            'finish']

        # for the kea argparse (starting with app.conf.arg_prefix)
        # default prefix = '---'
        # need to define how many arguments are taken from the command
        # line for each flag - the rest is handled by argparse
        self.kea_arg_harvest_extra = {}
        self.kea_argparse = argparse.ArgumentParser(
            prog='(kea){}'.format(name),
            description='Kea wrapper for: {}'.format(name),
            epilog='NOTE: Prefix all Kea arguments with: "' +
            self.conf['arg_prefix'] + '"')

        self._madapp = None  # hold the Leip Mad Application

        self.conf['appname'] = name
        self.discover(globals())

    @property
    def madapp(self):
        if not self._madapp is None:
            return self._madapp

        self._madapp = leip.app('mad2', disable_commands=True)
        return self._madapp

    def get_madfile(self, filename):
        return mad2util.get_mad_file(self.madapp, filename)


@leip.hook('pre_argparse')
def main_arg_define(app):
    app.kea_arg_harvest_extra['v'] = 0
    app.kea_arg_harvest_extra['e'] = 0
    app.kea_arg_harvest_extra['j'] = 1
    app.kea_arg_harvest_extra['h'] = 0
    app.kea_argparse.add_argument('-v', '--verbose', action='store_true')
    app.kea_argparse.add_argument('-e', '--command_echo', action='store_true',
                                  help='echo Kea commands to stdout')
    app.kea_argparse.add_argument('-j', '--threads', type=int,
                                  help='kea threads to use (if applicable)')


@leip.hook('argparse')
def kea_argparse(app):
    """
    Separate Kea arguments from tool arguments & feed the kea arguments
    to argparse
    """
    prefix = app.conf['arg_prefix']
    prelen = len(prefix)
    new_sysargv = []
    kea_argv = []
    i = 0
    while i < len(sys.argv):
        a = sys.argv[i]

        if a.startswith(prefix + '-'):
            flag = a[prelen + 1:]
            kea_argv.append('-' + flag)
            harvest_no = app.kea_arg_harvest_extra.get(flag, 0)
            if harvest_no > 0:
                harvest = sys.argv[i + 1:i + 1 + harvest_no]
                kea_argv.extend(harvest)
                i += harvest_no
        else:
            new_sysargv.append(a)

        i += 1

    app.kea_args = app.kea_argparse.parse_args(kea_argv)
    lg.debug("kea args: {}".format(" ".join(kea_argv)))
    lg.debug("com args: {}".format(" ".join(new_sysargv)))
    lg.debug("kea argparse: {}".format(str(app.kea_args)))
    sys.argv = new_sysargv


@leip.hook('post_argparse')
def main_arg_process(app):
    """
    Process parsed arguments
    """
    if app.kea_args.verbose:
        lg.setLevel(logging.DEBUG)
    if app.kea_args.command_echo:
        app.conf['command_echo'] = True
    app.conf['threads'] = app.kea_args.threads



@leip.hook('run')
def run_kea(app):
    lg.debug("Start Kea run")
    cl = [app.conf['executable']] + sys.argv[1:]
    lg.debug("command line: %s", " ".join(cl))

    if app.conf.get('command_echo'):
        print " ".join(cl)

    app.conf['cl'] = cl
    sp.Popen(cl).communicate()


@leip.hook('prepare', 10)
def prepare_config(app):

    lg.debug("prepare tool configuration")
    data = fantail.Fantail()

    appdata = app.conf['app'].get(app.conf['appname'], {})

    defdata = app.conf.get('group.default')

    group = app.conf.get('group', appdata.get('group'))
    grpdata = {}
    if group:
        grpdata = app.conf['group.{}'.format(group)]

    if defdata:
        data.update(defdata)
    if grpdata:
        data.update(grpdata)
    if appdata:
        data.update(appdata)

    app.conf.backfill(data)

    lg.debug("Found config: %s/%s", group, app.conf['appname'])


@leip.hook('prepare')
def find_executable(app):

    lg.debug("find executable location")

    if 'executable' in app.conf:
        return

    this = sys.argv[0]
    P = sp.Popen(['which', '-a', app.conf['appname']], stdout=sp.PIPE)
    out, err = P.communicate()
    for line in out.strip().split("\n"):
        if os.path.samefile(line, this):
            # this is the called executable wrapper - ignore
            continue
        else:
            app.conf['executable'] = line.strip()