import matplotlib.pyplot as plt


def plot(xarr, yarr):

    plt.plot(xarr, yarr)
    plt.xlabel('n - arraysize')
    plt.ylabel('iterations - repeat counts')
    plt.title('plot of size vs iterations')
    plt.show()
