# create_index.py
'''
params:
    path-to-model
    path-to-archive
    dir-to-save-index
'''
import os
import argparse
import numpy as np
from tqdm import tqdm
from pathlib import Path

import torch
from torch.utils.data import DataLoader

from src.index import HNSWIndex
from src.utils import Predictor, IMG_Dataset, transform

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # projects root directory


def create_index(path_to_data:str, path_to_model:str, dir_to_save_index:str, dim:int):
    path_to_index = os.path.join(dir_to_save_index, 'index.in')
    path_to_fnms = os.path.join(dir_to_save_index, 'fnms.pkl')

    dataset = IMG_Dataset(path_to_data, transform)
    dataset.save_fnms(path_to_fnms)
    fnms = dataset.get_fnms()

    loader = DataLoader(
        dataset,
        batch_size=128,
        shuffle=False,
        drop_last=False,
        num_workers=2
    )

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    emb_model = Predictor(path_to_model, transform, device)

    # create embeddings
    result_embeddings = []
    for batch in tqdm(loader):
        embeddings = emb_model.get_batched_embeddings(batch)
        result_embeddings.append(embeddings)
    result_embeddings = np.vstack(result_embeddings).reshape((-1, dim))
    num_embeddings = result_embeddings.shape[0]
    print(f'Num embeddings: {num_embeddings}, shape: {dim}.')

    # create index
    index = HNSWIndex(num_embeddings, dim)
    index.build(fnms, result_embeddings)
    index.save(path_to_index)

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_data', type=str, default=ROOT / 'data', help='Directory with images')
    parser.add_argument('--path_to_model', type=str, default=ROOT / 'resources/model.pth', help='Path to saved model')
    parser.add_argument('--path_to_index', type=str, default=ROOT / 'resources', help='Directory to save index')
    parser.add_argument('--dim', type=int, default=2048, help='Embeddings dim')

    return parser.parse_args()

def main(opt):
    print(f'Extracting embeddings and creating index')
    create_index(opt.path_to_data, opt.path_to_model, opt.path_to_index, opt.dim)
    print(f'Index saved to {opt.path_to_index}')

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)