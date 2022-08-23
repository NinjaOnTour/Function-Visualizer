import matplotlib.pyplot as plt
import numpy as np

def DrawGraph(func, max): # func: Function   ,   max: Maximum x value in graph

    xList = list(range(0, max))
    yList = list()

    for i in range(0, max):
        yList.append(func(i))
    
    plt.plot(xList, yList)
    plt.show()
