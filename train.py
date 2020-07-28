import fasttext
from glove import Corpus, Glove

def train():
    model = fasttext.train_unsupervised('masked_tags.txt', "cbow", dim=32)
    model.save_model("resources/fasttext_wikipedia_normal.bin")


if __name__ == "__main__":
    train()