"""
Standard library.
"""

import glob
import os
import sys


def main():
    """
    Docstring.
    Explain about functions.
    """

    print(main.__doc__)
    # About print().
    print_fmt()
    # Get paths, directory names and file names.
    path_get()
    # Create, rename, remove files and directories.
    path_ctrl()
    # Write to files.
    write()
    # Read files.
    read()


def path_get():

    # Get the current directory.
    dir_path = os.getcwd()

    # Get folders and files in the directory.
    file_names = os.listdir(dir_path)

    # Get names from a path.
    path = input('dir_path -> ')
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)

    # Split the path to the directory and the file.
    dir_path, file_name = os.path.split(path)

    # Separate to the file_path and the extension.
    file_path = input('file_path -> ')
    path_without_ext, ext = os.path.splitext(file_path)

    # Find files under the directory.
    dir_path = input('dir_path -> ')
    ext = '*.py'
    file_names = glob.glob(os.path.join(path, '**', ext), recursive=True)

    # Check existance.
    dir_path = input('dir_path -> ')
    print(os.path.isdir(dir_path))
    file_path = input('file_path -> ')
    print(os.path.isfile(file_path))
    path = input('path -> ')
    print(os.path.exists(path))

    # Convert to the absolute path.
    path = 'dir'
    abs_path = os.path.abspath(path)

    # Join paths.
    dir_path = 'directory'
    file_name = 'file'
    file_path = os.path.join(dir_path, file_name)


def path_cntr():

    # Make a directory.
    dir_path = 'test_dir'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        #os.makedirs(dir_path) # Recursivery.

    # Rename.
    before = 'test_dir'
    after = 'test_dir_rename'
    if os.path.exists(before):
        os.rename(before, after)
        #os.renames(before, after) # Recursivery.

    # Remove.
    dir_path = after
    if os.path.exists(dir_path):
        os.removedirs(dir_path)

    file_path = input('file_path -> ')
    if os.path.exists(file_path):
        os.remove(file_path)

    # Move to the directory.
    dir_path = input('dir_path -> ')
    if os.path.exists(dir_path):
        os.chdir(dir_path)


def write():

    data = ['Good morning',
            'Good afternoon',
            'Good evening',
            'Good bye',
            'Good night',
            ]

    file_path = os.path.abspath(__file__)
    file_path = os.path.dirname(file_path)
    file_path = os.path.join(file_path, 'test.txt')
    enc = 'utf-8'
    with open(file_path, mode='w', encoding=enc) as f:
        # Method 1.
        f.write('\n'.join(data))
        f.write('\n') # Add a newline in the end of line.
        # Method 2.
        for i in data:
            f.write(i)
            f.write('\n')
        # Method 3.
        f.writelines('\n'.join(data))
        f.write('\n') # Add a newline in the end of line.
        # Method 4.
        for i in data: f.writelines([i, '\n'])


def read():

    file_path = input('file_path -> ')
    enc = 'utf-8'
    with open(file_path, encoding=enc) as f:
        data = f.readlines()
    # Delete whitespaces(spaces, tabs, newlines) at both ends.
    data = [i.strip() for i in data]
    for i in data: print(i)


if __name__ == '__main__':
    main()
