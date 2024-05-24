# TRIP ADVISOR

```
python -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

```
python ./tripadvisor/manage.py runserver
```
```
docker pull qdrant/qdrant
```
```
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```
