#!/usr/bin/env python3
"""Replace Wrangler template tokens using literal environment values."""

import os
import sys
from pathlib import Path


PLACEHOLDERS = {
    "NAME": "${NAME}",
    "CUSTOM_DOMAIN": "${CUSTOM_DOMAIN}",
    "DOMAIN": '"${DOMAIN}"',
    "ADMIN": "${ADMIN}",
    "PASSWORD": "${PASSWORD}",
    "JWT_SECRET": "${JWT_SECRET}",
    "R2_BUCKET_NAME": "${R2_BUCKET_NAME}",
    "PROJECT_LINK": "${PROJECT_LINK}",
    "ANALYSIS_CACHE": "${ANALYSIS_CACHE}",
    "AI_MODEL": "${AI_MODEL}",
    "LINUXDO_CLIENT_ID": "${LINUXDO_CLIENT_ID}",
    "LINUXDO_CLIENT_SECRET": "${LINUXDO_CLIENT_SECRET}",
    "LINUXDO_CALLBACK_URL": "${LINUXDO_CALLBACK_URL}",
    "KV_NAMESPACE_ID": "${KV_NAMESPACE_ID}",
    "D1_DATABASE_ID": "${D1_DATABASE_ID}",
}


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("Usage: replace-wrangler-values.py CONFIG_FILE ENV_NAME [ENV_NAME ...]")

    config_path = Path(sys.argv[1])
    names = sys.argv[2:]
    unknown_names = [name for name in names if name not in PLACEHOLDERS]
    if unknown_names:
        raise SystemExit("Unsupported Wrangler environment name.")

    with config_path.open("r", encoding="utf-8", newline="") as config_file:
        config = config_file.read()

    for name in names:
        config = config.replace(PLACEHOLDERS[name], os.environ.get(name, ""))

    with config_path.open("w", encoding="utf-8", newline="") as config_file:
        config_file.write(config)


if __name__ == "__main__":
    main()
