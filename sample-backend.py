from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        search_id = request.args.get('id')

        # Method to get the individual through their "unique" (not unique) id
        if search_id:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['id'] == search_id:
                    subdict['users_list'].append(user)
            return subdict

        # Method to search through list if both name and job are provided
        if search_username and search_job:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict

        # If only name is provided
        if search_username:
            subdict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict

        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()

        # Generate randomized ID
        id = ""
        for i in range(3):
            id = id + str(random.choice(string.ascii_letters))

        id = id.lower()

        for i in range(3):
            id = id + str(random.randint(0, 9))

        userToAdd['id'] = id
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        if resp.status_code == 200:
            resp.status_code = 201
        return resp
    elif request.method == 'DELETE':
        resp = jsonify(success=False)
        userToDelete = request.get_json()
        if userToDelete in users['users_list']:
            users['users_list'].remove(userToDelete)
            resp = jsonify(success=True)
        return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id :
        for user in users['users_list']:
            if user['id'] == id:
                if request.method == 'DELETE':
                    users['users_list'].remove(user)
                    resp = jsonify(success=True)
                    if resp.status_code == 200:
                        resp.status_code = 204
                    return resp
                return user
        return ({})
    return users
    


users = {
    'users_list' :
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id' : 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}
