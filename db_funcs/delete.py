from db_funcs.basis import *


def delete_human(id, name, is_located_in):
  insert('DELETE DATA { <http://smarthome#' + id + '> ' +
                                  'rdf:type agn:Human ; ' +
                                  'agn:is_human_located_in <http://smarthome#' + is_located_in + '>; ' +
                                  'agn:has_human_name "' + name + '". }')


def delete_device(id, name, type, is_located_in):
  insert('DELETE DATA { <http://smarthome#' + id + '> ' +
                                  'rdf:type agn:' + type + ' ;' +
                                  'agn:is_device_located_in <http://smarthome#' + is_located_in + '>; ' +
                                  'agn:has_device_name "' + name + '". }')


def delete_room(id, name, type):
  insert('DELETE DATA { <http://smarthome#' + id + '> ' +
                                  'rdf:type agn:' + type + ' ;' +
                                  'agn:has_room_name "' + name + '". }')


def delete_door(id, name, is_door_open, is_door_of_list):
  is_open = 'false'
  if is_door_open:
    is_open = 'true'
  is_door_of = ''
  for d in is_door_of_list:
    is_door_of += 'agn:is_door_of "' + d + '" ; '

  insert('DELETE DATA { <http://smarthome#' + id + '> ' +
                                  'rdf:type agn:Door ;' +
                                  'agn:has_door_name "' + name + '" ; ' +
                                  is_door_of +
                                  'agn:is_door_open ' + is_open + '. }')


def delete_window(id, name, is_window_open, is_window_of_list):
  is_open = 'false'
  if is_window_open:
    is_open = 'true'
  is_window_of = ''
  for w in is_window_of_list:
    is_window_of += 'agn:is_window_of "' + w + '" ; '

  insert('DELETE DATA { <http://smarthome#' + id + '> ' +
                                  'rdf:type agn:Window ;' +
                                  'agn:has_window_name "' + name + '" ; ' +
                                  is_window_of +
                                  'agn:is_window_open ' + is_open + '. }')
