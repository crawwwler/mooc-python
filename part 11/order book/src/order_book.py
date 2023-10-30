class Task:
    id_count = 1
    def __init__(self, description: str, programmer: str, time: int, finished: bool = False):
        self._dsc = description
        self._prg = programmer
        self._time = time
        self._is_finished = finished
        self._id = Task.id_count
        Task.id_count += 1
    
    def __str__(self):
        finished = self._is_finished
        x = 'FINISHED' if finished else 'NOT FINISHED'
        return f"{self._id}: {self._dsc} ({self._time} hours), programmer {self._prg} {x}"
    
    @property
    def description(self):
        return self._dsc
    
    @property
    def programmer(self):
        return self._prg
    
    @property
    def id(self):
        return self._id
    
    def is_finished(self):
        return self._is_finished
    
    def mark_finished(self):
        self._is_finished = True

    @property
    def workload(self):
        return self._time


class OrderBook:
    def __init__(self):
        self._orders = []
        self._programmers = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        x = Task(description, programmer, workload)
        self._orders.append(x)
        self._programmers.append(programmer)
    
    def all_orders(self):
        return self._orders

    def programmers(self):
        return list(set(self._programmers))
    
    def mark_finished(self, id: int):
        for t in self.all_orders():
            if t.id == id :
                t.mark_finished()
                return True
        raise ValueError("ERROR!There's no such a task!")
    
    def finished_orders(self):
        return [t for t in self._orders if t.is_finished()]
    
    def unfinished_orders(self):
        return [t for t in self._orders if not t.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if len([p for p in self.programmers() if p == programmer]) == 0 :
            raise ValueError("ERROR!There's no such a programmer!")
        finished = [t for t in self.finished_orders() if t.programmer == programmer]
        unfinished = [t for t in self.unfinished_orders() if t.programmer == programmer]
        f = [0, 0]
        u = [0, 0]
        for t in finished:
            f[0] += 1
            f[1] += t.workload
        for t in unfinished:
            u[0] += 1
            u[1] += t.workload

        return (f[0], u[0], f[1], u[1])

    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i < len(self._orders):
            t = self._orders[self.i]
            self.i += 1
            return t
        else :
            raise StopIteration

