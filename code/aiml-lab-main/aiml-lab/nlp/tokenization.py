doc = nlp("Apple is looking at buying U.K. startup for \$1 billion")
    
    for token in doc:
        if not token.is\_stop and token.is\_alpha:
            print(token.text)
