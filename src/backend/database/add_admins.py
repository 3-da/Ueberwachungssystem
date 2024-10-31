from src.backend.database.database import session, Admin


class HandleAdmins:
    def __init__( self ):
        pass

    @staticmethod
    def add_admins( name, password, email, phone, img, oncall ):
        new_admin = Admin( name=name, password=password, email=email, phone=phone, img=img, oncall=oncall )
        session.add( new_admin )
        print( f"Admin {name} added." )

        session.commit( )

    @staticmethod
    def clear_table( ):
        session.query( Admin ).delete( )
        session.commit( )
        print( "Admin table cleared." )

    @staticmethod
    def remove_admin( admin_name ):
        admin = session.query( Admin ).filter_by( name=admin_name ).first( )
        if admin:
            session.delete( admin )
            session.commit( )
            print( f"Admin {admin_name} removed." )
        else:
            print( f"No {admin_name} found." )

    @staticmethod
    def get_admins( ):
        return session.query( Admin ).all( )

    @staticmethod
    def login_validation( ):
        admins = session.query( Admin ).all( )
        return [ (admin.name, admin.password) for admin in admins ]
