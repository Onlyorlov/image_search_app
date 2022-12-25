import pickle
import hnswlib
import numpy as np

class HNSWIndex():
    def __init__(self, max_elements:int, dim:int):
        '''
        Args:
            max_elements (int): Number of elements in index
            dim (int): Embedding dim
        '''
        self.max_elements = max_elements
        # Declaring index
        self.index = hnswlib.Index(space='cosine', dim=dim)
        self.index.init_index(max_elements=self.max_elements,
                              ef_construction=200, M=16)
        # Controlling the recall by setting ef:
        # higher ef leads to better accuracy, but slower search
        self.index.set_ef(200) # must be greater than k, btw!
 
    def build(self, fnms:list, data:np.array):
        # Index to fnms list
        self.fnms = fnms
        self.index.add_items(data)

    def query(self, vector:np.array, k:int=10):
        indices, _ = self.index.knn_query(vector, k=k) # can return distances as similarity measure
        return [self.fnms[i] for i in indices[0]] # expects query on one vector thus the slice
    
    def save(self, path_to_index:str):
        self.index.save_index(path_to_index)
    
    def load(self, path_to_index:str, path_to_fnms:str):
        self.index.load_index(path_to_index,
                              max_elements = self.max_elements)
        with open(path_to_fnms, 'rb') as f:
            self.fnms = pickle.load(f)