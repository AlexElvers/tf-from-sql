from tensorflow import keras


def create_model() -> keras.Model:
    input_layer = keras.Input(shape=(2,), dtype="float32")
    layer = keras.layers.Dense(3, activation="sigmoid")(input_layer)
    model = keras.Model(inputs=input_layer, outputs=layer)
    model.compile(loss="binary_crossentropy", optimizer="nadam")
    return model
