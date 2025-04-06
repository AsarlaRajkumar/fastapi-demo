from config import *
import datetime

engine = create_engine(DATBASE_URL, echo=True)

metadata = MetaData()

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    books = relationship("Book", back_populates="author")
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }



class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    books = relationship("Book", back_populates="genre")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }
    

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.id"), nullable=False)
    available_count = Column(Integer, default=0)
    created_at = Column(Date, default=datetime.date.today())
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.to_json() or None,
            "genre": self.genre.to_json() or None,
            "available_count": self.available_count,
            "created_at": str(self.created_at)
        }


Base.metadata.create_all(engine)

session = Session(bind=engine)