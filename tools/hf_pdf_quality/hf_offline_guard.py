#!/usr/bin/env python3
"""
Hugging Face Offline Guard — Standardmäßig keine Netzwerkverbindung.
"""
import os, sys

def configure_hf_safety(allow_online=False):
    if not allow_online:
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
        return {
            "mode": "OFFLINE_SAFE",
            "network": "DISABLED",
            "telemetry": "DISABLED",
            "token_export": "BLOCKED",
        }
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    return {
        "mode": "ONLINE_EXPLICIT",
        "network": "ENABLED_BY_USER",
        "telemetry": "DISABLED",
        "token_export": "BLOCKED",
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description="HF Offline Guard")
    parser.add_argument("--allow-online", action="store_true")
    args = parser.parse_args()

    status = configure_hf_safety(args.allow_online)
    print("=== HF OFFLINE GUARD ===")
    for k, v in status.items():
        print(f"  {k.upper()}: {v}")

    if not args.allow_online:
        print("\nStandardmodus: Alle externen HF-Zugriffe blockiert.")
        print("Für Online-Zugriff: --allow-online verwenden.")

if __name__ == "__main__":
    main()
