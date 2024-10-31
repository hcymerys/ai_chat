"""
1. Na podstawie instrukcji  https://python.langchain.com/docs/tutorials/pdf_qa/:
    a. Załaduj plik PDF sprawozdania finansowego firmy Nike z 2023 roku.
    b. Podziel dokument na mniejsze części
    c. Stwórz wektorową bazę danych w oparciu o dane pochodzące z pliku PDF
    d. Stwórz Retrieval w oparciu o bazę danych
    e. Stwórz Retrieval chain w oparciu o bazę danych i systemowy prompt
    f. Przygotuj aplikację przyjmującą input z konsoli i zwracającą odpowiedzi na ekran konsoli, w pętli
    g. Aplikacja powinna być w stanie odpowiadać na następujące pytania:
			- "What was Nike's revenue in 2023?"
			- "Who is Craig Williams?"
			- "Tell me about gross margin of Nike in 2023"
            - "Tell me revenues in footwear, apparell and equipment for Nike in 2023, 2022 and 2021"

2. Dodatkowe zadania:
    a. Do odpowiedzi aplikacji dodaj kontekst mówiący skąd dokładnie pochodzi odpowiedź (strona, fragment tekstu z PDF)
    b. Sprawdź jak będą wyglądały odpowiedzi dla chunk_size=100, chunk_overlap=0
    c. Sprawdź jak wyglądają wektory w bazie
    d. Zmień bazę wektorową z InMemoryVectorStore na ChromaDB (zaladowanie raz i czytanie z bazy)
"""
