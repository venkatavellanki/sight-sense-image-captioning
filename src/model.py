# model.py

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from config import *

def define_model(vocab_size, max_length):
    # Feature extractor model (image input)
    inputs1 = Input(shape=(4096,))
    fe1 = Dropout(DROPOUT_RATE)(inputs1)
    fe2 = Dense(EMBEDDING_DIM, activation='relu')(fe1)

    # Sequence model (text input)
    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, EMBEDDING_DIM, mask_zero=True)(inputs2)
    se2 = Dropout(DROPOUT_RATE)(se1)
    se3 = LSTM(LSTM_UNITS)(se2)

    # Decoder model
    decoder1 = add([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model
