from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
HEADERS_PEP_TABLE = ('Статус', 'Количество')
TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
PATTERN = r'(PEP \d+)'
DOMAIN = ['peps.python.org']
START_URL = ['https://peps.python.org/']