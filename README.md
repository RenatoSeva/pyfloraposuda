# PyfloraPosuda

Alplikacije se moze buildti untar docker containera:

    -docker build -t pyfloraposuda:latest .
    -docker run -p 8000:8000 pyfloraposuda:latest

Ako se aplikacija builda s docker naredbom -p 8000:8000, aplikacija se nalazi na linku localhost:8000

User za ulazak u aplikaciju je:

    -username: admin
    -password: Y8.B-u5RzWLM9fd

Pocetna stranica aplikacije(index.html) sadrži popis biljaka unesenih u sustav.

Ako korisnik nije prijavljen u headeru aplikacije se nalaze gumbi  login(Prijava korisnika u aplikaciju), Sign up (Kreiranje novog korisnika) i PyFloraPosuda gumb preusmjerava na početnu stranicu(index.html).




![Screenshot 2023-06-04 110528](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/a6b593a4-2c7a-4c60-b2cc-254808de0eb6)

Kada se korisnik prijavi prikazuje se popis biljaka. Korisnik može kreirati novu biljku pritiskom na gum Nova biljka

![Screenshot 2023-06-04 111535](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/2cc8770a-d8e8-4fea-bbe1-251c9c1f00d4)

Klikom na biljk,u s popisa otvaraju se detalji biljke gdje korisnik može ažurirati podatke o biljci te ju obrisati.

Ekran s podatcima biljke sadrži sliku biljke i ime bilje. Te prikazuje veše opise o biljci, vlažnost tla(opis koliko je potrebno zaljevanje biljke), svjetlina(koliko dnevnog svjetla je poželjno da biljka ima), idealna temperatura i dali je potrebno dodavati gnojivo/supstrat.

Pritiskom na gumb Ažurirj otvara se egran s detaljima biljke koje je potrebno ažurirati. Sva polja za unos su obavezna.

Na gumb obriši brišemo biljku iz aplikacije.


![Screenshot 2023-06-04 112529](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/4e60a7d7-32ae-4ae9-99ee-ae087cf1e2d3)
