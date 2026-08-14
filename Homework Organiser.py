import datetime as dt
import json


def show_homework():
    for x in homework_list:
        print(x)


def add_homework():
    homework_subject = str(input("Your homework subject:"))
    date = False
    
    while date == False:
        homework_due_date = input("Your homework due date (in the format YYYY-MM-DD):")
        
        try:
            homework_due_date_formatted = dt.datetime.strptime(homework_due_date, "%Y-%m-%d").date()
        
        except ValueError:
            print("Invalid date entered. Ensure date is in the format YYYY-MM-DD.")
            continue
        
        today = dt.date.today()
        
        if homework_due_date_formatted >= today:
            date = True
        else:
            print("Invalid date entered. Ensure date has not already passed.")

    homework_priority = str(input("Your homework priority: Options are [Low] or [Medium] or [High]")).lower()
    
    
    while homework_priority != 'low' and  homework_priority != 'medium' and  homework_priority != 'high':
        print("Invalid input entered.")
        print(homework_priority)
        homework_priority = str(input("Your homework priority: Options are [Low] or [Medium] or [High]")).lower()   
    
    homework_list.append({'subject': homework_subject, 'due date': homework_due_date, 'priority': homework_priority})
    
    homework_list.sort(key= lambda task:task['due date'])
    
    with open("To_Do_List.json", "w") as file:
        json.dump(homework_list, file)
    

again = True

homework_list = []

    
try:
    with open("To_Do_List.json", "r") as file:
        homework_list = json.load(file)
except FileNotFoundError:
    homework_list = []
    
    
while again == True:
    
    print("Menu:")
    print("Option 1: Show all homework")
    print("Option 2: Add a homework")
    print("Option 3: Exit")
    
    try:
        user_input = int(input("How could I help you? Only type the number:"))
        
    except ValueError:
        print("Inavlid input")
        continue

    if user_input == 1:
        show_homework()

    elif user_input == 2:
        add_homework()

    elif user_input == 3:
        again = False

    else:
        print("Invalid input")
        user_input = int(input("How could I help you? Only type the number:"))
        

        
    
