from typing import List
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = "buildings"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    adress: Mapped[str] = mapped_column(String(100))
    classrooms: Mapped[List["Classrooms"]] = relationship("Classroom",back_populates="building", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Building(id={self.id}, name={self.name})>"

class Classroom(Base):
    __tablename__ = "classroom"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20))
    capacity: Mapped[int] =  mapped_column(Integer)
    is_computer: Mapped[bool] = mapped_column(Boolean)
    building_id: Mapped[int] = mapped_column(Integer, ForeignKey("buildings.id"))
    Building: Mapped['Building'] = relationship("Building",back_populates='classrooms')

    def __repr__(self) -> str:
        return f"<Classroom(id={self.id}, name={self.name})>"

def create_tables(connection):
    Base.metadata.create_all(connection)