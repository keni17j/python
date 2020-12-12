import os
import sys
import glob
import datetime


def main():
    # ----- write ----
    file_path = r"test.txt"
    list = ["good morning", "good evening", "good night"]
    with open(file_path, mode="w") as f:
        # pattern 1
        f.write("\n".join(list)) # don't exist a newline in the end
        f.write("\n") # add a newline in the end
        # pattern 2
        for i in list:
            f.write(i)
            f.write("\n")
        # pattern 3
        for i in list: f.writelines([i, "\n"])


    # ----- read -----
    file_path = r"test.txt"
    enc = "utf-8"
    with open(file_path, encoding=enc) as f:
        list = f.readlines()
    # delete whitespaces(spaces, tabs, newlines) at both ends
    list = [i.strip() for i in list]
    for i in list: print(i)


def make_dir():
    # directory path(name)
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    date = datetime.datetime.now().strftime("%Y%m%d")
    dir_name = date + "_" + file_name[:-3]
    dir_path = os.path.join(dir_path, dir_name)
    # create a directory
    if not os.path.exists(dir_path): os.mkdir(dir_path)
    # move to the directory
    os.chdir(dir_path)


if __name__ == "__main__":
    # run the main function
    print("\n", "----- start -----", "\n")
    make_dir()
    main()
    print("\n", "----- end -----", "\n")
