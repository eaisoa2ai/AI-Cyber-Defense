# ============================================================================= 
# Configuration Management for Cybersecurity AI Agents Project
# =============================================================================
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env (change path if needed)
# Load .env from project root
load_dotenv("my_env.env")

def get_openai_key():
    return os.getenv("OPENAI_API_KEY")

def get_model_name():
    return os.getenv("MODEL_NAME", "gpt-5-nano")

def get_temperature():
    return float(os.getenv("TEMPERATURE", "0.0"))

def get_data_path():
    return os.getenv("DATA_PATH", "data/security_logs.csv")

def get_llm():
    """Get LLM instance for agent tools"""
    try:
        from langchain_openai import ChatOpenAI
        api_key = get_openai_key()
        if api_key:
            return ChatOpenAI(
                model=get_model_name(),
                temperature=get_temperature(),
                api_key=api_key
            )
        else:
            return None
    except ImportError:
        return None

def print_status():
    print("=== Configuration Status ===")
    print(f"OpenAI API Key: {'✅ Set' if get_openai_key() else '❌ Not set'}")
    print(f"Model: {get_model_name()}")
    print(f"Temperature: {get_temperature()}")
    print(f"Dataset Path: {get_data_path()}")
