from openai import OpenAI
from ..config import settings

def init_openai_api() -> OpenAI:
    if not settings.OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY not set')
    return OpenAI(api_key=settings.OPENAI_API_KEY)