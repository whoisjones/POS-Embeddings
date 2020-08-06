
def main():
    with open("resources/spacy_tagged_wikipedia.txt", "r") as file:
        text = file.read().lower()

        # proper nouns
        text = text.replace("_nnp", "_PN")
        text = text.replace("_nnps", "_PN")

        # nouns
        text = text.replace("_nns", "_N")
        text = text.replace("_nn", "_N")

        # verbs
        text = text.replace("_vbd", "_V")
        text = text.replace("_vbg", "_V")
        text = text.replace("_vbn", "_V")
        text = text.replace("_vbp", "_V")
        text = text.replace("_vbz", "_V")
        text = text.replace("_vb", "_V")

        # rest
        text = text.replace("_add", "_REST")
        text = text.replace("_afx", "_REST")
        text = text.replace("_cc", "_REST")
        text = text.replace("_cd", "_REST")
        text = text.replace("_dt", "_REST")
        text = text.replace("_ex", "_REST")
        text = text.replace("_fw", "_REST")
        text = text.replace("_gw", "_REST")
        text = text.replace("_hyph", "_REST")
        text = text.replace("_in", "_REST")
        text = text.replace("_jjr", "_REST")
        text = text.replace("_jjs", "_REST")
        text = text.replace("_jj", "_REST")
        text = text.replace("_ls", "_REST")
        text = text.replace("_md", "_REST")
        text = text.replace("_nfp", "_REST")
        text = text.replace("_nil", "_REST")
        text = text.replace("_pdt", "_REST")
        text = text.replace("_pos", "_REST")
        text = text.replace("_prp$", "_REST")
        text = text.replace("_prp", "_REST")
        text = text.replace("_rbr", "_REST")
        text = text.replace("_rbs", "_REST")
        text = text.replace("_rb", "_REST")
        text = text.replace("_rp", "_REST")
        text = text.replace("_sp", "_REST")
        text = text.replace("_sym", "_REST")
        text = text.replace("_to", "_REST")
        text = text.replace("_uh", "_REST")
        text = text.replace("_wdt", "_REST")
        text = text.replace("_wp$", "_REST")
        text = text.replace("_wp", "_REST")
        text = text.replace("_wrb", "_REST")
        text = text.replace("_xx", "_REST")
        text = text.replace("__sp", "_REST")
        text = text.replace("_-lrb-", "_REST")
        text = text.replace("_-rrb-", "_REST")
        text = text.replace("_,", "_REST")
        text = text.replace("_.", "_REST")
        text = text.replace("_:", "_REST")
        text = text.replace("_''", "_REST")
        text = text.replace("_``", "_REST")
        text = text.replace("_$", "_REST")

    with open("resources/en-wikipedia.tokenized.lowercased.spacy-grouped.txt", "w") as out:
        out.write(text)

if __name__ == "__main__":
    main()