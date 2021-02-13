english_vocab = open('bert-base-uncased/vocab.txt', 'r').read().split('\n')
roman_urdu_vocab = open('roman-urdu-vocab-uncased_50K-vocab.txt', 'r').read().split('\n')

common_vocab = list(set(english_vocab).intersection(set(roman_urdu_vocab)))

augmented_vocab = [''] * len(roman_urdu_vocab)

for vocab in common_vocab:
    augmented_vocab[english_vocab.index(vocab)] = vocab
    roman_urdu_vocab.pop(roman_urdu_vocab.index(vocab))

for i in range(len(augmented_vocab)):
    if augmented_vocab[i] == '':
        augmented_vocab[i] = roman_urdu_vocab.pop(0)

with open('augmented_vocab.txt', 'w') as v:
    v.write('\n'.join(augmented_vocab))
