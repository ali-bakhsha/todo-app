import PySimpleGUI
import functions

lable = PySimpleGUI.Text("Type in a to-do")
textbox = PySimpleGUI.InputText(tooltip="Enter a Text" , key = "todo")
button = PySimpleGUI.Button("Add")
exit = PySimpleGUI.Button("Exit")
window = PySimpleGUI.Window("title",
                            font=('Helvetica' , 20),
                            layout=[[lable],[textbox , button], [exit]])


while True:
    event , values= window.read()
    match event:
       case "Add":
           todos = functions.get_todos()
           print(todos)
           todos.append(values['todo']+"\n")
           print(todos)
           functions.write_todos(todos)

       case "Exit":
           break;
       case PySimpleGUI.WINDOW_CLOSED:
           break
window.close()