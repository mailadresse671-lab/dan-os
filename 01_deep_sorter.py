# 2026-02-08_Empire_Enforcer_v5_STABLE
import os
import shutil

# --- CONFIG ---
SOURCE = r"C:\Users\Danny\Desktop\GOOGLE_DRIVE_MASTER"
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
# BAU wird komplett nach DRAUSSEN verbannt
PRIVATE_OUTSIDE = r"C:\Users\Danny\Desktop\00_PRIVAT_QUARANTÄNE_BAU"

PROJECTS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE"]

def get_target_pillar(filename):
    """Ordnet Dateitypen den 5 Säulen zu."""
    fn = filename.upper()
    # Säule 3: Produktion (Audio & Sessions)
    if any(ex in fn for ex in [".WAV", ".MP3", ".ALS", ".LOGIC", ".FLAC", "BEAT", "INSTRUMENTAL"]):
        return "03_PRODUKTION"
    # Säule 5: Marketing (Visuals & Video)
    if any(ex in fn for ex in [".JPG", ".PNG", ".MP4", ".MOV", "COVER", "PROMO", "TIKTOK"]):
        return "05_MARKETING"
    # Säule 2: Kreativ (Lyrics & Konzepte)
    if any(ex in fn for ex in [".TXT", ".DOC", ".DOCX", "LYRICS", "TEXT"]):
        return "02_KREATIV"
    # Säule 4: Finals (Masters)
    if "MASTER" in fn or "FINAL" in fn:
        return "04_FINALS"
    # Säule 1: Strategie (Alles andere: PDFs, Reports)
    return "01_STRATEGIE"

def start_sorting():
    print("🛡️ DaN OS: Empire-Enforcer V5 startet die Säuberung...")
    os.makedirs(PRIVATE_OUTSIDE, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE):
        # Sicherheits-Check: Wir fassen niemals den .git Ordner an!
        if ".git" in root or "dan-os" in root:
            continue
            
        for file in files:
            old_path = os.path.join(root, file)
            fn_upper = file.upper()
            context = (fn_upper + root.upper())
            
            # 1. RADIKALE BAU-ISOLATION (WEG VOM DESKTOP-VAULT)
            if any(x in context for x in ["BAU", "RECHNUNG", "HAUS", "PLAN", "STATIK", "STEUER"]):
                dest_dir = PRIVATE_OUTSIDE
            
            # 2. MUSIK-SORTIERUNG
            else:
                pillar = get_target_pillar(file)
                # Prüfen, ob die Datei einem Projekt gehört
                target_project = None
                for p in PROJECTS:
                    if p in context:
                        target_project = p
                        break
                
                if target_project:
                    dest_dir = os.path.join(VAULT, target_project, pillar)
                else:
                    # Falls kein Projekt gefunden, in die globalen Säulen
                    dest_dir = os.path.join(VAULT, pillar)

            os.makedirs(dest_dir, exist_ok=True)
            try:
                shutil.move(old_path, os.path.join(dest_dir, file))
                print(f"✅ VERSCHOBEN: {file} -> {dest_dir}")
            except Exception as e:
                print(f"❌ ÜBERSPRUNGEN (besetzt): {file}")

if __name__ == "__main__":
    start_sorting()