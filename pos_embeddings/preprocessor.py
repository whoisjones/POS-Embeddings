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
        nlp = spacy.load("en_core_web_sm")
        tag_spacy(sentences, nlp)
    elif model=='flair':
        tagger = SequenceTagger.load('pos')
        tag_flair(sentences, tagger)
    else:
        raise Exception('No valid tagger provided. Please use "flair" or "spacy".')


def tag_spacy(sentences, tagger):
    outfile = Path(DATA_DIR) / "tagged_wikipedia.txt"
    with open(outfile, "w") as output:
        for idx, sentence in enumerate(sentences):
            str_sent = ""
            doc = tagger(sentence)
            for token in doc:
                text = token.text
                tag = "REST"
                for overall_tag, granular_tags in TAG_CLUSTERING.items():
                    if token.tag_ in granular_tags:
                        tag = overall_tag
                str_sent = str_sent + "{}_{} ".format(text, tag)
            output.write(str_sent)
            output.write("\n")
            output.write("\n")
            print(str_sent)
            print("sentence {} tagged.".format(idx))
    print("done")


def tag_flair(sentences, tagger):
    outfile = Path(DATA_DIR) / "tagged_wikipedia.txt"
    with open(outfile, "w") as output:
        for idx, sentence in enumerate(sentences):
            str_sent = ""
            sent = Sentence(sentence)
            tagger.predict(sent)
            for token in sent:
                text = token.text
                tag = "REST"
                for overall_tag, granular_tags in TAG_CLUSTERING.items():
                    if token.get_labels('pos')[0].value in granular_tags:
                        tag = overall_tag
                str_sent = str_sent + "{}_{} ".format(text, tag)
            output.write(str_sent)
            output.write("\n")
            output.write("\n")
            print(str_sent)
            print("sentence {} tagged.".format(idx))
    print("done")