from flair.models import SequenceTagger
from flair.data import Sentence
from pos_embeddings import TAG_CLUSTERING, DATA_DIR
from pathlib import Path

def preprocess(path):

    with open(path, 'r') as f:
        sentences = f.read().splitlines()

    tagger = SequenceTagger.load('pos')

    sentences = list(filter(None, sentences))

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
            print("sentence {} tagged.".format(idx))