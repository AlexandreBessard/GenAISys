from llama_cpp import Llama
import os
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to the GGUF quantized model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "DeepSeek-R1-Distill-Llama-8B-GGUF",
    "DeepSeek-R1-Distill-Llama-8B-Q4_K_M.gguf"
)

# Global variable for lazy loading
_model = None


def _load_model():
    """Lazy load the GGUF model."""
    global _model

    if _model is None:
        logger.info("Loading DeepSeek model from: %s", MODEL_PATH)
        load_start = time.time()
        _model = Llama(
            model_path=MODEL_PATH,
            n_ctx=2048,       # Context window
            n_threads=12,      # CPU threads (adjust based on your CPU)
            verbose=False
        )
        load_time = time.time() - load_start
        logger.info("Model loaded successfully in %.2f seconds", load_time)
    else:
        logger.debug("Using cached model instance")

    return _model


def make_deepseek_call(input: str, mrole: str = "system",
                       mcontent: str = "You are a helpful assistant. Keep it short",
                       user_role: str = "user",
                       max_new_tokens: int = 128,
                       temperature: float = 0.7) -> str:
    logger.info("DeepSeek call started | max_tokens=%d, temperature=%.2f", max_new_tokens, temperature)
    logger.debug("Input prompt length: %d characters", len(input))

    model = _load_model()

    # mcontent = system prompt (e.g., "You are a helpful assistant.")
    # input = conversation history + current user question (already formatted with User:/Assistant:)
    prompt = f"{mcontent}\n\n{input}\nAssistant:"

    logger.debug("Full prompt:\n%s", prompt)

    generation_start = time.time()
    output = model(
        prompt,
        max_tokens=max_new_tokens,
        temperature=temperature,
        stop=["User:", "\n\nUser"]
    )
    generation_time = time.time() - generation_start

    response = output["choices"][0]["text"].strip()

    # Extract token usage from output
    tokens_generated = output.get("usage", {}).get("completion_tokens", len(response.split()))
    tokens_per_sec = tokens_generated / generation_time if generation_time > 0 else 0

    logger.info("DeepSeek call completed | time=%.2fs, tokens=%d, speed=%.1f tokens/sec",
                generation_time, tokens_generated, tokens_per_sec)
    logger.debug("Response length: %d characters", len(response))

    return response