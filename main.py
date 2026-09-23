def classify_severity(score: int) -> str:
    """Klassificerer en sikkerhedshændelse ud fra dens score."""
    if score >= 7:
        return "HIGH"
    else:
        return "LOW"


current_score = 8
previous_score = 3

severity = classify_severity(previous_score)

print("Aktuel score:", current_score)
print("Klassifikation:", severity)