import os
import sys
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
parser.add_argument('new_name', type=str)
args = parser.parse_args()
nameFile=pathlib.Path(args.path)
nameFile.rename(nameFile.with_stem(args.new_name))
