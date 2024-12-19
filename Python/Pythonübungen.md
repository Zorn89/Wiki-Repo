# Übungen zu Python

## aktuelles Datum

import datetime

x = datetime.datetime.now()

print(x) 

## Tage bis zum Jahresende 


def end_of_year(year):
    today = datetime.date.today()
    diff = year.replace(year=today.year) - today
    if diff.days < 0:
        diff = year.replace(year=today.year + 1) - today
    return diff.days


def main():
    days = end_of_year(datetime.date(2024,12,31))
    print(f"Es sind noch {days} Tage bis Jahresende ")

  

if __name__ == '__main__':
    main()


## Taschenrechner

def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multi(x,y):
    return x * y
def div(x,y):
    return x / y


# def calculator (add, substrakt, mult, div): 

user_input = input("Wähle eine Grundrechenart (add, substrakt, mult, div): ")
result = (user_input)


user_input_1 = float(input("Gib mir eine Zahl: "))
result = (user_input_1)


user_input_2 = float(input("Gib mir weitere eine Zahl: "))
result = float(user_input_2)

user_input_1 = int(user_input_1)
user_input_2 = int(user_input_2)


if user_input == "add":
    print(f"Ergebnis: {user_input_1 + user_input_2}")
elif user_input == "substrakt":
    print(f"Ergebnis: {user_input_1 - user_input_2}")
elif user_input == "mult":
    print(f"Ergebnis: {user_input_1 * user_input_2}")
elif user_input == "div":
    print(f"Ergebnis: {user_input_1 / user_input_2}")