import PySimpleGUI
import functions
import time

PySimpleGUI.theme("Black")

clock = PySimpleGUI.Text(key="clock")
lable = PySimpleGUI.Text("Type in a to-do")
lable_status = PySimpleGUI.Text(key = "lableStatus")
textbox = PySimpleGUI.InputText(tooltip="Enter a Text" , key = "todo")
button = PySimpleGUI.Button("Add")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key = 'todos' , enable_events=True, size =[45,10])
button_edit = PySimpleGUI.Button("Edit")
button_complete = PySimpleGUI.Button("Complete")

exit = PySimpleGUI.Button("Exit")

layout = [[clock],
          [lable],
          [textbox , button],
          [list_box , button_edit, button_complete],
          [exit,lable_status]]


window = PySimpleGUI.Window("title",
                            font=('Helvetica' , 20),
                            layout=layout)


while True:
    event , values= window.read(timeout=1000)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    #print(event)
    #print(values)
    match event:
       case "Add":
           todos = functions.get_todos()
           todos.append(values['todo']+"\n")
           functions.write_todos(todos)
           window['todos'].update(values=todos)
           window['todo'].update(value="")
       case "Complete":
           try:
               todo_to_complete = values['todos'][0]
               todos = functions.get_todos()

               todos.remove(todo_to_complete)
               functions.write_todos(todos)

               window['todos'].update(values=todos)
               window['todo'].update(value="")
           except IndexError:
               # window["lableStatus"].update(value ="Please select an item first")
               PySimpleGUI.popup("Please select an item first", font=('Helvetica', 20))
       case "Edit":
           try:
               todo_to_edit = values['todos'][0]
               todo_from_user = values['todo']
               todos = functions.get_todos()

               index = todos.index(todo_to_edit)
               todos[index] = todo_from_user+"\n"

               functions.write_todos(todos)
               window['todos'].update(values=todos)
           except IndexError:
               #window["lableStatus"].update(value ="Please select an item first")
               PySimpleGUI.popup("Please select an item first", font=('Helvetica' , 20))
       case 'todos':
           window['todo'].update(value=values['todos'][0])
        # window['todo'].update(values=)
       case "Exit":
           break;
       case PySimpleGUI.WINDOW_CLOSED:
           break
window.close()