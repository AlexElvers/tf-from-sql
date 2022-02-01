import numpy as np

from tf_from_sql.db import SensorLogEntry, Session


def create_samples_from_db() -> tuple[np.ndarray, np.ndarray]:
    session = Session()
    session_log_entries = list(session.query(SensorLogEntry))

    num_sensors = 2  # sensors ids are in range(num_sensors)
    num_events = 3  # event ids are in range(num_events)

    # features
    X = np.zeros((len(session_log_entries), num_sensors), dtype="float32")
    # labels
    Y_true = np.zeros((len(session_log_entries), num_events), dtype="float32")
    for i, session_log_entry in enumerate(session_log_entries):
        # one-hot encoding of features and labels
        X[i, session_log_entry.sensor] = 1.0
        Y_true[i, session_log_entry.event] = 1.0

    return X, Y_true
