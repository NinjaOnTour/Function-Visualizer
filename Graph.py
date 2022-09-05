import matplotlib.pyplot as plt
import numpy as np

# func: Function
# min, max: Minimum and Maximum x value in graph
# step: increase between two x values
def DrawGraph(func, min, max, step, Title, labelX, labelY, gridOn): 
    xList = np.arange(min, max, step)
    yList = list()

    for i in xList:
        yList.append(func(i))
    
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.grid(gridOn)
    plt.title(Title)
    plt.plot(xList, yList)
    plt.show()
