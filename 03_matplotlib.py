"""
Matplotlib.
"""

import os
import sys

import matplotlib.pyplot as plt
import numpy as np


def main():

    # The pyplot API.
    pltAPI_single()  # Draw a graph.
    pltAPI_multiple()  # Draw graphs.
    # The object-oriented API.
    objAPI_single()  # Draw a graph.
    objAPI_multiple()  # Draw graphs.


def pltAPI_single():

    # A sample data.
    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # Extruct sampling datas.
    n = 10  # 1/n datas.
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # Create a figure.
    fig = plt.figure()
    #fig = plt.figure(figsize=(8,6))  # The size is inch.

    # Titles.
    plt.title('title', fontsize=20)
    plt.xlabel('x axis', fontsize=10)
    plt.ylabel('y axis', fontsize=10)

    # Sub scales.
    plt.minorticks_on()

    # Scale dierctions.
    plt.tick_params(which='both', direction='in')

    # Limit the range.
    plt.xlim(0, 360)
    plt.ylim(-3, 3)

    # Get limits.
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()

    # Intervals of scales.
    # When the range of scale is larger than limit, limit is overwritten.
    step = 45
    scale = np.arange(x_min, x_max+step, step)  # +step for including stop(x_max).
    plt.xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step)  # +step for including stop(y_max).
    plt.yticks(scale)

    # Replace each axix value.
    """
    plt.xticks([90, 270], ['peak', 'peak'])
    plt.yticks([-1, 1], ['peak', 'peak'])
    """

    # Draw grid lines.
    plt.grid(which='major', axis='both')

    # Drow lines.
    # Line type: '-', '--', ':', '-.'
    plt.axhline(1, c='#ff0000', ls=':')
    plt.axvline(90, c='#ff0000', ls=':')

    # Plot datas.
    plt.plot(x,
             y1,
             linestyle='-',  # '-', '--', ':', '-.'
             linewidth=1,
             color='#00ff00',
             marker='o',  # 'o', '^', 's', 'x', 'd', '+', '*', ...
             markersize=10,
             markerfacecolor='none',
             markeredgecolor='#00ff00',
             markeredgewidth=1,
             label='data1',
             )
    plt.plot(x,
             y2,
             linestyle='--',
             linewidth=1,
             color='#0000ff',
             marker='x',
             markersize=10,
             markerfacecolor='none',
             markeredgecolor='#0000ff',
             markeredgewidth=2,
             label='data2',
             )

    # Legends.
    plt.legend(loc='upper right', ncol=1, fontsize=10)
    #plt.legend(['data1', 'data2'])
    #plt.legend().remove()

    # Adjust size.
    #fig.tight_layout()

    # Save.
    #fig.savefig('test.png')

    # Show.
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


def pltAPI_multiple():

    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # Extruct sampling datas.
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # Create a figure.
    fig = plt.figure()

    # Subplot 1.
    plt.subplot(211)  # row:2, col:1, num:1

    # Setting.
    plt.title('title', fontsize=20)
    plt.xlabel('x axis', fontsize=10)
    plt.ylabel('y axis', fontsize=10)
    plt.minorticks_on()
    plt.tick_params(which='both', direction='in')
    plt.xlim(0, 360)
    plt.ylim(-3, 3)
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    step = 45
    scale = np.arange(x_min, x_max+step, step)
    plt.xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step)
    plt.yticks(scale)
    plt.grid(which='major', axis='both')
    plt.axhline(1, c='#ff0000', ls=':')
    plt.axvline(90, c='#ff0000', ls=':')

    # Plot.
    plt.plot(x,
             y1,
             linestyle='-',
             linewidth=1,
             color='#00ff00',
             marker='o',
             markersize=10,
             markerfacecolor='none',
             markeredgecolor='#00ff00',
             markeredgewidth=1,
             label='data1',
             )

    # Legends.
    plt.legend(loc='upper right', ncol=1, fontsize=10)

    # Subplot 2.
    plt.subplot(212)  # row:2, col:1, num:2

    # Setting.
    plt.title('title', fontsize=20)
    plt.xlabel('x axis', fontsize=10)
    plt.ylabel('y axis', fontsize=10)

    # Plot.
    plt.plot(x,
             y2,
             linestyle='--',
             linewidth=1,
             color='#0000ff',
             marker='x',
             markersize=10,
             markerfacecolor='none',
             markeredgecolor='#0000ff',
             markeredgewidth=2,
             label='data2',
             )

    # Adjust each subplot size.
    fig.tight_layout()

    # Save.
    #fig.savefig('test.png')

    # Show.
    plt.show(block=False)
    input()
    plt.close()


