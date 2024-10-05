from flask_restx import Api, Namespace, fields, Resource
from flask import Blueprint
from enum import Enum

api_bp = Blueprint('api', __name__)
api = Api(api_bp,
          title='Project and Plan Management API',
          version='1.0',
          description='API for managing projects, plans, and related operations',
          doc='/docs'
)

# Define namespaces
plan_ns = api.namespace('plans', description='Plan operations')
project_ns = api.namespace('projects', description='Project operations')

# Define models
plan_model = api.model('Plan', {
    'id': fields.String(required=True, description='The plan identifier'),
    'name': fields.String(required=True, description='The plan name'),
    'description': fields.String(required=True, description='The plan description'),
    'price': fields.Float(required=True, description='The plan price'),
    'features': fields.List(fields.String, description='List of plan features')
})

plan_input_model = api.model('PlanInput', {
    'name': fields.String(required=True, description='The plan name'),
    'description': fields.String(required=True, description='The plan description'),
    'price': fields.Float(required=True, description='The plan price'),
    'features': fields.List(fields.String, description='List of plan features')
})

user_plan_update_model = api.model('UserPlanUpdate', {
    'plan_id': fields.String(required=True, description='The new plan ID')
})

class ProjectStatus(Enum):
    DRAFT = 'DRAFT'
    GENERATING = 'GENERATING'
    COMPLETED = 'COMPLETED'

project_model = api.model('Project', {
    'id': fields.String(required=True, description='The project identifier'),
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(required=True, description='The project description'),
    'status': fields.String(required=True, description='The project status', enum=[status.value for status in ProjectStatus]),
    'created_at': fields.DateTime(required=True, description='The project creation date'),
    'updated_at': fields.DateTime(required=True, description='The project last update date')
})

project_input_model = api.model('ProjectInput', {
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(required=True, description='The project description')
})

generation_request_model = api.model('GenerationRequest', {
    'backend_framework': fields.String(required=True, description='The backend framework to use'),
    'frontend_framework': fields.String(required=True, description='The frontend framework to use'),
    'mobile_framework': fields.String(required=False, description='The mobile framework to use'),
    'use_repository_pattern': fields.Boolean(required=False, description='Whether to use repository pattern'),
    'coding_style': fields.String(required=False, description='The coding style to follow'),
    'include_admin_panel': fields.Boolean(required=False, description='Whether to include an admin panel'),
    'include_customer_website': fields.Boolean(required=False, description='Whether to include a customer website'),
    'include_mobile_app': fields.Boolean(required=False, description='Whether to include a mobile app'),
    'custom_options': fields.Raw(required=False, description='Any custom options for generation')
})

file_content_model = api.model('FileContent', {
    'content': fields.String(required=True, description='The content of the file')
})

download_url_model = api.model('DownloadURL', {
    'download_url': fields.String(required=True, description='The URL to download the project')
})

# Plan endpoints
@plan_ns.route('/<string:plan_id>')
@plan_ns.param('plan_id', 'The plan identifier')
class PlanResource(Resource):
    @plan_ns.doc('get_plan')
    @plan_ns.marshal_with(plan_model)
    @plan_ns.response(404, 'Plan not found')
    @api.doc(security='jwt')
    def get(self, plan_id):
        """Get a specific plan"""
        pass

@plan_ns.route('/')
class PlanListResource(Resource):
    @plan_ns.doc('list_plans')
    @plan_ns.marshal_list_with(plan_model)
    @api.doc(security='jwt')
    def get(self):
        """List all plans"""
        pass

@plan_ns.route('/user')
class UserPlanResource(Resource):
    @plan_ns.doc('get_user_plan')
    @plan_ns.marshal_with(plan_model)
    @plan_ns.response(404, 'Plan not found')
    @api.doc(security='jwt')
    def get(self):
        """Get the current user's plan"""
        pass

    @plan_ns.doc('update_user_plan')
    @plan_ns.expect(user_plan_update_model)
    @plan_ns.marshal_with(plan_model)
    @plan_ns.response(400, 'Invalid input')
    @plan_ns.response(404, 'Plan not found')
    @plan_ns.response(500, 'Update failed')
    @api.doc(security='jwt')
    def put(self):
        """Update the current user's plan"""
        pass

@plan_ns.route('/admin')
class AdminPlanResource(Resource):
    @plan_ns.doc('create_plan')
    @plan_ns.expect(plan_input_model)
    @plan_ns.marshal_with(plan_model, code=201)
    @api.doc(security='jwt')
    def post(self):
        """Create a new plan (Admin only)"""
        pass

