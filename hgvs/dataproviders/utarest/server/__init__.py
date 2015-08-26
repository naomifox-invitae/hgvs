# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask
from flask import jsonify
from flask import make_response
from flask_restful import Api

Server = Flask(__name__)
apis = Api(Server)

import hgvs.dataproviders.utarest.server.api
import hgvs.dataproviders.utarest.server.uri


@Server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



## <LICENSE>
## Copyright 2015 HGVS Contributors (https://bitbucket.org/biocommons/hgvs)
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## </LICENSE>