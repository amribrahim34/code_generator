from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.presentation.api.project_routes import ProjectResource, ProjectListResource
from src.presentation.api.user_routes import UserResource, UserListResource, UserLoginResource, UserRegisterResource
from src.presentation.api.plan_routes import PlanResource, PlanListResource
from src.infrastructure.adapters.sqlalchemy_project_repository import SQLAlchemyProjectRepository
from src.infrastructure.adapters.sqlalchemy_user_repository import SQLAlchemyUserRepository
from src.infrastructure.adapters.sqlalchemy_plan_repository import SQLAlchemyPlanRepository
from src.infrastructure.persistence.database import db

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# Load configuration
app.config.from_object('config.Config')

# Initialize SQLAlchemy
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Initialize repositories
project_repository = SQLAlchemyProjectRepository(db.session)
user_repository = SQLAlchemyUserRepository(db.session)
plan_repository = SQLAlchemyPlanRepository(db.session)

# Project routes
api.add_resource(ProjectResource, '/api/projects/<string:project_id>', 
                 resource_class_kwargs={'project_repository': project_repository})
api.add_resource(ProjectListResource, '/api/projects', 
                 resource_class_kwargs={'project_repository': project_repository})

# User routes
api.add_resource(UserResource, '/api/users/<string:user_id>', 
                 resource_class_kwargs={'user_repository': user_repository})
api.add_resource(UserListResource, '/api/users', 
                 resource_class_kwargs={'user_repository': user_repository})
api.add_resource(UserLoginResource, '/api/login', 
                 resource_class_kwargs={'user_repository': user_repository})
api.add_resource(UserRegisterResource, '/api/register', 
                 resource_class_kwargs={'user_repository': user_repository, 'plan_repository': plan_repository})

# Plan routes
api.add_resource(PlanResource, '/api/plans/<string:plan_id>', 
                 resource_class_kwargs={'plan_repository': plan_repository})
api.add_resource(PlanListResource, '/api/plans', 
                 resource_class_kwargs={'plan_repository': plan_repository})

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)