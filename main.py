import PySimpleGUI as sg
from db_stardog.select import *
from db_stardog.insert import *
from db_stardog.delete import *
from db_stardog.update import *
from gui.set_fileds import *
from gui.config import TableEventKey, FieldEventKey, ButtonEventKey



def update_connection_fields():
    left_id = window[FieldEventKey.FIELD_CONNECTION_LEFT.value].get()
    right_id = window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].get()

    is_device = (data['device_list'].get(right_id) != None)
    is_door = (data['door_list'].get(right_id) != None)
    is_window = (data['window_list'].get(right_id) != None)
    is_room = (data['room_list'].get(right_id) != None)

    if is_device:
        window[FieldEventKey.FIELD_CONNECTION_NAME.value].Update(values=data['connection_list']['human-device'])
    elif is_door:
        window[FieldEventKey.FIELD_CONNECTION_NAME.value].Update(values=data['connection_list']['human-door'])
    elif is_window:
        window[FieldEventKey.FIELD_CONNECTION_NAME.value].Update(values=data['connection_list']['human-window'])
    elif is_room:
        window[FieldEventKey.FIELD_CONNECTION_NAME.value].Update(values=data['connection_list']['human-room'])


    if len(left_id) > 0 and len(right_id) > 0:
        connection = get_connection_for(left_id, right_id)
        window[FieldEventKey.FIELD_CONNECTION_NAME.value].Update(value=connection)


def listen_table_event(event):
    if event == TableEventKey.TABLE_HUMAN.value:
        set_human_fields(window, values, tab_data, data)
        update_connection_fields()
    elif event == TableEventKey.TABLE_DEVICE.value:
        set_device_fields(window, values, tab_data, data)
        update_connection_fields()
    elif event == TableEventKey.TABLE_ROOM.value:
        set_room_fields(window, values, tab_data, data)
        update_connection_fields()
    elif event == TableEventKey.TABLE_DOOR.value:
        set_door_fields(window, values, tab_data, data)
        update_connection_fields()
    elif event == TableEventKey.TABLE_WINDOW.value:
        set_window_fields(window, values, tab_data, data)
        update_connection_fields()


def listen_cancel_button_event(event):
    if event == ButtonEventKey.BUTTON_CANCEL_HUMAN.value:
        set_human_fields(window, values, tab_data, data)
    elif event == ButtonEventKey.BUTTON_CANCEL_DEVICE.value:
        set_device_fields(window, values, tab_data, data)
    elif event == ButtonEventKey.BUTTON_CANCEL_ROOM.value:
        set_room_fields(window, values, tab_data, data)
    elif event == ButtonEventKey.BUTTON_CANCEL_DOOR.value:
        set_door_fields(window, values, tab_data, data)
    elif event == ButtonEventKey.BUTTON_CANCEL_WINDOW.value:
        set_window_fields(window, values, tab_data, data)


def listen_new_button_event(event):
    if event == ButtonEventKey.BUTTON_NEW_HUMAN.value:
        update_human_fields(window, '', '', '')
    elif event == ButtonEventKey.BUTTON_NEW_DEVICE.value:
        update_device_fields(window, '', '', '', '')
    elif event == ButtonEventKey.BUTTON_NEW_ROOM.value:
        update_room_fields(window, '', '', '')
    elif event == ButtonEventKey.BUTTON_NEW_DOOR.value:
        update_door_fields(window, '', False, '', '', '')
    elif event == ButtonEventKey.BUTTON_NEW_WINDOW.value:
        update_window_fields(window, '', False, '', '')


