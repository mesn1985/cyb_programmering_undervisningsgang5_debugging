# 🐞 Debugging af funktioner i Python

Dette repository bruges i **Programmering – undervisningsgang 5** til en øvelse i systematisk fejlfinding med Python og VS Code.

> Programmet kan køre uden at udløse en exception, men resultatet er ikke som forventet.

Din opgave er ikke at gætte dig frem til fejlen.

Du skal bruge debuggeren til at undersøge, **hvad programmet faktisk gør**.

---

## 🎯 Undervisningsformål

I øvelsen skal du træne i at:

* hente eksisterende kode med Git
* læse og forstå kode, du ikke selv har skrevet
* sætte et breakpoint i VS Code
* bruge **Step Over**
* bruge **Step Into**
* undersøge variabelværdier
* følge argumenter ind i parametre
* følge programflow gennem funktioner
* følge en returværdi tilbage til resten af programmet
* finde en logisk fejl, der ikke udløser en exception

Fokus er ikke på at lære alle funktioner i VS Code-debuggeren.

Fokus er på at bruge debuggeren til at forstå **programflow og dataflow**.

---

## 🛡️ Programmet

Programmet behandler en simpel sikkerhedshændelse.

Det skal:

```text
normalisere hændelsesteksten
↓
klassificere hændelsens score
↓
opbygge en samlet visning
↓
vise resultatet
```

Programmet arbejder med:

```text
Hændelse:
mistænkelig fil

Aktuel score:
8

Tærskel:
7
```

Reglen er:

```text
score under 7
→ LOW

score på 7 eller højere
→ HIGH
```

> Klassifikationen bruges kun som programmeringseksempel og er ikke en sikkerhedsstandard eller anbefalet risikovurdering.

---

## ✅ Forventet resultat

Med en aktuel score på:

```text
8
```

forventes:

```text
Hændelse: MISTÆNKELIG FIL
Score: 8
Klassifikation: HIGH
```

Programmet producerer imidlertid ikke dette resultat.

Koden kan godt køre.

Derfor skal du undersøge **hvor den faktiske udførelse begynder at afvige fra den forventede udførelse**.

---

## 🚀 Klon repository

Åbn en terminal og gå til den mappe, hvor du vil gemme projektet.

Klon repositoryet:

```bash
git clone https://github.com/mesn1985/cyb_programmering_undervisningsgang5_debugging.git
```

Gå derefter ind i projektmappen:

```bash
cd cyb_programmering_undervisningsgang5_debugging
```

Åbn projektet i VS Code.

---

## 📁 Filer

```text
cyb_programmering_undervisningsgang5_debugging/
├── README.md
└── security_monitor.py
```

Python-programmet findes i:

```text
security_monitor.py
```

---

## 🔎 Før du debugger

Læs først programmet uden at ændre noget.

Prøv at identificere:

```text
funktionerne

parametrene

argumenterne

returværdierne

de almindelige variabler
```

Overvej derefter:

```text
Hvilken værdi bør klassificeres?

Hvilken værdi forventer du bliver sendt til klassifikationsfunktionen?

Hvad forventer du funktionen returnerer?
```

Kør programmet normalt én gang.

Sammenlign det faktiske resultat med det forventede resultat.

---

## 🐞 Brug debuggeren

Brug derefter debuggeren i VS Code.

Arbejd systematisk:

```text
forventet resultat
↓
faktisk resultat
↓
breakpoint
↓
Step Over
↓
Step Into
↓
undersøg variabelværdier
↓
følg argument → parameter
↓
følg return → returværdi
↓
find hvor programmet afviger
```

Ret først koden, når du kan forklare **hvorfor** resultatet bliver forkert.

---

## 🔧 Efter rettelsen

Kør programmet igen.

Kontrollér, at resultatet nu er:

```text
Hændelse: MISTÆNKELIG FIL
Score: 8
Klassifikation: HIGH
```

Brug derefter:

```bash
git status
```

Undersøg hvad Git fortæller om:

```text
security_monitor.py
```

Overvej:

> Hvorfor registrerer Git nu filen som ændret?

Du behøver ikke pushe ændringen til dette repository(og bør ikke kunne føre det)

---

## 💭 Tænk over

Når øvelsen er færdig, bør du kunne forklare:

```text
Hvorfor kunne programmet køre, selvom resultatet var forkert?

Hvordan hjalp Step Into med at undersøge funktionskaldet?

Hvilken forskel så du mellem et argument og parameterens faktiske værdi?

Hvordan kunne Variables-visningen hjælpe dig?

Hvor i programmet opstod forskellen mellem forventet og faktisk programflow?

Hvorfor kan debugging være nyttigt, selv når Python ikke viser en fejlmeddelelse?
```

---

## 🧠 Husk

En fejl i et program behøver ikke give:

```text
SyntaxError

TypeError

ValueError
```

Programmet kan være gyldigt Python og stadig gøre **det forkerte**.

Debuggeren kan hjælpe dig med at undersøge:

> Hvad gør programmet faktisk – linje for linje?