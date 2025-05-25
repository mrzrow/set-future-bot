import os
from dotenv import load_dotenv
from pathlib import Path


root = Path(__file__).parent.parent.parent
load_dotenv(root / '.env')

TOKEN = os.environ.get('TOKEN')
