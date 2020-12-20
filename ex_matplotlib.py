import os
import sys
import glob
import datetime
import numpy as np
import matplotlib.pyplot as plt

def main():

    # single graph
    # -------------------------------------------------------
    x = np.arange(0, 100, 5)
    y = x ** 2

    #fig = plt.figure()
    fig = plt.figure(figsize=(8,6)) # the size is inch

    # scale dierction, set first!!!
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"

    # sub scales
    plt.minorticks_on()

    # grid lines
    plt.grid(which="major", axis="both")

    # titles
    plt.title("title", fontsize=20)
    plt.xlabel("x axis", fontsize=10)
    plt.ylabel("y axis", fontsize=10)

    # limit
    plt.xlim(0, 50)
    plt.ylim(0, 2500)

    # replace each axix value
    """
    plt.xticks([10, 20, 30], ["A", "B", "C"])
    plt.yticks([100, 400, 900], ["a", "b", "c"])
    """
    # change intervals of scales
    min, max = plt.xlim()
    scale = max / 5 # the number of scales
    scale = np.arange(min, max, scale)
    plt.xticks(scale)
    min, max = plt.ylim()
    scale = max / 5 # the number of scales
    scale = np.arange(min, max, scale)
    plt.yticks(scale)

    # drow lines
    min, max = plt.ylim()
    plt.vlines(40, min, max, "#ff0000", ":")
    min, max = plt.xlim()
    plt.hlines(1600/2, min, max, "#ff0000", ":")

    # plot datas
    plt.plot(x, y,
             linestyle="-", # "-", "--", ":", "-."
             linewidth=1,
             color="#00ff00",
             marker="o", # "o", "^", "s", "x", "d", "+", "*", ...
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#00ff00",
             markeredgewidth=1,
             label="data1")
    plt.plot(x, y/2,
             linestyle="--",
             linewidth=1,
             color="#0000ff",
             marker="x",
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#0000ff",
             markeredgewidth=2,
             label="data2")

    # legend
    plt.legend(loc="upper right")
    #plt.legend(["data1", "data2"])

    # show
    plt.show(block=False)
    plt.pause(5)
    plt.close()

    # save
    fig.savefig("test.png")


    # multiple graphs
    # -------------------------------------------------------










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
