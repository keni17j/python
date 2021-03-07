import sys
import os
import glob


def main():

    print("")
    # get paths and names, find files
    get()
    # create, rename, remove files and directories
    cntr()
    # check files, delete extensions, convert to abs, ...
    others()
    print("")


def get():

    # folders and files in the directory
    path = input("dir -> ")
    print(os.listdir(path), "\n")

    # file names
    path = input("file -> ")
    print(os.path.basename(path), "\n")

    # directory names
    path = input("file -> ")
    print(os.path.dirname(path), "\n")

    # split the directory and the file
    path = input("file -> ")
    print(os.path.split(path), "\n")

    # the current directory
    print(os.getcwd())

    # find files under the directory
    path = input("dir -> ")
    ext = "*.py"
    files = glob.glob(os.path.join(path, "**", ext), recursive=True)
    print(files)


def cntr():

    # make directories
    path = "test_dir"
    os.mkdir(path)
    os.makedirs(path) # recursivery

    # rename
    before = "test_dir"
    after = "test_dir_rename"
    os.rename(before, after)
    os.renames(before, after) # recursivery

    # remove files
    path = input("file -> ")
    os.remove(path)

    # remove directories
    path = input("dir -> ")
    os.removedirs(path)


def others():

    # check existance (files)
    path = input("file -> ")
    print(os.path.isfile(path), "\n")

    # check existance (directories)
    path = input("dir -> ")
    print(os.path.isdir(path), "\n")

    # check existance
    path = input("dir or file -> ")
    print(os.path.exists(path), "\n")

    # delete extensions
    path = input("file -> ")
    print(os.path.splitext(path), "\n")

    # convert to the absolute paths
    path = "dir"
    print(os.path.abspath(path))

    # join paths
    dir = "directory"
    file = "file"
    print(os.path.join(dir, file), "\n")

    # move to
    path = input("dir -> ")
    os.chdir(path)


if __name__ == "__main__": main()
