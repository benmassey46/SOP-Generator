import numpy as np

def cosine_similarity(v1, v2):
    """Calculates cosine similarity between two vectors, handling None and zero vectors."""
    if v1 is None or v2 is None:
        return 0.0 # Treat None input as no similarity

    # Ensure inputs are numpy arrays of appropriate type
    v1 = np.asarray(v1, dtype=np.float32)
    v2 = np.asarray(v2, dtype=np.float32)

    # Check for empty vectors (e.g., from encoding empty strings)
    if v1.size == 0 or v2.size == 0:
        return 0.0

    # Calculate norms
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    # Handle zero vectors (vectors with zero magnitude)
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0 # Or 1.0 if both are zero? Conventionally 0.0 for similarity.

    # Calculate cosine similarity
    # Ensure dot product is calculated correctly for 1D arrays
    dot_product = np.dot(v1, v2)
    similarity = dot_product / (norm_v1 * norm_v2)

    # Clip result to [0.0, 1.0] range due to potential floating-point inaccuracies
    # Especially relevant since we use normalize_embeddings=True for ST
    return np.clip(similarity, 0.0, 1.0)
