from flask_restx import Api, Namespace, fields, Resource
from flask import Blueprint
from enum import Enum

api_bp = Blueprint('api', __name__)
api = Api(api_bp,
          title='Project, Plan, and User Management API',
          version='1.0',
          description='API for managing projects, plans, users, and related operations',
          doc='/docs'
)

# Define namespaces
plan_ns = api.namespace('plans', description='Plan operations')
project_ns = api.namespace('projects', description='Project operations')
user_ns = api.namespace('users', description='User operations')

# ... (previous plan and project models remain the same)

# User models
user_model = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The user email'),
    'plan_id': fields.String(required=True, description='The user\'s plan ID')
})

user_input_model = api.model('UserInput', {
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})

user_login_model = api.model('UserLogin', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password')
})

token_model = api.model('Token', {
    'access_token': fields.String(required=True, description='JWT access token')
})

password_change_model = api.model('PasswordChange', {
    'old_password': fields.String(required=True, description='The current password'),
    'new_password': fields.String(required=True, description='The new password')
})

# ... (previous plan and project routes remain the same)

# User endpoints
@user_ns.route('/<string:user_id>')
@user_ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    @user_ns.response(403, 'Unauthorized access')
    @user_ns.response(404, 'User not found')
    @api.doc(security='jwt')
    def get(self, user_id):
        """Get a specific user"""
        pass

    @user_ns.doc('update_user')
    @user_ns.expect(user_input_model)
    @user_ns.marshal_with(user_model)
    @user_ns.response(403, 'Unauthorized access')
    @user_ns.response(404, 'User not found or update failed')
    @api.doc(security='jwt')
    def put(self, user_id):
        """Update an existing user"""
        pass

    @user_ns.doc('delete_user')
    @user_ns.response(200, 'User deleted successfully')
    @user_ns.response(403, 'Unauthorized access')
    @user_ns.response(404, 'User not found or deletion failed')
    @api.doc(security='jwt')
    def delete(self, user_id):
        """Delete a user"""
        pass

@user_ns.route('/')
class UserListResource(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    @api.doc(security='jwt')
    def get(self):
        """List all users (admin only)"""
        pass

@user_ns.route('/register')
class UserRegisterResource(Resource):
    @user_ns.doc('register_user')
    @user_ns.expect(user_input_model)
    @user_ns.marshal_with(user_model, code=201)
    @user_ns.response(400, 'User with this email already exists')
    @user_ns.response(500, 'Unable to retrieve free plan')
    def post(self):
        """Register a new user"""
        pass

@user_ns.route('/login')
class UserLoginResource(Resource):
    @user_ns.doc('login_user')
    @user_ns.expect(user_login_model)
    @user_ns.marshal_with(token_model)
    @user_ns.response(401, 'Invalid email or password')
    def post(self):
        """Login and receive an access token"""
        pass

@user_ns.route('/profile')
class UserProfileResource(Resource):
    @user_ns.doc('get_user_profile')
    @user_ns.marshal_with(user_model)
    @user_ns.response(404, 'User not found')
    @api.doc(security='jwt')
    def get(self):
        """Get the current user's profile"""
        pass

@user_ns.route('/change-password')
class UserChangePasswordResource(Resource):
    @user_ns.doc('change_user_password')
    @user_ns.expect(password_change_model)
    @user_ns.response(200, 'Password updated successfully')
    @user_ns.response(400, 'Invalid current password')
    @user_ns.response(500, 'Password update failed')
    @api.doc(security='jwt')
    def post(self):
        """Change the current user's password"""
        pass

# Setup JWT
api.authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# Import and add routes
from .plan_routes import *
from .project_routes import *
from .user_routes import *