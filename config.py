conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}
db_name = 'smarthome'

connection = {
  'human-device': ['has_access_to_device'],
  'human-door': ['has_access_to_door'],
  'human-window': ['has_access_to_window'],
  'human-room': ['is_human_located_in'],
  'device-room': ['is_device_located_in'],
  'door-room': ['is_door_of'],
  'window-room': ['is_window_of'],
}