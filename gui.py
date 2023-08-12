import functions
#import  PySimpleGUI as sg
import PySimpleGUI

lable = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter a code")
add_button = PySimpleGUI.Button("Add")
exit_button = PySimpleGUI.Button("Exit")


window = PySimpleGUI.Window('File Zipper', layout=[ [lable], [input_box, add_button] ] )


window.read()
window.close()


