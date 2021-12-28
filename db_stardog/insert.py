from db_stardog.basis import *


def insert_human(name, is_located_in):
  human_id = 'Human_' + get_unique_id()
  insert('INSERT DATA { agn:' + human_id + ' a agn:Human , owl:NamedIndividual ; ' +
                                  ' agn:is_human_located_in agn:' + is_located_in + ' ; ' +
                                  ' agn:has_human_name "' + name + '" . }')


def insert_device(name, type, is_located_in):
  device_id = type + '_' + get_unique_id()
  insert('INSERT DATA { agn:' + device_id + ' a agn:' + type + ' , owl:NamedIndividual ; ' +
                                  ' agn:is_device_located_in agn:' + is_located_in + ' ; ' +
                                  ' agn:has_device_name "' + name + '" . }')


def insert_device_type(name):
  insert('INSERT DATA { agn:' + name + ' a owl:Class ; rdfs:subClassOf agn:Device . }')


def insert_room(name, type):
  room_id = type + '_' + get_unique_id()
  insert('INSERT DATA { agn:' + room_id + ' a agn:' + type + ' , owl:NamedIndividual ; ' +
                                  ' agn:has_room_name "' + name + '" . }')


def insert_door(name, is_door_open, is_door_of_list):
  door_id = 'Door_' + get_unique_id()
  is_open = 'false'
  if is_door_open:
    is_open = 'true'
  is_door_of = ''
  for d in is_door_of_list:
    is_door_of += ' agn:is_door_of agn:' + d + ' ; '

  insert('INSERT DATA { agn:' + door_id + ' a agn:Door , owl:NamedIndividual ;' +
                                  ' agn:has_door_name "' + name + '" ; ' +
                                  is_door_of +
                                  ' agn:is_door_open ' + is_open + ' . }')


def insert_window(name, is_window_open, is_window_of_list):
  door_id = 'Window_' + get_unique_id()
  is_open = 'false'
  if is_window_open:
    is_open = 'true'
  is_window_of = ''
  for w in is_window_of_list:
    is_window_of += ' agn:is_window_of agn:' + w + ' ; '

  insert('INSERT DATA { agn:' + door_id + ' a agn:Window , owl:NamedIndividual ; ' +
                                  ' agn:has_window_name "' + name + '" ; ' +
                                  is_window_of +
                                  ' agn:is_window_open ' + is_open + ' . }')


def insert_connection(left_id, connection_name, right_id):
  insert('INSERT DATA { agn:' + left_id + ' agn:' + connection_name + ' agn:' + right_id + ' . }')
