import stardog
import stardog_db_manager

conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}
admin = stardog.Admin(**conn_details)

stardog_db_manager.create_database(admin, 'db')