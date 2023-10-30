def read_input(ask: str, num1: int, num2: int):
    while True:
        try:
            number = input(ask)
            number = int(number)
            if number >= num1 and number <= num2 :
                return number
        except:
            pass
            
        print(f"You must type in an integer between {num1} and {num2}")
