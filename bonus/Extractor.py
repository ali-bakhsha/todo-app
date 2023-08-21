import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

lable1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

lable2 = sg.Text("Select dest folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="dest_folder")

extract_button = sg.Button("Extract")
output_lable = sg.Text(key="output", text_color="green")

exit_button = sg.Button("Exit" , key = "exit")

window = sg.Window("File Zipper",
                   layout=[[lable1],
                           [input1 , choose_button1],
                           [lable2],
                           [input2 , choose_button2],
                           [extract_button , output_lable],
                                                      ])
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Extract":
            filpath = values["archive"]
            folderpath = values["dest_folder"]

            extract_archive(filpath , folderpath)
            window["output"].update(value="Extraction Completed")
        case sg.WINDOW_CLOSED:
            break;
window.close()