def listen_add_button_event(event):
    if event == ButtonEventKey.BUTTON_ADD_HUMAN.value:
        name = window[FieldEventKey.FIELD_HUMAN_NAME.value].get()
        room_id = window[FieldEventKey.FIELD_HUMAN_LOCATION.value].get()[0]
        insert_human(name, room_id)
        return True
    elif event == ButtonEventKey.BUTTON_ADD_DEVICE.value:
        name = window[FieldEventKey.FIELD_DEVICE_NAME.value].get()
        type = window[FieldEventKey.FIELD_DEVICE_TYPE.value].get()[0]
        room_id = window[FieldEventKey.FIELD_DEVICE_LOCATION.value].get()[0]
        insert_device(name, type, room_id)
        return True
    elif event == ButtonEventKey.BUTTON_ADD_ROOM.value:
        name = window[FieldEventKey.FIELD_ROOM_NAME.value].get()
        type = window[FieldEventKey.FIELD_ROOM_TYPE.value].get()[0]
        insert_room(name, type)
        return True
    elif event == ButtonEventKey.BUTTON_ADD_DOOR.value:
        name = window[FieldEventKey.FIELD_DOOR_NAME.value].get()
        is_open = window[FieldEventKey.FIELD_DOOR_IS_OPEN.value].get()
        is_door_of_list = [window[FieldEventKey.FIELD_DOOR_ROOM_A.value].get()[0],
                           window[FieldEventKey.FIELD_DOOR_ROOM_B.value].get()[0]]
        insert_door(name, is_open, is_door_of_list)
        return True
    elif event == ButtonEventKey.BUTTON_ADD_WINDOW.value:
        name = window[FieldEventKey.FIELD_WINDOW_NAME.value].get()
        is_open = window[FieldEventKey.FIELD_WINDOW_IS_OPEN.value].get()
        is_window_of_list = [window[FieldEventKey.FIELD_WINDOW_ROOM.value].get()[0]]
        insert_window(name, is_open, is_window_of_list)
        return True


def listen_delete_button_event(event):
    if event == ButtonEventKey.BUTTON_DELETE_HUMAN.value:
        if len(values[TableEventKey.TABLE_HUMAN.value]) == 1:
            index = values[TableEventKey.TABLE_HUMAN.value][0]
            id = tab_data['human_list'][index][0]
            delete_human(id)
            return True
    elif event == ButtonEventKey.BUTTON_DELETE_DEVICE.value:
        if len(values[TableEventKey.TABLE_DEVICE.value]) == 1:
            index = values[TableEventKey.TABLE_DEVICE.value][0]
            id = tab_data['device_list'][index][0]
            delete_device(id)
            return True
    # if event == ButtonEventKey.BUTTON_DELETE_ROOM.value:
    #     if len(values[TableEventKey.TABLE_ROOM.value]) == 1:
    #         index = values[TableEventKey.TABLE_ROOM.value][0]
    #         id = tab_data['room_list'][index][0]
    #         delete_room(id)
    #         return True
    elif event == ButtonEventKey.BUTTON_DELETE_DOOR.value:
        if len(values[TableEventKey.TABLE_DOOR.value]) == 1:
            index = values[TableEventKey.TABLE_DOOR.value][0]
            id = tab_data['door_list'][index][0]
            delete_door(id)
            return True
    elif event == ButtonEventKey.BUTTON_DELETE_WINDOW.value:
        if len(values[TableEventKey.TABLE_WINDOW.value]) == 1:
            index = values[TableEventKey.TABLE_WINDOW.value][0]
            id = tab_data['window_list'][index][0]
            delete_door(id)
            return True


def listen_connect_button_event(event):
    left_id = window[FieldEventKey.FIELD_CONNECTION_LEFT.value].get()
    connection = window[FieldEventKey.FIELD_CONNECTION_NAME.value].get().replace(' ', '_')
    right_id = window[FieldEventKey.FIELD_CONNECTION_RIGHT.value].get()

    is_room = (data['room_list'].get(right_id) != None)

    if len(left_id) > 0 and not is_room:
        if event == ButtonEventKey.BUTTON_CONNECT.value:
            insert_connection(left_id, connection, right_id)
            update_connection_fields()
        elif event == ButtonEventKey.BUTTON_DISCONNECT.value:
            delete_connection(left_id, right_id)
            update_connection_fields()


