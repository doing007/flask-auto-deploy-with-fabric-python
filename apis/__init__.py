from flask_restplus import Api

from .module_name import api as ns1

api = Api(
    title='API Title',
    version='1.0',
    description='API description',
)

api.add_namespace(ns1)
