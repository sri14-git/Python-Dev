# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import FreeSimpleGUI as sg

text=sg.Text("Hello world")
input_text=sg.InputText(tooltip="Enter Value",key="text")
done_button=sg.Button("Done")
window=sg.Window("My To-Do App",layout=[[text],[input_text,done_button]])
event,doc=window.read()
print(doc)
window.close()



