#!/bin/bash
# A Simple Shell Script To Combine all preprocess steps and create needed files in default folders
# Usage: ./preprocess_script.sh --path_to_zip_archive=PATH_TO_ARCHIVE

python create_dataset.py "$@" && python create_model.py && python create_index.py