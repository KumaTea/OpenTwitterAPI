import os


PROJECT_DIR = '.OpenTwitterAPI'
CONFIG_FILE = 'config.ini'
DATA_DIR = 'data'


def get_home_dir():
    """Return the home directory of the current user."""
    return os.path.expanduser('~')


CONFIG_FILE_PATH = os.path.join(get_home_dir(), PROJECT_DIR, CONFIG_FILE)
