## Warsztaty AI - Jak zbudować bota z użyciem RAG

### Przygotowanie
1. Zainstaluj potrzebne biblioteki
```bash
python -m pip install -r requirements.txt
```
* W przypadku:
```shell
  Building wheels for collected packages: chroma-hnswlib
  Building wheel for chroma-hnswlib (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for chroma-hnswlib (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [5 lines of output]
      running bdist_wheel
      running build
      running build_ext
      building 'hnswlib' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/       
      [end of output]
```
* Zainstaluj Microsoft Visual C++ 14.0 lub nowszy z [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) - instrukcja https://github.com/WPSemantix/timbr_python_connector/issues/2
* Następnie zainstaluj biblioteki ponownie
* Alternatywnie zainstaluj python w wersji 3.10/11
2. Wejdź na discord serwer i skopiuj API key.
3. Dodaj plik .env do katalogu z projektem i dodaj do niego klucz API o treści: `OPEN_API_KEY=<api_key>`
4. Uruchom skrypt
```bash
python simple_chat.py
```
5. Gotowe! Możesz teraz rozmawiać z botem.

### Zadanie
1. Stwórz rozbudowanego bota wg instrukcji PDF. Kod źródłowy umieść w pliku `exercise.py`.
