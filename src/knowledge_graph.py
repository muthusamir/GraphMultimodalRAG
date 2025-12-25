import clip
import torch
from transformers import pipeline

class KnowledgeGraphBuilder:
    def __init__(self, config):
        self.config = config
        self.ner = pipeline("ner", grouped_entities=True)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.clip_model, self.preprocess = clip.load(self.config['model']['clip_model'], device=self.device)

    def extract_entities(self, text):
        return self.ner(text)

    def extract_image_embedding(self, image_path):
        image = self.preprocess(Image.open(image_path)).unsqueeze(0).to(self.device)
        with torch.no_grad():
            embedding = self.clip_model.encode_image(image)
        return embedding.cpu().numpy()

    def build_from_directory(self, path):
        # Simplified: build graph from files in path
        print(f"Building graph from {path}...")
        # In full version: add nodes/edges to Neo4j or FAISS
        return "knowledge_graph_object"  # placeholder
