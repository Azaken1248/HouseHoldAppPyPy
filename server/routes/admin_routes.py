# server/routes/admin_routes.py
from flask import Blueprint, request, render_template, redirect, url_for, flash
from server.models import db, User, Service, ServiceRequest

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@admin_routes.route('/admin/manage_services', methods=['GET', 'POST'])
def manage_services():
    if request.method == 'POST':
        # Process service creation, updating, deletion
        service_name = request.form['name']
        price = float(request.form['price'])
        service = Service(name=service_name, price=price)
        db.session.add(service)
        db.session.commit()
        flash("Service added successfully.")
        return redirect(url_for('admin_routes.manage_services'))
    services = Service.query.all()
    return render_template('service_management.html', services=services)
