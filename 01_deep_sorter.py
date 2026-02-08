# 2026-02-08_Empire_Enforcer_v8_FINAL_RECOVERY
import os
import shutil
import subprocess
from datetime import datetime

# --- SETUP ---
SOURCE = r"C:\Users\Danny\Desktop\DESKTOP_INBOX\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

# Keywords für deine Projekte - HIER ERWEITERN falls nötig!
PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE", "DAN"]

def get_target_pillar(filename):
    fn = filename.upper()
    # 03 PRODUKTION
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", ".FLP", ".ZIP", ".RAR", "BEAT"]): return "03_PRODUKTION"
    # 05 MARKETING
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", ".HEIC", "COVER", "PROMO"]): return "05_MARKETING"
    # 02 KREATIV
    if any(ex in fn for ex in [".TXT", ".DOC", ".DOCX", "LYRICS", "TEXT", "CONCEPT"]): return "02_KREATIV"
    # 04 FINALS
    if any(x in fn for x in ["MASTER", "FINAL", "MIX_V"]): return "04_FINALS"
    # 01 STRATEGIE (Standard für PDF/Rest)
    return "01_STRATEGIE"

def run_git_save():
    print("\n📤 GitHub Auto-Save wird ausgeführt...")
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto-Save: {timestamp} (V8 Run)"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Alles im Tresor gesichert!")
    except Exception as e:
        print(f"⚠️ Git-Fehler: {e}")

def start_sorting():
    print(f"🚀 DaN OS: Scanne {SOURCE}...")
    moved_count = 0
    
    if not os.path.exists(SOURCE):
        print("❌ FEHLER: Quellordner nicht gefunden!")
        return

    for root, dirs, files in os.walk(SOURCE):
        if ".git" in root or "dan-os" in root: continue
        
        for file in files:
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            full_context = (fn_upper + root.upper()) # Durchsucht Dateiname + Ordnername
            
            # 1. BAU-FILTER
            if any(x in full_context for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "IMMOBILIE"]):
                dest_dir = PRIVATE_OUTSIDE
            else:
                # 2. PROJEKT-MAPPING
                target_project = next((p for p in PROJECTS if p in full_context), None)
                pillar = get_target_pillar(file)
                
                if target_project:
                    dest_dir = os.path.join(VAULT, target_project, pillar)
                else:
                    dest_dir = os.path.join(VAULT, pillar)

            os.makedirs(dest_dir, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest_dir, file))
                print(f"✅ {file} -> {os.path.basename(dest_dir)}")
                moved_count += 1
            except: pass
    
    print(f"\n--- FERTIG: {moved_count} Dateien verarbeitet. ---")
    if moved_count > 0:
        run_git_save()

if __name__ == "__main__":
    start_sorting()