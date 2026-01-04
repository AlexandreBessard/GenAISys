from openai import OpenAI
from ..config import settings
# Singleton pattern
# Private variable
_openai_client: OpenAI | None = None

def init_openai_api() -> OpenAI:
    """Initialize and return an OpenAI client.

    Reads the API key from application settings and creates
    an authenticated OpenAI client instance.

    Returns:
        OpenAI: Configured OpenAI client ready for API calls.

    Raises:
        RuntimeError: If OPENAI_API_KEY is not configured.
    """
    global _openai_client # This tell Python to use the _open_client variable defined outside the function
    if _openai_client is None:
        if not settings.OPENAI_API_KEY:
            raise RuntimeError('OPENAI_API_KEY not set')
        _openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    return _openai_client