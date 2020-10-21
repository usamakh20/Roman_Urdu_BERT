import tokenizers

roman_BWPT = tokenizers.BertWordPieceTokenizer(
    vocab_file=None,  # because initially we have no vocab file
    # add_special_tokens=True, # This argument doesn't work in the latest version of BertWordPieceTokenizer
    unk_token='[UNK]',
    sep_token='[SEP]',
    cls_token='[CLS]',
    clean_text=True,
    handle_chinese_chars=True,
    strip_accents=True,
    lowercase=False,
    wordpieces_prefix='##'
)

roman_BWPT.train(
    files=["ROMAN_URDU_DATASET.txt"],
    vocab_size=30000,
    min_frequency=3,
    limit_alphabet=1000,
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[MASK]', '[SEP]']
)

roman_BWPT.save_model(".", "roman-urdu-vocab-cased.txt")
