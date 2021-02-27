import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertForSequenceClassification, BertTokenizer, Trainer, TrainingArguments
from transformers.trainer_utils import EvaluationStrategy
from torch.utils.data import DataLoader
from transformers import AdamW
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = BertForSequenceClassification.from_pretrained('results_senti_mix/checkpoint-4000',num_labels=3)
# model = BertForSequenceClassification.from_pretrained('bert_bilingual_roman_urdu', num_labels=3)
tokenizer = BertTokenizer.from_pretrained('bert_bilingual_roman_urdu')

senti_mix_train = pd.read_csv('fine_tuning_data/SentiMix_train_ru.csv')
senti_mix_test = pd.read_csv('fine_tuning_data/SentiMix_test_ru.csv')

sentiment_categorical = senti_mix_train['sentiment'].astype('category').cat
class_names = list(sentiment_categorical.categories)

sentences_train = list(senti_mix_train.sentence)
sentiment_train = list(sentiment_categorical.codes)

X_test = list(senti_mix_test.sentence)
y_test = list(senti_mix_test['sentiment'].astype('category').cat.codes)

X_train, X_val, y_train, y_val = train_test_split(sentences_train, sentiment_train, test_size=0.1)

train_encodings = tokenizer(X_train, truncation=True, padding=True, max_length=128)
val_encodings = tokenizer(X_val, truncation=True, padding=True, max_length=128)
test_encodings = tokenizer(X_test, truncation=True, padding=True, max_length=128)


class SentiMixDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


train_dataset = SentiMixDataset(train_encodings, y_train)
val_dataset = SentiMixDataset(val_encodings, y_val)
test_dataset = SentiMixDataset(test_encodings, y_test)


def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }


training_args = TrainingArguments(
    output_dir='results_senti_mix',  # output directory
    overwrite_output_dir=True,
    num_train_epochs=100,  # total number of training epochs
    per_device_train_batch_size=64,  # batch size per device during training
    per_device_eval_batch_size=64,  # batch size for evaluation
    warmup_steps=500,  # number of warmup steps for learning rate scheduler
    weight_decay=0.01,  # strength of weight decay
    logging_dir='./logs',  # directory for storing logs
    logging_steps=100,
    evaluation_strategy=EvaluationStrategy.EPOCH,
)

trainer = Trainer(
    model=model,  # the instantiated 🤗 Transformers model to be trained
    args=training_args,  # training arguments, defined above
    train_dataset=train_dataset,  # training dataset
    eval_dataset=test_dataset,  # evaluation dataset
    compute_metrics=compute_metrics
)

# trainer.train()

print(trainer.evaluate())

# train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
# model.to(device)
# model.train()
# optim = AdamW(model.parameters(), lr=5e-5)

# for epoch in range(3):
#     for batch in train_loader:
#         optim.zero_grad()
#         input_ids = batch['input_ids'].to(device)
#         attention_mask = batch['attention_mask'].to(device)
#         labels = batch['labels'].to(device)
#         outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
#         loss = outputs[0]
#         loss.backward()
#         optim.step()
#
# model.eval()
