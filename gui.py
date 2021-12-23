import PySimpleGUI as sg
from config import connection as con
from db_funcs.select import *
from db_funcs.insert import *
from db_funcs.delete import *
from gui.set_fileds import *

def update_app():
    d = data()
    tab_data = convert_for_tab(data)

def update_connection_fields(object_id, object_class):
    if len(values['_table_human_row_']) == 1 and object_id is not None:
        table_row_index = values['_table_human_row_'][0]
        human_id = tab_data['human_list'][table_row_index][0]
        connection = get_connection(human_id, object_id).replace('_', ' ')
        available_connection_list = [c.replace('_', ' ') for c in con['human-' + object_class]]
        window['_connection_'].Update(value=connection, values=available_connection_list)

def get_id(table_row_name, list_name):
    if len(values[table_row_name]) == 1:
        index = values[table_row_name][0]
        id = tab_data[list_name][index][0]
        return id
    return None

def listen_event(event):
    if event == '_table_human_row_':
        set_human_fields(window, values, tab_data, data)
    elif event == '_table_device_row_':
        id = set_device_fields(window, values, tab_data, data)
        update_connection_fields(id, 'device')
    elif event == '_table_room_row_':
        id = set_room_fields(window, values, tab_data, data)
        update_connection_fields(id, 'room')
    elif event == '_table_door_row_':
        id = set_door_fields(window, values, tab_data, data)
        update_connection_fields(id, 'door')
    elif event == '_table_window_row_':
        id = set_window_fields(window, values, tab_data, data)
        update_connection_fields(id, 'window')

def listen_cancel_button_event(event):
    if event == '_human_cancel_btn_':
        set_human_fields(window, values, tab_data, data)
    elif event == '_device_cancel_btn_':
        set_device_fields(window, values, tab_data, data)
    elif event == '_room_cancel_btn_':
        set_room_fields(window, values, tab_data, data)
    elif event == '_door_cancel_btn_':
        set_door_fields(window, values, tab_data, data)
    elif event == '_window_cancel_btn_':
        set_window_fields(window, values, tab_data, data)
    # elif event == '_connection_cancel_btn_':
    #     set_connection_fields()
def listen_new_button_event(event):
    if event == '_human_new_btn_':
        update_human_fields(window, '', '', '')
    elif event == '_device_new_btn_':
        update_device_fields(window, '', '', '', '')
    elif event == '_room_new_btn_':
        update_room_fields(window, '', '', '')
    elif event == '_door_new_btn_':
        update_door_fields(window, '', False, '', '', '')
    elif event == '_window_new_btn_':
        update_window_fields(window, '', False, '', '')
def listen_add_button_event(event):
    if event == '_human_add_btn_':
        name = window['_human_name_'].get()
        room = window['_human_is_located_in_'].get()[0]
        room_id = data['reverse_room_list'][room]
        insert_human(name, room_id)
    elif event == '_device_add_btn_':
        name = window['_device_name_'].get()
        type = window['_device_type_'].get()[0]
        room = window['_device_is_located_in_'].get()[0]
        room_id = data['reverse_room_list'][room]
        insert_device(name, type, room_id)
    elif event == '_room_add_btn_':
        update_room_fields(window, '', '', '')
    elif event == '_door_add_btn_':
        update_door_fields(window, '', False, '', '', '')
    elif event == '_window_add_btn_':
        update_window_fields(window, '', False, '', '')

def listen_delete_button_event(event):
    if event == '_human_delete_btn_':
        id = get_id('_table_human_row_', 'human_list')
        name = data['human_list'].get(id)['name']
        is_located_in = data['human_list'].get(id)['is_located_in']
        delete_human(id, name, is_located_in)
    elif event == '_device_delete_btn_':
        delete_device('', '', '', '')
    elif event == '_room_delete_btn_':
        delete_room('', '', '')
    elif event == '_door_delete_btn_':
        delete_door('', False, '', [])
    elif event == '_window_delete_btn_':
        delete_window('', False, '', '')

def data():
    room_list = get_room_list()
    return {
        'human_list': get_human_list(),
        'device_list': get_device_list(),
        'room_list': room_list[0],
        'reverse_room_list': room_list[1],
        'door_list': get_door_list(),
        'window_list': get_window_list(),
        'device_type_list': get_device_type_list(),
        'room_type_list': get_room_type_list()
    }
def convert_for_tab(data):
    return {
        'human_list': [[human] for human in data['human_list']],
        'device_list': [[device] for device in data['device_list']],
        'room_list': [[room] for room in data['room_list']],
        'room_name_list': [[data['room_list'].get(room)['name']] for room in data['room_list']],
        'door_list': [[door] for door in data['door_list']],
        'window_list': [[window] for window in data['window_list']],
        'device_type_list': [[device_type] for device_type in data['device_type_list']],
        'room_type_list': [[room_type] for room_type in data['room_type_list']]
    }


data = data()
tab_data = convert_for_tab(data)


