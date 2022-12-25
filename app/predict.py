import torch

from src.utils import Predictor, transform
from src.index import HNSWIndex
from app.config import settings

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
emb_model = Predictor(settings.path_to_model, transform, device)

index = HNSWIndex(settings.num_items, settings.emb_dim)
index.load(settings.path_to_index, settings.path_to_fnms)

def get_candidates(image_bytes:bytes, k=10):
    '''
    Args:
        image_bytes (bytes): Query image in bytes
        k (int): Number of nearest neighbours for search
    '''
    embedding = emb_model.get_embedding(image_bytes)
    closest = index.query(embedding, k)
    return closest