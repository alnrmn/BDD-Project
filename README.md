# BDD Project - https://demo.nopcommerce.com/

## Descrierea Proiectului
Acest proiect implementează un framework de testare automată 
utilizând Selenium WebDriver și BDD cu Behave pentru website-ul https://demo.nopcommerce.com/. 
Proiectul conține teste automate pentru următoarele funcționalități:
1. Register feature
2. Featured Products feature
3. Community Poll feature

## Structura Proiectului
1. Folder features = Feature files (fișiere scrise într-un limbaj natural (Gherkin) care să descrie scenariile de business)
    - Scenario (testul pe care vrem sa îl facem)
    - Scenario Outline (folosit atunci când vrem să executăm aceiași pași de mai multe ori folosind diverse seturi de inputs)
    - Given (contextul în care se desfășoară acțiunea)
    - When (acțiunea pe care o facem)
    - Then (deznodământul - verificarea pe care vrem să o facem)


2. Folder steps = Step definition files (maparea tehnică a fișierelor de business - feature files):`steps_community_poll.py`;
                  `steps_featured_products.py`, `steps_register.py`

3. Folder pages = Pagini de mapare pentru elementele/acțiunile din browser folosind POM - page object model
      - Conține fișiere pentru fiecare pagină testată a aplicației (`home_page.py`, `register_page.py`)
      - `base_page.py` (o clasă ce conține metode și elemente universale care pot fi folosite în toate paginile în care ne aflăm)

4. Fișier `browser.py` (conține instrucțiuni de instanțiere/instalare și deschidere browser)

5. Fișier `environment.py` (conține instanțierea tuturor claselor de tip pages)

6. Fișier `behave.ini` - Configurația pentru Behave (framework Python care ne ajută să scriem teste într-un format mai uman, folosind sintaxa Gherkin)

7. Fișier `README.md`: Acest fișier (conține detalii despre proiect)

## Instruțiuni pentru Rulare
Se instalează următoarele librării din Terminal (Alt + F12):
`pip install selenium behave behave-html-formatter webdriver-manager` 
sau
`pip install - r requirements.txt`

## Comanda de rulare a testelor în Terminal-ul PyCharm (ALT + F12)
1. dupa tag (se creeaza si raport de executie)
behave -f html -o all_tests_report.html (toate testele)
behave -f html -o smoke_tests_report.html --tags=SMOKE_TEST (teste Smoke)
behave -f html -o negative_tests_report.html --tags=NEGATIVE_TEST (teste negative)
behave -f html -o integration_tests_report.html --tags=INTEGRATION_TEST (testele de integrare)
behave -f html -o community_poll_feature.html --tags=COMMUNITY_POLL_FEATURE (Community Poll feature)
behave -f html -o register_feature.html --tags=REGISTER_FEATURE (Register feature)
behave -f html -o featured_products_feature.html --tags=FEATURED_PRODUCTS_FEATURE (Featured Products feature)

2. dupa "calea" din proiect a fisierului.feature (nu se creeaza raport de executie, doar se ruleaza testele)
behave features/community_poll.feature (Community Poll feature)
behave features/featured_products.feature (Featured Products feature)
behave features/register.feature (Register feature)
behave (toate feature-urile)

## Concluzii
`Pe baza feature-ului de `Register` au fost create 2 scenarii de testare:`
1. Atunci când se creează un cont nou inserând date in toate câmpurile obligatorii ale paginii (marcate cu *)
   pentru a ne asigura ca acest proces funcționează cum ar trebui
2. Atunci când se încearcă creerea unui cont nou fără a adăuga nimic în câmpul Last name
   pentru a ne asigura ca acel câmp împiedică creerea contului dacă nu este completat corespunzător

`Pe baza secțiunii `Featured Products` din home page s-a creat o suită de 4 teste care verifică dacă
atunci când se dă click pe fiecare produs din listă, se accesează într-adevar pagina corespunzătoare produsului respectiv.`

`Pe baza secțiunii `Community poll` din home page s-a creat o suită de 4 teste care verifică dacă un vizitator al paginii
poate sa voteze dacă nu este logat / înregistrat pe pagină.`


`Per total s-au executat teste pentru `3 feature-uri` (funcționalități) și `10 scenarii de testare`, care însumează un total de `44 pași.` 
Fiecare dintre aceste teste au fost executate cu succes.`

`Alte teste care ar mai putea fi executate pentru feature-ul `Register`:`
Încercare de înregistrare a unui cont nou atunci când:
a. e-mail-ul este introdus într-un format invalid (Ex. a@b). Restul câmpurilor se completează corect.
b. în câmpurile First name si Last name se introduc doar cifre sau alte caractere diferite de litere. Restul câmpurilor se completează corect.
c. nu se introduce nimic în niciunl din câmpurile obligatorii
d. parola introdusă în Confirm Password este diferită decât cea din Password. Restul câmpurilor se completează corect.
etc.

`Alte teste care ar mai putea fi executate pe pagina web prezentată mai sus:`
a. după înregistrarea unui cont nou, de testat feature-ul My Account (schimbat date personale, adrese etc.)
b. funcționalitatea butonului de Log Out după ce un utilizator este logat pe pagină
c. funcționalitatea feature-ului Wishlist (adăugare de produse, ștergere de produse etc.)
d. funcționalitatea feature-ului Shopping Cart (adăugare de produse, ștergere de produse etc.)
e. de testat dacă după ce este accesat un produs de pe pagina web, acesta apare mai apoi in secțiunea "Recently viewed products"
f. funcționalitatea Compare products
g. functionalitățile "grid view" și "list view" dintr-o listă de produse
h. funcționalitatea butoanelor de sortare dintr-o listă de produse
etc.

