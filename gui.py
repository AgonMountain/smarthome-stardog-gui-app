import PySimpleGUI as sg

device_types = ('Laptop', 'Smartphone', 'Teapot')
room_types = ('Bathroom', 'Bedroom', 'Children\'s room', 'Dining room', 'Kitchen', 'Living room', 'Office', 'Outside')

actual_humans = [['yury kiselev'], ['victor noskin']]
actual_devices = [['laptop1'], ['laptop2']]
actual_rooms = [['room1'], ['room2']]
actual_doors = [['door1'], ['door2']]
actual_windows = [['window1'], ['window2']]


tab1_humans_layout = [
                [sg.Table(headings=['Actual'], values=actual_humans)],
                [sg.Text('Name', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Is now in (room)', size=(15, 1)),
                 sg.InputCombo(actual_rooms, size=(20, 1), default_value='????')],
                [sg.Button(button_text='Save'),
                 sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'),
                 sg.Button(button_text='Delete')]
            ]
tab2_devices_layout = [
                [sg.Table(headings=['Actual'], values=actual_devices)],
                [sg.Text('Device type', size=(15, 1)),
                 sg.InputCombo(device_types, size=(20, 1), default_value=device_types[0]),
                 sg.Button(button_text='Add new type')],
                [sg.Text('Device name', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Is now in (room)', size=(15, 1)),
                 sg.InputCombo(actual_rooms, size=(20, 1), default_value='????')],
                [sg.Button(button_text='Save'),
                 sg.Button(button_text='Cancel')]
            ]
tab3_rooms_layout = [
                [sg.Table(headings=['Actual'], values=actual_rooms)],
                [sg.Text('Room type', size=(15, 1)),
                 sg.InputCombo(room_types, size=(20, 1), default_value=room_types[0]),
                 sg.Button(button_text='Add new type')],
                [sg.Text('Room name', size=(15, 1)),
                 sg.InputText()],
                [sg.Button(button_text='Save'),
                 sg.Button(button_text='Cancel')]
        ]
tab4_doors_layout = [
                [sg.Table(headings=['Actual'], values=actual_doors)],
                [sg.Text('Door between', size=(15, 1)),
                 sg.InputCombo('????', size=(20, 1), default_value='????'),
                 sg.Text('and', size=(3, 1)),
                 sg.InputCombo('????', size=(20, 1), default_value='????')],
                [sg.Text('Door name', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Status', size=(15, 1)),
                 sg.Radio('Is Open', "RADIO_DOOR", size=(10, 1)),
                 sg.Radio('Is Closed', "RADIO_DOOR", default=True)],
                [sg.Button(button_text='Save'),
                 sg.Button(button_text='Cancel')]
            ]
tab5_windows_layout = [
                [sg.Table(headings=['Actual'], values=actual_windows)],
                [sg.Text('Window is in', size=(15, 1)),
                 sg.InputCombo('????', size=(20, 1), default_value='????')],
                [sg.Text('Window name', size=(15, 1)),
                 sg.InputText()],
                [sg.Text('Status', size=(15, 1)),
                 sg.Radio('Is Open', "RADIO_WINDOW", size=(10,1)),
                 sg.Radio('Is Closed', "RADIO_WINDOW", default=True)],
                [sg.Button(button_text='Save'),
                 sg.Button(button_text='Cancel')]
            ]

layout = [[sg.TabGroup([[sg.Tab('Devices', tab2_devices_layout),
                            sg.Tab('Rooms', tab3_rooms_layout),
                            sg.Tab('Doors', tab4_doors_layout),
                            sg.Tab('Windows', tab5_windows_layout)]])],
            [sg.InputCombo('????', size=(40, 1), default_value='????'),
             sg.Button(button_text='Connect'),
             sg.Button(button_text='Disconnect')],
            [sg.TabGroup([[sg.Tab('Humans', tab1_humans_layout)]])]]




window = sg.Window('SmartHome', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()