@plan_ns.route('/admin/<string:plan_id>')
@plan_ns.param('plan_id', 'The plan identifier')
class AdminPlanResource(Resource):
    @plan_ns.doc('update_plan')
    @plan_ns.expect(plan_input_model)
    @plan_ns.marshal_with(plan_model)
    @plan_ns.response(404, 'Plan not found or update failed')
    @api.doc(security='jwt')
    def put(self, plan_id):
        """Update an existing plan (Admin only)"""
        pass

    @plan_ns.doc('delete_plan')
    @plan_ns.response(200, 'Plan deleted successfully')
    @plan_ns.response(404, 'Plan not found or deletion failed')
    @api.doc(security='jwt')
    def delete(self, plan_id):
        """Delete a plan (Admin only)"""
        pass

@plan_ns.route('/free')
class FreePlanResource(Resource):
    @plan_ns.doc('get_free_plan')
    @plan_ns.marshal_with(plan_model)
    @plan_ns.response(404, 'Free plan not found')
    def get(self):
        """Get the free plan"""
        pass

@plan_ns.route('/subscription')
class SubscriptionPlansResource(Resource):
    @plan_ns.doc('list_subscription_plans')
    @plan_ns.marshal_list_with(plan_model)
    def get(self):
        """List all subscription plans"""
        pass

# Project endpoints
@project_ns.route('/<string:project_id>')
@project_ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):
    @project_ns.doc('get_project')
    @project_ns.marshal_with(project_model)
    @project_ns.response(404, 'Project not found')
    @api.doc(security='jwt')
    def get(self, project_id):
        """Get a specific project"""
        pass

    @project_ns.doc('update_project')
    @project_ns.expect(project_input_model)
    @project_ns.marshal_with(project_model)
    @project_ns.response(404, 'Project not found or update failed')
    @api.doc(security='jwt')
    def put(self, project_id):
        """Update an existing project"""
        pass

    @project_ns.doc('delete_project')
    @project_ns.response(200, 'Project deleted successfully')
    @project_ns.response(404, 'Project not found or deletion failed')
    @api.doc(security='jwt')
    def delete(self, project_id):
        """Delete a project"""
        pass

@project_ns.route('/')
class ProjectListResource(Resource):
    @project_ns.doc('list_projects')
    @project_ns.marshal_list_with(project_model)
    @api.doc(security='jwt')
    def get(self):
        """List all projects for the current user"""
        pass

    @project_ns.doc('create_project')
    @project_ns.expect(project_input_model)
    @project_ns.marshal_with(project_model, code=201)
    @api.doc(security='jwt')
    def post(self):
        """Create a new project"""
        pass

@project_ns.route('/<string:project_id>/generate')
@project_ns.param('project_id', 'The project identifier')
class ProjectGenerationResource(Resource):
    @project_ns.doc('generate_project')
    @project_ns.expect(generation_request_model)
    @project_ns.response(202, 'Project generation started')
    @project_ns.response(404, 'Project not found')
    @api.doc(security='jwt')
    def post(self, project_id):
        """Start project generation"""
        pass

@project_ns.route('/<string:project_id>/files/<path:file_path>')
@project_ns.param('project_id', 'The project identifier')
@project_ns.param('file_path', 'The file path within the project')
class ProjectFileResource(Resource):
    @project_ns.doc('get_project_file')
    @project_ns.marshal_with(file_content_model)
    @project_ns.response(404, 'File not found')
    @api.doc(security='jwt')
    def get(self, project_id, file_path):
        """Get the content of a project file"""
        pass

    @project_ns.doc('update_project_file')
    @project_ns.expect(file_content_model)
    @project_ns.response(200, 'File updated successfully')
    @project_ns.response(400, 'No content provided')
    @project_ns.response(404, 'File not found or update failed')
    @api.doc(security='jwt')
    def put(self, project_id, file_path):
        """Update the content of a project file"""
        pass

@project_ns.route('/<string:project_id>/download')
@project_ns.param('project_id', 'The project identifier')
class ProjectDownloadResource(Resource):
    @project_ns.doc('download_project')
    @project_ns.marshal_with(download_url_model)
    @project_ns.response(404, 'Project not found or download generation failed')
    @api.doc(security='jwt')
    def get(self, project_id):
        """Get a download URL for the project"""
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