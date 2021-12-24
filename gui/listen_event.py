# from gui.update_fields import *
# from gui.set_fileds import *
# from db_stardog.insert import *
# from db_stardog.delete import *
#
# def get_id(values, tab_data, table_row_name, list_name):
#     if len(values[table_row_name]) == 1:
#         index = values[table_row_name][0]
#         id = tab_data[list_name][index][0]
#         return id
#     return None
#
# def listen_event(window, values, event, tab_data, data):
#     if event == '_table_human_row_':
#         set_human_fields(window, values, tab_data, data)
#     elif event == '_table_device_row_':
#         id = set_device_fields(window, values, tab_data, data)
#         update_connection_fields(id, 'device')
#     elif event == '_table_room_row_':
#         id = set_room_fields(window, values, tab_data, data)
#         update_connection_fields(id, 'room')
#     elif event == '_table_door_row_':
#         id = set_door_fields(window, values, tab_data, data)
#         update_connection_fields(id, 'door')
#     elif event == '_table_window_row_':
#         id = set_window_fields(window, values, tab_data, data)
#         update_connection_fields(id, 'window')
#
# def listen_cancel_button_event(window, values, event, tab_data, data):
#     if event == '_human_cancel_btn_':
#         set_human_fields(window, values, tab_data, data)
#     elif event == '_device_cancel_btn_':
#         set_device_fields(window, values, tab_data, data)
#     elif event == '_room_cancel_btn_':
#         set_room_fields(window, values, tab_data, data)
#     elif event == '_door_cancel_btn_':
#         set_door_fields(window, values, tab_data, data)
#     elif event == '_window_cancel_btn_':
#         set_window_fields(window, values, tab_data, data)
#     # elif event == '_connection_cancel_btn_':
#     #     set_connection_fields()
# def listen_new_button_event(window, values, event, tab_data, data):
#     if event == '_human_new_btn_':
#         update_human_fields(window, '', '', '')
#     elif event == '_device_new_btn_':
#         update_device_fields(window, '', '', '', '')
#     elif event == '_room_new_btn_':
#         update_room_fields(window, '', '', '')
#     elif event == '_door_new_btn_':
#         update_door_fields(window, '', False, '', '', '')
#     elif event == '_window_new_btn_':
#         update_window_fields(window, '', False, '', '')
# def listen_add_button_event(window, values, event, tab_data, data):
#     if event == '_human_add_btn_':
#         name = window['_human_name_'].get()
#         room = window['_human_is_located_in_'].get()[0]
#         room_id = data['reverse_room_list'][room]
#         insert_human(name, room_id)
#     elif event == '_device_add_btn_':
#         name = window['_device_name_'].get()
#         type = window['_device_type_'].get()[0]
#         room = window['_device_is_located_in_'].get()[0]
#         room_id = data['reverse_room_list'][room]
#         insert_device(name, type, room_id)
#     elif event == '_room_add_btn_':
#         update_room_fields(window, '', '', '')
#     elif event == '_door_add_btn_':
#         update_door_fields(window, '', False, '', '', '')
#     elif event == '_window_add_btn_':
#         update_window_fields(window, '', False, '', '')
# # def listen_delete_button_event(event, tab_data, data):
# #     if event == '_human_delete_btn_':
# #         id = get_id('_table_human_row_', 'human_list')
# #         name = data['human_list'].get(id)['name']
# #         is_located_in = data['human_list'].get(id)['is_located_in']
# #         delete_human(id, name, is_located_in)
# #     elif event == '_device_delete_btn_':
# #         delete_device('', '', '', '')
# #     elif event == '_room_delete_btn_':
# #         delete_room('', '', '')
# #     elif event == '_door_delete_btn_':
# #         delete_door('', False, '', [])
# #     elif event == '_window_delete_btn_':
# #         delete_window('', False, '', '')