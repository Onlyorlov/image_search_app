# Find closest images with ML, FastAPI and Docker

## 1. Create model, generate embeddings and train ANN index

[Download Image Dataset](https://products-10k.github.io)

```bash
./preprocess_sript.sh --path_to_zip_archive=/content/test.zip # archive location
```

[Example in Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)

### 1.a Or you can download prepared files for test part of the Products-10k Dataset

[Link to zip archive](https://drive.google.com/file/d/15Y9IkanJFk3hombQu3HgPmrKKxDfAt4l/view?usp=sharing)

### 2. Create Docker container

```bash
docker build -t image-search .

docker run -p 80:80 image-search
```
