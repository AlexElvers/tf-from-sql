from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///db.sqlite3")  # use echo=True to show SQL statements
Session = sessionmaker(bind=engine)
Base = declarative_base()


class SensorLogEntry(Base):
    __tablename__ = "sensor_log_entries"

    id = Column(Integer, primary_key=True)
    sensor = Column(Integer)
    event = Column(Integer)

    def __repr__(self) -> str:
        return f"<SensorLogEntry(id={self.id!r}, sensor={self.sensor!r}, event={self.event!r})>"
