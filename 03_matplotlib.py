import sys
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # pyplot API
    pltAPI_single() # draw a graph
    pltAPI_multiple() # draw graphs
    # object-oriented API
    objAPI_single() # draw a graph
    objAPI_multiple() # draw graphs


def pltAPI_single():

    # datas
    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # 1/n
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # create a figure
    #fig = plt.figure(figsize=(8,6)) # the size is inch
    fig = plt.figure()

    # titles
    plt.title("title", fontsize=20)
    plt.xlabel("x axis", fontsize=10)
    plt.ylabel("y axis", fontsize=10)

    # sub scales
    plt.minorticks_on()

    # scale dierction
    plt.tick_params(which="both", direction="in")

    # limit (range)
    plt.xlim(0, 360)
    plt.ylim(-3, 3)

    # get limits
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()

    # intervals of scales
    # when the range of scale is larger than limit, limit is overwritten
    step = 45
    scale = np.arange(x_min, x_max+step, step) # +step is to include stop(x_max)
    plt.xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step) # +step is to include stop(y_max)
    plt.yticks(scale)

    # replace each axix value
    """
    plt.xticks([90, 270], ["peak", "peak"])
    plt.yticks([-1, 1], ["peak", "peak"])
    """

    # grid lines
    plt.grid(which="major", axis="both")

    # drow lines
    # line type: "-", "--", ":", "-."
    plt.axhline(1, c="#ff0000", ls=":")
    plt.axvline(90, c="#ff0000", ls=":")

    # plot datas
    plt.plot(x, y1,
             linestyle="-", # "-", "--", ":", "-."
             linewidth=1,
             color="#00ff00",
             marker="o", # "o", "^", "s", "x", "d", "+", "*", ...
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#00ff00",
             markeredgewidth=1,
             label="data1")
    plt.plot(x, y2,
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
    plt.legend(loc="upper right", ncol=1, fontsize=10)
    #plt.legend(["data1", "data2"])
    #plt.legend().remove() # delete

    # adjust size
    #fig.tight_layout()


    # save
    #fig.savefig("test.png")

    # show
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


def pltAPI_multiple():

    # datas
    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # 1/n
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # create a figure
    fig = plt.figure()

    # subplot 1
    plt.subplot(211) # row:2, col:1, num:1

    # setting
    plt.title("title", fontsize=20)
    plt.xlabel("x axis", fontsize=10)
    plt.ylabel("y axis", fontsize=10)
    plt.minorticks_on()
    plt.tick_params(which="both", direction="in")
    plt.xlim(0, 360)
    plt.ylim(-3, 3)
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    step = 45
    scale = np.arange(x_min, x_max+step, step) # +step is to include stop(x_max)
    plt.xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step) # +step is to include stop(y_max)
    plt.yticks(scale)
    plt.grid(which="major", axis="both")
    plt.axhline(1, c="#ff0000", ls=":")
    plt.axvline(90, c="#ff0000", ls=":")

    # plot
    plt.plot(x, y1,
             linestyle="-", # "-", "--", ":", "-."
             linewidth=1,
             color="#00ff00",
             marker="o", # "o", "^", "s", "x", "d", "+", "*", ...
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#00ff00",
             markeredgewidth=1,
             label="data1")

    # legend
    plt.legend(loc="upper right", ncol=1, fontsize=10)

    # subplot 2
    plt.subplot(212) # row:2, col:1, num:1

    # setting
    plt.title("title", fontsize=20)
    plt.xlabel("x axis", fontsize=10)
    plt.ylabel("y axis", fontsize=10)

    # plot
    plt.plot(x, y2,
             linestyle="--",
             linewidth=1,
             color="#0000ff",
             marker="x",
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#0000ff",
             markeredgewidth=2,
             label="data2")

    # adjust each subplot size
    fig.tight_layout()

    # save
    #fig.savefig("test.png")

    # show
    plt.show(block=False)
    input()
    plt.close()


def objAPI_single():

    # datas
    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # 1/n
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # create a figure
    fig, ax = plt.subplots()

    # titles
    ax.set_title("title", fontsize=20)
    ax.set_xlabel("x axis", fontsize=10)
    ax.set_ylabel("y axis", fontsize=10)

    # sub scales
    ax.minorticks_on()

    # scale dierction
    ax.tick_params(which="both", direction="in")

    # limit (range)
    ax.set_xlim(0, 360)
    ax.set_ylim(-3, 3)

    # get limits
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    # intervals of scales
    # when the range of scale is larger than limit, limit is overwritten
    step = 45
    scale = np.arange(x_min, x_max+step, step) # +step is to include stop(x_max)
    ax.set_xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step) # +step is to include stop(y_max)
    ax.set_yticks(scale)

    # replace each axix value
    """
    ax.set_xticks([90, 270], ["peak", "peak"])
    ax.set_yticks([-1, 1], ["peak", "peak"])
    """

    # grid lines
    ax.grid(which="major", axis="both")

    # drow lines
    # line type: "-", "--", ":", "-."
    ax.axhline(1, c="#ff0000", ls=":")
    ax.axvline(90, c="#ff0000", ls=":")

    # plot datas
    ax.plot(x, y1,
             linestyle="-", # "-", "--", ":", "-."
             linewidth=1,
             color="#00ff00",
             marker="o", # "o", "^", "s", "x", "d", "+", "*", ...
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#00ff00",
             markeredgewidth=1,
             label="data1")
    ax.plot(x, y2,
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
    ax.legend(loc="upper right", ncol=1, fontsize=10)
    #ax.legend(["data1", "data2"])
    #ax.legend().remove() # delete

    # save
    #plt.savefig("test.png")

    # show
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


def objAPI_multiple():

    # datas
    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # 1/n
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # create a figure
    fig, axs = plt.subplots(2, 1)
    #fig, axs = plt.subplots(2, 2)

    # subplot 1
    ax = axs[0]
    #ax = axs[0,0]

    # setting
    ax.set_title("title", fontsize=20)
    ax.set_xlabel("x axis", fontsize=10)
    ax.set_ylabel("y axis", fontsize=10)
    ax.minorticks_on()
    ax.tick_params(which="both", direction="in")
    ax.set_xlim(0, 360)
    ax.set_ylim(-3, 3)
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    step = 45
    scale = np.arange(x_min, x_max+step, step) # +step is to include stop(x_max)
    ax.set_xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step) # +step is to include stop(y_max)
    ax.set_yticks(scale)
    ax.grid(which="major", axis="both")
    ax.axhline(1, c="#ff0000", ls=":")
    ax.axvline(90, c="#ff0000", ls=":")

    # plot
    ax.plot(x, y1,
             linestyle="-", # "-", "--", ":", "-."
             linewidth=1,
             color="#00ff00",
             marker="o", # "o", "^", "s", "x", "d", "+", "*", ...
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#00ff00",
             markeredgewidth=1,
             label="data1")

    # legend
    ax.legend(loc="upper right", ncol=1, fontsize=10)

    # subplot 2
    ax = axs[1]
    #ax = axs[1,1]

    # setting
    ax.set_title("title", fontsize=20)
    ax.set_xlabel("x axis", fontsize=10)
    ax.set_ylabel("y axis", fontsize=10)

    # plot
    ax.plot(x, y2,
             linestyle="--",
             linewidth=1,
             color="#0000ff",
             marker="x",
             markersize=10,
             markerfacecolor="none",
             markeredgecolor="#0000ff",
             markeredgewidth=2,
             label="data2")

    # adjust each subplot size
    fig.tight_layout()

    # save
    #plt.savefig("test.png")

    # show
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


if __name__ == "__main__": main()
