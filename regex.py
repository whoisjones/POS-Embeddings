
def main():
    with open("resources/spacy_tagged_wikipedia.txt", "r") as file:
        text = file.read()

        # proper nouns
        text = text.replace("_NNP", "_PN")
        text = text.replace("_NNPS", "_PN")

        # nouns
        text = text.replace("_NNS", "_N")
        text = text.replace("_NN", "_N")

        # verbs
        text = text.replace("_VB", "_V")
        text = text.replace("_VD", "_V")
        text = text.replace("_VG", "_V")
        text = text.replace("_VN", "_V")
        text = text.replace("_VP", "_V")
        text = text.replace("_VZ", "_V")

        # rest
        text = text.replace("_ADD", "_REST")
        text = text.replace("_AFX", "_REST")
        text = text.replace("_CC", "_REST")
        text = text.replace("_CD", "_REST")
        text = text.replace("_DT", "_REST")
        text = text.replace("_EX", "_REST")
        text = text.replace("_FW", "_REST")
        text = text.replace("_GW", "_REST")
        text = text.replace("_HYPH", "_REST")
        text = text.replace("_IN", "_REST")
        text = text.replace("_JJ", "_REST")
        text = text.replace("_JJR", "_REST")
        text = text.replace("_JJS", "_REST")
        text = text.replace("_LS", "_REST")
        text = text.replace("_MD", "_REST")
        text = text.replace("_NFP", "_REST")
        text = text.replace("_NIL", "_REST")
        text = text.replace("_PDT", "_REST")
        text = text.replace("_POS", "_REST")
        text = text.replace("_PRP", "_REST")
        text = text.replace("_PRP$", "_REST")
        text = text.replace("_RB", "_REST")
        text = text.replace("_RBR", "_REST")
        text = text.replace("_RBS", "_REST")
        text = text.replace("_RP", "_REST")
        text = text.replace("_SP", "_REST")
        text = text.replace("_SYM", "_REST")
        text = text.replace("_TO", "_REST")
        text = text.replace("_UH", "_REST")
        text = text.replace("_WDT", "_REST")
        text = text.replace("_WP", "_REST")
        text = text.replace("_WP$", "_REST")
        text = text.replace("_WRB", "_REST")
        text = text.replace("_XX", "_REST")
        text = text.replace("__SP", "_REST")
        text = text.replace("_-LRB-", "_REST")
        text = text.replace("_-RRB-", "_REST")
        text = text.replace("_,", "_REST")
        text = text.replace("_.", "_REST")
        text = text.replace("_:", "_REST")
        text = text.replace("_''", "_REST")
        text = text.replace("_``", "_REST")
        text = text.replace("_$", "_REST")

    with open("masked_tags.txt", "w") as out:
        out.write(text)

if __name__ == "__main__":
    main()