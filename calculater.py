from datetime import datetime
import math


class Calculator:

    def __init__(self):
        self.history = []

        try:
            with open("history.txt", "r") as file:
                self.history = file.read().splitlines()
        except FileNotFoundError:
            pass

    def save_history(self, text):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry = (f"{time} {text}")

        self.history.append(entry)

        with open("history.txt", "a") as file:
            file.write(entry + "\n")

    def show_history(self):
        if self.history:
            print("\n===== HISTORY =====")
            for item in self.history:
                print(item)
        else:
            print("No History Found!")

    def clear_history(self):
        self.history.clear()

        with open("history.txt", "w"):
            pass

        print("History Cleared Successfully!")

    def calculate(self):

        while True:
            
            
            print("\n===== ADVANCED CALCULATOR =====")
            print("please enter the table no. not splilling")
            print("1. addition")
            print("2. subtraction")
            print("3. multiplication")
            print("4. division")
            print("5. percentage")
            print("6. square")
            print("7. cube")
            print("8. square root")
            print("9. power")
            print("10. modulus")
            print("11. show History")
            print("12. clear History")
            print("13. exit")
            

            choice = input("Enter Choice: ")

            if choice == "13":
                print("Thanks For Using Calculator!")
                break

            if choice == "11":
                self.show_history()
                continue

            if choice == "12":
                self.clear_history()
                continue

            try:

                if choice in ["6", "7", "8"]:
                    num = float(input("Enter Number: "))

                    if choice == "6":
                        result = num ** 2
                        text = f"{num}² = {result}"

                    elif choice == "7":
                        result = num ** 3
                        text = f"{num}³ = {result}"

                    elif choice == "8":
                        result = math.sqrt(num)
                        text = f"√{num} = {result}"

                else:

                    num1 = float(input("Enter First Number: "))
                    num2 = float(input("Enter Second Number: "))

                    if choice == "1":
                        result = num1 + num2
                        text = f"{num1} + {num2} = {result}"

                    elif choice == "2":
                        result = num1 - num2
                        text = f"{num1} - {num2} = {result}"

                    elif choice == "3":
                        result = num1 * num2
                        text = f"{num1} × {num2} = {result}"

                    elif choice == "4":
                        if num2 == 0:
                            print("Cannot Divide By Zero!")
                            continue

                        result = num1 / num2
                        text = f"{num1} ÷ {num2} = {result}"

                    elif choice == "5":
                        result = (num1 / num2) * 100
                        text = f"{result}%"

                    elif choice == "9":
                        result = num1 ** num2
                        text = f"{num1}^{num2} = {result}"

                    elif choice == "10":
                        result = num1 % num2
                        text = f"{num1} % {num2} = {result}"

                    else:
                        print("Invalid Choice!")
                        continue

                print("\nResult:", text)
                self.save_history(text)

            except ValueError:
                print("Please Enter Valid Number!")

            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    calc = Calculator()
    calc.calculate()