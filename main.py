"""Undervisningseksempel til debugging af funktioner i Python.

Programmet behandler en simpel sikkerhedshændelse ved at normalisere
hændelsesteksten, klassificere en numerisk score og opbygge en samlet
visning af resultatet.

Programmet kan køres uden at udløse en exception, men resultatet er ikke
som forventet. Formålet er at bruge debuggeren i VS Code til at følge
programflow og variabelværdier og finde årsagen.
"""


def normalize_event(event: str) -> str:
    """Returnerer hændelsesteksten uden ekstra mellemrum og med store bogstaver."""
    return event.strip().upper()


def classify_severity(score: int, threshold: int) -> str:
    """Klassificerer en score som HIGH eller LOW ud fra en tærskelværdi."""
    if score >= threshold:
        return "HIGH"
    else:
        return "LOW"


def format_summary(event: str, score: int, severity: str) -> str:
    """Returnerer en samlet tekstbeskrivelse af sikkerhedshændelsen."""
    return (
        f"Hændelse: {event}\n"
        f"Score: {score}\n"
        f"Klassifikation: {severity}"
    )


event = "  mistænkelig fil  "

current_score = 8
previous_score = 4
alert_threshold = 7

normalized_event = normalize_event(event)

severity = classify_severity(previous_score, alert_threshold)

summary = format_summary(
    normalized_event,
    current_score,
    severity
)

print(summary)