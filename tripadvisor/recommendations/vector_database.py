# encapsualtes the interaction with the vector database.
# contains the complete logic from embedding data - operation - decodeing data.

from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams
from sentence_transformers import SentenceTransformer
from django.conf import settings

# Class to interact with vector database.
# Contains methods to insert, search and delete vectors.
class VectorDatabase():
    def __init__(self):
        self.host = settings.QDRANT_HOST
        self.port=settings.QDRANT_PORT
        self.client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        self.transformer = SentenceTransformer('all-MiniLM-L6-v2')
        self.size = 768
        self.distance = 'Cosine'

    def createCollection(self, collection_name):
        if not self.client.collection_exists(collection_name=collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=self.size,
                    distance=self.distance
                )
            )
        return
    
    def embedData(self, data):
        return self.transformer.encode(data)
    
    def insertData(self, collection_name, data):
        embedded_data = self.embedData(data)
        point = PointStruct(
            id=data["id"], 
            vector=embedded_data, 
            payload={"text": data["text"], "metadata": data["metadata"]}
        )
        self.client.upsert(collection_name=collection_name, points=[point])
        return
    
    def searchQuery(self, collection_name, query, top_k=5):
        embedded_query = self.embedData(query)
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=embedded_query,
            limit=top_k
        )
        results = []
        for res in search_result:
            results.append({
                "id": res.id,
                "text": res.payload["text"],
                "metadata": res.payload["metadata"]
            })
        return results