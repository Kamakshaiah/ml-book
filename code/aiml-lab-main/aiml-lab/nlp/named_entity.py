doc = nlp("Apple is looking at buying U.K. startup for \$1 billion")
    for ent in doc.ents:
        print((ent.text, ent.label_))
