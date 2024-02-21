#!/usr/bin/python3
'''This is another alchemy adding stuff'''

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from relationship_city import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new1 = State(name="California")
    new2 = City(name='San Francisco')
    new1.cities.append(new2)
    session.add(new1)
    session.add(new2)
    session.commit()
