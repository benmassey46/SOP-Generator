import openai
import config

# --- Initialize API Clients ---
# --- OpenAI Client ---
openai_client = None
if config.OPENAI_API_KEY:
    try:
        openai_client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        print("OpenAI client initialized successfully.")
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}. OpenAI functions unavailable.")
        config.OPENAI_API_KEY = None # Mark as unavailable
else:
    print("Warning: OPENAI_API_KEY environment variable not found. OpenAI functions unavailable.")


# -- Expert file API ---
expert_file = None
try:
    expert_filename = config.EXPERT_FILE_PATH
    expert_file = open(expert_filename)
except Exception as e:
    print(f"Error {e} opening user file {expert_filename}")
