import os
import requests
import sys
import zipfile
from pathlib import Path

from pos_embeddings import DATA_DIR

def download(path, download_url, return_txt_path=True):

    print("check is file exits...")
    if not path.is_file():
        print("does not exist - downloading it...")
        with open(path, "wb") as f:
            print("Downloading %s" % os.path.basename(path))
            response = requests.get(download_url, stream=True)
            total_length = response.headers.get("content-length")

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for resources in response.iter_content(chunk_size=4096):
                    dl += len(resources)
                    f.write(resources)
                    done = int(50 * dl / total_length)
                    sys.stdout.write(
                        "\r[%s%s]" % ("=" * done, " " * (50 - done))
                    )
                    sys.stdout.flush()
                print("\n" + 50 * "-")
    else:
        print("zip file found...")

    txt_path = Path(DATA_DIR) / "en-wikipedia.tokenized.txt"

    print("check if txt file exists...")
    if not os.path.isfile(txt_path):
        print("no txt file found...")
        print("extract downloaded zip file...")
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(DATA_DIR)
        print("done...")
    else:
        print("txt file found...")

    if return_txt_path:
        return txt_path