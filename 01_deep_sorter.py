# 2026-02-08_Empire_Enforcer_v7_AUTOSAVE
import os
import shutil
import subprocess
from datetime import datetime

# --- PFADE ---
SOURCE = r"C:\Users\Danny\Desktop\DESKTOP_INBOX\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE", "DAN"]

def get_target_pillar(filename):
    fn = filename.upper()
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", "BEAT"]): return "03_PRODUKTION"
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", "COVER"]): return "05_MARKETING"
    if any(ex in fn for ex in [".TXT", ".DOC", "LYRICS"]): return "02_KREATIV"
    if "MASTER" in fn or "FINAL" in fn: return "04_FINALS"
    return "01_STRATEGIE"

def run_git_save():
    """Automatisiert den GitHub Upload."""
    print("\n📤 Starte Auto-Save zu GitHub...")
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-Save: {timestamp} (Sorter Run)"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Backup erfolgreich erstellt!")
    except Exception as e:
        print(f"⚠️ Git-Save fehlgeschlagen: {e}")

def start_sorting():
    print(f"🔍 Scan läuft in: {SOURCE}")
    count = 0
    
    if not os.path.exists(SOURCE):
        print(f"❌ PFAD NICHT GEFUNDEN: {SOURCE}")
        return

    for root, dirs, files in os.walk(SOURCE):
        if ".git" in root: continue
        for file in files:
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            
            # 1. BAU-CHECK
            if any(x in (fn_upper + root.upper()) for x in ["BAU", "RECHNUNG", "HAUS"]):
                dest = PRIVATE_OUTSIDE
            else:
                # 2. PROJEKT-SUCHE
                target_project = next((p for p in PROJECTS if p in (fn_upper + root.upper())), None)
                pillar = get_target_pillar(file)
                dest = os.path.join(VAULT, target_project, pillar) if target_project else os.path.join(VAULT, pillar)

            os.makedirs(dest, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest, file))
                print(f"✅ Verschoben: {file}")
                count += 1
            except Exception as e:
                print(f"❌ Fehler bei {file}: {e}")
    
    print(f"\n--- FERTIG: {count} Dateien verarbeitet. ---")
    run_git_save()

if __name__ == "__main__":
    start_sorting()