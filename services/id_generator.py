import uuid
import re


def generate_unique_id():
    # Generiere eine UUID (Universally Unique Identifier)
    generated_uuid = str(uuid.uuid4())

    # Entferne Bindestriche und andere nicht erlaubte Zeichen
    cleaned_id = re.sub(r'[^a-zA-Z0-9_]', '', generated_uuid)

    # Überprüfe, ob die bereinigte ID nicht leer ist
    if cleaned_id:
        # Füge einen Buchstaben als Präfix hinzu (Constraint AASd-002)
        cleaned_id = 'a' + cleaned_id[1:] if cleaned_id[0].isdigit() else cleaned_id

        return cleaned_id
    else:
        # Wenn die ID leer ist, versuche erneut (rekursiver Aufruf)
        return generate_unique_id()
