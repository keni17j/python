import os
import sys
import glob
import datetime
import numpy as np


def main():
    # find files
    dir_path = input("--> ")
    res = glob.glob(os.path.join(dir_path, "**", "*.py"), recursive=True)
    print(res, "\n")

    # create a list
    list = [0, 1, 2, 3, 4]
    list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    list = [i for i in range(5)]
    list = ["abc", "def", "ghi"]
    list = [[j for j in i] for i in list]

    # show the list
    list1 = ["a", "b", "c", "d"]
    list2 = ["e", "f", "g", "h"]
    for i,j in enumerate(list1): print(i, j)
    for i,j in zip(list1, list2): print(i, j)

    # stack
    list = [["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
            ["i", "j", "k", "l"]]
    list_append = []
    for i in list: list_append.append(i)
    # when the variable is used at first time here
    for i in list: list_vstack = np.vstack((list_vstack, i)) if "list_vstack" in locals() else i



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
