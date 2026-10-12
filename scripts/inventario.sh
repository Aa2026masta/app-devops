#!/usr/bin/env bash
set -euo pipefail

pasta="${1:-.}"        # se não passar argumento, usa a pasta atual

if [ ! -d "$pasta" ]; then
  echo "Erro: '$pasta' não é uma pasta"
  exit 1
fi

total=0
for f in "$pasta"/*; do
  if [ -f "$f" ]; then
    echo "Ficheiro: $(basename "$f")"
    total=$((total + 1))
  fi
done

echo "Total de ficheiros: $total"
