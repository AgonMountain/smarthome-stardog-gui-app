import stardog
import re

conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}
db_name = 'smarthome'

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


def insert():
  return None


def update():
  return None


def delete():
  return None
