#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Uso: $0 <nome>"
  exit 1
fi

nome="$1"
echo "Olá, $nome!"
