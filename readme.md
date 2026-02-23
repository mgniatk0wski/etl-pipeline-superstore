OPIS PL

Superstore ETL – Data Pipeline do PostgreSQL

Prosty proces ETL czyszczący surowe dane sprzedażowe i ładujący je do lokalnej bazy danych.
Język: Python 3
Środowisko: Visual Studio Code, Docker

Cel projektu
- Oczyszczenie surowego pliku CSV z danymi sklepu
- Zmiana typów danych i standaryzacja nazw kolumn
- Postawienie izolowanej bazy danych bez konfliktów systemowych
- Automatyczne załadowanie gotowych danych do SQL

Jak to działa?
- Skrypt w Jupyter Notebook czyści brudne dane i wylicza czas dostawy
- Zapisuje plik superstore_processed.csv
- Docker podnosi kontener z bazą PostgreSQL na porcie 5433
- Skrypt load.py czyta czysty CSV i wrzuca go bezpośrednio do tabeli orders

Wykorzystane technologie

Technologia | Zastosowanie
--- | ---
Python 3 | Język główny
Pandas | Ekstrakcja i transformacja danych (Czyszczenie)
Docker / Compose | Infrastruktura bazy danych (Kontener)
PostgreSQL 13 | Relacyjna baza danych
SQLAlchemy | Łączenie Pythona z SQL
psycopg2-binary | Sterownik bazy PostgreSQL
Jupyter Notebook | Środowisko do wstępnej analizy i testów

Struktura projektu
<pre>
├── data/
│   ├── processed_data/ → superstore_processed.csv (ignorowane w git)
│   └── raw_data/ → Sample_Superstore.csv (ignorowane w git)
├── notebooks/
│   └── exploration.ipynb → analiza i transformacja
├── src/
│   ├── load.py → skrypt ładujący dane do bazy
│   └── check_db.py → testowe odpytanie bazy
├── docker-compose.yaml → konfiguracja bazy
├── requirements.txt → pakiety pythona
└── .gitignore → ignorowanie danych i środowiska
</pre>
Jak uruchomić

docker-compose up -d
pip install -r requirements.txt
python src/load.py

Główne funkcjonalności
- Przetwarzanie danych w pamięci (Pandas)
- Omijanie konfliktów portów systemowych (mapowanie 5433:5432)
- Automatyczne tworzenie schematu tabeli w SQL na podstawie DataFrame
- Skrypt weryfikujący połączenie i obecność danych w bazie (check_db.py)

Licencja
Projekt edukacyjny / portfolio — kod otwarty.

---

DESCRIPTION EN

Superstore ETL – PostgreSQL Data Pipeline

A simple ETL process that cleans raw sales data and loads it into a local database.
Language: Python 3
Environment: Visual Studio Code, Docker

Project goals
- Clean raw CSV file containing store data
- Fix data types and standardize column names
- Set up an isolated database without system conflicts
- Automatically load processed data into SQL

How it works
- Jupyter Notebook script cleans raw data and calculates delivery time
- Saves superstore_processed.csv file
- Docker starts a PostgreSQL container on port 5433
- load.py script reads the clean CSV and pushes it directly to the orders table

Used technologies

Technology | Purpose
--- | ---
Python 3 | Main language
Pandas | Data extraction and transformation (Cleaning)
Docker / Compose | Database infrastructure (Container)
PostgreSQL 13 | Relational database
SQLAlchemy | Connecting Python to SQL
psycopg2-binary | PostgreSQL database adapter
Jupyter Notebook | Environment for initial analysis and testing

Project structure
<pre>
├── data/
│   ├── processed_data/ → superstore_processed.csv (git ignored)
│   └── raw_data/ → Sample_Superstore.csv (git ignored)
├── notebooks/
│   └── exploration.ipynb → analysis and transformation
├── src/
│   ├── load.py → script loading data to db
│   └── check_db.py → test db query
├── docker-compose.yaml → database config
├── requirements.txt → python packages
└── .gitignore → ignoring data and env files
</pre>
How to run

docker-compose up -d
pip install -r requirements.txt
python src/load.py

Main features
- In-memory data processing (Pandas)
- Bypassing system port conflicts (mapped 5433:5432)
- Automatic SQL table schema creation based on DataFrame
- Verification script checking connection and data presence (check_db.py)

License
Educational / portfolio project — free to use and modify.