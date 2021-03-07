english_vocab = open('bert-base-uncased/vocab.txt', 'r').read().split('\n')[:-1]
roman_urdu_vocab = open('vocabulary/roman-urdu-vocab-uncased_50000-vocab.txt', 'r').read().split('\n')[:-1]

common_vocab = list(set(english_vocab).intersection(set(roman_urdu_vocab)))

augmented_vocab = [''] * len(roman_urdu_vocab)

for vocab in common_vocab:
    augmented_vocab[english_vocab.index(vocab)] = vocab
    roman_urdu_vocab.pop(roman_urdu_vocab.index(vocab))

for i in range(len(augmented_vocab)):
    if augmented_vocab[i] == '':
        augmented_vocab[i] = roman_urdu_vocab.pop(0)

with open('vocabulary/augmented_vocab.txt', 'w') as v:
    v.write('\n'.join(augmented_vocab))
