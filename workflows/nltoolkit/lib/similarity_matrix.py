from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

f = open("/root/Myfolder/scoringDocuments/doc1")
doc1 = str.decode(f.read(), "UTF-8", "ignore")
f = open("/root/Myfolder/scoringDocuments/doc2")
doc2 = str.decode(f.read(), "UTF-8", "ignore")
f = open("/root/Myfolder/scoringDocuments/doc3")
doc3 = str.decode(f.read(), "UTF-8", "ignore")

train_set = ["president of India",doc1, doc2, doc3]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)  #finds the tfidf score with normalization
print "cosine scores ==> ",cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)  #here the first element of tfidf_matrix_train is matched with other three elements


from nltk.classify.util import names_demo, names_demo_features
