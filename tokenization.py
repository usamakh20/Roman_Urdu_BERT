import tokenizers

vocab_length = 105879

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
    vocab_size=vocab_length,
    min_frequency=3,
    limit_alphabet=1000,
    show_progress=True,
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[MASK]', '[SEP]']
)

roman_BWPT.save_model("vocabulary", "roman-urdu-vocab-uncased_"+str(vocab_length))

