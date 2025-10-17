from sqlalchemy import select

from sqlalchemy.orm import sessionmaker

from db.connection import get_connection
from db.models.models import create_tables, Classroom

engine = get_connection()
#create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

classrooms = select(Classroom)

stm = select(Classroom)
for classroom in session.scalars(stm):
    print(classroom)