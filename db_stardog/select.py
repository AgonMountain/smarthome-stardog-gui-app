from db_stardog.basis import *


def get_human_list():
  human_list = dict()
  human_id_list = [val for val in select('SELECT ?x WHERE { ?x rdf:type agn:Human }')]
  for id in human_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_human_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_located_in = select('SELECT ?x WHERE { ?y agn:is_human_located_in ?x FILTER regex(str(?y), "' + id + '")}')
    human_list.update({id: {'name': name[0], 'is_located_in': is_located_in[0]}})
  return human_list


def get_device_type_list():
  return [val for val in select('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Device }')]


def get_device_list():
  device_type_list = get_device_type_list()
  device_list = dict()
  for type in device_type_list:
    device_id_list = select('SELECT ?x WHERE { ?x rdf:type agn:' + type + ' }')
    for id in device_id_list:
      name = select('SELECT ?x WHERE { ?y agn:has_device_name ?x FILTER regex(str(?y), "' + id + '")}')
      is_located_in = select('SELECT ?x WHERE { ?y agn:is_device_located_in ?x FILTER regex(str(?y), "' + id + '")}')
      device_list.update({id: {'type': type, 'name': name[0], 'is_located_in': is_located_in[0]}})
  return device_list


def get_room_type_list():
  return [val for val in select('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Room }')]


def get_room_list():
  room_type_list = get_room_type_list()
  room_list = dict()
  reverse_room_list = dict()
  for type in room_type_list:
    room_id_list = select('SELECT ?x WHERE { ?x rdf:type agn:' + type + ' }')
    for id in room_id_list:
      name = select('SELECT ?x WHERE { ?y agn:has_room_name ?x FILTER regex(str(?y), "' + id + '")}')
      room_list.update({id: {'type': type, 'name': name[0]}})
      reverse_room_list.update({name[0]: id})
  return room_list, reverse_room_list


def get_door_list():
  door_list = dict()
  door_id_list = [val for val in select('SELECT ?x WHERE { ?x rdf:type agn:Door }')]
  for id in door_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_door_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_open = select('SELECT ?x WHERE { ?y agn:is_door_open ?x FILTER regex(str(?y), "' + id + '")}')
    is_door_of_list = select('SELECT ?x WHERE { ?y agn:is_door_of ?x FILTER regex(str(?y), "' + id + '")}')
    if len(is_door_of_list) == 1:
      is_door_of_list += ['None']
    door_list.update({id: {'name': name[0], 'is_open': is_open[0], 'is_door_of_A': is_door_of_list[0],
                           'is_door_of_B': is_door_of_list[1]}})
  return door_list


def get_window_list():
  window_list = dict()
  window_id_list = [val for val in select('SELECT ?x WHERE { ?x rdf:type agn:Window }')]
  for id in window_id_list:
    name = select('SELECT ?x WHERE { ?y agn:has_window_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_window_of = select('SELECT ?x WHERE { ?y agn:is_window_of ?x FILTER regex(str(?y), "' + id + '")}')
    is_open = select('SELECT ?x WHERE { ?y agn:is_window_open ?x FILTER regex(str(?y), "' + id + '")}')
    window_list.update({id: {'name': name[0], 'is_window_of': is_window_of[0], 'is_open': is_open[0]}})
  return window_list


def get_connection(object, subject):
  val = select('SELECT ?x WHERE { ?y ?x ?z FILTER (regex(str(?y), "' + object + '") && regex(str(?z), "' + subject + '")) }')
  if len(val) > 0:
    val = val[0]
  else:
    val = 'None'
  return val


def get_predicates(object, subject):
  val = select(
    'SELECT ?x WHERE { agn:' + object + ' ?x agn:' + subject + ' }')
  if len(val) > 0:
    val = val[0]
  else:
    val = 'None'
  return val
