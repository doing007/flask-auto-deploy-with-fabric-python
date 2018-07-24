

import os
import yaml
import json

from flask_restplus import Namespace, Resource, fields
api = Namespace('Services', description='')
from flask import request, jsonify

from werkzeug.datastructures import FileStorage

# Import Globally loaded models file here so that we can use them
from . import models as model

parser = api.parser()
parser.add_argument('sample_text', type=str, help='Help text', location='form')
parser.add_argument('file', type=FileStorage, location='files')

@api.route('/')
class ClassName(Resource):
    def __init__(self, host):
        super(ClassName, self).__init__(host)
        self._init_models()
        self.config = self._get_config()
        # Add all global configuration in config.yaml so you access it through self.config
        print(self.config)

    @api.doc(parser= parser)
    def post(self):
        print(request.form)
        if 'sample_text' not in request.form:
            return api.abort(400, "Input sample text required", status= "error")

        print(self.mod)

        return { 'status': 'success', 'data': request.form['sample_text'] }, 200

    def _init_models(self):
        self.mod = model.test_var
        self.graph = model.graph


    def _get_config(self):
        config = yaml.safe_load(open(os.path.join(self._get_cwd(),"config.yml")))
        return config

    def _get_cwd(self):
        return os.getcwd()
