# config.py

# File and path configs
RAW_CAPTIONS_FILE = "data/raw/Flickr8k.token.txt"
TRAIN_IMAGES_FILE = "data/raw/Flickr8k_text/Flickr_8k.trainImages.txt"
TEST_IMAGES_FILE = "data/raw/Flickr8k_text/Flickr_8k.testImages.txt"
DEV_IMAGES_FILE = "data/raw/Flickr8k_text/Flickr_8k.devImages.txt"
IMAGE_DIR = "data/raw/Flickr8k_Dataset/"
PROCESSED_CAPTIONS = "data/processed/captions_cleaned.txt"

# Model parameters
MAX_LENGTH = 35
VOCAB_SIZE = 8000
EMBEDDING_DIM = 256
LSTM_UNITS = 256
DROPOUT_RATE = 0.5

# Training
EPOCHS = 50
BATCH_SIZE = 64
