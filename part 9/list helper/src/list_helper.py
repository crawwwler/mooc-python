class ListHelper:

    @classmethod
    def greatest_frequency(cls, x: list):
        dic = {}
        for i in x :
            dic[i] = 0
        for i in x:
            dic[i] += 1
        y = 0
        to_re = 0
        for key, value in dic.items():
            if value > y :
                y = value
                to_re = key
        return to_re
    
    @classmethod
    def doubles(cls, x: list):
        dic = {}
        for i in x :
            dic[i] = 0
        for i in x:
            dic[i] += 1
        y = 0
        for value in dic.values():
            if value > 1 :
                y += 1
        return y



