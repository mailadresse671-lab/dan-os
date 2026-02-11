# 2026-02-08_Lyric_Math_Analyzer_v1
import os
import tomllib
import requests # Falls nicht installiert: pip install requests

def load_secrets():
    with open("secrets.toml", "rb") as f:
        return tomllib.load(f)

def analyze_lyrics(file_path):
    secrets = load_secrets()
    api_key = secrets["AI_KEYS"]["GROQ_API_KEY"]
    
    with open(file_path, "r", encoding="utf-8") as f:
        lyrics = f.read()

    print(f"🧠 Analysiere {os.path.basename(file_path)} nach Melodischer Mathematik...")

    prompt = f"""
    Analysiere diesen Songtext nach den Regeln der 'Melodischen Mathematik' (Major-Level-Standard):
    1. Chorus-Eintritt: Ist das Setup so, dass der Chorus vor 0:50 Min knallen kann?
    2. Syllabische Spiegelung: Sind die Zeilenlängen in den Versen konsistent für den Flow?
    3. Glue-Hooks: Gibt es repetitive Phrasen, die im Ohr bleiben?
    4. Kritik: Wo ist der Text zu kompliziert/ineffizient?

    Songtext:
    {lyrics}
    """

    # API Call zu Groq (oder Gemini, je nach Key)
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    
    if response.status_code == 200:
        print("\n--- ANALYSE ERGEBNIS ---")
        print(response.json()['choices'][0]['message']['content'])
    else:
        print(f"❌ Fehler: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Beispiel: Wir nehmen den ersten Text aus PRINZESSIN
    target = r"C:\Users\Danny\Desktop\00_DaN_EMPIRE_VAULT_2026\PRINZESSIN\02_KREATIV"
    files = [f for f in os.listdir(target) if f.endswith(".txt")]
    
    if files:
        analyze_lyrics(os.path.join(target, files[0]))
    else:
        print("ℹ️ Keine .txt Datei in PRINZESSIN/02_KREATIV gefunden. Bitte eine Datei dorthin verschieben oder Pfad anpassen.")