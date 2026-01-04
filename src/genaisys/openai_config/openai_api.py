import logging
import os
from typing import Optional

from openai import APIError, RateLimitError, APITimeoutError, APIConnectionError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from .openai_setup import init_openai_api

# Configure logging
logger = logging.getLogger(__name__)

# Default configuration (can be overridden via environment variables)
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
DEFAULT_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1024"))
DEFAULT_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0"))
DEFAULT_TIMEOUT = int(os.getenv("OPENAI_TIMEOUT", "30"))
MAX_RETRIES = int(os.getenv("OPENAI_MAX_RETRIES", "3"))


@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((RateLimitError, APITimeoutError, APIConnectionError)),
    before_sleep=lambda retry_state: logger.warning(
        f"Retrying API call (attempt {retry_state.attempt_number}/{MAX_RETRIES})..."
    )
)
def make_openai_api_call(
    input: str,
    mrole: str = "system",
    mcontent: str = "You are a helpful assistant.",
    user_role: str = "user",
    model: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = None,
    timeout: Optional[int] = None
) -> str:
    """
    Make an API call to OpenAI with retry logic and error handling.

    Args:
        input: The user input/prompt
        mrole: Role for system message (default: "system")
        mcontent: System message content (default: "You are a helpful assistant.")
        user_role: Role for user message (default: "user")
        model: OpenAI model to use (default: gpt-4o)
        temperature: Response randomness 0-1 (default: 0)
        max_tokens: Maximum response tokens (default: 1024)
        timeout: Request timeout in seconds (default: 30)

    Returns:
        str: The assistant's response content

    Raises:
        APIError: For non-retryable API errors
    """
    # Use defaults if not specified
    model = model or DEFAULT_MODEL
    temperature = temperature if temperature is not None else DEFAULT_TEMPERATURE
    max_tokens = max_tokens or DEFAULT_MAX_TOKENS
    timeout = timeout or DEFAULT_TIMEOUT

    messages_obj = [
        {"role": mrole, "content": mcontent},
        {"role": user_role, "content": input}
    ]

    params = {
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    try:
        client = init_openai_api()

        logger.debug(f"Making API call to {model} with {len(input)} chars input")

        response = client.chat.completions.create(
            messages=messages_obj,
            model=model,
            timeout=timeout,
            **params
        )

        # Log token usage for cost monitoring
        if response.usage:
            logger.info(
                f"Token usage - Prompt: {response.usage.prompt_tokens}, "
                f"Completion: {response.usage.completion_tokens}, "
                f"Total: {response.usage.total_tokens}"
            )

        return response.choices[0].message.content

    except RateLimitError as e:
        logger.warning(f"Rate limit exceeded: {e}")
        raise  # Will be retried by tenacity

    except APITimeoutError as e:
        logger.warning(f"Request timed out: {e}")
        raise  # Will be retried by tenacity

    except APIConnectionError as e:
        logger.warning(f"Connection error: {e}")
        raise  # Will be retried by tenacity

    except APIError as e:
        logger.error(f"OpenAI API error: {e}")
        return f"API Error: {str(e)}"

    except Exception as e:
        logger.exception(f"Unexpected error in API call: {e}")
        return f"Unexpected error: {str(e)}"
