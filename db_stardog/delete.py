from db_stardog.basis import *


def delete_human(human_id):
  insert('DELETE WHERE { agn:' + human_id + ' ?p ?o . }')


def delete_device(device_id):
  insert('DELETE WHERE { agn:' + device_id + ' ?p ?o . }')


# def delete_room(room_list, room_id):
#   room_item_list = select('SELECT DISTINCT ?o WHERE { ?o ?p ?s . FILTER regex(str(?s), "' + room_id + '") }')
#
#   if len(room_list) > 1:
#     room_id_container = room_list[0]
#     if room_id_container == room_id:
#       room_id_container = room_list[1]
#
#     for room_item in room_item_list:
#       insert('INSERT DATA { agn:' + room_item + '' ' agn:' + room_id_container + ' , owl:NamedIndividual ; ' +
#              ' agn:has_room_name "' + name + '" . }')
#
#   insert('DELETE WHERE { agn:' + room_id + ' ?p ?o . }')


def delete_door(door_id):
  insert('DELETE WHERE { agn:' + door_id + ' ?p ?o . }')


def delete_window(window_id):
  insert('DELETE WHERE { agn:' + window_id + ' ?p ?o . }')


def delete_connection(left_id, right_id):
  insert('DELETE WHERE { agn:' + left_id + ' ?p ' + ' agn:' + right_id + ' . }')
