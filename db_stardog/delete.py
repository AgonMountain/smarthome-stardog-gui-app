from db_stardog.basis import *


def delete_human(human_id):
  insert('DELETE WHERE { agn:' + human_id + ' ?p ?o . }')


def delete_device(device_id):
  insert('DELETE WHERE { agn:' + device_id + ' ?p ?o . }')


def delete_room(room_id):
  insert('DELETE WHERE { agn:' + room_id + ' ?p ?o . }')


def delete_door(door_id):
  insert('DELETE WHERE { agn:' + door_id + ' ?p ?o . }')


def delete_window(window_id):
  insert('DELETE WHERE { agn:' + window_id + ' ?p ?o . }')


def delete_connection(left_id, right_id):
  insert('DELETE WHERE { agn:' + left_id + ' ?p ' + ' agn:' + right_id + ' . }')
