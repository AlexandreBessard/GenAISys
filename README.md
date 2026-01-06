# GenAISys
AI system built in Python

# Environment variable:
PyCharm setup

Run/Debug Configuration → Environment variables: PyCharm will auto-read .env if you enable “Autoload environment variables from .env files” (Settings → Build, Execution, Deployment → Python → Enable).

Or set variables directly in the Run Configuration.

- Create a .env file at the root directory with the OPENAI_API_KEY

To download the DeepSeek model locally:
huggingface-cli download bartowski/DeepSeek-R1-Distill-Llama-8B-GGUF --include "DeepSeek-R1-Distill-Llama-8B-Q4_K_M.gguf" --local-dir src/genaisys/models/DeepSeek-R1-Distill-Llama-8B-GGUF