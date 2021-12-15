import stardog
import re

from config import conn_details, db_name



def get_human_list():
  human_list = dict()
  human_id_list = [val for val in query('SELECT ?x WHERE { ?x rdf:type agn:Human }')]
  for id in human_id_list:
    name = query('SELECT ?x WHERE { ?y agn:has_human_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_located_in = query('SELECT ?x WHERE { ?y agn:is_human_located_in ?x FILTER regex(str(?y), "' + id + '")}')
    human_list.update({id: {'name': name[0], 'is_located_in': is_located_in[0]}})
  return human_list


def get_device_list():
  device_type_list = [val for val in query('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Device }')]
  device_list = dict()
  device_list.update({'type_list': device_type_list})
  for type in device_type_list:
    device_id_list = query('SELECT ?x WHERE { ?x rdf:type agn:' + type + ' }')
    for id in device_id_list:
      name = query('SELECT ?x WHERE { ?y agn:has_device_name ?x FILTER regex(str(?y), "' + id + '")}')
      is_located_in = query('SELECT ?x WHERE { ?y agn:is_device_located_in ?x FILTER regex(str(?y), "' + id + '")}')
      device_list.update({id: {'type': type, 'name': name[0], 'is_located_in': is_located_in[0]}})
  return device_list


def get_room_list():
  room_type_list = [val for val in query('SELECT ?x WHERE { ?x rdfs:subClassOf agn:Room }')]
  room_list = dict()
  room_list.update({'type_list': room_type_list})
  for type in room_type_list:
    room_id_list = query('SELECT ?x WHERE { ?x rdf:type agn:' + type + ' }')
    for id in room_id_list:
      name = query('SELECT ?x WHERE { ?y agn:has_room_name ?x FILTER regex(str(?y), "' + id + '")}')
      room_list.update({id: {'type': type, 'name': name[0]}})
  return room_list


def get_door_list():
  door_list = dict()
  door_id_list = [val for val in query('SELECT ?x WHERE { ?x rdf:type agn:Door }')]
  for id in door_id_list:
    name = query('SELECT ?x WHERE { ?y agn:has_door_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_open = query('SELECT ?x WHERE { ?y agn:is_door_open ?x FILTER regex(str(?y), "' + id + '")}')
    is_door_of_list = query('SELECT ?x WHERE { ?y agn:is_door_of ?x FILTER regex(str(?y), "' + id + '")}')
    if len(is_door_of_list) == 1:
      is_door_of_list += ['None']
    door_list.update({id: {'name': name[0], 'is_open': is_open[0], 'is_door_of_A': is_door_of_list[0],
                           'is_door_of_B': is_door_of_list[1]}})
  return door_list


def get_window_list():
  window_list = dict()
  window_id_list = [val for val in query('SELECT ?x WHERE { ?x rdf:type agn:Window }')]
  for id in window_id_list:
    name = query('SELECT ?x WHERE { ?y agn:has_window_name ?x FILTER regex(str(?y), "' + id + '")}')
    is_window_of = query('SELECT ?x WHERE { ?y agn:is_window_of ?x FILTER regex(str(?y), "' + id + '")}')
    is_open = query('SELECT ?x WHERE { ?y agn:is_window_open ?x FILTER regex(str(?y), "' + id + '")}')
    window_list.update({id: {'name': name[0], 'is_window_of': is_window_of[0], 'is_open': is_open[0]}})
  return window_list


def value(source):
  value = []
  for i in range(len(source['results']['bindings'])):
    if re.search('(#)', source['results']['bindings'][i]['x']['value']) != None:
      value.append(re.search('[_\w\/\.]+#([_\w]+)', source['results']['bindings'][i]['x']['value']).group(1))
    else:
      value.append(source['results']['bindings'][i]['x']['value'])
  return value



def query(query, prefix='PREFIX agn: <http://www.semanticweb.org/agonm/ontologies/2021/10/stardog-smarthome#>'):
  with stardog.Connection(db_name, **conn_details) as conn:
    result = conn.select(prefix + ' ' + query)
  return value(result)
