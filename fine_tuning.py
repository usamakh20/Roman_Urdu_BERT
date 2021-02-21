from transformers import BertForSequenceClassification, BertTokenizer, BertModel
model = BertModel.from_pretrained('bert_bilingual_roman_urdu')
tokenizer = BertTokenizer.from_pretrained('bert_bilingual_roman_urdu')