def listen_save_button_event(event):
    if event == ButtonEventKey.BUTTON_SAVE_HUMAN.value:
        index = values[TableEventKey.TABLE_HUMAN.value][0]     #///////////////////////////////////////////////////////////////////
        human_id = tab_data['human_list'][index][0]
        old_data = {'name': data['human_list'].get(human_id)['name'],
                    'is_located_in':data['human_list'].get(human_id)['is_located_in']}
        name = window[FieldEventKey.FIELD_HUMAN_NAME.value].get()
        room_id = window[FieldEventKey.FIELD_HUMAN_LOCATION.value].get()[0]
        update_human(old_data, human_id, name, room_id)
        return True
    elif event == ButtonEventKey.BUTTON_SAVE_DEVICE.value:
        index = values[TableEventKey.TABLE_DEVICE.value][0]  # ///////////////////////////////////////////////////////////////////
        device_id = tab_data['device_list'][index][0]
        old_data = {'name': data['device_list'].get(device_id)['name'],
                    'type': data['device_list'].get(device_id)['type'],
                    'is_located_in': data['device_list'].get(device_id)['is_located_in']}
        name = window[FieldEventKey.FIELD_DEVICE_NAME.value].get()
        type = window[FieldEventKey.FIELD_DEVICE_TYPE.value].get()[0]
        room_id = window[FieldEventKey.FIELD_DEVICE_LOCATION.value].get()[0]
        update_device(old_data, device_id, name, type, room_id)
        return True
    elif event == ButtonEventKey.BUTTON_SAVE_ROOM.value:
        index = values[TableEventKey.TABLE_ROOM.value][0]  # ///////////////////////////////////////////////////////////////////
        room_id = tab_data['room_list'][index][0]
        old_data = {'name': data['room_list'].get(room_id)['name'],
                    'type': data['room_list'].get(room_id)['type']}
        name = window[FieldEventKey.FIELD_ROOM_NAME.value].get()
        type = window[FieldEventKey.FIELD_ROOM_TYPE.value].get()[0]
        update_room(old_data, room_id, name, type)
        return True
    elif event == ButtonEventKey.BUTTON_SAVE_DOOR.value:
        index = values[TableEventKey.TABLE_DOOR.value][0]  # ///////////////////////////////////////////////////////////////////
        door_id = tab_data['door_list'][index][0]
        old_data = {'name': data['door_list'].get(door_id)['name'],
                    'is_open': data['door_list'].get(door_id)['is_open'],
                    'is_door_of_list': [data['door_list'].get(door_id)['is_door_of_A'], data['door_list'].get(door_id)['is_door_of_B']]}
        name = window[FieldEventKey.FIELD_ROOM_NAME.value].get()
        is_open = window[FieldEventKey.FIELD_DOOR_IS_OPEN.value].get()
        is_door_of_list = [window[FieldEventKey.FIELD_DOOR_ROOM_A.value].get()[0],
                           window[FieldEventKey.FIELD_DOOR_ROOM_B.value].get()[0]]
        update_door(old_data, door_id, name, is_open, is_door_of_list)
        return True
    elif event == ButtonEventKey.BUTTON_SAVE_WINDOW.value:
        index = values[TableEventKey.TABLE_WINDOW.value][0]  # ///////////////////////////////////////////////////////////////////
        window_id = tab_data['window_list'][index][0]
        old_data = {'name': data['window_list'].get(window_id)['name'],
                    'is_open': data['window_list'].get(window_id)['is_open'],
                    'is_window_of_list': [data['window_list'].get(window_id)['is_window_of']]}
        name = window[FieldEventKey.FIELD_WINDOW_NAME.value].get()
        is_open = window[FieldEventKey.FIELD_WINDOW_IS_OPEN.value].get()
        is_window_of_list = [window[FieldEventKey.FIELD_WINDOW_ROOM.value].get()[0]]
        update_window(old_data, window_id, name, is_open, is_window_of_list)
        return True


def get_actual_data():
    return {
        'human_list': get_human_list(),
        'device_list': get_device_list(),
        'room_list': get_room_list(),
        'door_list': get_door_list(),
        'window_list': get_window_list(),
        'device_type_list': get_device_type_list(),
        'room_type_list': get_room_type_list(),
        'connection_list': get_connection_list()
    }


def convert_for_tab(data):
    return {
        'human_list': [[human] for human in data['human_list']],
        'device_list': [[device] for device in data['device_list']],
        'room_list': [[room] for room in data['room_list']],
        'door_list': [[door] for door in data['door_list']],
        'window_list': [[window] for window in data['window_list']],
        'device_type_list': [[device_type] for device_type in data['device_type_list']],
        'room_type_list': [[room_type] for room_type in data['room_type_list']]
    }


data = get_actual_data()
tab_data = convert_for_tab(data)


def update_app_data():

    d = get_actual_data()
    t_d = convert_for_tab(d)

    update_human_fields(window, '', '', '')
    update_device_fields(window, '', '', '', '')
    update_room_fields(window, '', '', '')
    update_door_fields(window, '', False, '', '', '')
    update_window_fields(window, '', False, '', '')

    window[TableEventKey.TABLE_HUMAN.value].Update(values=t_d['human_list'])
    window[TableEventKey.TABLE_DEVICE.value].Update(values=t_d['device_list'])
    window[TableEventKey.TABLE_ROOM.value].Update(values=t_d['room_list'])
    window[TableEventKey.TABLE_DOOR.value].Update(values=t_d['door_list'])
    window[TableEventKey.TABLE_WINDOW.value].Update(values=t_d['window_list'])

    window[FieldEventKey.FIELD_HUMAN_LOCATION.value].Update(values=t_d['room_list'])
    window[FieldEventKey.FIELD_DEVICE_LOCATION.value].Update(values=t_d['room_list'])
    window[FieldEventKey.FIELD_DOOR_ROOM_A.value].Update(values=t_d['room_list'])
    window[FieldEventKey.FIELD_DOOR_ROOM_B.value].Update(values=t_d['room_list'])
    window[FieldEventKey.FIELD_WINDOW_ROOM.value].Update(values=t_d['room_list'])

    return d


