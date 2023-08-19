#!/usr/bin/python3
'''
All states via SQLAlchemy

Write a script that lists all State objects
from the database hbtn_0e_6_usa

Your script should take 3 arguments:
mysql username, mysql password and database name

You must use the module SQLAlchemy

You must import State and Base from model_state
from model_state import Base, State

Your script should connect to a MySQL server
running on localhost at port 3306

Results must be sorted in ascending order by states.id

Your code should not be executed when imported
'''

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
