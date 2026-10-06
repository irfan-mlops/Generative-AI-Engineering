"""
Download a model from Hugging Face Hub.

Usage:
    python download_hf_model.py --model_id microsoft/Phi-3-mini-4k-instruct --output_dir models/phi3

For gated/private models:
    1. Create a Hugging Face access token.
    2. Set it as an environment variable:
       Windows PowerShell:
           $env:HF_TOKEN="hf_xxxxxxxxxxxxxxxxx"
    3. Run the script normally.
"""

import os
import argparse
from huggingface_hub import snapshot_download


def download_model(model_id: str, output_dir: str, revision: str = "main"):
    token = os.getenv("HF_TOKEN")

    print(f"\nModel      : {model_id}")
    print(f"Save folder: {output_dir}")
    print(f"Revision   : {revision}")
    print("\nDownloading model from Hugging Face...\n")

    local_path = snapshot_download(
        repo_id=model_id,
        local_dir=output_dir,
        revision=revision,
        token=token,
        resume_download=True,
    )

    print("\nDownload completed successfully.")
    print(f"Model saved at: {local_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Download a complete model repository from Hugging Face Hub."
    )

    parser.add_argument(
        "--model_id",
        required=True,
        help="Hugging Face model ID, e.g. microsoft/Phi-3-mini-4k-instruct",
    )

    parser.add_argument(
        "--output_dir",
        required=True,
        help="Local folder where the model will be saved.",
    )

    parser.add_argument(
        "--revision",
        default="main",
        help="Repository revision/branch/tag. Default: main",
    )

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    download_model(
        model_id=args.model_id,
        output_dir=args.output_dir,
        revision=args.revision,
    )


if __name__ == "__main__":
    main()
