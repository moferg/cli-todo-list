# CLI TODO LIST - Marshall Ferguson - 7/2020

print("Welcome to the TODO List App!")

# TODO - Prompt the user to input some TODOs

todo_list = []
todo = input("Please enter a TODO to add to your list.     ")
todo_list.append(todo)

# TODO - Output the TODOs to the user

print(todo_list)

# TODO - Ask the user if they want to add more TODOs, check some off, or exit the app

user_choice = ''
while user_choice != 'exit':
    user_choice = input("Enter '1' to add more TODOs, '2' to check off TODOs, or 'exit' to exit the app.     ")
    if user_choice == '1':
        todo = input("Please enter a TODO to add to your list.     ")
        todo_list.append(todo)
    elif user_choice == '2':
        print(todo_list)
        print("Please enter the number of the TODO item to check off")
        todo_num = input("Only enter in a number. e.g. '1', '3', or '7'     ")
        todo_num = int(todo_num)
        todo_list.pop(todo_num - 1)
        print(todo_list)
    