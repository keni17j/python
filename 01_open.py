import sys
import os

def main():

    print("")
    # read files
    read()
    # write to files
    write()
    print("")


def read():

    #file_path = r"test.txt"
    file_path = input("file path --> ")
    enc = "utf-8"

    with open(file_path, encoding=enc) as f:
        list = f.readlines()
    # delete whitespaces(spaces, tabs, newlines) at both ends
    list = [i.strip() for i in list]
    for i in list: print(i)


def write():

    list = ["good morning", "good evening", "good night"]
    file_path = os.path.abspath(__file__)
    file_path = os.path.dirname(file_path)
    file_path = os.path.join(file_path, "test.txt")

    with open(file_path, mode="w") as f:
        # method 1
        f.write("\n".join(list))
        f.write("\n") # add a newline in the end of line
        # method 2
        for i in list:
            f.write(i)
            f.write("\n")
        # method 3
        f.writelines("\n".join(list))
        f.write("\n") # add a newline in the end of line
        # method 4
        for i in list: f.writelines([i, "\n"])


if __name__ == "__main__": main()
