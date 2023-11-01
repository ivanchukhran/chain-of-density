import numpy as np
import matplotlib.pyplot as plt

def density_plot(x):
    plt.plot(x)
    plt.title('Entity Density')
    plt.xticks(np.arange(0, len(x), 1))
    plt.xlabel('CoD step')
    plt.ylabel('Entity Density')
    return plt.show()


def extractive_density_plot(x):
    plt.plot(x)
    plt.title('Extractive Density')
    plt.xticks(np.arange(0, len(x), 1))
    plt.xlabel('CoD step')
    plt.ylabel('Extractive Density')
    return plt.show()


def fusion_plot(x):
    plt.plot(x)
    plt.title('Fusion')
    plt.xticks(np.arange(0, len(x), 1))
    plt.xlabel('CoD step')
    plt.ylabel('Fusion')
    return plt.show()