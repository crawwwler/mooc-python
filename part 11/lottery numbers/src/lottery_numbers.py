class LotteryNumbers:
    def __init__(self, week: int, nums: list):
        self.week = week
        self.nums = nums
        self.matches = 0
    def number_of_hits(self, numbers: list):
        return len([n for n in numbers if n in self.nums])
    def hits_in_place(self, numbers: list):
        return [n if n in self.nums else -1 for n in numbers]