def objAPI_single():

    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # Extruct sampling datas.
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # Create a figure.
    fig, ax = plt.subplots()

    # Titles.
    ax.set_title('title', fontsize=20)
    ax.set_xlabel('x axis', fontsize=10)
    ax.set_ylabel('y axis', fontsize=10)

    # Sub scales.
    ax.minorticks_on()

    # Scale dierctions.
    ax.tick_params(which='both', direction='in')

    # Limit the range.
    ax.set_xlim(0, 360)
    ax.set_ylim(-3, 3)

    # Get limits.
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    # Intervals of scales.
    # When the range of scale is larger than limit, limit is overwritten.
    step = 45
    scale = np.arange(x_min, x_max+step, step)  # +step is to include stop(x_max).
    ax.set_xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step)  # +step is to include stop(y_max).
    ax.set_yticks(scale)

    # Replace each axix value.
    """
    ax.set_xticks([90, 270], ['peak', 'peak'])
    ax.set_yticks([-1, 1], ['peak', 'peak'])
    """

    # Draaw Grid lines.
    ax.grid(which='major', axis='both')

    # Drow lines.
    # Line type: '-', '--', ':', '-.'
    ax.axhline(1, c='#ff0000', ls=':')
    ax.axvline(90, c='#ff0000', ls=':')

    # Plot datas.
    ax.plot(x,
            y1,
            linestyle='-',  # '-', '--', ':', '-.'
            linewidth=1,
            color='#00ff00',
            marker='o',  # 'o', '^', 's', 'x', 'd', '+', '*', ...
            markersize=10,
            markerfacecolor='none',
            markeredgecolor='#00ff00',
            markeredgewidth=1,
            label='data1',
            )
    ax.plot(x,
            y2,
            linestyle='--',
            linewidth=1,
            color='#0000ff',
            marker='x',
            markersize=10,
            markerfacecolor='none',
            markeredgecolor='#0000ff',
            markeredgewidth=2,
            label='data2',
            )

    # Legends.
    ax.legend(loc='upper right', ncol=1, fontsize=10)
    #ax.legend(['data1', 'data2'])
    #ax.legend().remove()

    # Save.
    #plt.savefig('test.png')

    # Show.
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


def objAPI_multiple():

    x = np.arange(720)
    rad = np.pi * x / 180
    y1 = np.sin(rad)
    y2 = np.cos(rad)

    # Extruct sampling datas.
    n = 10
    x = x[::n]
    y1 = y1[::n]
    y2 = y2[::n]

    # Create a figure.
    fig, axs = plt.subplots(2, 1)
    #fig, axs = plt.subplots(2, 2)

    # Subplot 1.
    ax = axs[0]
    #ax = axs[0,0]

    # Setting.
    ax.set_title('title', fontsize=20)
    ax.set_xlabel('x axis', fontsize=10)
    ax.set_ylabel('y axis', fontsize=10)
    ax.minorticks_on()
    ax.tick_params(which='both', direction='in')
    ax.set_xlim(0, 360)
    ax.set_ylim(-3, 3)
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    step = 45
    scale = np.arange(x_min, x_max+step, step)
    ax.set_xticks(scale)
    step = 0.5
    scale = np.arange(y_min, y_max+step, step)
    ax.set_yticks(scale)
    ax.grid(which='major', axis='both')
    ax.axhline(1, c='#ff0000', ls=':')
    ax.axvline(90, c='#ff0000', ls=':')

    # Plot.
    ax.plot(x,
            y1,
            linestyle='-',  # '-', '--', ':', '-.'
            linewidth=1,
            color='#00ff00',
            marker='o',  # 'o', '^', 's', 'x', 'd', '+', '*', ...
            markersize=10,
            markerfacecolor='none',
            markeredgecolor='#00ff00',
            markeredgewidth=1,
            label='data1',
            )

    # Legends.
    ax.legend(loc='upper right', ncol=1, fontsize=10)

    # Subplot 2.
    ax = axs[1]
    #ax = axs[1,1]

    # Setting.
    ax.set_title('title', fontsize=20)
    ax.set_xlabel('x axis', fontsize=10)
    ax.set_ylabel('y axis', fontsize=10)

    # Plot
    ax.plot(x,
            y2,
            linestyle='--',
            linewidth=1,
            color='#0000ff',
            marker='x',
            markersize=10,
            markerfacecolor='none',
            markeredgecolor='#0000ff',
            markeredgewidth=2,
            label='data2',
            )

    # Adjust each subplot size.
    fig.tight_layout()

    # Save.
    #plt.savefig('test.png')

    # Show.
    plt.show(block=False)
    #plt.pause(10)
    input()
    plt.close()
    #plt.show()


if __name__ == '__main__':
    main()
