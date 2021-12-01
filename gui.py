import PySimpleGUI as sg



tab1_humans_layout = [
                [sg.Text('Name', size=(15, 1)), sg.InputText()],
                [sg.Button(button_text='Save'), sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'), sg.Button(button_text='Delete')]
            ]
tab2_devices_layout = [
                [sg.Text('Device type', size=(15, 1)),
                 sg.InputCombo(('Laptop',
                                'Smartphone',
                                'Teapot'),
                               size=(20, 1), default_value='Smartphone'),
                 sg.Button(button_text='Add new type')],
                [sg.Text('Device name', size=(15, 1)), sg.InputText()],
                [sg.Button(button_text='Save'), sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'), sg.Button(button_text='Delete')]
            ]
tab3_rooms_layout = [
                [sg.Text('Room type', size=(15, 1)),
                 sg.InputCombo(('Bathroom',
                                'Bedroom',
                                'Childrensroom',
                                'Diningroom',
                                'Kitchen',
                                'Livingroom',
                                'Office',
                                'Outside'),
                               size=(20, 1), default_value='Bedroom'),
                 sg.Button(button_text='Add new type')],
                [sg.Text('Room name', size=(15, 1)), sg.InputText()],
                [sg.Button(button_text='Save'), sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'), sg.Button(button_text='Delete')]
        ]
tab4_doors_layout = [
                [sg.Text('Door between', size=(15, 1)),
                 sg.InputCombo(('A'),
                               size=(20, 1), default_value='A'),
                 sg.Text('and', size=(3, 1)),
                 sg.InputCombo(('B'),
                               size=(20, 1), default_value='B')
                 ],
                [sg.Text('Door name', size=(15, 1)), sg.InputText()],
                [sg.Text('Status', size=(15, 1)),
                    sg.Radio('Is Open', "RADIO_DOOR", size=(10,1)),
                    sg.Radio('Is Closed', "RADIO_DOOR", default=True)],
                [sg.Button(button_text='Save'), sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'), sg.Button(button_text='Delete')]
            ]
tab5_windows_layout = [
                [sg.Text('Window name', size=(15, 1)), sg.InputText()],
                [sg.Text('Status', size=(15, 1)),
                    sg.Radio('Is Open', "RADIO_WINDOW", size=(10,1)),
                    sg.Radio('Is Closed', "RADIO_WINDOW", default=True)],
                [sg.Button(button_text='Save'), sg.Button(button_text='Cancel'),
                 sg.Button(button_text='Add'), sg.Button(button_text='Delete')]
            ]

layout = [ [sg.TabGroup([[
                sg.Tab('Devices', tab2_devices_layout),
                sg.Tab('Rooms', tab3_rooms_layout),
                sg.Tab('Doors', tab4_doors_layout),
                sg.Tab('Windows', tab5_windows_layout)
                ]])],
            [sg.TabGroup([[
                sg.Tab('Humans', tab1_humans_layout)
                ]])]
        ]




window = sg.Window('SmartHome', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

window.close()