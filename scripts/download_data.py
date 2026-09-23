"""
Descarga el dataset de préstamos de Lending Club (2007-2011) usado en este TP.

Fuente: mirror en GitHub del dataset original de Lending Club, distribuido
públicamente para uso académico. ~39.700 préstamos, 111 columnas, sin
codificar (texto crudo), tal como lo publica Lending Club.

Uso:
    python scripts/download_data.py
"""
import os
import urllib.request

URL = "https://raw.githubusercontent.com/akshayr89/Lending-Club---Exploratory-Data-Analysis/master/loan.csv"
DEST = os.path.join(os.path.dirname(__file__), "..", "data", "loan.csv")

def main():
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    print(f"Descargando dataset desde:\n{URL}")
    urllib.request.urlretrieve(URL, DEST)
    size_mb = os.path.getsize(DEST) / (1024 * 1024)
    print(f"Listo: {DEST} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    main()
