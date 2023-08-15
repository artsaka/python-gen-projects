class NumberList:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        # use a while loop to repeatedly prompt the user for input,
        # appending each number to a list until the user enters a non-numeric value ('q', in this case)
        while True:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            try:
                number = float(user_input)
                self.numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")

    def print_numbers(self):
        print(f"Numbers: {self.numbers}")

# Create an instance of the NumberList class and call its methods
number_list = NumberList()
number_list.get_numbers()
number_list.print_numbers()