#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

import sys

from emmorph2ud.converter import EmMorph2UD


def main():
    conv = EmMorph2UD()
    # print('TEST:', conv.process_sentence([['veszeget', 'vesz', '[/V][_Freq/V][Prs.NDef.3Sg]']], [0, 1, 2]))
    for line in sys.stdin:
        token, lemma, elemzes = line.strip().split('\t')[:3]
        univpos, univfeature = conv.parse(token, lemma, elemzes)
        print(token, lemma, elemzes, univpos, univfeature, sep='\t')


if __name__ == '__main__':
    main()
