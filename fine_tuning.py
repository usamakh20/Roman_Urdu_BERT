import pandas as pd
from sklearn.model_selection import train_test_split

senti_mix = pd.read_csv('fine_tuning_data/SentiMix_ru.csv')

sentiment_categorical = senti_mix.sentiment.astype('category').cat
class_names = list(sentiment_categorical.categories)

sentences = list(senti_mix.sentence)
labels = list(sentiment_categorical.codes)

X_train, X_test, y_train, y_test = train_test_split(sentences, labels, test_size=0.3)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1)

# train_encodings = tokenizer(train_texts, truncation=True, padding=True)
# val_encodings = tokenizer(val_texts, truncation=True, padding=True)
# test_encodings = tokenizer(test_texts, truncation=True, padding=True)

