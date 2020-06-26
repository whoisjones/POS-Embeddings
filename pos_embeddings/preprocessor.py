from flair.models import SequenceTagger
from flair.data import Sentence
import spacy
from pos_embeddings import TAG_CLUSTERING, DATA_DIR
from pathlib import Path

def preprocess(path, cluster_tags, model='spacy'):

    with open(path, 'r') as f:
        sentences = f.read().splitlines()

    sentences = list(filter(None, sentences))

    if model=='spacy':
        spacy.prefer_gpu()
        nlp = spacy.load("en_core_web_sm")
        tag_spacy(sentences, nlp, cluster_tags)
    elif model=='flair':
        tagger = SequenceTagger.load('pos-fast')
        tag_flair(sentences, tagger, cluster_tags)
    else:
        raise Exception('No valid tagger provided. Please use "flair" or "spacy".')


def tag_spacy(sentences, tagger, cluster_tags):
    outfile = Path(DATA_DIR) / "tagged_wikipedia.txt"
    with open(outfile, "w") as output:
        for sentence in sentences:
            str_sent = ""
            doc = tagger(sentence)
            for token in doc:
                str_sent = str_sent + "{}_{} ".format(token.text, token.tag_)
            output.write(str_sent + '\n')
    print("done")


def tag_flair(sentences, tagger, cluster_tags):
    outfile = Path(DATA_DIR) / "tagged_wikipedia.txt"
    with open(outfile, "w") as output:
        for sentence in sentences:
            str_sent = ""
            sent = Sentence(sentence)
            tagger.predict(sent, mini_batch_size=64)
            for token in sent:
                str_sent = str_sent + "{}_{} ".format(token.text, token.get_labels('pos')[0].value)
            output.write(str_sent + '\n')
    print("done")