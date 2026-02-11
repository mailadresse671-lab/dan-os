# 2026-02-08_YouTube_Guardian_v1_SAFETY_FIRST
import os
import tomllib  # Nutzt das moderne TOML-Format

# --- KONFIGURATION ---
VAULT = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026"
SECRETS_FILE = os.path.join(VAULT, "secrets.toml")

def check_security_clearance():
    print("🛡️  DaN OS: Starte Sicherheits-Check für YouTube-Schnittstelle...")
    
    # 1. Existenzprüfung
    if not os.path.exists(SECRETS_FILE):
        print(f"❌ KRITISCH: 'secrets.toml' wurde nicht im Vault gefunden!")
        print("💡 Aktion: Erstelle die Datei manuell und füge deine Keys ein.")
        return False

    # 2. Key-Validierung
    try:
        with open(SECRETS_FILE, "rb") as f:
            secrets = tomllib.load(f)
            
        # Prüfe notwendige Sektionen
        yt_secrets = secrets.get("YOUTUBE", {})
        client_id = yt_secrets.get("CLIENT_ID", "")
        client_secret = yt_secrets.get("CLIENT_SECRET", "")

        if not client_id or not client_secret or client_id == "DEINE_ID":
            print("⚠️  WARNUNG: YouTube-Zugangsdaten sind unvollständig oder noch im Template-Status.")
            return False
            
        print("✅ Sicherheits-Check bestanden: 'secrets.toml' ist korrekt konfiguriert.")
        return True

    except Exception as e:
        print(f"❌ FEHLER beim Lesen der Secrets: {e}")
        return False

def init_connection():
    if check_security_clearance():
        print("🚀 Status: Verbindung zu YouTube bereit für Initialisierung (OAuth2 Flow).")
        # Hier wird später der Upload-Code angedockt
    else:
        print("🛑 Zugriff verweigert: Bitte korrigiere deine secrets.toml.")

if __name__ == "__main__":
    init_connection()