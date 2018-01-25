#model.py 负责ORM

from sqlalchemy import Column,Integer,BigInteger,String,ForeignKey,DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT
from . import config
#基类
Base = declarative_base()

#实体类
#+----------+--------------+------+-----+---------+----------------+
#| Field    | Type         | Null | Key | Default | Extra          |
#+----------+--------------+------+-----+---------+----------------+
#| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
#| name     | varchar(48)  | NO   |     | NULL    |                |
#| email    | varchar(64)  | NO   | UNI | NULL    |                |
#| password | varchar(128) | NO   |     | NULL    |                |
#+----------+--------------+------+-----+---------+----------------+


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(48),nullable=False)
    email = Column(String(64),nullable=False,unique=True)
    password = Column(String(128),nullable=False)

    def __repr__(self):
        return "<User (id={},name={},email={},password={})>".format(self.id,self.name,self.email,self.password)


#+-----------+--------------+------+-----+---------+----------------+
#| Field | Type | Null | Key | Default | Extra |
#+-----------+--------------+------+-----+---------+----------------+
#| id | bigint(20) | NO | PRI | NULL | auto_increment |
#| title | varchar(256) | NO | | NULL | |
#| author_id | int(11) | NO | MUL | NULL | |
#| postdate | datetime | NO | | NULL | |
#+-----------+--------------+------+-----+---------+----------------+

class Post(Base):
    __tablename__ ='post'
    id = Column(BigInteger,primary_key=True,autoincrement=True)
    title = Column(String(256),nullable=False)
    author_id = Column(Integer,ForeignKey('user.id'),nullable=False)
    postdate = Column(DateTime,nullable=False)

    author = relationship('User')
    content = relationship('Content',uselist= False)

    def __repr__(self):
        return "<Post (id={},title={},author_id={})>".format(
            self.id ,self.title,self.author_id
        )

#+---------+------------+------+-----+---------+----------------+
#| Field   | Type       | Null | Key | Default | Extra          |
#+---------+------------+------+-----+---------+----------------+
#| id      | bigint(20) | NO   | PRI | NULL    | auto_increment |
#| content | longtext   | NO   |     | NULL    |                |
#+---------+------------+------+-----+---------+----------------+

class Content(Base):
    __tablename__ = "content"

    id = Column(BigInteger,ForeignKey('post.id'),primary_key=True)
    content = Column(LONGTEXT,nullable=False)

    def __repr__(self):
        return "<User (id={},content={}>".format(
            self.id,self.content[:20])

#连接数据库
engine = create_engine(config.URL,echo=config.DATABASE_DEBUG)

#创建删除表
def createtables():
    Base.metadata.create_all(engine)


def droptables():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

#获取session
session = Session()






