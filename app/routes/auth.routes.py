from flask import Blueprint
from app.controllers import auth_controller

bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.route('/login', methods=['GET', 'POST'])(auth_controller.login)
bp.route('/logout')(auth_controller.logout)
bp.route('/register', methods=['GET', 'POST'])(auth_register.cadastro)
