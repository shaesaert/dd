"""Compare runtimes of `dd` and `pyeda`."""
import pickle
from matplotlib import pyplot as plt


def plot():
    fname = 'dd_times.p'
    f = open(fname, 'r')
    dd_times = pickle.load(f)
    fname = 'pyeda_times.p'
    f = open(fname, 'r')
    pyeda_times = pickle.load(f)
    n = 9
    x = range(1, n + 1)
    t_dd = [dd_times[i] for i in x]
    t_pyeda = [pyeda_times[i] for i in x]
    number_of_vars = [i*2 for i in x]
    plt.plot(x, t_dd, 'b-o', label='dd')
    plt.plot(x, t_pyeda, 'r-+', label='PyEDA')
    plt.plot(x, number_of_vars, 'g--', label='number of variables')
    plt.xlabel('Number of queens')
    plt.ylabel('Time (sec)')
    plt.grid('on')
    plt.legend(loc='upper left')
    plt.yscale('log')
    plt.savefig('comparison.pdf', bbox_inches='tight')


if __name__ == '__main__':
    plot()
