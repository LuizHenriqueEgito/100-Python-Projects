# Perform functions that perform queries on the database
import PySimpleGUI as sg

layout = [  [sg.Text('Icon Test')],
            [sg.Text(size=(25,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

sg.Window('Icon Test', layout, icon=r'M:\disco M\Python\PythonProjects\100-Python-Projects\02-SistemaDeLogin\src\program_image.ico').read(close=True)