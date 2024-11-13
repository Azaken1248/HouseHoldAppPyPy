# server/utils/db_utils.py
from server.models import db, User

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_service(name, price, description, time_required):
    service = Service(name=name, price=price, description=description, time_required=time_required)
    db.session.add(service)
    db.session.commit()
    return service
