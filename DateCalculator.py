class DateCalculator:
    def __init__(self, year, month, day):
        if month == 1 or month == 2:
            month += 12
            year -= 1

            self.year = year
            self.month = month
            self.day = day

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        y = self.year
        k = y % 100
        j = y // 100

        h = (q + (13 *(m+1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]

if __name__ == "__main__":
        print("Enter a date to find the day of the week it is: ")
        try:
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))

            if not (1<= month <= 12):
                print("Invalid month. Please enter a valid number")
            elif not (1 <= day <= 31):
                print("Invalid day!!")
            else:
                calculator = DateCalculator(year, month, day)
                result = calculator.calculate_day_of_week()
                print(f"The day of the week for entered {day}/{month}/{year} is {result}.")
        except ValueError:
            print("Please enter numbers only!!")

