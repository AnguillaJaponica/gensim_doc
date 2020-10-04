from gensim import corpora
from collections import defaultdict
from pprint import pprint
import logging
logging.basicConfig(
    '%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)
documents = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [
    [word for word in document.lower().split() if word not in stoplist]
    for document in documents
]
# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]

pprint(texts)

dictionary = corpora.Dictionary(texts)
# store the dictionary, for future reference
dictionary.save('./deerwester.dict')
print(dictionary)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
# the word "interaction" does not appear in the dictionary and is ignored
print(new_vec)

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(
    'deerwester.mm',
    corpus)  # store to disk, for later use
print(corpus)
