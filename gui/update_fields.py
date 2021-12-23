

def update_human_fields(window, name, is_located_in, connection):
    window['_human_name_'].Update(value=name)
    window['_human_is_located_in_'].Update(value=is_located_in)
    window['_connection_left_'].Update(value=connection)


def update_room_fields(window, name, type, connection):
    window['_room_name_'].Update(value=name)
    window['_room_type_'].Update(value=type)
    window['_connection_right_'].Update(value=connection)


def update_device_fields(window, name, type, is_located_in, connection):
    window['_device_name_'].Update(value=name)
    window['_device_type_'].Update(value=type)
    window['_device_is_located_in_'].Update(value=is_located_in)
    window['_connection_right_'].Update(value=connection)


def update_door_fields(window, name, is_open, is_door_of_a, is_door_of_b, connection):
    window['_door_name_'].Update(value=name)
    window['_door_is_open_'].Update(value=is_open)
    window['_door_is_closed_'].Update(value=is_open == False)
    window['_is_door_of_A_'].Update(value=is_door_of_a)
    window['_is_door_of_B_'].Update(value=is_door_of_b)
    window['_connection_right_'].Update(value=connection)


def update_window_fields(window, name, is_open, is_window_of, connection):
    window['_window_name_'].Update(value=name)
    window['_window_is_open_'].Update(value=is_open)
    window['_window_is_closed_'].Update(value=is_open == False)
    window['_is_window_of_'].Update(value=is_window_of)
    window['_connection_right_'].Update(value=connection)
