#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine
    engine = create_engine(f'mysql+mysqldb: // {username}: {password}
                           @localhost/{database}', pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Perform a query to retrieve all State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # Iterate through the list of states and print them
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
