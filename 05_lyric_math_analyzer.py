import os
import toml
import argparse

def get_vault_path():
    if os.path.exists("secrets.toml"):
        try:
            config = toml.load("secrets.toml")
            return config.get("system", {}).get("vault_path", os.getcwd())
        except:
            return os.getcwd()
    return os.getcwd()

VAULT_BASE = get_vault_path()

def analyze_project(project_name):
    # Wir prüfen den Hauptordner des Projekts
    project_path = os.path.join(VAULT_BASE, project_name)
    target = os.path.join(project_path, "02_KREATIV")
    
    print(f"--- SYSTEM-CHECK ---")
    print(f"Suche in: {project_path}")
    
    if not os.path.exists(project_path):
        print(f"❌ FEHLER: Projekt-Ordner '{project_name}' existiert nicht.")
        print(f"Vorhandene Ordner: {[d for d in os.listdir(VAULT_BASE) if os.path.isdir(os.path.join(VAULT_BASE, d))]}")
        return

    if not os.path.exists(target):
        print(f"⚠️ HINWEIS: Ordner '02_KREATIV' fehlt. Erstelle ihn jetzt...")
        os.makedirs(target, exist_ok=True)

    files = [f for f in os.listdir(target) if f.endswith(".txt")]
    if not files:
        print(f"ℹ️ Keine Texte (.txt) in {target} gefunden. Bitte lege dort deine Lyrics ab.")
        return

    print(f"✅ {len(files)} Dateien gefunden. Starte Melodic Math Analyse...")
    for file in files:
        print(f" > Analysiere: {file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    args = parser.parse_args()
    analyze_project(args.project)
