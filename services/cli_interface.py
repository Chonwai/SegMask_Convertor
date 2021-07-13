#!/usr/bin/env python

import sys
import argparse

from .annotation2mask import annotation2mask

def annotation_2_mask_action(command_parser):
    parser = command_parser.add_parser('annotation_2_mask')
    parser.add_argument("--annotations_path", type=str,
                        required=True, help='Please enter the annotations path.')
    parser.add_argument("--images_path", type=str,
                        required=True, help='Please enter the images path.')
    parser.add_argument("--result_path", type=str,
                        required=True, help='Please enter the result path.')

    def action(args):
        annotation2mask(args.annotations_path,
                        args.images_path, args.result_path)

    parser.set_defaults(func=action)


def main():
    assert len(sys.argv) >= 2, \
        "python convertor.py annotation2mask <arguments>"

    main_parser = argparse.ArgumentParser()
    command_parser = main_parser.add_subparsers()

    # Add individual commands
    annotation_2_mask_action(command_parser)

    args = main_parser.parse_args()

    args.func(args)
