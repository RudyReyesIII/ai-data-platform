import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

INPUT_PATH = Path(os.environ["INPUT_PATH"])
OUTPUT_PATH = Path(os.environ["OUTPUT_PATH"])
