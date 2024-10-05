from flask_restx import Api, Namespace, fields, Resource
from flask import Blueprint

api_bp = Blueprint('api', __name__)
api = Api(api_bp,
          title='Plan Management API',
          version='1.0',
          description='API for managing subscription plans',
          doc='/docs'
)

# Define namespaces
plan_ns = api.namespace('plans', description='Plan operations')

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