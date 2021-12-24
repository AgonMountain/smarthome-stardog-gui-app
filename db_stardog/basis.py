from datetime import datetime
import stardog
import re
from config import conn_details, db_name


def insert(query, prefix='PREFIX agn: <http://smarthome#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'):
  with stardog.Connection(db_name, **conn_details) as conn:
    conn.update(prefix + ' ' + query)


def select(query, prefix='PREFIX agn: <http://smarthome#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>'):
  with stardog.Connection(db_name, **conn_details) as conn:
    result = conn.select(prefix + ' ' + query)
  return value(result)


def value(source):
  value = []
  for i in range(len(source['results']['bindings'])):
    if re.search('(#)', source['results']['bindings'][i]['x']['value']) != None:
      value.append(re.search('[_\w\/\.]+#([_\w]+)', source['results']['bindings'][i]['x']['value']).group(1))
    else:
      value.append(source['results']['bindings'][i]['x']['value'])
  return value


def get_unique_id():
  return datetime.now().strftime("%Y%m%d%H%M%S")
