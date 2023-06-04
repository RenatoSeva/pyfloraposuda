# PyfloraPosuda

Alplikacije se moze buildti untar docker containera:
    'docker build -t pyfloraposuda:latest .
    -docker run -p 8000:8000 pyfloraposuda:latest

Ako se aplikacija builda s docker naredbom -p 8000:8000, aplikacija se nalazi na linku localhost:8000

User za ulazak u aplikaciju je:

    -username: admin
    -password: Y8.B-u5RzWLM9fd

Pocetna stranica aplikacije(index.html) sadrži popis biljaka unesenih u sustav.

Ako korisnik nije prijavljen u headeru aplikacije se nalaze gumbi  login(Prijava korisnika u aplikaciju), Sign up (Kreiranje novog korisnika) i PyFloraPosuda gumb preusmjerava na početnu stranicu(index.html).

image.png



