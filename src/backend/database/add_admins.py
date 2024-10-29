from src.backend.database.database import session, Admin


class HandleAdmins:
    def __init__(self):
        self.admins = [
            {"password": "pass123", "oncall": False, "img": "path/img1.png", "name": "admin1", "email": "admin@email1.com", "phone": "123123123"},
            {"password": "pass456", "oncall": False, "img": "path/img2.png", "name": "admin2", "email": "admin@email2.com", "phone": "456456456"},
            {"password": "pass789", "oncall": True, "img": "path/img3.png", "name": "admin3", "email": "admin@email3.com", "phone": "789789789"},
        ]

    def add_admins(self):
        for admin in self.admins:
            new_admin = Admin(**admin)
            session.add(new_admin)
            print(f"Admin {admin['name']} added.")

        session.commit()

    @staticmethod
    def clear_table():
        session.query(Admin).delete()
        session.commit()
        print("Admin table cleared.")


if __name__ == "__main__":
    add_admins = HandleAdmins()
    add_admins.add_admins()

    # enable to clear Admin table
    # add_admins.clear_table()