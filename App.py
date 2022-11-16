import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from Scheduling import *
from Task import *

#example = np.array([[1, 2, 3], [3, 3, 4], [2, 4, 5]])


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Deadline Monotonic Schedule")
        self.geometry("600x400+50+50")

        Label(self, text='Period').grid(row=0, column=1)
        Label(self, text='Execution Time').grid(row=0, column=2)
        Label(self, text='Deadline').grid(row=0, column=3)
        Label(self, text='Task 1').grid(row=1)
        Label(self, text='Task 2').grid(row=2)
        Label(self, text='Task 3').grid(row=3)
        Label(self, text='Task 4').grid(row=4)
        Label(self, text='Task 5').grid(row=5)

        entries_period = [Entry(self) for _ in range(5)]
        entries_exec = [Entry(self) for _ in range(5)]
        entries_deadline = [Entry(self) for _ in range(5)]

        for entry in entries_period:
            entry.grid(row=entries_period.index(entry)+1, column=1)

        for entry in entries_exec:
            entry.grid(row=entries_exec.index(entry)+1, column=2)

        for entry in entries_deadline:
            entry.grid(row=entries_deadline.index(entry)+1, column=3)

        #[Task(i+1, entries_exec[i].get(), entries_deadline[i].get(), entries_period[i].get) for i in range(5)]

        self.button = Button(self, text='Generuj', command=lambda: display(Scheduling([Task(i+1, int(entries_exec[i].get()), int(
            entries_deadline[i].get()), int(entries_period[i].get())) for i in range(5)]).sort_tasks())).grid(row=5, column=4)


def display(tasks):
    task = []
    begin = []
    end = []
    colors = ['red', 'blue', 'green', 'yellow', 'grey']

    for i in range(0, len(tasks)):
        task.append(tasks[i].number)
        begin.append(tasks[i].start)
        end.append(tasks[i].end)

    # task_arr = np.array(task)
    # begin_arr = np.array(begin)
    # end_arr = np.array(end)

    fig, ax = plt.subplots()

    for i in range(5):
        tmp = []
        for j in task:
            if(j == i+1):
                tmp.append((begin[j], end[j]-begin[j]))
        ax.broken_barh(tmp, (i*10, 9), facecolors=colors[i])

    ax.set_ylim(5, 35)
    ax.set_xlim(0, max(end)+1)
    ax.set_yticks([5, 15, 25, 35, 45])
    mylist = sorted(list(dict.fromkeys(task)))
    ax.set_yticklabels(mylist)

    # plt.barh(range(len(begin_arr)), end_arr-begin_arr, left=begin_arr)

    plt.ylabel("Task")
    # plt.yticks(range(len(begin_arr)), task_arr)
    # plt.xlim([0, max(end)+1])
    plt.show()
