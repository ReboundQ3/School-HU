import PySimpleGUI as sg

value_list = [f'Listbox {i}' for i in range(1, 6)]
layout = [
    [sg.Listbox(value_list, size=(30, 5), font=("Courier New", 16), enable_events=True, key="-LISTBOX-")],
    [sg.StatusBar("", size=(30, 1), key='-STATUS-')],
]

window = sg.Window('Title', layout, finalize=True)
listbox, status = window['-LISTBOX-'], window['-STATUS-']

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '-LISTBOX-':
        selection = values[event]
        if selection:
            item = selection[0]
            index = listbox.get_indexes()[0]
            status.update(f'Line {index+1}, "{item}" selected')

window.close()