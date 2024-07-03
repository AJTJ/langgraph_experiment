import getpass
import os
from dotenv import load_dotenv

def load_env():
  load_dotenv()

  def _set_env(var: str):
      if not os.environ.get(var):
          os.environ[var] = getpass.getpass(f"{var}: ")

  _set_env('ANTHROPIC_API_KEY')
  _set_env("LANGSMITH_API_KEY")
  os.environ["LANGCHAIN_TRACING_V2"] = "true"
  os.environ["LANGCHAIN_PROJECT"] = "LangGraph Tutorial"

