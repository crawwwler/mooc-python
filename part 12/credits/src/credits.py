from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda summ, item: summ + item.credits, attempts, 0)


def sum_of_passed_credits(attempts: list):
    return reduce(lambda summ, item: summ + item.credits, filter(lambda item: item.grade >= 1, attempts), 0)


def average(attempts: list):
    sumg = reduce(lambda summ, item: summ + item.grade, filter(lambda item: item.grade >= 1, attempts),0)
    return sumg / len(list(filter(lambda item: item.grade >=1, attempts)))

