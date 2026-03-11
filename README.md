# 🎬 AI Movie Catalog & Tracker

> Nowoczesna aplikacja webowa do przeglądania bazy filmów, zarządzania prywatną listą "do obejrzenia", oceniania tytułów oraz otrzymywania spersonalizowanych rekomendacji od asystenta AI.

## Opis projektu
Projekt realizowany w ramach przedmiotu **Indywidualny Projekt Programistyczny**. Aplikacja łączy programowanie obiektowe (OOP) w języku Python, analizę danych oraz nowoczesny web development. Dane o filmach są wczytywane z publicznych zbiorów (Kaggle), przetwarzane przy użyciu biblioteki Pandas, a lokalny model sztucznej inteligencji pełni rolę osobistego doradcy filmowego.

## Planowane funkcjonalności
* **Katalog filmów:** Przeglądanie bazy z zaawansowanym filtrowaniem (gatunek, rok wydania, średnia ocen).
* **Szczegóły produkcji:** Wyświetlanie kompleksowych informacji: tytuł, reżyser, opis fabuły oraz plakat.
* **Lista "Do obejrzenia":** Zarządzanie prywatną listą filmów dla zalogowanego użytkownika.
* **System oceniania:** Możliwość oceniania obejrzanych filmów w skali od 1 do 5.
* **Asystent AI (Ollama):** Czat z lokalnym modelem językowym, generującym rekomendacje i odpowiadającym na pytania ze świata kina.
* **Panel statystyczny:** Wizualizacja nawyków użytkownika i trendów (np. ulubione gatunki) za pomocą interaktywnych wykresów.

## Stos technologiczny

**Backend (Logika i Przetwarzanie Danych):**
* **Python** (podejście obiektowe) – główna logika biznesowa
* **Pandas** – wczytywanie, czyszczenie i operacje na danych z plików CSV (Kaggle)
* **Flask / FastAPI** – udostępnianie danych poprzez REST API
* **Ollama** – lokalny model AI odpowiedzialny za system rekomendacji

**Frontend (Interfejs Użytkownika):**
* **React** – budowa dynamicznego interfejsu aplikacji (SPA)
* **Recharts** – renderowanie nowoczesnych wykresów w panelu statystycznym

**Przechowywanie Danych (Faza Prototypu / MVP):**
* **Pliki JSON** – zapis profili użytkowników, ich list oraz ocen (zaimplementowane z użyciem Wzorca Repozytorium dla zachowania czystości architektury obiektowej).

---
*Projekt zrealizowany w ramach przedmiotu: Indywidualny Projekt Programistyczny.*
