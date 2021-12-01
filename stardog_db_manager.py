

def create_database(admin, name):
  '''Создать базу данных'''
  admin.new_database(name)


def drop_database(admin, name):
  '''Удалить базу данных'''
  db = admin.database(name)
  db.drop()


def add(admin, database_name):
  '''Добавить запись в базу данных'''
  None

def update(admin, database_name):
  '''Обновить запись в базе данных'''
  None

def remove(admin, database_name):
  '''Удалить запись из базы данных'''
  None



  #db = admin.new_database('db')

  # with stardog.Connection('db', **conn_details) as conn:
  #   conn.begin()
  #   conn.add(stardog.content.File('./test/data/example.ttl'))
  #   conn.commit()
  #   results = conn.select('select * { ?a ?p ?o }')

  # db.drop()