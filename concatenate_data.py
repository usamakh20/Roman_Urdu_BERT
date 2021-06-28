import glob

files = glob.glob('data/' + '*')

text_data = []
for file in files:
    with open(file, 'r') as data:
        text = list(filter(lambda x: x != '\n', data.readlines()))
        text_data.append(''.join(text))

with open('all_data.txt','w') as f:
    f.write('\n'.join(text_data))