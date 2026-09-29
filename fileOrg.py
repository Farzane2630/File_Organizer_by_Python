import sys
from pathlib import Path

file_extentions = {
    "pdf": "PDFs",
    "png": "Images",
    "jpg":"Images",
    "jpeg":"Images",
    "gif":"Images",
    "doc": "Documents",
    "docx": "Documents",
    "html": "Code",
    "js": "Code",
    "jsx": "Code",
    "tsx": "Code",
    "ts": "Code",
    "txt": "Documents",
    "ipynb": "Documents",
    "md": "Documents",
    "csv": "Data",
    "xlsx": "Data",
    "iso": "Data",
    "json": "Data",
    "zip": "Archives",
    "rar": "Archives",
    "tar": "Archives",
    "tgz": "Archives",
    "exe":"Executables",
    "mp3":"Music",
    "wav":"Music",
    "mp4":"Videos",
    "avi":"Videos",
    "flv":"Videos",
    "wmv":"Videos",
    "svg": "Icons",
    "odg": "Icons",
    "deb": "Pkgs",
    "rpm": "Pkgs"
}


destination = Path(sys.argv[1])

for item in destination.iterdir():
    # check is file or dir
    if item.is_file():
        # normalize extentions to lowercase
        ext = item.suffix.lower().strip(".")
        if ext:
            target_dir = destination / file_extentions[ext]
            target_dir.mkdir(exist_ok=True)
            item.rename(target_dir / item.name)
                

                
    


