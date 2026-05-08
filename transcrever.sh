#!/bin/bash
# Aguarda o arquivo de video aparecer e transcreve com Whisper
VIDEO="/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/reuniao-lgpd-06-05-26.mp4"
OUTPUT="/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD/transcricao-reuniao-lgpd-06-05-26.txt"
OUTDIR="/home/cnmfs/ICT/PROTOTYPE/LAYER/LGPD"

echo "Aguardando o arquivo de video em:"
echo "  $VIDEO"
echo ""
echo "Cole ou mova o .mp4 para esse caminho."
echo "O script vai detectar e iniciar a transcricao automaticamente."
echo "=============================================="

# Wait for file
while [ ! -f "$VIDEO" ]; do
    sleep 3
done

SIZE=$(stat -c%s "$VIDEO")
echo "[$(date)] Video detectado: $(numfmt --to=iec $SIZE)"
echo "[$(date)] Iniciando transcricao Whisper (medium, pt-BR)..."
echo ""

whisper "$VIDEO" \
    --model medium \
    --language pt \
    --output_dir "$OUTDIR" \
    --output_format txt \
    --fp16 False \
    --verbose True

# Move output to final location
if [ -f "${OUTDIR}/reuniao lgpd 06 05 26.txt" ]; then
    mv "${OUTDIR}/reuniao lgpd 06 05 26.txt" "$OUTPUT"
fi

echo ""
echo "=============================================="
echo "[$(date)] TRANSCRICAO FINALIZADA"
echo "Arquivo: $OUTPUT"
if [ -f "$OUTPUT" ]; then
    LINES=$(wc -l < "$OUTPUT")
    echo "Linhas: $LINES"
fi
