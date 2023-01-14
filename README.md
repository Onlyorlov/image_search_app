# Find closest images with ML, FastAPI and Docker

## 1. Create model, generate embeddings and train ANN index

```bash
./preprocess_sript.sh --path_to_zip_archive=/content/test.zip # images archive location
```

### 1.a Or you can download prepared files for test part of the Products-10k Dataset

You need to put files inside of this [zip archive](https://drive.google.com/file/d/15Y9IkanJFk3hombQu3HgPmrKKxDfAt4l/view?usp=sharing) in `resources/`, download [images](https://products-10k.github.io) and extract them to `data/`.

## 2. Create Docker containers

```bash
docker build -f backend.dockerfile -t image-search .

# docker run -it \
#     -p 8080:80 \
#     -v $(pwd)/data:/app/data \
#     image-search
```

```bash
docker build -f frontend.dockerfile -t image-search-front . 

# docker run -it \
#     -p 8000:8000 \
#     image-search-front
```

## 3. Run docker-compose

```bash
docker-compose up
```
