from smart_open import open


class MyCorpus(object):
    def __iter__(self):
        for line in open('https://radimrehurek.com/gensim/mycorpus.txt'):
            yield dictionary.doc2bow(line.lower().split())
