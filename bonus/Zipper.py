import PySimpleGUI
import PySimpleGUI as sg
import zip_creator
lable1 = sg.Text("Select files to complress:")
input1 = sg.InputText(tooltip="select files", key = 'files')
choose_button1 = sg.FilesBrowse("Choose", key = 'chooseFiles')

lable2 = sg.Text("Select destination folder:")
input2 = sg.InputText(tooltip="select folder" , key = 'folder')
choose_button2 = sg.FolderBrowse("Choose", key = 'chooseFolder')

compress_button = sg.Button("Compress")
output_lable = PySimpleGUI.Text(key = "output")
window = sg.Window("File Zipper",
                   layout=[[lable1, input1, choose_button1],
                           [lable2, input2, choose_button2],
                           [compress_button,output_lable]])

while True:
    events, values = window.read()
    print(events)
    print(values)
    filepath = values['chooseFiles'].split(";")
    folderpath = values['chooseFolder']
    print(filepath)
    match events:
        case 'Compress':
            zip_creator.make_archive(filepaths=filepath, dest_dir=folderpath)
            window["output"].update(value = "Compression Completed!")
window.close()

