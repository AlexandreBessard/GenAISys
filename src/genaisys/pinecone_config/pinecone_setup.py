from pinecone import Pinecone, ServerlessSpec
from ..config import settings

# Singleton instances
_pinecode_client: Pinecone | None = None
_serverless_spec : ServerlessSpec | None = None

def get_pinecode_client() -> Pinecone:
    global _pinecode_client
    if _pinecode_client is None:
        if not settings.PINECONE_API_KEY:
            raise RuntimeError("Pinecode client not set")
        _pinecode_client = Pinecone(api_key=settings.PINECONE_API_KEY)
    return _pinecode_client

def get_serverless_spec(
        cloud="aws",
        region="us-east-1") -> ServerlessSpec:
    global _serverless_spec
    if _serverless_spec is None:
        _serverless_spec = ServerlessSpec(cloud=cloud, region=region)
    return _serverless_spec