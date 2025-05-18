from database.database import session, Bewegung
from datetime import datetime

class SaveImage:
    def add_entry(bild_name, timestamp):
        new_entry = Bewegung(bild_name=bild_name, datetime=timestamp)
        session.add(new_entry)
        session.commit()
        print(f"Bild {bild_name} erfolgreich in Datenbanktabelle gespeichert.")

