import click
import numpy as np

from tf_from_sql.data import create_samples_from_db
from tf_from_sql.db import Base, SensorLogEntry, Session, engine
from tf_from_sql.model import create_model

rng = np.random.default_rng()


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    Base.metadata.create_all(engine)
    session = Session()
    # fill table with random data
    for i in range(100):
        sensor = int(rng.integers(2))
        # event = int(rng.integers(3))
        event = int(rng.choice(3, p=(sensor == 0) * np.array([0.2, 0.3, 0.5]) + (sensor == 1) * np.array([0.8, 0.2, 0.0])))
        session.add(SensorLogEntry(sensor=sensor, event=event))
    session.commit()


@cli.command()
def show_data():
    session = Session()
    for sensor_log_entry in session.query(SensorLogEntry):
        print(sensor_log_entry)


@cli.command()
def train_and_predict():
    X, Y_true = create_samples_from_db()

    # train
    model = create_model()
    model.fit(X, Y_true, epochs=10)

    # predict
    Y_pred = model.predict(X)

    print("X:")
    print(X[:15])

    print("Y_true:")
    print(Y_true[:15])

    print("Y_pred:")
    print(Y_pred[:15])


if __name__ == "__main__":
    cli()
