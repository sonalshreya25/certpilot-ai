from pathlib import Path
from typing import List, Dict

KNOWLEDGE_DIR = Path(__file__).resolve().parents[1] / "data" / "knowledge_base"

def load_knowledge_documents() -> List[Dict[str, str]]:
    docs = []
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        docs.append({
            "source": path.name,
            "content": path.read_text(encoding="utf-8")
        })
    return docs

def simple_retrieve(query: str, limit: int = 3) -> List[Dict[str, str]]:
    """Tiny local retrieval for MVP. Later replace with Foundry IQ / Azure AI Search."""
    query_terms = {term.lower() for term in query.split() if len(term) > 2}
    scored = []
    for doc in load_knowledge_documents():
        content_lower = doc["content"].lower()
        score = sum(1 for term in query_terms if term in content_lower)
        if score > 0:
            scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:limit]]
