from db_stardog.basis import *


def update_human(old_data, human_id, name, is_located_in):
  insert('DELETE WHERE { agn:' + human_id + ' a agn:Human , owl:NamedIndividual ; ' +
                                  ' agn:is_human_located_in agn:' + old_data['is_located_in'] + ' ; ' +
                                  ' agn:has_human_name "' + old_data['name'] + '" . }')

  insert('INSERT DATA { agn:' + human_id + ' a agn:Human , owl:NamedIndividual ; ' +
                                  ' agn:is_human_located_in agn:' + is_located_in + ' ; ' +
                                  ' agn:has_human_name "' + name + '" . }')


def update_device(old_data, device_id, name, type, is_located_in):
  insert('DELETE WHERE { agn:' + device_id + ' a agn:' + old_data['type'] + ' , owl:NamedIndividual ; ' +
         ' agn:is_device_located_in agn:' + old_data['is_located_in'] + ' ; ' +
         ' agn:has_device_name "' + old_data['name'] + '" . }')

  insert('INSERT DATA { agn:' + device_id + ' a agn:' + type + ' , owl:NamedIndividual ; ' +
                                  ' agn:is_device_located_in agn:' + is_located_in + ' ; ' +
                                  ' agn:has_device_name "' + name + '" . }')


def update_device_type(name):
  insert('INSERT DATA { agn:' + name + ' a owl:Class ; rdfs:subClassOf agn:Device . }')


def update_room(old_data, room_id, name, type):
  insert('DELETE WHERE { agn:' + room_id + ' a agn:' + old_data['type'] + ' , owl:NamedIndividual ; ' +
         ' agn:has_room_name "' + old_data['name'] + '" . }')

  insert('INSERT DATA { agn:' + room_id + ' a agn:' + type + ' , owl:NamedIndividual ; ' +
                                  ' agn:has_room_name "' + name + '" . }')


def update_door(old_data, door_id, name, is_door_open, is_door_of_list):
  is_open = 'false'
  if old_data['is_open']:
    is_open = 'true'
  is_door_of = ''
  for d in old_data['is_door_of_list']:
    if d != 'None':
      is_door_of += ' agn:is_door_of agn:' + d + ' ; '

  insert('DELETE WHERE { agn:' + door_id + ' a agn:Door , owl:NamedIndividual ;' +
         ' agn:has_door_name "' + old_data['name'] + '" ; ' +
         is_door_of +
         ' agn:is_door_open ' + is_open + ' . }')

  is_open = 'false'
  if is_door_open:
    is_open = 'true'
  is_door_of = ''
  for d in is_door_of_list:
    if d != 'None':
      is_door_of += ' agn:is_door_of agn:' + d + ' ; '

  insert('INSERT DATA { agn:' + door_id + ' a agn:Door , owl:NamedIndividual ;' +
                                  ' agn:has_door_name "' + name + '" ; ' +
                                  is_door_of +
                                  ' agn:is_door_open ' + is_open + ' . }')


def update_window(old_data, window_id, name, is_window_open, is_window_of_list):
  is_open = 'false'
  if old_data['is_open']:
    is_open = 'true'
  is_window_of = ''
  for w in old_data['is_window_of_list']:
    is_window_of += ' agn:is_window_of agn:' + w + ' ; '

  insert('DELETE WHERE { agn:' + window_id + ' a agn:Window , owl:NamedIndividual ; ' +
         ' agn:has_window_name "' + old_data['name'] + '" ; ' +
         is_window_of +
         ' agn:is_window_open ' + is_open + ' . }')

  is_open = 'false'
  if is_window_open:
    is_open = 'true'
  is_window_of = ''
  for w in is_window_of_list:
    is_window_of += ' agn:is_window_of agn:' + w + ' ; '

  insert('INSERT DATA { agn:' + window_id + ' a agn:Window , owl:NamedIndividual ; ' +
                                  ' agn:has_window_name "' + name + '" ; ' +
                                  is_window_of +
                                  ' agn:is_window_open ' + is_open + ' . }')


def update_connection(left_id, connection_name, right_id):
  insert('INSERT DATA { agn:' + left_id + ' agn:' + connection_name + ' agn:' + right_id + ' . }')
