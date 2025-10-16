from db.connection import get_connection

engine = get_connection()
engine.connect()
engine.close()