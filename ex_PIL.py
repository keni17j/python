import os
import sys
import glob
import datetime
import PIL

def main():
    # select an image
    file_path = input("--> ")

    



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