tab1_humans_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['human_list'], enable_events=True,
                                      key=TableEventKey.TABLE_HUMAN.value),
                            sg.Frame('', [
                                [sg.Text('Human name', size=(15, 1)),
                                 sg.InputText(key=FieldEventKey.FIELD_HUMAN_NAME.value, size=(30, 1))],
                                [sg.Text('Is located in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_list'], size=(30, 1), readonly=True,
                                               enable_events=True, key=FieldEventKey.FIELD_HUMAN_LOCATION.value)],
                                [sg.Button(button_text='Add', key=ButtonEventKey.BUTTON_ADD_HUMAN.value),
                                 sg.Button(button_text='Save', key=ButtonEventKey.BUTTON_SAVE_HUMAN.value),
                                 sg.Button(button_text='Cancel', key=ButtonEventKey.BUTTON_CANCEL_HUMAN.value)]
                            ])],
                            [sg.Button(button_text='New', key=ButtonEventKey.BUTTON_NEW_HUMAN.value),
                             sg.Button(button_text='Delete', key=ButtonEventKey.BUTTON_DELETE_HUMAN.value)]
                      ]
tab2_devices_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['device_list'],
                                      enable_events=True, key=TableEventKey.TABLE_DEVICE.value),
                             sg.Frame('', [
                                [sg.Text('Device type', size=(15, 1)),
                                 sg.InputCombo(tab_data['device_type_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_DEVICE_TYPE.value),
                                 #sg.Button(button_text='Add new type')
                                 ],
                                [sg.Text('Device name', size=(15, 1)),
                                 sg.InputText(size=(30,1), key=FieldEventKey.FIELD_DEVICE_NAME.value)],
                                [sg.Text('Is located in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_DEVICE_LOCATION.value)],
                                [sg.Button(button_text='Add', key=ButtonEventKey.BUTTON_ADD_DEVICE.value),
                                 sg.Button(button_text='Save', key=ButtonEventKey.BUTTON_SAVE_DEVICE.value),
                                 sg.Button(button_text='Cancel', key=ButtonEventKey.BUTTON_CANCEL_DEVICE.value)]
                            ])],
                            [sg.Button(button_text='New', key=ButtonEventKey.BUTTON_NEW_DEVICE.value),
                             sg.Button(button_text='Delete', key=ButtonEventKey.BUTTON_DELETE_DEVICE.value)]
                    ]
tab3_rooms_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['room_list'],
                                      enable_events=True, key=TableEventKey.TABLE_ROOM.value),
                            sg.Frame('', [
                                [sg.Text('Room type', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_type_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_ROOM_TYPE.value)],
                                [sg.Text('Room name', size=(15, 1)),
                                 sg.InputText(key=FieldEventKey.FIELD_ROOM_NAME.value, size=(30, 1))],
                                [sg.Button(button_text='Add', key=ButtonEventKey.BUTTON_ADD_ROOM.value),
                                 sg.Button(button_text='Save', key=ButtonEventKey.BUTTON_SAVE_ROOM.value),
                                 sg.Button(button_text='Cancel', key=ButtonEventKey.BUTTON_CANCEL_ROOM.value)]
                            ])],
                            [sg.Button(button_text='New', key=ButtonEventKey.BUTTON_NEW_ROOM.value),
                             # sg.Button(button_text='Delete', key=ButtonEventKey.BUTTON_DELETE_ROOM.value)
                             ]
                    ]
