import os
import shutil
from datetime import datetime

# --- DNA AUS RESCUE_ARCHITECTURE & DEEP_SORTER ---
VAULT = os.path.expanduser("~/EMPIRE_PROJECTS/00_DaN_EMPIRE_VAULT_2026")
CLUSTERS = ["PRINZESSIN", "SCHERBENHAUFEN", "ES_KOMMT", "MAGNET", "MEER", "RENE"]
COLUMNS = {
    "01": "01_STRATEGIE_UND_ANALYSE",
    "02": "02_KREATIV_TEXT_IDEEN",
    "03": "03_PRODUKTION_AUDIO",
    "04": "04_FINALS_UND_MASTERS",
    "05": "05_MARKETING_UND_VISUALS"
}

def run_factory_check():
    print("🚀 DaN O.S. FACTORY ENGINE STARTET...")
    for project in CLUSTERS:
        proj_path = os.path.join(VAULT, project)
        if not os.path.exists(proj_path):
            os.makedirs(proj_path)
            print(f"📁 Projekt-Cluster angelegt: {project}")
        
        for col_id, col_name in COLUMNS.items():
            path = os.path.join(proj_path, col_name)
            if not os.path.exists(path):
                os.makedirs(path)

    print("✅ ARCHITEKTUR GEPRÜFT. SYSTEM BEREIT FÜR AI STUDIO EXPORT.")

if __name__ == "__main__":
    run_factory_check()
