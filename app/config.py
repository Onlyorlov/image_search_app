from pathlib import Path
from pydantic import BaseSettings

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # projects root directory

class Settings(BaseSettings):
    app_name: str = 'Awesome API'
    app_version: str = 'v0.0'
    port: int = 8080
    data_dir: str = 'data/'
    path_to_model: str = str(ROOT / 'resources/model.pth')
    path_to_index: str = str(ROOT / 'resources/index.in')
    path_to_fnms: str = str(ROOT / 'resources/fnms.pkl')
    num_items: int = 55376
    emb_dim: int = 2048
    k: int = 10 # num nearest neighbours

settings = Settings()