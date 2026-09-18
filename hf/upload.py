"""Mirror the benchmark (plus agent transcripts, which git ignores) to a Hugging Face dataset.

    hf auth login                      # once, with a write token
    python3 hf/upload.py <namespace>   # e.g. python3 hf/upload.py FaroutYLq
"""
import sys
from pathlib import Path
from huggingface_hub import HfApi

ROOT = Path(__file__).resolve().parent.parent
ns = sys.argv[1]
repo = f"{ns}/AxionLimitBench"
api = HfApi()
api.create_repo(repo, repo_type="dataset", exist_ok=True)
api.upload_file(path_or_fileobj=ROOT / "hf/README.md", path_in_repo="README.md", repo_id=repo, repo_type="dataset")
api.upload_large_folder(folder_path=ROOT, repo_id=repo, repo_type="dataset",
                        ignore_patterns=[".git/**", ".gitignore", "hf/**", "README.md", "**/work/**",
                                         "**/__pycache__/**", "*.pyc", ".DS_Store", "**/.cache/**"])
print("uploaded to", f"https://huggingface.co/datasets/{repo}")
