# 2026-02-08_Empire_Enforcer_v9_INBOX_SCAN
import os
import shutil
import subprocess
from datetime import datetime

# --- SETUP: QUELLE AUF INBOX GEÄNDERT ---
SOURCE = r"C:\Users\Danny\Desktop\DESKTOP_INBOX"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

# Keywords für Projekte
PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE", "DAN"]

def get_target_pillar(filename):
    fn = filename.upper()
    # Säule 3: Produktion
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", ".FLP", ".ZIP", ".RAR", "BEAT"]): return "03_PRODUKTION"
    # Säule 5: Marketing
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", ".HEIC", "COVER", "PROMO"]): return "05_MARKETING"
    # Säule 2: Kreativ
    if any(ex in fn for ex in [".TXT", ".DOC", ".DOCX", "LYRICS", "TEXT", "CONCEPT"]): return "02_KREATIV"
    # Säule 4: Finals
    if any(x in fn for x in ["MASTER", "FINAL", "MIX_V"]): return "04_FINALS"
    # Säule 1: Strategie (PDFs, Verträge etc.)
    return "01_STRATEGIE"

def run_git_save():
    print("\n📤 GitHub Auto-Save (Empire-Backup)...")
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-Save: {timestamp} (Inbox Scan V9)"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Fortschritt im GitHub-Tresor gesichert.")
    except Exception as e:
        print(f"⚠️ Git-Fehler: {e}")

def start_sorting():
    print(f"🚀 DaN OS: Scanne jetzt die gesamte Inbox: {SOURCE}")
    moved_count = 0
    
    if not os.path.exists(SOURCE):
        print("❌ FEHLER: Inbox-Pfad nicht gefunden!")
        return

    for root, dirs, files in os.walk(SOURCE):
        # Ignoriere System-Ordner und das Archiv selbst
        if any(x in root for x in [".git", "dan-os", "00_DaN_EMPIRE_VAULT_2026"]):
            continue
        
        for file in files:
            # Überspringe Desktop-Systemdateien
            if file.lower() in ["desktop.ini", "thumbs.db"]: continue
            
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            full_context = (fn_upper + root.upper())
            
            # 1. BAU-FILTER (Radikale Trennung)
            if any(x in full_context for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "IMMOBILIE", "STATIK"]):
                dest_dir = PRIVATE_OUTSIDE
            else:
                # 2. PROJEKT-MAPPING (Musik)
                target_project = next((p for p in PROJECTS if p in full_context), None)
                pillar = get_target_pillar(file)
                
                if target_project:
                    dest_dir = os.path.join(VAULT, target_project, pillar)
                else:
                    dest_dir = os.path.join(VAULT, pillar)

            os.makedirs(dest_dir, exist_ok=True)
            try:
                # Nutze shutil.move - falls Datei existiert, wird sie nicht überschrieben (Sicherheit)
                target_path = os.path.join(dest_dir, file)
                if not os.path.exists(target_path):
                    shutil.move(old_path, target_path)
                    print(f"✅ {file} -> {os.path.basename(dest_dir)}")
                    moved_count += 1
                else:
                    print(f"ℹ️ {file} existiert bereits im Ziel - übersprungen.")
            except Exception as e:
                print(f"❌ Fehler bei {file}: {e}")
    
    print(f"\n--- SCAN FERTIG: {moved_count} neue Dateien verarbeitet. ---")
    if moved_count > 0:
        run_git_save()

if __name__ == "__main__":
    start_sorting()