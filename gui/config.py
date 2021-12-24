from enum import Enum


class EventKey(Enum):

  TABLE_HUMAN = '_table_human_row_'
  TABLE_DEVICE = '_table_device_row_'
  TABLE_ROOM = '_table_room_row_'
  TABLE_DOOR = '_table_door_row_'
  TABLE_WINDOW = '_table_window_row_'
  BUTTON_NEW = '_button_new_'
  BUTTON_ADD = '_button_add_'
  BUTTON_SAVE = '_button_save_'
  BUTTON_UPDATE = '_button_update_'
  BUTTON_CANCEL = '_button_cancel_'
  BUTTON_DELETE = '_button_delete_'
  BUTTON_CONNECT = '_button_connect_'
  BUTTON_DISCONNECT = '_button_disconnect_'
  FIELD_HUMAN_NAME = '_field_human_name_'
  FIELD_HUMAN_LOCATION = '_field_human_location_'
  FIELD_DEVICE_TYPE = '_field_device_type_'
  FIELD_DEVICE_NAME = '_field_device_name_'
  FIELD_DEVICE_LOCATION = '_field_device_location_'
  FIELD_ROOM_TYPE = '_field_room_type_'
  FIELD_ROOM_NAME = '_field_room_name_'
  FIELD_DOOR_ROOM_A = '_field_doom_room_a_'
  FIELD_DOOR_ROOM_B = '_field_doom_room_b_'
  FIELD_DOOR_NAME = '_field_doom_name_'
  FIELD_DOOR_IS_OPEN = '_field_doom_is_open_'
  FIELD_DOOR_IS_CLOSE = '_field_doom_is_close_'
  FIELD_WINDOW_ROOM = '_field_window_room_'
  FIELD_WINDOW_NAME = '_field_window_name_'
  FIELD_WINDOW_IS_OPEN = '_field_window_is_open_'
  FIELD_WINDOW_IS_CLOSE = '_field_window_is_close_'
  FIELD_CONNECTION_LEFT = '_field_connection_left_'
  FIELD_CONNECTION_RIGHT = '_field_connection_right_'
  FIELD_CONNECTION_NAME = '_field_connection_name_'


# event_key  = {
#   table_human = '_table_human_row_',
#   'table-device' = '_table_device_row_',
#   'table-room' = '_table_room_row_',
#   'table-door' = '_table_door_row_',
#   'table-window' = '_table_window_row_',
#   'button-new' = '_button_new_',
#   'button-add' = '_button_add_',
#   'button-update' = '_button_update_',
#   'button-cancel' = '_button_cancel_',
#   'button-delete' = '_button_delete_',
#   'button-connect' = '_button_connect_',
#   'button-disconnect' = '_button_disconnect_',
#   'field-human-name' = '',
#   'field-human-location' = '',
#   'field-device-type' = '',
#   'field-device-name' = '',
#   'field-device-location' = '',
#   'field-room-type' = '',
#   'field-room-name' = '',
#   'field-door-room-a' = '',
#   'field-door-room-b' = '',
#   'field-door-name' = '',
#   'field-door-is-open' = '',
#   'field-window-room' = '',
#   'field-window-name' = '',
#   'field-window-is-open' = '',
#   'field-connection-left' = '',
#   'field-connection-right' = '',
#   'field-connection-name' = '',
# }