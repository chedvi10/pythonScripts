import argparse
from pathlib import Path


parser = argparse.ArgumentParser('replace old str to new str')
parser.add_argument('path', type = str, help='path to replace str')
parser.add_argument('old', type = str, help='str to change')
parser.add_argument('new',type = str, help ='new str')

args = parser.parse_args()
file_to_change = Path(args.path)
for file_path  in file_to_change.rglob('*'):
    if file_path .is_file():
        with open(file_path , 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file_write:
            for line in lines:
                new_line = line.replace(args.old, args.new)
                file_write.write(new_line)


