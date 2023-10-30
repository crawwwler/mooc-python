class Course:
    def __init__(self, name: str, grade: int, credit: int):
        self._name = name
        self._grade = grade
        self._credit = credit
    
    @property
    def name(self):
        return self._name  
    @property
    def grade(self):
        return self._grade
    
    def set_grade(self, g: int):
        if self._grade > g :
            return
        self._grade = g
    @property
    def credit(self):
        return self._credit
    
    def __str__(self):
        return f"{self.name} ({self.credit} cr) grade {self.grade}"


class Info:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name: str, grade: int, credit: int):
        c = Course(name, grade, credit)
        if not name in self.__courses:
            self.__courses[name] = c
        self.__courses[name].set_grade(grade)
    def course_data(self, name: str):
        if not name in self.__courses:
            return None
        return self.__courses[name]
    
    def total_of_credits(self):
        total = 0
        for course in self.__courses.values():
            total += course.credit
        return total
    
    def average_of_grades(self):
        sum = 0
        for course in self.__courses.values():
            sum += course.grade
        return sum / len(self.__courses)
    
    def print_dis(self):
        dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for c in self.__courses.values():
            dic[c.grade] += 1
        for key, value in reversed(dic.items()):
            print(f"{key}:", "x"*value)
    
    def statistics(self):
        noc = f"{len(self.__courses)} completed courses"
        toc = self.total_of_credits()
        avg = self.average_of_grades()
        print(f"{noc}, a total of {toc} credits")
        print(f"mean {avg:.1f}")
        print("grade distribution")
        self.print_dis()


class UI():
    def __init__(self):
        self.info = Info()
    
    def menu(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.info.add_course(course, grade, credit)
    
    def desc(self):
        course = input("course: ")
        x = self.info.course_data(course)
        if x == None:
            print("no entry for this course")
            return
        print(x)

    def stats(self):
        self.info.statistics()

    def start(self):
        self.menu()
        while True:
            cmd = input("command: ")

            if cmd == "0":
                break
            if cmd == "1":
                self.add()
            if cmd == "2":
                self.desc()
            if cmd == "3":
                self.stats()




x = UI()
x.start()