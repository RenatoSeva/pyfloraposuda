# PyfloraPosuda

Alplikacije se moze buildti untar docker containera:

    -docker build -t pyfloraposuda:latest .
    -docker run -p 8000:8000 pyfloraposuda:latest

Ako se aplikacija builda s docker naredbom -p 8000:8000, aplikacija se nalazi na linku localhost:8000

User za ulazak u aplikaciju je:

    -username: admin
    -password: Y8.B-u5RzWLM9fd

## Pocetna stranica aplikacije(index.html) sadrži popis biljaka unesenih u sustav.

Ako korisnik nije prijavljen u headeru aplikacije se nalaze gumbi  **login**(Prijava korisnika u aplikaciju), **Sign up** (Kreiranje novog korisnika) i **PyFloraPosuda** gumb preusmjerava na početnu stranicu(index.html).




![Screenshot 2023-06-04 110528](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/a6b593a4-2c7a-4c60-b2cc-254808de0eb6)

Kada se korisnik prijavi prikazuje se popis biljaka s njihovim detaljim o njegi. Korisnik može kreirati novu biljku pritiskom na gumb **Nova biljka**.

![Screenshot 2023-06-04 111535](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/2cc8770a-d8e8-4fea-bbe1-251c9c1f00d4)

Klikom na biljku s popisa otvaraju se detalji biljke gdje korisnik može ažurirati podatke o biljci te ju obrisati.

### Podatci o biljci koji se čuvaju u bazi podataka

    id: INT
    name: VARCHAR
    image: VARCHAR
    humidity: VARCHAR
    brightness: VARCHAR
    temperature: VARCHAR
    substrate: VARCHAR

Ekran s podatcima biljke sadrži sliku biljke i ime biljke. Te prikazuje više opisa o biljci, vlažnost tla (opis koliko je potrebno zaljevanje biljke), svjetlina(koliko dnevnog svjetla je poželjno da biljka ima), idealna temperatura i jeli je potrebno dodavati gnojivo/supstrat.

Pritiskom na gumb **Ažuriraj** otvara se ekran s detaljima biljke koji se mogu ažurirati. Sva polja za unos su obavezna.

Na gumb **Obriši** brišemo biljku iz aplikacije.

![Screenshot 2023-06-04 112529](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/4e60a7d7-32ae-4ae9-99ee-ae087cf1e2d3)

Na gumb **Posuda** otvara se popis posuda koje je korisnik unio u aplikaciju.

### Podatci o posudi koji se čuvaju u bazi podataka

    id: INT
    name: VARCHAR
    plant_id: BIGINT(FK na tablicu plant_plant)
    user_id: BIGINT(FK na tablcu auth_user)
    status: VARCHAR
    senzor_Brightness_id: BIGINT(FK na tablicu pot_senzors)
    senzor_Humidity_id: BIGINT(FK na tablicu pot_senzors)
    senzor_Ph_id: BIGINT (FK na tablicu pot_senzors)
    senzor_Tmp_id: BIGINT (FK na tablicu pot_senzors)
    indoor: BOOL

### Tablica pot_senzor popis polja

    id: INTEGER
    type: VARCHAR
    date: DATETIME
    currentValue: REAL

podatci se popunjavaju prilikom kreiranja nove posude
Kreiraju se 4 senzora po posudi. Senzor temperature, Sezor Ph, Senzor osvjetljenja, Senzor vlažnosti.
Stupac u tablici currentValue sadrži zadnje očitane vrijednosti sa senzora.
i novo kreirani se spramju u tablicu posude


### Tablia pot_senzor_values polja

    id: INT
    value: REAL
    senzor_id: BIGINT
    date: DATETIME

tablica sadrži povjest očitanih vrijednosti sa senzora.

Popis posuda sadrži ime posude i status posude. Na gumb **Nova posuda** otvara se ekran za kreiranje nove posude.

Potrebno je odabrati predhodno kreiranu biljku, odabrati poziciju biljke(ako je izvan stana/kuće odznačiti Indoor, ako je u stanu/kući selektirati kućicu), te je potrebno dodati opisno ime(koja je pozicija posude).

![Screenshot 2023-06-04 143051](https://github.com/RenatoSeva/pyfloraposuda/assets/78822975/0ee99530-65dc-4c56-b054-c45c1e99a8ef)


