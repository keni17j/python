import sys
import numpy as np
import math


def main():

    # precision: the number of digits after the decimal point
    # suppress: no exponential notation
    np.set_printoptions(precision=2, suppress=True)

    print("")
    ndarrays()
    #statistics()
    #fft()
    hist()
    print("")


def ndarrays():

    # list
    x = np.array([0, 1, 2, 3, 4], dtype=int)
    x = np.array([0, 1, 2, 3, 4])

    # reverse
    x = x[::-1]

    # step
    x = x[::2]

    # start, stop, step
    x = np.arange(0, 10, 1.1, dtype=float)
    x = np.arange(10)

    # start, stop, num(elements)
    # endpoint=True: step = (stop - start) / (num + 1), include stop
    # endpoint=False: step = (stop - start) / num, not include stop
    # retstep: add the step in the array (when print)
    x = np.linspace(0, 10, 5, endpoint=False, retstep=True, dtype=float)

    # size
    x = np.zeros((3,4), dtype=int)

    # size, value
    x = np.full((3,3), 9, dtype=int)

    # start, stop, size
    x = np.random.randint(1, 10, (3,3))

    # list, size
    # replace: duprication
    y = ["red", "blue", "yellow", "white", "black"]
    x = np.random.choice(y, (3,3))
    x = np.random.choice(y, 3, replace=False)

    # replace
    x = np.arange(10, dtype=object) # object can include different types
    x[x>5] = ">5"

    x = np.arange(10, dtype=object) # object can include different types
    idx = np.where(x>5) # indexes
    x[idx] = ">5"

    x = np.arange(10) # object can include different types
    x = np.where(x>5, 1, 0) # replace 100 to 1 and others to 0

    # sort
    y = np.random.randint(0, 100, 10)
    x = np.sort(y)
    idx = np.argsort(y) # indexes
    x = y[idx]

    # list, padding size, "constant", valuesß
    x = np.pad(x, (3,3), "constant", constant_values=(1,9))

    # vstack
    x = np.vstack((x, x))

    # hstack
    x = np.hstack((x, x))


def statistics():

    x = np.random.randint(1, 10, (10,))
    print(x)

    # these functions can select the axis

    # max
    max = np.amax(x)
    idx = np.argmax(x) # index

    # min
    min = np.amin(x)
    idx = np.argmin(x) # index

    # sum
    sum = np.sum(x)

    # mean
    mean = np.mean(x)
    mean = np.nanmean(x) # ignore NaN(Not a Number)

    # variance
    # ddof=m: 1/(n-m)
    # ddof=0: sample
    # ddof=1: unbiased
    var = np.var(x, ddof=0)
    var = np.nanvar(x, ddof=0) # ignore NaN(Not a Number)

    # standard deviation
    # ddof=m: 1/(n-m)
    # ddof=0: sample
    # ddof=1: unbiased
    std = np.std(x, ddof=0)
    std = np.nanstd(x, ddof=0) # ignore NaN(Not a Number)

    # cumulataive sum
    x = np.cumsum(x)

    # cumulataive product
    x = np.cumprod(x)

    # delete deplications
    x = np.unique(x)

    print(max,
          min,
          sum,
          mean,
          std,
          var)


def fft():

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


def hist():

    # histogram
    x = np.random.randn(1000)
    hist, bins = np.histogram(x)
    print("hist", hist) # bins[0] <= x < bins[1], bins[1] <= x < bins[2], ...
    print("bins" ,bins)
    print("")

    # select bins
    hist, bins = np.histogram(x, bins=[-3,-2,-1,0,1,2,3])
    print("hist", hist)
    print("bins" ,bins)
    print("")

    # Sturges's rule
    k = int(math.log2(len(x)) + 1)
    hist, bins = np.histogram(x, bins=k)
    print("Sturgens's rule", "k =", k)
    print("hist", hist)
    print("bins" ,bins)


if __name__ == "__main__": main()
