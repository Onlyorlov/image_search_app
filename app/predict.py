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

import os

# def get_bytes_values(image_names):
#     for image_name in image_names:
#         image_pth = os.path.join(settings.data_dir, image_name)
#         with open(image_pth, 'rb') as f:
#             image_bytes = f.read()
#         yield image_bytes

def get_bytes_values(image_list):
    try:
        image_data=[]
        for image in image_list:
            image_pth = os.path.join(settings.data_dir, image)
            with open(image_pth, 'rb') as f:
                image_bytes = f.read()
            image_data.append(('files',(image.split('.')[0],image_bytes,'image/png')))#('files',(image_name,open image,type))
        return image_data
    except Exception as er:
        print("error occured")
        return "{} error occured".format(er)