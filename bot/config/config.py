from dotenv import load_dotenv
import os
from pathlib import Path


root = Path(__file__).parent.parent.parent
load_dotenv(dotenv_path=root / '.env', override=True)

TOKEN = os.environ.get('TOKEN')
