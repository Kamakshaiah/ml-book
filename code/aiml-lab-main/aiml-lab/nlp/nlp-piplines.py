import spacy

nlp = spacy.load("en_core_web_sm")
##all_stopwords = nlp.Defaults.stop_words
##lemmatizer = nlp.get_pipe('lemmatizer')

if __name__ == '__main__':
##    doc = nlp("This is a sentence. This is another sentence.")
##    or sent in doc.sents:
##    print(sent.text)

##    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
##    
##    for token in doc:
##        if not token.is_stop and token.is_alpha:
##            print(token.text)

##    doc = nlp("I was reading the paper.")
##    for token in doc:
##        print((token.text, token.lemma_))

    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    for ent in doc.ents:
        print((ent.text, ent.label_))
