import nltk
import codecs

filename = '/Users/benjsto/Dropbox/Apps/quotoxic/don_quixote_trimmed_short.txt'

lines = []
tagged_words = []

BOM = codecs.BOM_UTF8.decode('utf8')
with codecs.open(filename, encoding='utf-8') as f:
    for line in f:
        lines.append(nltk.word_tokenize(str(line.lstrip(BOM).strip())))

for line in lines:
    tagged_line = nltk.pos_tag(line)

    for word in tagged_line:
        tagged_words.append(word)

print(tagged_words)
print(str(len(tagged_words)) + " tagged words")
