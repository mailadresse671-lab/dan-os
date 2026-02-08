#!/bin/bash
# Automatische Sicherung für DaN Empire OS

echo "📤 Starte automatische Sicherung..."

# 1. Alles markieren
git add .

# 2. Zeitstempel für das Commit-Log erstellen
timestamp=$(date +"%Y-%m-%d %H:%M")

# 3. Commit ausführen
git commit -m "Auto-Save: $timestamp"

# 4. Hochladen
git push

echo "✅ Alles im GitHub-Tresor gesichert!"