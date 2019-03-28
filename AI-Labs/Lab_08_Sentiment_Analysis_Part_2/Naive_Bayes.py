import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

vocab_size = 5000
alpha = 0.00001
data = pd.read_csv("IMDBcleanedData.tsv", sep='\t')
vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=vocab_size)
x = data["review"]
y = data["sentiment"]
assert len(x) == len(y)
print("Training with alpha {} and vocab size {}".format(alpha, vocab_size))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=20, random_state=0)
x_train = vectorizer.fit_transform(x_train).toarray()
clf = MultinomialNB(alpha=alpha)
clf.fit(x_train, np.array(y_train))
x_test = vectorizer.transform(x_test).toarray()
y_prediction = clf.predict(x_test)
acc = accuracy_score(y_test, y_prediction)
print("The accuracy is: ", acc)
