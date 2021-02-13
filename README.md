Run the following commands

wget --header="Host: storage.googleapis.com" --header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36" --header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" --header="Accept-Language: en-GB,en-US;q=0.9,en;q=0.8" --header="Referer: https://github.com/google-research/bert/blob/master/multilingual.md" "https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip" -c -O 'multi_cased_L-12_H-768_A-12.zip'

1. Complete training code is present in BERT_ROMAN_URDU.ipynb
2. Use learning rate 2e-5 when starting from a pretrained model otherwise use 1e-4

### Experiments
1. Experiment with different vocabulary sizes (Note common tokens and performance)