"""Embedding service for generating text embeddings using SentenceTransformer."""

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-base")