#!/bin/bash
count=0
for f in data_parts/all_data*; do
  echo "Creating Pretraining for $f ......"
  python bert-master/create_pretraining_data.py \
    --input_file "$f" \
    --output_file "pretraining_data/tf_examples_multi.tfrecord$count" \
    --vocab_file augmented_vocab.txt \
    --do_lower_case True \
    --max_seq_length $1 \
    --max_predictions_per_seq 20 \
    --masked_lm_prob 0.15 \
    --random_seed 42 \
    --dupe_factor 5
  (( count++ ))
done
