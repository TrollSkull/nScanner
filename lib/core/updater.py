from pathlib import Path
import tempfile
import zipfile
import shutil
import sys

import requests

from .metadata import __version__
from .const import Colors

PROJECT_ROOT = Path(__file__).resolve().parents[2]
REPO = "TrollSkull/nScanner"

LATEST_RELEASE = f"https://api.github.com/repos/{REPO}/releases/latest"

def update_tool():
    response = requests.get(LATEST_RELEASE, timeout = 10)
    response.raise_for_status()

    data = response.json()
    zip_url = data["zipball_url"]

    print(Colors.BLUE + "\n[nScanner]" + Colors.WHITE + " Downloading update...")

    with tempfile.TemporaryDirectory() as tmp:
        zip_path = Path(tmp) / "update.zip"

        with requests.get(zip_url, stream=True) as request:
            request.raise_for_status()

            with open(zip_path, "wb") as file:
                for chunk in request.iter_content(8192):
                    file.write(chunk)

        with zipfile.ZipFile(zip_path) as zip:
            zip.extractall(tmp)

        extracted = next(Path(tmp).iterdir())

        for item in extracted.iterdir():
            target = PROJECT_ROOT / item.name

            if target.exists():
                if target.is_dir():
                    shutil.rmtree(target)

                else:
                    target.unlink()

            shutil.move(str(item), str(target))

    print(Colors.GREEN + "\n[nScanner]" + Colors.WHITE + " Update completed successfully. " + f"({__version__} > {data["name"]})")
    sys.exit(0)
