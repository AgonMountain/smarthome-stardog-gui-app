from db_funcs.basis import *


def insert_human(name, is_located_in):
  human_id = 'human_' + get_unique_id()
  insert('INSERT DATA { <http://smarthome#' + human_id + '> ' +
                                  'rdf:type agn:Human ;' +
                                  'agn:is_human_located_in <http://smarthome#' + is_located_in + '>; ' +
                                  'agn:has_human_name "' + name + '". }')


def insert_device(name, type, is_located_in):
  device_id = 'device_' + get_unique_id()
  insert('INSERT DATA { <http://smarthome#' + device_id + '> ' +
                                  'rdf:type agn:' + type + ' ;' +
                                  'agn:is_device_located_in <http://smarthome#' + is_located_in + '>; ' +
                                  'agn:has_device_name "' + name + '". }')


def insert_device_type(name):
  insert('INSERT DATA { <http://smarthome#' + name + '> rdfs:subClassOf agn:Device . }')


def insert_room(name, type):
  room_id = 'room_' + get_unique_id()
  insert('INSERT DATA { <http://smarthome#' + room_id + '> ' +
                                  'rdf:type agn:' + type + ' ;' +
                                  'agn:has_room_name "' + name + '". }')


def insert_door(name, is_door_open, is_door_of_list):
  door_id = 'door_' + get_unique_id()
  is_open = 'false'
  if is_door_open:
    is_open = 'true'
  is_door_of = ''
  for d in is_door_of_list:
    is_door_of += 'agn:is_door_of "' + d + '" ; '

  insert('INSERT DATA { <http://smarthome#' + door_id + '> ' +
                                  'rdf:type agn:Door ;' +
                                  'agn:has_door_name "' + name + '" ; ' +
                                  is_door_of +
                                  'agn:is_door_open ' + is_open + '. }')


def insert_window(name, is_window_open, is_window_of_list):
  door_id = 'window_' + get_unique_id()
  is_open = 'false'
  if is_window_open:
    is_open = 'true'
  is_window_of = ''
  for w in is_window_of_list:
    is_window_of += 'agn:is_window_of "' + w + '" ; '

  insert('INSERT DATA { <http://smarthome#' + door_id + '> ' +
                                  'rdf:type agn:Window ;' +
                                  'agn:has_window_name "' + name + '" ; ' +
                                  is_window_of +
                                  'agn:is_window_open ' + is_open + '. }')
