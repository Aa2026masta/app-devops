#!/usr/bin/env bash
set -euo pipefail

ORIGEM="${1:?Uso: $0 <pasta_origem> <pasta_destino>}"
DESTINO="${2:?Uso: $0 <pasta_origem> <pasta_destino>}"

if [ ! -d "$ORIGEM" ]; then
  echo "Erro: origem '$ORIGEM' não existe"
  exit 1
fi

DATA=$(date +%Y-%m-%d_%H%M%S)
FICHEIRO="$DESTINO/backup_$DATA.tar.gz"

mkdir -p "$DESTINO"
tar -czf "$FICHEIRO" -C "$ORIGEM" .
echo "Backup criado: $FICHEIRO"
