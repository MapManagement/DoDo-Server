import sys
sys.path.append("..")
from requirements import secrets_file

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column


engine = create_engine(secrets_file.connection_credentials)
Base = declarative_base()


class ToDo(Base):

    __tablename__ = "todos"
    t_id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("profiles.p_id"))
    text = Column(String)
    is_done = Column(Boolean)
    color = Column(String)

    def __init__(self, t_id, creator_id, text, color, is_done):
        self.t_id = t_id
        self.creator_id = creator_id
        self.text = text
        self.color = color
        self.is_done = is_done


class Note(Base):

    __tablename__ = "notes"
    n_id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey("profiles.p_id"))
    title = Column(String)
    content = Column(String)
    creation_date = Column(DateTime)
    is_visible = Column(Boolean)
    is_highlighted = Column(Boolean)
    color = Column(String)

    def __init__(self, n_id, creator_id, title, content, color, is_visible, is_highlighted, creation_date):
        self.n_id = n_id
        self.creator_id = creator_id
        self.title = title
        self.content = content
        self.creation_date = creation_date
        self.is_visible = is_visible
        self.is_highlighted = is_highlighted
        self.color = color


class Profile(Base):

    __tablename__ = "profiles"
    p_id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    creation_date = Column(DATETIME)

    def __init__(self, p_id, name, creation_date):
        self.p_id = p_id
        self.name = name
        self.creation_date = creation_date


class Tag(Base):

    __tablename__ = "tags"
    ta_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, ta_id, name):
        self.ta_id = ta_id
        self.name = name


Base.metadata.create_all(engine)