from gui.update_fields import *
from gui.config import EventKey

def set_human_fields(window, values, tab_data, data):
    if len(values[EventKey.TABLE_HUMAN.value]) == 1:
        index = values[EventKey.TABLE_HUMAN.value][0]
        human_id = tab_data['human_list'][index][0]
        human = data['human_list'].get(human_id)
        room = data['room_list'].get(human['is_located_in'])
        update_human_fields(window, human['name'], room['name'], human['name'])
        return human_id
    else:
        return None


def set_room_fields(window, values, tab_data, data):
    if len(values[EventKey.TABLE_ROOM.value]) == 1:
        index = values[EventKey.TABLE_ROOM.value][0]
        room_id = tab_data['room_list'][index][0]
        room = data['room_list'].get(room_id)
        update_room_fields(window, room['name'], room['type'], room['name'])
        return room_id
    else:
        return None


def set_device_fields(window, values, tab_data, data):
    if len(values[EventKey.TABLE_DEVICE.value]) == 1:
        index = values[EventKey.TABLE_DEVICE.value][0]
        device_id = tab_data['device_list'][index][0]
        device = data['device_list'].get(device_id)
        room = data['room_list'].get(device['is_located_in'])
        update_device_fields(window, device['name'], device['type'], room['name'], device['name'])
        return device_id
    else:
        return None


def set_door_fields(window, values, tab_data, data):
    if len(values[EventKey.TABLE_DOOR.value]) == 1:
        index = values[EventKey.TABLE_DOOR.value][0]
        door_id = tab_data['door_list'][index][0]
        door = data['door_list'].get(door_id)
        is_open = True
        if door['is_open'] == 'false':
            is_open = False
        is_door_of_a = data['room_list'].get(door['is_door_of_A'])['name']
        is_door_of_b = 'None'
        if door['is_door_of_B'] != 'None':
            is_door_of_b = data['room_list'].get(door['is_door_of_B'])['name']
        update_door_fields(window, door['name'], is_open, is_door_of_a, is_door_of_b, door['name'])
        return door_id
    else:
        return None


def set_window_fields(window, values, tab_data, data):
    if len(values[EventKey.TABLE_WINDOW].value) == 1:
        index = values[EventKey.TABLE_WINDOW.value][0]
        window_id = tab_data['window_list'][index][0]
        room_window = data['window_list'].get(window_id)
        is_open = True
        if room_window['is_open'] == 'false':
            is_open = False
        is_window_of = data['room_list'].get(room_window['is_window_of'])['name']
        update_window_fields(window, room_window['name'], is_open, is_window_of, room_window['name'])
        return window_id
    else:
        return None
