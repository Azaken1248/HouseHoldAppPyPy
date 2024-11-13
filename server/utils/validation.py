# server/utils/validation.py
def validate_user_form(form_data):
    required_fields = ['username', 'password', 'role']
    for field in required_fields:
        if not form_data.get(field):
            return False, f"{field} is required."
    return True, ""
