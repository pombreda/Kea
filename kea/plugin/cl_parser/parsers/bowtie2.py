#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import graken, Parser


__version__ = (2015, 1, 2, 20, 53, 46, 4)

__all__ = [
    'bowtie2Parser',
    'bowtie2Semantics',
    'main'
]


class bowtie2Parser(Parser):
    def __init__(self, whitespace='', nameguard=True, **kwargs):
        super(bowtie2Parser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            **kwargs
        )

    @graken()
    def _start_(self):
        with self._choice():
            with self._option():
                self._bowtie2_()
            with self._option():
                self._bowtie2_00_()
            with self._option():
                self._bowtie2_01_()
            with self._option():
                self._bowtie2_02_()
            with self._option():
                self._bowtie2_03_()
            with self._option():
                self._bowtie2_04_()
            self._error('no available options')

    @graken()
    def _bowtie2_(self):
        self._token('bowtie2')
        self._check_eof()

    @graken()
    def _bowtie2_00_(self):
        self._token('bowtie2')

        def block0():
            self._pattern(r'\s+')
            self._bowtieoptions_()
        self._closure(block0)
        self._pattern(r'\s+')
        self._token('-x')
        self._pattern(r'\s+')
        self._database_()
        self._pattern(r'\s+')
        self._token('-1')
        self._pattern(r'\s+')
        self._forward_reads_()
        self._pattern(r'\s+')
        self._token('-2')
        self._pattern(r'\s+')
        self._reverse_reads_()
        self._pattern(r'\s+')
        self._token('-S')
        self._pattern(r'\s+')
        self._samout_()
        self._check_eof()

    @graken()
    def _bowtie2_01_(self):
        self._token('bowtie2')

        def block0():
            self._pattern(r'\s+')
            self._bowtieoptions_()
        self._closure(block0)
        self._pattern(r'\s+')
        self._token('-x')
        self._pattern(r'\s+')
        self._database_()
        self._pattern(r'\s+')
        self._token('-1')
        self._pattern(r'\s+')
        self._forward_reads_()
        self._pattern(r'\s+')
        self._token('-2')
        self._pattern(r'\s+')
        self._reverse_reads_()
        self._check_eof()

    @graken()
    def _bowtie2_02_(self):
        self._token('bowtie2')

        def block0():
            self._pattern(r'\s+')
            self._bowtieoptions_()
        self._closure(block0)
        self._pattern(r'\s+')
        self._token('-x')
        self._pattern(r'\s+')
        self._database_()
        self._pattern(r'\s+')
        self._token('-U')
        self._pattern(r'\s+')
        self._reads_()
        self._pattern(r'\s+')
        self._token('-S')
        self._pattern(r'\s+')
        self._samout_()
        self._check_eof()

    @graken()
    def _bowtie2_03_(self):
        self._token('bowtie2')

        def block0():
            self._pattern(r'\s+')
            self._bowtieoptions_()
        self._closure(block0)
        self._pattern(r'\s+')
        self._token('-x')
        self._pattern(r'\s+')
        self._database_()
        self._pattern(r'\s+')
        self._token('-U')
        self._pattern(r'\s+')
        self._reads_()
        self._check_eof()

    @graken()
    def _bowtie2_04_(self):
        self._token('bowtie2')
        self._check_eof()

    @graken()
    def _samout_(self):
        self._pattern(r'\S+')
        self.ast.setlist('samout', self.last_node)

        self.ast._define(
            [],
            ['samout']
        )

    @graken()
    def _forward_reads_(self):
        self._pattern(r'\S+')
        self.ast.setlist('forward_reads', self.last_node)

        self.ast._define(
            [],
            ['forward_reads']
        )

    @graken()
    def _reverse_reads_(self):
        self._pattern(r'\S+')
        self.ast.setlist('reverse_reads', self.last_node)

        self.ast._define(
            [],
            ['reverse_reads']
        )

    @graken()
    def _reads_(self):
        self._pattern(r'\S+')
        self.ast.setlist('reads', self.last_node)

        self.ast._define(
            [],
            ['reads']
        )

    @graken()
    def _database_(self):
        self._pattern(r'\S+')
        self.ast.setlist('database', self.last_node)

        self.ast._define(
            [],
            ['database']
        )

    @graken()
    def _bowtieoptions_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._bowtieoptions_flag_()
                with self._option():
                    self._token('--qseq')
                with self._option():
                    self._token('-s')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--skip')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-u')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--upto')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-5')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--trim5')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-3')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--trim3')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--phred33')
                with self._option():
                    self._token('--phred64')
                with self._option():
                    self._token('--int-quals')
                with self._option():
                    self._token('--very-fast')
                with self._option():
                    self._token('--fast')
                with self._option():
                    self._token('--sensitive')
                with self._option():
                    self._token('--very-sensitive')
                with self._option():
                    self._token('--very-fast-local')
                with self._option():
                    self._token('--fast-local')
                with self._option():
                    self._token('--sensitive-local')
                with self._option():
                    self._token('--very-sensitive-local')
                with self._option():
                    self._token('-N')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-L')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-i')
                    self._pattern(r'\s+')
                    self._str_()
                with self._option():
                    self._token('--n-ceil')
                    self._pattern(r'\s+')
                    self._str_()
                with self._option():
                    self._token('--dpad')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--gbar')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--ignore-quals')
                with self._option():
                    self._token('--nofw')
                with self._option():
                    self._token('--norc')
                with self._option():
                    self._token('--no-1mm-upfront')
                with self._option():
                    self._token('--end-to-end')
                with self._option():
                    self._token('--local')
                with self._option():
                    self._token('--ma')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--mp')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--np')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--rdg')
                    self._pattern(r'\s+')
                    self._twoints_()
                with self._option():
                    self._token('--rfg')
                    self._pattern(r'\s+')
                    self._twoints_()
                with self._option():
                    self._token('--score-min')
                    self._pattern(r'\s+')
                    self._str_()
                with self._option():
                    self._token('-k')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--all')
                with self._option():
                    self._token('-D')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-R')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-I')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--minins')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('-X')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--maxins')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--fr')
                with self._option():
                    self._token('--rf')
                with self._option():
                    self._token('--ff')
                with self._option():
                    self._token('--no-mixed')
                with self._option():
                    self._token('--no-discordant')
                with self._option():
                    self._token('--no-dovetail')
                with self._option():
                    self._token('--no-contain')
                with self._option():
                    self._token('--no-overlap')
                with self._option():
                    self._token('--time')
                with self._option():
                    self._token('--un')
                    self._pattern(r'\s+')
                    self._path_()
                with self._option():
                    self._token('--al')
                    self._pattern(r'\s+')
                    self._path_()
                with self._option():
                    self._token('--un-conc')
                    self._pattern(r'\s+')
                    self._path_()
                with self._option():
                    self._token('--al-conc')
                    self._pattern(r'\s+')
                    self._path_()
                with self._option():
                    self._token('--un-gz')
                    self._pattern(r'\s+')
                    self._path_()
                with self._option():
                    self._token('--quiet')
                with self._option():
                    self._token('--met-file')
                    self._pattern(r'\s+')
                    self._file_()
                with self._option():
                    self._token('--met-stderr')
                with self._option():
                    self._token('--met')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--no-unal')
                with self._option():
                    self._token('--no-head')
                with self._option():
                    self._token('--no-sq')
                with self._option():
                    self._token('--rg-id')
                    self._pattern(r'\s+')
                    self._str_()
                with self._option():
                    self._token('--rg')
                    self._pattern(r'\s+')
                    self._str_()
                with self._option():
                    self._token('--omit-sec-seq')
                with self._option():
                    self._token('-p')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--threads')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--reorder')
                with self._option():
                    self._token('--mm')
                with self._option():
                    self._token('--qc-filter')
                with self._option():
                    self._token('--seed')
                    self._pattern(r'\s+')
                    self._int_()
                with self._option():
                    self._token('--non-deterministic')
                with self._option():
                    self._token('--version')
                with self._option():
                    self._token('--help')
                self._error('expecting one of: --all --end-to-end --fast --fast-local --ff --fr --help --ignore-quals --int-quals --local --met-stderr --mm --no-1mm-upfront --no-contain --no-discordant --no-dovetail --no-head --no-mixed --no-overlap --no-sq --no-unal --nofw --non-deterministic --norc --omit-sec-seq --phred33 --phred64 --qc-filter --qseq --quiet --reorder --rf --sensitive --sensitive-local --time --version --very-fast --very-fast-local --very-sensitive --very-sensitive-local')

    @graken()
    def _bowtieoptions_flag_(self):
        self._token('-')

        def block0():
            with self._choice():
                with self._option():
                    self._token('q')
                with self._option():
                    self._token('f')
                with self._option():
                    self._token('r')
                with self._option():
                    self._token('c')
                with self._option():
                    self._token('a')
                with self._option():
                    self._token('t')
                with self._option():
                    self._token('h')
                self._error('expecting one of: a c f h q r t')
        self._positive_closure(block0)

    @graken()
    def _twoints_(self):
        self._pattern(r'[0-9]+,[0-9]')
        self.ast.setlist('twoints', self.last_node)

        self.ast._define(
            [],
            ['twoints']
        )

    @graken()
    def _file_(self):
        self._pattern(r'\S+')

    @graken()
    def _path_(self):
        self._file_()

    @graken()
    def _int_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _integer_(self):
        self._int_()

    @graken()
    def _float_(self):
        self._pattern(r'[0-9\.]+')

    @graken()
    def _string_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._pattern(r'"[^"]*"')
                with self._option():
                    self._pattern(r"'[^']*'")
                with self._option():
                    self._pattern(r'\S+')
                self._error('expecting one of: "[^"]*" \'[^\']*\' \\S+')

    @graken()
    def _str_(self):
        self._string_()


class bowtie2Semantics(object):
    def start(self, ast):
        return ast

    def bowtie2(self, ast):
        return ast

    def bowtie2_00(self, ast):
        return ast

    def bowtie2_01(self, ast):
        return ast

    def bowtie2_02(self, ast):
        return ast

    def bowtie2_03(self, ast):
        return ast

    def bowtie2_04(self, ast):
        return ast

    def samout(self, ast):
        return ast

    def forward_reads(self, ast):
        return ast

    def reverse_reads(self, ast):
        return ast

    def reads(self, ast):
        return ast

    def database(self, ast):
        return ast

    def bowtieoptions(self, ast):
        return ast

    def bowtieoptions_flag(self, ast):
        return ast

    def twoints(self, ast):
        return ast

    def file(self, ast):
        return ast

    def path(self, ast):
        return ast

    def int(self, ast):
        return ast

    def integer(self, ast):
        return ast

    def float(self, ast):
        return ast

    def string(self, ast):
        return ast

    def str(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = bowtie2Parser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in bowtie2Parser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for bowtie2.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )
