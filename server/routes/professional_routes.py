# server/routes/professional_routes.py
from flask import Blueprint, render_template, request, session
from server.models import db, ServiceRequest

professional_routes = Blueprint('professional_routes', __name__)

@professional_routes.route('/professional/requests')
def view_requests():
    if 'user_id' in session:
        requests = ServiceRequest.query.filter_by(professional_id=session['user_id']).all()
        return render_template('service_request.html', requests=requests)
    return redirect(url_for('user_routes.login'))
