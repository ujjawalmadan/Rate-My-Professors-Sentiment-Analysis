import pickle

def predict_sentiment(string, method):
    if method == 'VADER':
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        analyser = SentimentIntensityAnalyzer()
        score = analyser.polarity_scores([string])
        model = pickle.load(open('models/vader.pkl', 'rb'))
        prob = round(model.predict_proba([[score['pos'], score['neg'], score['compound']]]).max()*100)
        return list(model.predict([[score['pos'], score['neg'], score['compound']]]).flatten()), str(prob) + '%'

    elif method == 'TextBlob':
        from textblob import TextBlob
        score = TextBlob(string).polarity
        model = pickle.load(open('models/textblob.pkl', 'rb'))
        prob = round(model.predict_proba([[score]]).max()*100)
        return list(model.predict([[score]])), str(prob) + '%'

    elif method == 'Logistic Regression':
        model = pickle.load(open('models/Logistic.pkl', 'rb'))
        prob = round(model.predict_proba([string]).max()*100)
        return model.predict([string]), str(prob) + '%'

    elif method == 'Support Vector Machine':
        model = pickle.load(open('models/SVC.pkl', 'rb'))
        return model.predict([string]), 'NA'

    elif method == 'Naive-Bayes':
        model = pickle.load(open('models/NB.pkl', 'rb'))
        prob = round(model.predict_proba([string]).max()*100)
        return model.predict([string]), str(prob) + '%'

    elif method == 'FastText':
        import fasttext
        model = fasttext.load_model("models/fasttext.ftz")
        score = model.predict([string])[0][0][0][-1]
        prob = str(round(model.predict([string], k=5)[1][0][0]*100, 0))[0:2]
        return [score], prob + '%'

    elif method == 'Ensemble':
        logistic_model = pickle.load(open('models/Logistic.pkl', 'rb'))
        logistic_prob = logistic_model.predict_proba([string])[0]

        NB_model = pickle.load(open('models/NB.pkl', 'rb'))
        NB_prob = NB_model.predict_proba([string])[0]

        import fasttext
        fasttext_model = fasttext.load_model("models/fasttext.ftz")
        fasttext_score = fasttext_model.predict([string])[0][0][0][-1]
        fasttext_prob = fasttext_model.predict([string], k=5)
        values = fasttext_prob[1][0]
        order = [int(i[-1])-1 for i in fasttext_prob[0][0]]
        values = [values[i] for i in order]

        final = list(zip(logistic_prob, NB_prob, values))
        final = list(map(sum, final))
        score = final.index(max(final)) + 1
        prob = round(max(final)/3*100)

        return [score], str(prob) + '%'

    else:
        return ['NA'], 'NA'

