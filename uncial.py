#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unicodedata


def convert_letter(let):
    if let == u'ς':
        return u'Σ'
    ii = ord(let)
    if ii >= 913 and ii <= 937:
        return let
    if ii >= 945 and ii <= 969:
        return unichr(ord(let) - 32)
    if ii == 0x0345:
        return u'Ι'
    return ''


def convert_line(line):
    line = unicodedata.normalize('NFD', line)
    output = ''
    for ll in line:
        let = convert_letter(ll)
        output += let
    return output


def convert_input():
    output = u''
    for line in sys.stdin:
        output += convert_line(unicode(line, 'UTF-8')) + "\n"
    return output


def main():
    print convert_input().encode('utf-8')


if __name__ == '__main__':
    main()