tab4_doors_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['door_list'],
                                      enable_events=True, key=TableEventKey.TABLE_DOOR.value),
                             sg.Frame('', [
                                [sg.Text('Door between', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_DOOR_ROOM_A.value),
                                 sg.Text('and', size=(3, 1)),
                                 sg.InputCombo(tab_data['room_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_DOOR_ROOM_B.value)],
                                [sg.Text('Door name', size=(15, 1)),
                                 sg.InputText(key=FieldEventKey.FIELD_DOOR_NAME.value, size=(30, 1))],
                                [sg.Text('Status', size=(15, 1)),
                                 sg.Radio('Is Open', 'RADIO_DOOR', size=(10, 1), key=FieldEventKey.FIELD_DOOR_IS_OPEN.value),
                                 sg.Radio('Is Closed', 'RADIO_DOOR', default=True, key=FieldEventKey.FIELD_DOOR_IS_CLOSE.value)],
                                 [sg.Button(button_text='Add', key=ButtonEventKey.BUTTON_ADD_DOOR.value),
                                  sg.Button(button_text='Save', key=ButtonEventKey.BUTTON_SAVE_DOOR.value),
                                  sg.Button(button_text='Cancel', key=ButtonEventKey.BUTTON_CANCEL_DOOR.value)]
                             ])],
                            [sg.Button(button_text='New', key=ButtonEventKey.BUTTON_NEW_DOOR.value),
                             sg.Button(button_text='Delete', key=ButtonEventKey.BUTTON_DELETE_DOOR.value)]
                    ]
tab5_windows_layout = [
                            [sg.Table(headings=['Actual'], values=tab_data['window_list'],
                                      enable_events=True, key=TableEventKey.TABLE_WINDOW.value),
                             sg.Frame('', [
                                [sg.Text('Window is in', size=(15, 1)),
                                 sg.InputCombo(tab_data['room_list'], size=(30, 1),
                                               readonly=True, key=FieldEventKey.FIELD_WINDOW_ROOM.value)],
                                [sg.Text('Window name', size=(15, 1)),
                                 sg.InputText(key=FieldEventKey.FIELD_WINDOW_NAME.value, size=(30, 1))],
                                [sg.Text('Status', size=(15, 1)),
                                 sg.Radio('Is Open', "RADIO_WINDOW", size=(10,1), key=FieldEventKey.FIELD_WINDOW_IS_OPEN.value),
                                 sg.Radio('Is Closed', "RADIO_WINDOW", default=True, key=FieldEventKey.FIELD_WINDOW_IS_CLOSE.value)],
                                 [sg.Button(button_text='Add', key=ButtonEventKey.BUTTON_ADD_WINDOW.value),
                                  sg.Button(button_text='Save', key=ButtonEventKey.BUTTON_SAVE_WINDOW.value),
                                  sg.Button(button_text='Cancel', key=ButtonEventKey.BUTTON_CANCEL_WINDOW.value)]])
                            ],
                            [sg.Button(button_text='New', key=ButtonEventKey.BUTTON_NEW_WINDOW.value),
                             sg.Button(button_text='Delete', key=ButtonEventKey.BUTTON_DELETE_WINDOW.value)]
                    ]
layout = [
            [sg.TabGroup([[sg.Tab('Devices', tab2_devices_layout),
                            sg.Tab('Rooms', tab3_rooms_layout),
                            sg.Tab('Doors', tab4_doors_layout),
                            sg.Tab('Windows', tab5_windows_layout)]])],
            [sg.Text('Human', size=(30, 1)),
             sg.Text('Connection', size=(30, 1)),
             sg.Text(''),
             sg.Text('Object', size=(30, 1))],
            [sg.InputText(size=(30,1), readonly=True, key=FieldEventKey.FIELD_CONNECTION_LEFT.value),
             sg.InputCombo([], size=(30, 1), readonly=True, key=FieldEventKey.FIELD_CONNECTION_NAME.value),
             sg.InputText(size=(30,1), readonly=True, key=FieldEventKey.FIELD_CONNECTION_RIGHT.value)],
            [sg.Button(button_text='Connect', key=ButtonEventKey.BUTTON_CONNECT.value),
             sg.Button(button_text='Disconnect', key=ButtonEventKey.BUTTON_DISCONNECT.value)],
            [sg.TabGroup([[sg.Tab('Humans', tab1_humans_layout)]])]]

window = sg.Window('Smart-home', layout)
update = False

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    listen_table_event(event)
    listen_cancel_button_event(event)
    listen_new_button_event(event)
    update = (listen_save_button_event(event) or update)
    update = (listen_add_button_event(event) or update)
    update = (listen_delete_button_event(event) or update)
    update = (listen_connect_button_event(event) or update)

    if update:
        data = update_app_data()
        tab_data = convert_for_tab(data)
        update = False

window.close()

