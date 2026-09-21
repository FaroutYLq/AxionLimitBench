"""Mirror the benchmark (plus agent transcripts, which git ignores) to a Hugging Face dataset.

    hf auth login                      # once, with a write token
    python3 hf/upload.py <namespace> [paper.pdf]   # e.g. python3 hf/upload.py FaroutYLq ../AxionLimitBench-paper/arxiv/main.pdf

The optional second argument is the paper PDF (preprint footer, not the "do not
distribute" submission build); it is published as paper.pdf at the repository root.
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
if len(sys.argv) > 2:
    api.upload_file(path_or_fileobj=sys.argv[2], path_in_repo="paper.pdf", repo_id=repo, repo_type="dataset")
api.upload_large_folder(folder_path=ROOT, repo_id=repo, repo_type="dataset",
                        ignore_patterns=[".git/**", ".gitignore", "hf/**", "README.md", "**/work/**",
                                         "**/__pycache__/**", "*.pyc", ".DS_Store", "**/.cache/**"])
print("uploaded to", f"https://huggingface.co/datasets/{repo}")
