from django.apps import AppConfig

from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer


class RecommendationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recommendations'

    def ready(self):
        self.transformer = SentenceTransformer('all-MiniLM-L6-v2')
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")

