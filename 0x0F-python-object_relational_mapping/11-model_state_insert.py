#!/usr/bin/python3
'''This is another alchemy adding stuff'''

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    st = session.query(State)
    st = st.filter(State.name == "Louisiana").one_or_none()
    print("{}".format(st.id))
    session.close()
