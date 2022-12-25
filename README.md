# Find closest images with ML, FastAPI and Docker

## 1. Create model, generate embeddings and train ANN index

```bash
./preprocess_sript.sh --path_to_zip_archive=/content/test.zip # images archive location
```

### 1.a Or you can download prepared files for test part of the Products-10k Dataset

You need to put files inside of this [zip archive](https://drive.google.com/file/d/15Y9IkanJFk3hombQu3HgPmrKKxDfAt4l/view?usp=sharing) in `resources/` folder.

You can download images [here](https://products-10k.github.io)(but we don't use them for now).

## 2. Create Docker container

```bash
docker build -t image-search .

docker run -p 80:80 image-search
```
