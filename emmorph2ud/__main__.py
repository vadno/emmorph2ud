#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

from xtsv import build_pipeline, parser_skeleton


def main():

    argparser = parser_skeleton(description='emmorph2ud - a script converts the output tag of emMorph morphological'
                                            ' analyzer to the corresponding output tag of magyarlanc 3.0')
    opts = argparser.parse_args()

    # Set input and output iterators...
    if opts.input_text is not None:
        input_data = opts.input_text
    else:
        input_data = opts.input_stream
    output_iterator = opts.output_stream

    # Set the tagger name as in the tools dictionary
    used_tools = ['emmorph2ud']
    presets = []

    # Init and run the module as it were in xtsv

    # The relevant part of config.py
    # from emdummy import DummyTagger
    em_morph2ud = ('emmorph2ud', 'EmMorph2UD', 'emmorph2ud', (),
                   {'source_fields': {'form', 'lemma', 'xpostag'}, 'target_fields': ['upostag', 'feats']})
    tools = [(em_morph2ud, ('conv-morph', 'emmorph2ud'))]

    # Run the pipeline on input and write result to the output...
    output_iterator.writelines(build_pipeline(input_data, used_tools, tools, presets))


if __name__ == '__main__':
    main()
