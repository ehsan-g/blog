from cerberus import Validator


# Check error example
def f_name(field, value, error):
    if not value:
        error(field, 'error message')
        print(error)


schema = {'name': {'check_with': f_name, 'required': True, 'minlength': 4, 'maxlength': 70, 'type': 'string', 'empty': False},
          'email': {'required': True, 'maxlength': 255, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
          'password': {'required': True, 'minlength': 6, 'type': 'string', 'empty': False, },
          'role': {'type': 'list', 'allowed': ['Nakama', 'admin', 'Admin']}
          }

# document = {'name': 'Ehsan', 'email': 'yeee@dd.company', 'password': '123456', 'role': ['Admin']}


# Unlike other validation tools, Cerberus will not halt and raise an exception on the first validation issue.
# The whole document will always be processed, and False will be returned if validation failed.
v = Validator()










