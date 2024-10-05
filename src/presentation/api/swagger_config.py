from flask_restx import Api, Namespace, fields
from flask import Blueprint, jsonify
from src.core.entities.project import ProjectStatus
from flask_swagger_ui import get_swaggerui_blueprint

# Create a blueprint for the API
api_bp = Blueprint('api', __name__)
api = Api(api_bp,
          title='FastStack API',
          version='1.0',
          description='API for managing projects, plans, and users in the FastStack application',
          doc='/docs'  # This will serve your Swagger UI
)

# Define namespaces for different parts of your API
user_ns = api.namespace('users', description='User operations')
project_ns = api.namespace('projects', description='Project operations')
plan_ns = api.namespace('plans', description='Plan operations')

# Setup Swagger UI
SWAGGER_URL = '/swagger-ui'
API_URL = '/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "FastStack API"
    }
)

# Define models
user_model = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'username': fields.String(required=True, description='The username'),
    'email': fields.String(required=True, description='The user email'),
    'plan_id': fields.String(required=True, description='The user\'s plan ID')
})

plan_model = api.model('Plan', {
    'id': fields.String(required=True, description='The plan identifier'),
    'name': fields.String(required=True, description='The plan name'),
    'description': fields.String(required=True, description='The plan description'),
    'price': fields.Float(required=True, description='The plan price'),
    'features': fields.List(fields.String, description='List of plan features')
})

project_model = api.model('Project', {
    'id': fields.String(required=True, description='The project identifier'),
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(required=True, description='The project description'),
    'status': fields.String(required=True, description='The project status', enum=[status.value for status in ProjectStatus]),
    'created_at': fields.DateTime(required=True, description='The project creation date'),
    'updated_at': fields.DateTime(required=True, description='The project last update date')
})

# Setup JWT
api.authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

# Import routes
from .user_routes import *
from .project_routes import *
from .plan_routes import *

# Add routes to namespaces
user_ns.add_resource(UserResource, '/<string:user_id>')
user_ns.add_resource(UserListResource, '/')
user_ns.add_resource(UserRegisterResource, '/register')
user_ns.add_resource(UserLoginResource, '/login')
user_ns.add_resource(UserProfileResource, '/profile')
user_ns.add_resource(UserChangePasswordResource, '/change-password')

project_ns.add_resource(ProjectResource, '/<string:project_id>')
project_ns.add_resource(ProjectListResource, '/')
project_ns.add_resource(ProjectGenerationResource, '/<string:project_id>/generate')
project_ns.add_resource(ProjectFileResource, '/<string:project_id>/files/<path:file_path>')
project_ns.add_resource(ProjectDownloadResource, '/<string:project_id>/download')

plan_ns.add_resource(PlanResource, '/<string:plan_id>')
plan_ns.add_resource(PlanListResource, '/')
plan_ns.add_resource(UserPlanResource, '/user')
plan_ns.add_resource(AdminPlanResource, '/admin', '/admin/<string:plan_id>')
plan_ns.add_resource(FreePlanResource, '/free')
plan_ns.add_resource(SubscriptionPlansResource, '/subscription')

authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
api.authorizations = authorizations

def get_swagger_json():
    return jsonify(api.__schema__)