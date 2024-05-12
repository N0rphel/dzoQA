import datasets
from datasets import DownloadManager

dl_manager = DownloadManager()
url = "https://n0rphel.github.io/dzoqa.github.io/data3.json"
lin2 = 'https://github.com/N0rphel/dzoQA/raw/main/dataset/data3.json.gz'
out = dl_manager.download_and_extract(lin2)
print(out)