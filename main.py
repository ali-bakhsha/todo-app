#from modules.functions import get_todos,write_todos
import functions
import time


print("test")
print(f"It is {time.strftime('%b %d , %Y : %H:%M:%S')}")
todos = []
# print("HI Hi")
while True:
    user_action = input("Type add, show(display),edit, compelete or exit: ")
    user_action = user_action.strip()

    #if 'add' in user_action or 'new' in user_action :

    if user_action.startswith("add"):
        todo = user_action[4:]+'\n'
        todos = functions.get_todos()


        todos.append(todo)
        functions.write_todos(todos_arg=todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        print(todos)
        #file.close()

        #todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.title()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index = index -1
            new_todo = input("enter new todo: ")

            todos = function.get_todos(filepath='../files/todos.txt')

            todos[index] = new_todo+'\n'

            functions.write_todos(filepath='../files/todos.txt',todos_arg=todos)

        except ValueError:
            print("Your command is not valid.")
            continue;


    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos('../files/todos.txt')

            #index = int(input("enter a number of todo to compelete: "))
            index = int(user_action[9:])
            index = index-1

            removed_todos = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos_arg=todos)

            message = f"Todo '{removed_todos}' was removed from the list"
            print(message)
        except :
            print("invalid command or Data")
            continue
    elif user_action == 'exit':
        break
    else:
        print("incorrct command")


print("End")



