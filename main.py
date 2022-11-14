import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

example = np.array([[1, 2, 3], [3, 3, 4], [2, 4, 5]])


def display(tasks):
    task = []
    begin = []
    end = []

    for i in range(0, int(tasks.size/3)):
        task.append(tasks[i][0])
        begin.append(tasks[i][1])
        end.append(tasks[i][2])

    task_arr = np.array(task)
    begin_arr = np.array(begin)
    end_arr = np.array(end)

    plt.barh(range(len(begin_arr)), end_arr-begin_arr, left=begin_arr)

    plt.ylabel("Task")
    plt.yticks(range(len(begin_arr)), task_arr)
    plt.xlim([0, max(end)+1])
    plt.show()


root = Tk()
root.title("Deadline Monotonic Schedule")
root.geometry("600x400+50+50")
root.resizable(False, False)
button = Button(root, text='Generuj', command=lambda: display(example))
button.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()
