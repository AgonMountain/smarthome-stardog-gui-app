import stardog
import re


def value(source):
  value = []
  for i in range(len(source['results']['bindings'])):
    value.append(re.search('[_\w\/\.]+#([_\w]+)', source['results']['bindings'][i]['x']['value']).group(1))
  return value


def query(query_predicate, query_object, db_name, conn_details):
  with stardog.Connection(db_name, **conn_details) as conn:
    result = conn.select('PREFIX agn: <http://www.semanticweb.org/agonm/ontologies/2021/10/stardog-smarthome#> '
                          'SELECT ?x WHERE { ?x ' + query_predicate + ' agn:' + query_object + '}')
  return result


conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}

with stardog.Admin(**conn_details) as admin:
  db = admin.database('db9')

  print(value(query('rdf:type', 'Human', 'db9', conn_details)))


