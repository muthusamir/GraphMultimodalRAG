# GraphMultimodalRAG
#Enhancing Vision-Language Retrieval with Graph-Based and Multimodal RAG Integration

**Official implementation** of the paper:  
*"Enhancing Vision-Language Retrieval with Graph-Based and Multimodal RAG Integration"*

This repository provides the complete code to reproduce the proposed framework integrating **LightRAG**'s graph-based indexing with **Multimodal RAG** for vision-language and domain-specific tasks.

## Highlights
- Unified knowledge graph with CLIP embeddings and NER
- Dual-level retrieval with dynamic modality balancing
- Contrastive learning for hallucination mitigation
- Evaluated on HotpotQA, FEVER, M2RAG, PDF-MVQA, and JurisDocQA-5K

## Installation

```bash
git clone https://github.com/muthusamir/GraphMultimodalRAG.git
cd GraphMultimodalRAG
pip install -r requirements.txt
