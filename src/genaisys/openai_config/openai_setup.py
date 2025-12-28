from openai import OpenAI
from ..config import settings


def init_openai_api() -> OpenAI:
    """Initialize and return an OpenAI client.

    Reads the API key from application settings and creates
    an authenticated OpenAI client instance.

    Returns:
        OpenAI: Configured OpenAI client ready for API calls.

    Raises:
        RuntimeError: If OPENAI_API_KEY is not configured.
    """
    if not settings.OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY not set')
    return OpenAI(api_key=settings.OPENAI_API_KEY)