import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "resources"
)
DATA_INFO = [
                ("en-wikipedia.tokenized.zip", "https://nlp.informatik.hu-berlin.de/resources/en-wikipedia.tokenized.zip"),
            ]

TAG_CLUSTERING = {
                    'NN':['NN', 'NNS', 'NR', 'NRS', 'NP', 'NPS', 'NNP', 'NNPS'],
                    'VB':['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
                    'JJ':['JJ', 'JJR', 'JJS', 'JJT'],
                    'RB':['RB','RBR', 'RBT', 'RN', 'RP', 'RBS']
                    #'PN':['PN', 'PP', 'PPL', 'PPLS', 'PPO', 'PPS', 'PPSS']
                 }