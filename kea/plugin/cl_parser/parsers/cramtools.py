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


__version__ = (2014, 12, 11, 16, 18, 27, 3)

__all__ = [
    'cramtoolsParser',
    'cramtoolsSemantics',
    'main'
]


class cramtoolsParser(Parser):
    def __init__(self, whitespace=None, nameguard=True, **kwargs):
        super(cramtoolsParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            **kwargs
        )

    @graken()
    def _start_(self):
        with self._group():
            self._token('cramtools')

            def block0():
                with self._choice():
                    with self._option():
                        with self._group():
                            self._token('cram')

                            def block1():
                                with self._choice():
                                    with self._option():
                                        with self._group():
                                            self._token('--capture-tags')
                                            self._pattern(r'.[QC]+.')
                                    with self._option():
                                        self._token('--capture-all-tags')
                                    with self._option():
                                        self._token('--encrypt')
                                    with self._option():
                                        with self._group():
                                            self._token('-I')
                                            self._pattern(r'.*.bam')
                                            self.ast['input'] = self.last_node
                                    self._error('expecting one of: --capture-all-tags --capture-tags --encrypt -I')
                            self._closure(block1)
                    with self._option():
                        with self._group():
                            self._token('bam')

                            def block4():
                                with self._choice():
                                    with self._option():
                                        with self._group():
                                            with self._choice():
                                                with self._option():
                                                    self._token('--password')
                                                with self._option():
                                                    self._token('-p')
                                                self._error('expecting one of: --password -p')
                                    with self._option():
                                        with self._group():
                                            with self._group():
                                                with self._choice():
                                                    with self._option():
                                                        self._token('-f')
                                                    with self._option():
                                                        self._token('-required-flags')
                                                    self._error('expecting one of: -f -required-flags')
                                            self._token('re#\\w+')
                                    self._error('expecting one of: --password -f -p -required-flags')
                            self._closure(block4)
                    with self._option():
                        pass
                    self._error('expecting one of: bam cram')
            self._closure(block0)
            self._check_eof()

        self.ast._define(
            ['input'],
            []
        )


class cramtoolsSemantics(object):
    def start(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = cramtoolsParser(parseinfo=False)
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
            for r in cramtoolsParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for cramtools.")
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

