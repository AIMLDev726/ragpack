import os
from ragpackai import ragpackai
from dotenv import load_dotenv

load_dotenv()

# Set your Gemini API key (not project)
gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key:
    os.environ["GOOGLE_API_KEY"] = gemini_key
else:
    print("GEMINI_API_KEY not set in environment")
    exit(1)

# pack = RAGPack.from_files(
#     files=["examples/ai_overview.txt"],
#     embed_model="google:models/embedding-001"
# )
# pack.save("test_gemini.rag")

pack = ragpackai.load(
    "test_gemini.rag",
    llm_config={
        "provider": "google",
        "model_name": "gemini-2.5-flash"
    },
)

answer = pack.ask("Tell me about context given.")
print(answer)