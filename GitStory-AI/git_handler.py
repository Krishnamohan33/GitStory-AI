import os
from git import Repo

TEMP_DIR = "temp_repo"

def get_repo_path(url):
    if os.path.exists(TEMP_DIR):
        return TEMP_DIR

    Repo.clone_from(url, TEMP_DIR)
    return TEMP_DIR