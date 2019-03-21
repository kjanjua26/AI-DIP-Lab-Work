import pandas as pd 
import re 
import nltk 
from bs4 import BeautifulSoup 
from tqdm import tqdm 

nltk.download('stopwords')
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))

regex = re.compile('[^a-zA-Z]')
def cleanData(reviews):
	for ind, data in tqdm(reviews.iterrows()):
		# removing HTML tags, non-alpha characters, making it lower case and spliting it to words. 
		words = regex.sub(' ', BeautifulSoup(data['review'], "lxml").text).lower().split() 
		words_without_stopwords = [w for w in words if w not in stops] # removing stopwords 
		sentence = ' '.join(words_without_stopwords) # joining back to sentence
		reviews["review"][ind] = sentence
	print(reviews.head())
def main():
	reviews = pd.read_csv("labeledTrainData.tsv", sep='\t')
	print(reviews.info())
	print(reviews.shape)
	print(reviews.head())
	cleanData(reviews)

main()
