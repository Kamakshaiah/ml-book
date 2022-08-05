txt = 'This is sentence one. This is sentence two.'
txt.split('.')

out = txt.split('.')
print(out[0])
print(out[1])

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence. This is another sentence.")

for sent in doc.sents:
    print(sent.text)
