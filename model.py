import sys
from sqlalchemy import Boolean, Column, Integer, String, LargeBinary, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from setting import Base
from setting import ENGINE

# Chats
class Chats(Base):
    __tablename__ = 'chats'
    id = Column('id', Integer, primary_key = True)
    userId = Column('userId', Integer)
    userName = Column('userName', String(255))
    userIcon = Column('userIcon', LargeBinary,nullable=False)
    message = Column('message', String(255))
    created_at = Column('created_at', Timestamp)
    updated_at = Column('updated_at', Timestamp)
    isDelete = Column('isDelete', Boolean, default=False)

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)