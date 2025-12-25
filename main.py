import argparse
import yaml
from src.knowledge_graph import KnowledgeGraphBuilder
from src.retrieval import DualLevelRetriever
from src.generation import MultimodalGenerator
from src.modality_controller import ModalityController

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main(args):
    config = load_config()

    # 1. Build Knowledge Graph
    print("Building knowledge graph...")
    kg_builder = KnowledgeGraphBuilder(config)
    kg = kg_builder.build_from_directory(args.data_path)

    # 2. Dual-Level Retrieval
    retriever = DualLevelRetriever(kg, config)
    controller = ModalityController(config)

    # 3. Query Processing
    retrieved = retriever.retrieve(args.query_text, args.query_image)
    balanced = controller.balance(retrieved)

    # 4. Generation
    generator = MultimodalGenerator(config)
    response = generator.generate(balanced, args.query_text)

    print("\nResponse:")
    print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="data/")
    parser.add_argument("--query_text", type=str, default="What is the liability clause?")
    parser.add_argument("--query_image", type=str, default=None)
    args = parser.parse_args()
    main(args)
