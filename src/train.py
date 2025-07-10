# train.py

from data_loader import create_sequences
from model import define_model
from config import *
import pickle

def train_model(train_descriptions, train_features, tokenizer):
    model = define_model(VOCAB_SIZE, MAX_LENGTH)
    X1, X2, y = create_sequences(tokenizer, MAX_LENGTH, train_descriptions, train_features, VOCAB_SIZE)
    model.fit([X1, X2], y, epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)
    model.save("models/sight_sense_captioning.h5")
