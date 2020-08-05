import fasttext
import os
from gensim.models import Word2Vec

class MySentences(object):
     def __init__(self, dirname, filename):
         self.dirname = dirname
         self.filename = filename

     def __iter__(self):
         for line in open(os.path.join(self.dirname, self.filename)):
             yield line.split()

def train():
    for method in ["cbow", "skipgram"]:
        for dim in [25, 100]:
            model = fasttext.train_unsupervised("resources/en-wikipedia.tokenized.spacy-grouped.txt'", method, maxn=0, min_count=50, dim=dim)
            model.save_model(f"resources/POStagged_{method}_{dim}dim.bin")

            POSsentences = MySentences("resources", "en-wikipedia.tokenized.spacy-grouped.txt")
            model = Word2Vec(POSsentences,
                             size=dim,
                             window=10 if method == "skipgram" else 5,
                             min_count=50,
                             sg= 1 if method == "skipgram" else 0)

            model.save(f"resources/word2vec_POStagged_{method}_{dim}dim.model")

        for dim in [25, 100, 400]:
            model = fasttext.train_unsupervised("resources/en-wikipedia.tokenized.txt", method, maxn=0, min_count=50, dim=dim)
            model.save_model(f"resources/standard_{method}_{dim}dim.bin")

            normalsentences = MySentences("resources", "en-wikipedia.tokenized.txt")
            model = Word2Vec(normalsentences,
                             size=dim,
                             window=10 if method == "skipgram" else 5,
                             min_count=50,
                             sg=1 if method == "skipgram" else 0)

            model.save(f"resources/word2vec_normal_{method}_{dim}dim.model")



if __name__ == "__main__":
    train()