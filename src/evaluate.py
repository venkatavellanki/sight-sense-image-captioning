# evaluate.py

from nltk.translate.bleu_score import corpus_bleu

def evaluate_model(model, descriptions, photos, tokenizer, max_length):
    actual, predicted = [], []
    for key, desc_list in descriptions.items():
        yhat = generate_caption(model, tokenizer, photos[key], max_length)
        references = [d.split() for d in desc_list]
        actual.append(references)
        predicted.append(yhat.split())
    score = corpus_bleu(actual, predicted)
    print(f"BLEU Score: {score:.4f}")
