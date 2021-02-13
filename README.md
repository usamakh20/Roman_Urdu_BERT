Run the following commands

wget --header="Host: storage.googleapis.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" --header="Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" --header="Referer: https://github.com/google-research/bert/blob/master/multilingual.md" "https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip" -c -O 'multi_cased_L-12_H-768_A-12.zip'

mv multi_cased_L-12_H-768_A-12.zip multi_cased.zip

unzip multi_cased.zip

rm multi_cased.zip

wget --header="Host: codeload.github.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" --header="Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" --header="Referer: https://github.com/google-research/bert" --header="Cookie: _octo=GH1.1.68793831.1588906101; _ga=GA1.2.19990328.1588906163; logged_in=no; _gat=1; tz=Asia%2FKarachi" --header="Connection: keep-alive" "https://codeload.github.com/google-research/bert/zip/master" -c -O 'bert-master.zip'

unzip bert-master.zip

rm bert-master.zip

python tokenization.py

python bert-master/create_pretraining_data.py \
    --input_file ROMAN_URDU_DATASET.txt \
    --output_file tf_examples_multi.tfrecord \
    --vocab_file roman-urdu-vocab-cased.txt \
    --do_lower_case False \
    --max_seq_length 128 \
    --max_predictions_per_seq 10 \
    --masked_lm_prob 0.15 \
    --random_seed 42 \
    --dupe_factor 5

python bert-master/run_pretraining.py --input_file tf_examples_multi.tfrecord --output_dir trained_model --do_train True --do_eval True --bert_config_file multi_cased/bert_config.json --init_checkpoint multi_cased/bert_model.ckpt.index --train_batch_size 32 --max_seq_length 128 --max_predictions_per_seq 10 --num_train_steps 10000 --num_warmup_steps 10 --learning_rate 2e-5 

use learning rate 2e-5 when starting from a pretrained model otherwise use 1e-4