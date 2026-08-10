import datetime as dt
import json


def show_homework():
    for x in homework_list:
        print(x)


def add_homework():
    homework_subject = str(input("Your homework subject:"))
    
    homework_due_date = str(input("Your homework due date (in the format YYYY-MM-DD):"))
    homework_due_date_formatted = dt.datetime.strptime(homework_due_date, "%Y-%m-%d")

    homework_priority = str(input("Your homework priority:"))
    
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

    user_input = int(input("How could I help you? Only type the number:"))

    if user_input == 1:
        show_homework()

    elif user_input == 2:
        add_homework()

    elif user_input == 3:
        again = False

    else:
        print("Invalid input")
        user_input = int(input("How could I help you? Only type the number:"))
        

#Learnt how to create dictionary
#How to use datetime module 
#How to sort lists
#How to use a lambda expression
#How and when to use a json file
        
        
        #Next steps:
            #To delete a task
            #To retrieve certain tasks - like closest due date? highest priority? latest one added?
            #Maybe to choose how the list is sorted? - by subject? by due date? by priority?