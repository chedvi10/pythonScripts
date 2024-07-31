# File Management Utility Scripts

This README explains how to use the following three scripts:

1. changeText.py
2. changeFileName.py
3. copyFiles.py

## changeText.py

This script replaces an old string with a new string in all files within a specified directory and its subdirectories.

Usage:
python changeText.py `<path>` `<old_string>` `<new_string>`

- `<path>`: The path to the directory where the replacement should be performed
- `<old_string>`: The string to be replaced
- `<new_string>`: The new string that will replace the old one

## changeFileName.py

This script changes the name of a file (without changing its extension) to a new name.

Usage:
python changeFileName.py `<file_path>` `<new_name>`

- `<file_path>`: The full path to the file to be renamed
- `<new_name>`: The new name to be given to the file (without extension)

## copyFiles.py

This script copies files of a specific type from one directory to another.

Usage:
python copyFiles.py `<source_directory>` `<file_extension>` `<destination_directory>`

- `<source_directory>`: The path to the directory from which to copy the files
- `<file_extension>`: The type of files to copy (e.g., txt, pdf, jpg)
- `<destination_directory>`: The path to the directory where the files should be copied

Note: Run these scripts with Python 3 and ensure all required libraries are installed.