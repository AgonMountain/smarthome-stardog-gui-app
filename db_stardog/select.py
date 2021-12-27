from db_stardog.basis import *


def get_human_list():
  human_list = dict()
  human_id_list = [val for val in select('SELECT ?x WHERE { ?x a agn:Human }')]
  for human_id in human_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_human_name ?x FILTER regex(str(?y), "' + human_id + '")}')
    is_located_in = select('SELECT ?x WHERE { ?y agn:is_human_located_in ?x FILTER regex(str(?y), "' + human_id + '")}')
    human_list.update({human_id: {'name': name[0], 'is_located_in': is_located_in[0]}})
  return human_list


def get_device_type_list():
  return [val for val in select('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Device }')]


def get_device_list():
  device_type_list = get_device_type_list()
  device_list = dict()
  for device_type in device_type_list:
    device_id_list = select('SELECT ?x WHERE { ?x a agn:' + device_type + ' }')
    for device_id in device_id_list:
      name = select('SELECT ?x WHERE { ?y agn:has_device_name ?x FILTER regex(str(?y), "' + device_id + '")}')
      is_located_in = select('SELECT ?x WHERE { ?y agn:is_device_located_in ?x FILTER regex(str(?y), "' + device_id + '")}')
      device_list.update({device_id: {'type': device_type, 'name': name[0], 'is_located_in': is_located_in[0]}})
  return device_list


def get_room_type_list():
  return [val for val in select('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Room }')]


def get_room_list():
  room_type_list = get_room_type_list()
  room_list = dict()
  for room_type in room_type_list:
    room_id_list = select('SELECT ?x WHERE { ?x a agn:' + room_type + ' }')
    for room_id in room_id_list:
      name = select('SELECT ?x WHERE { ?y agn:has_room_name ?x FILTER regex(str(?y), "' + room_id + '")}')
      room_list.update({room_id: {'type': room_type, 'name': name[0]}})
  return room_list


def get_door_list():
  door_list = dict()
  door_id_list = [val for val in select('SELECT ?x WHERE { ?x a agn:Door }')]
  for door_id in door_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_door_name ?x FILTER regex(str(?y), "' + door_id + '")}')
    is_open = select('SELECT ?x WHERE { ?y agn:is_door_open ?x FILTER regex(str(?y), "' + door_id + '")}')
    is_door_of_list = select('SELECT ?x WHERE { ?y agn:is_door_of ?x FILTER regex(str(?y), "' + door_id + '")}')
    if len(is_door_of_list) == 1:
      is_door_of_list += ['None']
    door_list.update({door_id: {'name': name[0], 'is_open': is_open[0], 'is_door_of_A': is_door_of_list[0],
                           'is_door_of_B': is_door_of_list[1]}})
  return door_list


def get_window_list():
  window_list = dict()
  window_id_list = [val for val in select('SELECT ?x WHERE { ?x a agn:Window }')]
  for window_id in window_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_window_name ?x FILTER regex(str(?y), "' + window_id + '")}')
    is_window_of = select('SELECT ?x WHERE { ?y agn:is_window_of ?x FILTER regex(str(?y), "' + window_id + '")}')
    is_open = select('SELECT ?x WHERE { ?y agn:is_window_open ?x FILTER regex(str(?y), "' + window_id + '")}')
    window_list.update({window_id: {'name': name[0], 'is_window_of': is_window_of[0], 'is_open': is_open[0]}})
  return window_list


def get_connection(left_id, right_id):
  val = select('SELECT ?x WHERE { agn:' + left_id + ' ?x agn:' + right_id + ' }')
  if len(val) > 0:
    val = val[0].replace('_', ' ')
  else:
    val = 'has no connection'
  return val
