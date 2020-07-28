import fasttext

def train():
    model = fasttext.train_unsupervised("resources/en-wikipedia.tokenized.spacy-grouped.txt'", "cbow", dim=32)
    model.save_model("resources/fasttext_wikipedia_spacy.bin")



if __name__ == "__main__":
    train()