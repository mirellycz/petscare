from flask import Blueprint, render_template, request, redirect
from app.models.appointment import Appointment
from app import db

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Captura dados do formulário
        new_appt = Appointment(
            user_id=current_user.id,
            pet_name=request.form['pet_name'],
            date=request.form['date'],
            service_type=request.form['service_type']
        )
        db.session.add(new_appt)
        db.session.commit()
        return redirect('/')
    return render_template('appointment.html')