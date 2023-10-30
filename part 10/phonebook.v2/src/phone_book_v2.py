
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, adrs: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(adrs)

    def get_entry(self, name: str):
        if (not name in self.__persons) or (len(self.__persons[name].numbers()) == 0):
            return None
        return self.__persons[name].numbers()
    
    def get_address(self, name: str):
        if (not name in self.__persons) or (self.__persons[name].address() == None):
            return None
        return self.__persons[name].address()

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        address = self.__phonebook.get_address(name)
        if numbers == None:
            print("number unknown")  
        else :
            for number in numbers:
                print(number)  
        if address == None:
            print("address unknown")
        else:
            print(address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self, name: str):
        self._name = name
        self._numbers = []
        self._address = None
    def add_number(self, number: str):
        if not number in self._numbers and number != "":
            self._numbers.append(number)

    def add_address(self, adrs: str):
        if adrs != "":
            self._address = adrs

    def name(self):
        return self._name
    def numbers(self):
        return self._numbers
    def address(self):
        if self._address == None:
            return None
        return self._address





# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()




