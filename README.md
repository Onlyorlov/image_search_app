# Find closest images with ML, FastAPI and Docker

## 1. Create model, generate embeddings and train ANN index

```bash
./preprocess_sript.sh --path_to_zip_archive=/content/test.zip # images archive location
```

### 1.a Or you can download prepared files for test part of the Products-10k Dataset

You need to put files inside of this [zip archive](https://drive.google.com/file/d/15Y9IkanJFk3hombQu3HgPmrKKxDfAt4l/view?usp=sharing) in `resources/`, download [images](https://products-10k.github.io) and extract them to `data/`.
You will need to add csv file with product descriptions manually to `resources/` folder from [kaggle](https://www.kaggle.com/competitions/products-10k/data?select=test.csv).

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

## 3a. Populate database when running for the first time

```bash
python ingest_data.py \
    --user=admin \
    --password=admin \
    --host=localhost \
    --port=5432 \
    --db=prod_db \
    --table_name=product_info \
    --fpth=./resources/test_kaggletest.csv
```

<!-- ROADMAP -->
## Roadmap

* [x] Fix Readme

* [ ] Add requirements.txt

* [ ] JS host and port as params

* [ ] Add all params to env variables

* [ ] Add About The Project

* [ ] Cleanup
