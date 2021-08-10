# Multilingual, Bilingual and Monolingual BERT for Roman Urdu

1. Complete training code is present in BERT_PRETRAINING_ROMAN_URDU.ipynb
2. Use learning rate 2e-5 when starting from a pretrained model otherwise use 1e-4

### Experiments
1. Experiment with different vocabulary sizes (Note common tokens and performance)


### Fine Tuning
export BERT_BASE_DIR=bert_bilingual_roman_urdu

transformers-cli convert --model_type bert \
  --tf_checkpoint $BERT_BASE_DIR/model.ckpt-100000 \
  --config bert-base-uncased/bert_config.json \
  --pytorch_dump_output $BERT_BASE_DIR/pytorch_model.bin
  
 ### Trained Models
 Download Trained models from:
 https://drive.google.com/drive/folders/10GCkA1DlorddMkeR_u5yi8k2Mt85vgXy?usp=sharing

## Important!!!

This project contains large files that have been split to meet GitHub file size requirements.
Please run: "python3 file_split_merge.py --merge" at project root to get the original files back