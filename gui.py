import PySimpleGUI
import functions

lable = PySimpleGUI.Text("Type in a to-do")
textbox = PySimpleGUI.InputText(tooltip="Enter a Text" , key = "todo")
button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key = 'todos' , enable_events=True, size =[45,10])
button_edit = PySimpleGUI.Button("Edit")
button_complete = PySimpleGUI.Button("Complete")

exit = PySimpleGUI.Button("Exit")
layout = [[lable],
          [textbox , button],
          [list_box , button_edit, button_complete],
          [exit]]
button_lables = ["Add" , "Edit" , "Exit"]
window = PySimpleGUI.Window("title",
                            font=('Helvetica' , 20),
                            layout=layout)


while True:
    event , values= window.read()
    print(event)
    print(values)
    match event:
       case "Add":
           todos = functions.get_todos()
           todos.append(values['todo']+"\n")
           functions.write_todos(todos)
           window['todos'].update(values=todos)
           window['todo'].update(value="")
       case "Complete":
           todo_to_complete = values['todos'][0]
           todos = functions.get_todos()

           todos.remove(todo_to_complete)
           functions.write_todos(todos)

           window['todos'].update(values=todos)
           window['todo'].update(value="")

       case "Edit":
           todo_to_edit = values['todos'][0]
           todo_from_user = values['todo']
           todos = functions.get_todos()

           index = todos.index(todo_to_edit)
           todos[index] = todo_from_user+"\n"



           functions.write_todos(todos)
           window['todos'].update(values=todos)

       case 'todos':
           window['todo'].update(value=values['todos'][0])
        # window['todo'].update(values=)
       case "Exit":
           break;
       case PySimpleGUI.WINDOW_CLOSED:
           break
window.close()