import io
import torch
from PIL import Image
import torchvision.transforms as transforms
import os
import cv2
import torch
import pickle
from torch.utils.data import Dataset

transform = transforms.Compose([
    transforms.ToTensor(), # converts numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0] 
    transforms.Resize([int(224), int(224)]),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225])
    ])

class Predictor():
    def __init__(self, path_to_model:str, transform, device:str='cpu'):
        '''
        Args:
            path_to_model (str): Path to the model for embeddings
            transform (torchvision.transforms.transforms.Compose): Transformation 
            to be applied on a sample.
        '''
        self.device = device

        self.model = torch.load(path_to_model)
        self.model.to(self.device)
        self.model.eval()

        self.transform = transform

    def get_embedding(self, image_bytes:bytes):
        image = Image.open(io.BytesIO(image_bytes))
        tensor = self.transform(image).unsqueeze(0)
        embedding = self.model.forward(tensor.to(self.device))
        return embedding.detach().cpu().numpy().flatten()

    def get_batched_embeddings(self, batch:torch.Tensor):
        embeddings = self.model.forward(batch.to(self.device))
        return embeddings.detach().cpu().numpy()


class IMG_Dataset(Dataset):
    def __init__(self, path_to_data:str, transform=None):
        '''
        Args:
            dataset_path (str): Path to the dir with data.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        '''
        self.data_path = path_to_data
        fnms = os.listdir(path= path_to_data)
        self.fnms = [f for f in fnms if not f.startswith('.')] #remove hidden files

        self.transform = transform

    def __len__(self):
        return len(self.fnms)

    def __getitem__(self, index:int):
        fnm = self.fnms[index]
        image = cv2.imread(os.path.join(self.data_path, fnm))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # BGR to RGB

        if self.transform:
            image = self.transform(image)
        return image
    
    def get_fnms(self):
        return self.fnms

    def save_fnms(self, path_to_fnms:str):
        with open(path_to_fnms, 'wb') as fp:
            pickle.dump(self.fnms, fp)