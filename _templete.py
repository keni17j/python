import os
import sys
import glob
import datetime


def main():
    print("hello")


if __name__ == '__main__':
    # create a new directory
    file_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    date = datetime.datetime.now().strftime("%Y%m%d")
    dir_name = date + "_" + file_name[:-3]
    dir_path = os.path.join(dir_path, dir_name)
    if not os.path.exists(dir_path): os.mkdir(dir_path)
    # run the main function
    print("\n", "----- start -----", "\n")
    main()
    print("\n", "----- end -----", "\n")
