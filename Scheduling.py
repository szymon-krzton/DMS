from Task import *
from math import gcd

class Scheduling():
    def __init__(self, tasks):
        self.tasks = tasks
        self.lcm = find_lcm(self.tasks)

    def sort_tasks(self):
        priority_list = sorted(self.tasks, key=lambda x: x.deadline)
        # for task in sorted_tasks:
        #     print(str(task.get_number())+"\t"+str(task.get_computingTime())+"\t"+str(task.get_deadline())+"\t"+str(task.get_period()))
        for i in range(self.lcm):
            if(i>0):
                for task in priority_list:
                    if((i%task.period)==0):
                        task.status = True

            for task in priority_list:
                if(task.deadline < ((i%task.deadline) + task.computingTime - 1) and task.status):
                    print(str(i) + " " + str(task.number))
                    return False
                
                if((task.deadline >= (i%task.deadline)) and task.status):
                    task.start = i
                    task.end = i+task.computingTime
                    task.status = False
                    i = i + task.computingTime - 1
                    break
        return priority_list


def find_lcm(list_of_tasks):
    list_of_deadlines = []
    for task in list_of_tasks:
        list_of_deadlines.append(task.get_deadline())
    lcm = 1
    for i in list_of_deadlines:
        lcm = lcm*i//gcd(lcm, i)
    return lcm