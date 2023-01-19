import os
import argparse
from pathlib import Path

import torch
import torch.nn as nn
import torchvision.models as models

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # projects root directory

def create_model(path_to_save_model:str):
    if not os.path.exists(os.path.dirname(path_to_save_model)):
        os.makedirs(os.path.dirname(path_to_save_model))
    
    resnet50 = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)
    modules = list(resnet50.children())[:-1]
    for param in modules:
        param.requires_grad = False
    embed_model = nn.Sequential(*modules)
    torch.save(embed_model, path_to_save_model)

    tensor = torch.zeros((1, 3, 224, 224))
    embed_model.eval()
    embedding = embed_model.forward(tensor)
    print(f'Embeddings shape: {embedding.detach().numpy().flatten().shape}')

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_save_model', type=str, default=ROOT / 'resources/model.pth', help='Path to save embedding model')

    return parser.parse_args()

def main(opt):
    print(f'Creating embedding model')
    create_model(opt.path_to_save_model)
    print(f'Model saved to {opt.path_to_save_model}')

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)