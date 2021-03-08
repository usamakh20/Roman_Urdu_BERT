from collections import Counter
import tokenizers

special = ['[PAD]', '[UNK]', '[CLS]', '[MASK]', '[SEP]']

english_vocab = open('bert-base-uncased/vocab.txt', 'r').read().split('\n')[:-1]

roman_BWPT = tokenizers.BertWordPieceTokenizer(
    # add_special_tokens=True, # This argument doesn't work in the latest version of BertWordPieceTokenizer
    unk_token='[UNK]',
    sep_token='[SEP]',
    cls_token='[CLS]',
    clean_text=True,
    handle_chinese_chars=True,
    strip_accents=True,
    lowercase=True,
    wordpieces_prefix='##'
)

roman_BWPT.train(
    files=["all_data.txt"],
    vocab_size=2200,
    min_frequency=3,
    limit_alphabet=25,
    show_progress=True,
    special_tokens=special
)

vocab_dict = roman_BWPT.get_vocab()

common_vocab = list(set(english_vocab).intersection(set(vocab_dict)))


def vocab_filter(item):
    return item[0] not in common_vocab


filtered_vocab = Counter(dict(filter(vocab_filter, vocab_dict.items()))).most_common()

for i in range(1000):
    if '[unused' in english_vocab[i]:
        english_vocab[i] = filtered_vocab.pop()[0]

with open('vocabulary/extended_vocab.txt', 'w') as v:
    v.write('\n'.join(english_vocab)+'\n')