"""
Numpy.
"""

import math
import sys

import matplotlib.pyplot as plt
import numpy as np


def main():

    # Notation settings.
    # precision: The number of digits after the decimal point.
    # suppress: No exponential notation.
    np.set_printoptions(precision=2, suppress=True)

    basic()
    statistics()
    fft()
    hist()


def basic():

    # Create ndarrays.
    x = np.array([0, 1, 2, 3, 4])
    x = np.array([0, 1, 2, 3, 4], dtype=np.uint64)
    x = np.zeros((3, 4), dtype=int)
    x = np.ones((3, 4), dtype=int)
    x = np.full((3, 4), 9, dtype=int)
    x = np.empty((3, 4), dtype=int)
    x = np.empty_like(x)
    x = np.arange(0, 10, 2, dtype=float)  # (start, stop, step)
    x = np.arange(10)
    # (start, stop, num)
    # endpoint = True: step = (stop-start) / (num-1), include stop.
    # endpoint = False: step = (stop-start) / num, not include stop.
    # retstep: Add the step to the return value.
    x = np.linspace(0, 10, 5, endpoint=True, retstep=True, dtype=float)

    # Copy arrays.
    # The original array will be modified by changing the created array.
    x = np.array([0, 1, 2, 3])
    y = x
    y[0] = 3  # x[0] = 3
    y = x.copy()
    y[0] = 0  # x[0] = 3

    # Get shapes.
    x = np.arange(9).reshape(3, 3)
    print(x.ndim)
    print(x.size)
    print(x.shape)

    # Add elements.
    x = np.arange(3)
    x = np.hstack((x, x))
    x = np.vstack((x, x))
    x = np.stack((x, x))  # Add a new axis.

    # Sort elements.
    x = np.random.randint(0, 100, (10,))
    x = np.sort(x)
    idx = np.argsort(x)
    x = x[idx]

    # Revers elements.
    x = np.flip(x)

    # Use slice.
    x = x[1:3]
    x = x[:-1]
    x = x[::2]  # 2 steps.
    x = x[::-1]  # Invert.

    # Reshape.
    x = np.arange(12)
    x = np.reshape(x, (3, 4))
    x = x.reshape(2, -1)
    x = x.flatten()
    x = x[np.newaxis, :]  # Add a new axis.
    x = x.transpose()
    x = x.T

    # Use random.
    x = np.random.random(10)
    x = np.random.randint(1, 10, (3, 3))  # (start, stop, size)
    y = ['red', 'blue', 'yellow', 'white', 'black']
    x = np.random.choice(y, (3, 3))
    x = np.random.choice(y, 3, replace=False)  # No duprications.

    # Get indexes of elements satisfying conditions.
    x = np.arange(9).reshape(3, 3)
    idx = np.nonzero(x > 5)
    print(np.count_nonzero(x > 5))  # The number of elements.
    idx = list(zip(idx[0], idx[1]))
    idx = np.nonzero(x > 5)
    idx = np.array([[i, j]for i, j in zip(idx[0], idx[1])])
    idx = np.where(x > 5)
    idx = list(zip(idx[0], idx[1]))

    # Separate.
    x = np.hsplit(x, 3)

    # Get uniques in an array.
    x = np.random.randint(1, 10, (10,))
    x = np.unique(x)
    x, idx, cnt = np.unique(x, return_index=True, return_counts=True)  # idx is each first index.

    # Replace elements satisfying conditions.
    x = np.arange(10, dtype=object)  # Object can include different types.
    x[x > 5] = '>5'
    x = np.arange(10, dtype=object)
    x = np.where(x > 5, '>5', x)  # (conditions, true case, false case)

    # Padding.
    # (list, padding size, 'constant', padding values)
    x = np.pad(x, (3, 3), 'constant', constant_values=('L', 'R'))


def statistics():
    """
    Statistics functions.
    These can select an axis if you need.
    """

    x = np.random.randint(1, 100, (100,))

    max = x.max()
    max = np.amax(x)
    idx = np.argmax(x)

    min = x.min()
    min = np.amin(x)
    idx = np.argmin(x)

    sum = x.sum()
    sum = np.sum(x)

    mean = np.mean(x)
    mean = np.nanmean(x) # Ignore NaN(Not a Number).

    med = np.median(x)

    # Variance.
    # ddof = m: 1 / (n-m)
    # ddof = 0: Sample variance.
    # ddof = 1: Unbiased variance.
    var = np.var(x, ddof=0)
    var = np.nanvar(x, ddof=0) # Ignore NaN(Not a Number).

    # Standard deviation.
    # ddof = m: 1 / (n-m)
    # ddof = 0: Sample standard deviation.
    # ddof = 1: Unbiased standard deviation.
    std = np.std(x, ddof=0)
    std = np.nanstd(x, ddof=0) # Ignore NaN(Not a Number).

    # Cumulataive sum.
    x = np.cumsum(x)

    # Cumulataive product.
    x = np.cumprod(x)

    # Delete deplications.
    x = np.unique(x)

    print('max', max,
          '\n' 'min', min,
          '\n' 'sum', sum,
          '\n' 'mean', mean,
          '\n' 'med', med,
          '\n' 'std', std,
          '\n' 'var', var,
          )


def fft():

    # Sample data.
    f1 = 20  # [Hz].
    f2 = 40
    sampling = 1000  # [Hz], smpring >> f.
    period = 5  # [s].
    samples = sampling * period
    t = np.linspace(0, period, samples)
    y1 = np.sin(2*np.pi*f1*t)
    y2 = np.sin(2*np.pi*f2*t)
    y = y1# + y2
    n = 2 ** 8  # The number of datas, < smples.
    t = t[:n]
    y = y[:n]
    print(np.amax(y), np.amin(y))
    if n > samples :
        print('Error: n > samples')
        return

    # FFT.
    fft = np.fft.fft(y)
    fft = np.abs(fft)  # Calculate the amplitudespectrum.
    fft[0] = fft[0] / n
    fft[1:] = fft[1:] / n * 2
    fft = fft[:n//2]
    freq = np.fft.fftfreq(n, 1/sampling)
    freq = freq[:n//2]

    print(np.amax(fft), np.amin(fft))

    plt.plot(freq, fft)
    plt.show(block=False)
    input('press enter')
    plt.close()


def hist():

    x = np.random.randn(1000)
    hist, bins = np.histogram(x)
    print('hist', hist)  # bins[0] <= x < bins[1], bins[1] <= x < bins[2], ...
    print('bins' ,bins)

    # Select bins.
    sel_bins = [-3, -2, -1, 0, 1, 2, 3]
    hist, bins = np.histogram(x, bins=sel_bins)
    print('hist', hist)
    print('bins' ,bins)
    print('')

    # The Sturges's rule.
    k = int(math.log2(len(x)) + 1)
    hist, bins = np.histogram(x, bins=k)
    print("Sturgens's rule", 'k =', k)
    print('hist', hist)
    print('bins', bins)


if __name__ == '__main__':
    main()
