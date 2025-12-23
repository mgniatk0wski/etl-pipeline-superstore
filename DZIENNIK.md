# DZIENNIK

## ETAP 1: Inicjalizacja projektu i środowiska
**CEL:** Stworzenie izolowanego środowiska pracy, aby uniknąć konfliktów bibliotek i zachować porządek zgodny z dobrymi praktykami inżynierii danych.

**Kroki:**

1. Utworzenie struktury katalogów:
    * `data/raw` - na surowe pliki CSV (odseparowanie danych od kodu)
    * `notebooks/` - na eksperymenty i analize
    * `src/` - na finalne skrypty Python.
2. Konfiguracja Virtual Enviroment (`venv`):
    * Zainstalowano: `pandas`, `sqlalchemy`, `psycopg2-binary`.
    * Stworzono: `requirements.txt` dla powtarzalności środowiska.
3. Inicjalizacja Git i Konfiguracja `.gitignore`:
    * Uruchomienie śledzenia zmian
    * Napotkany problem: Początkowo plik `.gitignore` blokował widoczność wszystkich plików (przez wildcard `*` przeniesiony z venv)
    * Rozwiazanie: Wyczyszczenie `.gitignore` i dodanie precyzyjnych reguł (ignorowanie `venv/`, `DS_Store`, `data/`)
4. Integracja z GitHubem
    * Utworzenie pustego repozytorium publiczengo
    * Podpięcie zdalnego serwera (`git remote add`)
    * Pchnięcie pierwszej wersji projektu (`git push`)

## ETAP 2: Ekstrakcja i transformacja wstępna (Jupyter)
**CEL:** Zrozumienie struktury danych, naprawa typów danych i przygotowanie ich do załadowania do SQL.

**Kroki:**

1. Wczytywanie danych z uwzględnieniem kodowania (`encoding='latin1' - rozwiazanie problemow z bledami znakow`).
2. Audyt danych (`df.info()`):
    * **Zidentyfikowane problemy:**
        * Kolumny `Order Date` i `Ship date` sa typu `object` zamiast `datetime`.
        * Nazwy kolumn zawieraja spacje i myslinki (np. `Row Id`, `Sub-Category`) co jest niezgodne ze standardem SQL.
    * **Czyszczenie i transformacja danych:**
        * Przy standaryzacji nazw kolumn zastosowano `snake_case`, by ułatwić późniejsze zapytania SQL.
        * Przy konwersji typów danych dla pól `order_date` oraz `ship_date` zastosowano format `datetime64[ns]` uzywajac do tego metody `.astype()`