import fasttext

def train():
    for dim in [25, 100]:
        model = fasttext.train_unsupervised("resources/en-wikipedia.tokenized.spacy-grouped.txt", "skipgram", minn=0, maxn=0, dim=dim)
        model.save_model(f"resources/fasttext_wikipedia_spacy_{dim}dim.bin")

    for dim in [25, 100, 400]:
        model = fasttext.train_unsupervised("resources/en-wikipedia.tokenized.txt", "skipgram", minn=0, maxn=0, dim=dim)
        model.save_model(f"resources/fasttext_wikipedia_normal_{dim}dim.bin")


if __name__ == "__main__":
    train()