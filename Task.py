class Task():
    def __init__(self, number, computingTime, deadline, period):
        self.number = number
        self.computingTime = computingTime
        self.deadline = deadline
        self.period = period
        self.status = False
        self.start = 0
        self.end = 0

    def get_number(self):
        return self.number

    def get_computingTime(self):
        return self.computingTime

    def get_deadline(self):
        return self.deadline

    def get_period(self):
        return self.period