tab1_humans_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['human_list'], enable_events=True, key='_table_human_row_'),
                            sg.Frame('', [
                                [sg.Text('Human name', size=(15, 1)),
                                 sg.InputText(key='_human_name_', size=(30,1))],
                                [sg.Text('Is located in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_name_list'], size=(30, 1), readonly=True, enable_events=True, key='_human_is_located_in_')],
                                [sg.Button(button_text='Add', key='_human_add_btn_'), sg.Button(button_text='Save'), sg.Button(button_text='Cancel', key='_human_cancel_btn_')]
                            ])],
                            [sg.Button(button_text='New', key='_human_new_btn_'), sg.Button(button_text='Delete', key='_human_delete_btn_')]
                      ]
tab2_devices_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['device_list'], enable_events=True, key='_table_device_row_'),
                             sg.Frame('', [
                                [sg.Text('Device type', size=(15, 1)),
                                 sg.InputCombo(tab_data['device_type_list'], size=(30, 1), readonly=True, key='_device_type_'),
                                 sg.Button(button_text='Add new type')],
                                [sg.Text('Device name', size=(15, 1)),
                                 sg.InputText(size=(30,1), key='_device_name_')],
                                [sg.Text('Is located in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_name_list'], size=(30, 1), readonly=True, key='_device_is_located_in_')],
                                [sg.Button(button_text='Add', key='_device_add_btn_'), sg.Button(button_text='Save'), sg.Button(button_text='Cancel', key='_device_cancel_btn_')]
                            ])],
                            [sg.Button(button_text='New', key='_device_new_btn_'), sg.Button(button_text='Delete')]
                    ]
tab3_rooms_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['room_list'], enable_events=True, key='_table_room_row_'),
                            sg.Frame('', [
                                [sg.Text('Room type', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_type_list'], size=(30, 1), readonly=True, key='_room_type_')],
                                [sg.Text('Room name', size=(15, 1)),
                                 sg.InputText(key='_room_name_', size=(30,1))],
                                [sg.Button(button_text='Add', key='_room_add_btn_'), sg.Button(button_text='Save'), sg.Button(button_text='Cancel', key='_room_cancel_btn_')]
                            ])],
                            [sg.Button(button_text='New', key='_room_new_btn_'), sg.Button(button_text='Delete')]
                    ]
tab4_doors_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['door_list'], enable_events=True, key='_table_door_row_'),
                             sg.Frame('', [
                                [sg.Text('Door between', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_name_list'], size=(30, 1), readonly=True, key='_is_door_of_A_'),
                                 sg.Text('and', size=(3, 1)),
                                 sg.InputCombo(tab_data['room_name_list'], size=(30, 1), readonly=True, key='_is_door_of_B_')],
                                [sg.Text('Door name', size=(15, 1)),
                                 sg.InputText(key='_door_name_', size=(30,1))],
                                [sg.Text('Status', size=(15, 1)),
                                 sg.Radio('Is Open', "RADIO_DOOR", size=(10, 1), key='_door_is_open_'),
                                 sg.Radio('Is Closed', "RADIO_DOOR", default=True, key='_door_is_closed_')],
                                [sg.Button(button_text='Add', key='_door_add_btn_'), sg.Button(button_text='Save'), sg.Button(button_text='Cancel', key='_door_cancel_btn_')]
                            ])],
                            [sg.Button(button_text='New', key='_door_new_btn_'), sg.Button(button_text='Delete')]
                    ]
tab5_windows_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['window_list'], enable_events=True, key='_table_window_row_'),
                             sg.Frame('', [
                                [sg.Text('Window is in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_name_list'], size=(30, 1), readonly=True, key='_is_window_of_')],
                                [sg.Text('Window name', size=(15, 1)),
                                 sg.InputText(key='_window_name_', size=(30,1))],
                                [sg.Text('Status', size=(15, 1)),
                                 sg.Radio('Is Open', "RADIO_WINDOW", size=(10,1), key='_window_is_open_'),
                                 sg.Radio('Is Closed', "RADIO_WINDOW", default=True, key='_window_is_closed_')],
                                [sg.Button(button_text='Add', key='_window_add_btn_'), sg.Button(button_text='Save'), sg.Button(button_text='Cancel', key='_window_cancel_btn_')]
                            ])],
                            [sg.Button(button_text='New', key='_window_new_btn_'), sg.Button(button_text='Delete')]
                    ]
layout = [
    [sg.TabGroup([[sg.Tab('Devices', tab2_devices_layout),
                            sg.Tab('Rooms', tab3_rooms_layout),
                            sg.Tab('Doors', tab4_doors_layout),
                            sg.Tab('Windows', tab5_windows_layout)]])],
            [sg.Text('Human', size=(30, 1)), sg.Text('Connection', size=(30, 1)), sg.Text(''), sg.Text('Object', size=(30, 1))],
            [sg.InputText(size=(30,1), readonly=True, key='_connection_left_'),
             sg.InputCombo('', size=(30, 1), readonly=True, key='_connection_'),
             sg.InputText(size=(30,1), readonly=True, key='_connection_right_')],
            [sg.Button(button_text='Connect'),
             sg.Button(button_text='Disconnect')],
            [sg.TabGroup([[sg.Tab('Humans', tab1_humans_layout)]])]]

window = sg.Window('Smarthome+Stardog', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])

    listen_event(event)
    listen_cancel_button_event(event)
    listen_new_button_event(event)
    listen_add_button_event(event)
    listen_delete_button_event(event)

window.close()

