from pathlib import Path
from pos_embeddings import downloader, preprocessor, DATA_DIR, DATA_INFO

def main():

    for name, url in DATA_INFO:
        path = Path(DATA_DIR) / name
        #txt_file_path = downloader.download(path=path, download_url=url, return_txt_path=True)
        txt_file_path = Path(DATA_DIR) / "tiny-wiki.txt"
        preprocessor.preprocess(txt_file_path)

if __name__ == "__main__":
    main()