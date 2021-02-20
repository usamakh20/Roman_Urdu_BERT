# Multilingual, Bilingual and Monolingual BERT for Roman Urdu

1. Complete training code is present in BERT_ROMAN_URDU.ipynb
2. Use learning rate 2e-5 when starting from a pretrained model otherwise use 1e-4

### Experiments
1. Experiment with different vocabulary sizes (Note common tokens and performance)


### Fine Tuning
export BERT_BASE_DIR=bert_bilingual_roman_urdu

transformers-cli convert --model_type bert \
  --tf_checkpoint $BERT_BASE_DIR/model.ckpt-100000 \
  --config bert-base-uncased/bert_config.json \
  --pytorch_dump_output $BERT_BASE_DIR/pytorch_model.bin

