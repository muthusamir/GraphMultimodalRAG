class DualLevelRetriever:
    def retrieve(self, kg, query_text, query_image=None):
        # Low-level: entity match
        # High-level: graph traversal
        return {"text_nodes": [], "image_nodes": []}
