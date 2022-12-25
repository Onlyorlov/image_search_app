import os
import zipfile
import argparse
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # projects root directory

def create_dataset(path_to_dataset:str, path_to_zip_archive:str):
    '''
    Args:
        path_to_zip_archive (string): Path to archived data
        path_to_dataset (string): Directory with Images
    '''
    if not os.path.exists(path_to_dataset):
        os.makedirs(path_to_dataset)
    
    # extract without structure
    with zipfile.ZipFile(path_to_zip_archive, 'r') as zip_ref:
        for zip_info in zip_ref.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip_ref.extract(zip_info, path_to_dataset)

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_to_zip_archive', type=str, required=True, help='Path to archived data')
    parser.add_argument('--path_to_save_data', type=str, default=ROOT / 'data', help='Directory to save images')

    return parser.parse_args()

def main(opt):
    print(f'Extracting images')
    create_dataset(opt.path_to_save_data, opt.path_to_zip_archive)
    print(f'Images saved to {opt.path_to_save_data}')

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)