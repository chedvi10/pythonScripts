import argparse
import shutil
import pathlib
parser = argparse.ArgumentParser()
parser.add_argument('old', type=str, help="the folder of files to remove")
parser.add_argument('ending', type=str, help="type of files to remove")
parser.add_argument('new', type=str, help="the folder to put the files")

args = parser.parse_args()
path = pathlib.Path(args.old)
for file in path.rglob(f"*.{args.ending}"):
    shutil.copy(file, args.new)