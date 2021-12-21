
from flask import Flask, request
from flask_restx import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from ressources.ressource_pile import OperatorStack as p

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app=app, version='0.1', title='Api RPN',
          description='', validate=True)

operators = ['+', '-', '*', '/']

stacks = {}


@api.route("/operators")
class Operators(Resource):
    def get(self):
        """get list of operators

        Returns:
            [list]: [list of operator]
        """
        return operators, 201


@api.route("/stack")
class Stack(Resource):
    def get(self):
        """get all stacks

        Returns:
            [dict]: [return all stacks]
        """
        return stacks, 201

    def post(self):
        """post new stack

        Returns:
            [dict]: [dict of stack with the new stack]
        """
        values = {len(stacks): []}
        stacks.update(values)
        return stacks, 201


@api.route("/stack/<int:id>")
@api.response(404, 'Todo not found')
@api.param('id', 'The id stack')
class TodoStack(Resource):
    def get(self, id: int):
        """get stack by id

        Args:
            id (int): [id of stack]

        Returns:
            [dict]: [dit of stack]
        """
        if id in stacks.keys():
            return {id: stacks.get(id)}, 201
        else:
            api.abort(404, f"Stack {id} doesn't exist")

    @api.doc('delete_stack')
    @api.response(204, 'stack deleted')
    def delete(self, id: int):
        """delete stack by id

        Args:
            id (int): [id of stack]

        Returns:
            [dict]: [dict of stack]
        """
        if id in stacks.keys():
            stacks.pop(id)
            return stacks, 204
        else:
            api.abort(404, f"Stack {id} doesn't exist")


@api.route("/stack/<int:id>/<int:value>")
@api.response(404, 'Todo not found')
@api.param('id', 'value,' 'The id and value of stack')
class PushStack(Resource):
    def post(self, id: int, value: int):
        """post new value to the stack by id

        Args:
            id (int): [id of stack]
            value (int): [value to push]

        Returns:
            [dict]: [dict of stack after the push]
        """
        if id in stacks.keys():
            stacks[id].append(value)
            return stacks, 201
        else:
            api.abort(404, f"Stack {id} doesn't exist")


@api.route("/stack/<int:id>/<string:op>")
@api.response(404, 'Todo not found')
@api.param('id', 'value,' 'The id and value of stack')
class OpStack(Resource):
    def post(self, id: int, op: str):
        """post to perform +, -, *, and /

        Args:
            id (int): [id of stack]
            op (str): [operator]

        Returns:
            [dict]: [dict of all stack ]
        """
        if id not in stacks.keys():
            api.abort(404, f"Stack {id} doesn't exist")
        elif op not in operators:
            api.abort(404, f"Stack {op} doesn't exist")
        elif len(stacks[id]) < 1:
            api.abort(404, f"Stack {op} doesn't have two values")
        else:
            if op == '+':
                p.addition_stack(stacks[id])
            elif op == '-':
                p.substraction_stack(stacks[id])
            elif op == '*':
                p.multiplication_stack(stacks[id])
            else:
                p.division_stack(stacks[id])
            return stacks, 201


if __name__ == '__main__':
    app.run(debug=True)
