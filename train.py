import fasttext

def train():
    with open('resources/en-wikipedia.tokenized.txt', "r") as f:
        text = f.read()
        text.lower()

        with open("resources/en-wikipedia.tokenized.lowercase.txt") as out:
            out.write(text)

    model = fasttext.train_unsupervised('resources/en-wikipedia.tokenized.lowercase.txt', "cbow", dim=32)
    model.save_model("resources/fasttext_wikipedia_normal.bin")



if __name__ == "__main__":
    train()