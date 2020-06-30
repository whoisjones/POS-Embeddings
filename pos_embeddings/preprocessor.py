from flair.models import SequenceTagger
from flair.data import Sentence
import spacy
from pos_embeddings import TAG_CLUSTERING, DATA_DIR
from pathlib import Path

def preprocess(path, model='spacy'):

    with open(path, 'r') as f:
        sentences = f.read().splitlines()

    sentences = list(filter(None, sentences))

    if model=='spacy':
        spacy.require_gpu()
        nlp = spacy.load("en_core_web_sm")
        tag_spacy(sentences, nlp)
    elif model=='flair':
        tagger = SequenceTagger.load('pos-fast')
        tag_flair(sentences, tagger)
    else:
        raise Exception('No valid tagger provided. Please use "flair" or "spacy".')


def tag_spacy(sentences, tagger):
    outfile = Path(DATA_DIR) / "spacy_tagged_wikipedia.txt"
    print("starts tagging...")
    with open(outfile, "w") as output:
        for idx, sentence in enumerate(sentences):
            doc = tagger(sentence)
            output.write(format_text_spacy(doc))
            output.write("\n")
            if idx % 10000 == 0:
                print(idx)
    print("done")

def format_text_spacy(sentence):
    list = []
    for token in sentence:
        list.append(token.text + "_" + token.tag_)
    return " ".join(list)


def tag_flair(sentences, tagger):
    list = [Sentence(elem) for elem in sentences]
    outfile = Path(DATA_DIR) / "flair_tagged_wikipedia.txt"
    tagger.predict(list, mini_batch_size=64)
    list = [format_text_flair(elem) for elem in list]
    with open(outfile, "w") as output:
        output.write("\n".join(list))

def format_text_flair(sentence):
    list = []
    for token in sentence:
        list.append(token.text + "_" + token.get_labels('pos')[0].value)
    return " ".join(list)