from pathlib import Path
import argparse
from pos_embeddings import downloader, preprocessor, DATA_DIR, DATA_INFO
from datetime import datetime

def main():
    startTime = datetime.now()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--tiny-wiki",
        "-f",
        required=False,
        action="store_true",
        help="Use tiny dataset for test purposes"
    )

    args = parser.parse_args()

    for name, url in DATA_INFO:
        path = Path(DATA_DIR) / name
        if args.tiny_wiki:
            txt_file_path = Path(DATA_DIR) / 'tiny-wiki.txt'
        else:
            txt_file_path = downloader.download(path=path, download_url=url, return_txt_path=True)
        preprocessor.preprocess(txt_file_path)
        print(datetime.now() - startTime)

if __name__ == "__main__":
    main()