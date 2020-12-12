import os
import sys
import glob
import datetime
import numpy as np
import math
import matplotlib.pyplot as plt
import time


def main():

    x = np.array([0, 1, 2, 3, 4])
    print(x)

    x = np.arange(10)
    print(x)
    x = np.arange(0, 10, 1)
    print(x)


    x = np.full((3,3), 9)
    print(x)

    x = np.random.randint(1, 10, (3,3))
    print(x)

    x = ["red", "blue", "yellow", "white", "black"]
    x = np.random.choice(x, 5, replace=False) # no duprication
    print(x)

    x = np.zeros((3,))
    print(x)

    x = np.pad(x, (3,3), "constant", constant_values=(1,9))
    print(x)

    x = np.arange(0, 100, 10)
    print(x)
    x_obj = x.astype(object) # object can include different types
    x_obj[x_obj>50] = ">50"
    print(x_obj)

    idx = np.where(x>50)[0] # get indexes by np.where
    x_where = x
    x_where[idx] = 100
    print(x_where)

    x_where = np.where(x_where==100, 1, 0) # replace 100 to 1 and others to 0
    print(x_where)

    x = np.arange(0, 100, 10)
    print(x)


    sys.exit()
    # --------------------------------------------------------------------------

    # fft sample data
    f1 = 20 # [Hz]
    f2 = 40
    sampling = 1000 # [Hz], smpring late, >> f
    t = 5 # [s]
    samples = sampling * t
    x = np.linspace(0, t, samples)
    y1 = np.sin(2 * np.pi * f1 * x)
    y2 = np.sin(2 * np.pi * f2 * x)
    y = y1# + y2
    n = 2 ** 8 # the number of datas, < smples
    x = x[:n]
    y = y[:n]
    print(np.amax(y), np.amin(y))
    if n > samples :
        print("error: n > samples")
        sys.exit()

    # fft
    fft = np.fft.fft(y)
    fft = np.abs(fft)
    fft[0] = fft[0] / n
    fft[1:] = fft[1:] / n * 2
    fft = fft[:int(n/2)]
    freq = np.fft.fftfreq(n, 1/sampling)
    freq = freq[:int(n/2)]

    print(np.amax(fft), np.amin(fft))
    plt.plot(freq, fft)
    plt.show(block=False)
    plt.pause(10)
    plt.close()

    # histogram
    x = np.random.randn(1000)
    hist, bins = np.histogram(x)
    print("hist", hist) # bins[0] <= x < bins[1], bins[1] <= x < bins[2], ...
    print("bins" ,bins)

    # select bins
    hist, bins = np.histogram(x, bins=[-3,-2,-1,0,1,2,3])
    print("hist", hist)
    print("bins" ,bins)

    # Sturges's rule
    k = int(math.log2(len(x)) + 1)
    hist, bins = np.histogram(x, bins=k)
    print("Sturgens's rule", "k =", k)
    print("hist", hist)
    print("bins" ,bins)


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
    #make_dir()
    main()
    print("\n", "----- end -----", "\n")
