#!/usr/bin/env python

import sys
import os
import datetime
import pathlib

rules = {
    # replace key with val
    "-": " ",
    "_": " ",
    "GMT20": "",
    "Recording": "",
}


class termcolor:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def applyRules(s, trim=True):
    for key, value in rules.items():
        s = s.replace(key, value)
    if trim:
        s = " ".join(s.strip().split())
    return s


def run():
    for file in sys.argv[1:]:
        normalized_path = os.path.abspath(file)
        if not pathlib.Path(normalized_path).exists():
            print(termcolor.FAIL + "× " + termcolor.ENDC + normalized_path)
            continue
        basename = os.path.basename(normalized_path)
        dirname = os.path.dirname(normalized_path)
        newname = applyRules(basename)
        print(
            termcolor.OKGREEN
            + "✓ "
            + termcolor.ENDC
            + dirname
            + "/"
            + termcolor.OKGREEN
            + newname
            + termcolor.ENDC
        )
        os.rename(normalized_path, dirname + "/" + newname)
