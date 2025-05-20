from datetime import datetime
from backend.database.database import Bewegung, session

class SaveImage:
    @staticmethod
    def add_entry(bild_name, timestamp):
        new_entry = Bewegung(bild_name=bild_name, datetime=timestamp)
        session.add(new_entry)
        session.commit()
        print(f"Bild {bild_name} erfolgreich in Datenbanktabelle gespeichert.")

