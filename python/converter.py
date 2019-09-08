#!/usr/bin/env python3
"""
Ad2A3
Adobe Xd to Arma 3 UI Config Converter
This tool converts Adobe Xd SVG exports into ArmA3 UI configurations
"""
import argparse
import os
import logging
from pathlib import Path

PARSER = argparse.ArgumentParser(prog='Ad2A3 v0.0.1', description='This tool converts Adobe Xd SVG exports into ArmA3 UI configurations',
                                 epilog="<Epilog Missing>")
# PARSER.add_argument('tag', help='the tag of your mod')
# PARSER.add_argument('addon', help='the addon the function should be created for')
# PARSER.add_argument('name', help='name of the function (without fn prefix)')
# PARSER.add_argument('category', nargs="?", default="functions",
#                     help='the category where the function is defined')
# PARSER.add_argument('-v', '--verbose', dest='verbose', action='store_true',
#                     help='prints log messages to follow the process')
# PARSER.add_argument('-t', '--template', dest='template', action='store_true',
#                     help='uses a template for creating function files')
# PARSER.add_argument('-d', '--dry-run', dest='dryrun', action='store_true',
#                     help='performs a dry run without changing any files')
# PARSER.add_argument('-o', '--overwrite', dest='overwrite', action='store_true',
#                     help='overwrites existing function entry and file')

ARGS = PARSER.parse_args()

