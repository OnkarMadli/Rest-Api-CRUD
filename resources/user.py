from flask_restful import Resource, request, reqparse
from flask_jwt import jwt_required
from models.user import UserModel
import simplejson as json
from werkzeug.security import safe_str_cmp, check_password_hash
#changed

class UserRegister(Resource):
	parser = reqparse.RequestParser()

	parser.add_argument('FirstName',
		type=str,
		required=False
		# help="FirstName cannot be blank"
	)

	parser.add_argument('LastName',
		type=str,
		required=False
		# help="LastName cannot be blank"
	)


	parser.add_argument('EmailId',
		type=str,
		required=True,
		help="Email cannot be blank"
	)

	parser.add_argument('City',
		type=str,
		required=False
		# help="City cannot be blank"
	)

	parser.add_argument('Phone',
		type=str,
		required=False
		# help="phone cannot be blank"
	)

	parser.add_argument('DoB',
		type=str,
		required=False
		# help="Dobl cannot be blank"
	)

	parser.add_argument('UserId',
		type=str,
		required=False
		# help="UserId cannot be blank"
	)

	parser.add_argument('MembershipType',
		type=str,
		required=False
		# help="Email cannot be blank"
	)

	parser.add_argument('MembershipSince',
		type=str,
		required=False
		# help="MembershipSince cannot be blank"
	)

	parser.add_argument('MembershipTill',
		type=str,
		required=False
		# help="MembershipTill cannot be blank"
	)

	parser.add_argument('Rank',
		type=str,
		required=False
		# help="Rank cannot be blank"
	)

	parser.add_argument('Role',
		type=str,
		required=False
		# help="Role cannot be blank"
	)

	parser.add_argument('Points',
		type=str,
		required=False
		# help="Email cannot be blank"
	)
	parser.add_argument('Password',
		type=str,
		required=True,
		help="password cannot be blank"
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_email(data['EmailId']):
			return {"message": "Email already exists"}, 400

		user = UserModel(EmailId = data['EmailId'], Password = data['Password'])
		user.save_to_db()
		return {"message": "User created successfully."}, 201


class User(Resource):
	def post(self):
		data = request.data
		dataDict = json.loads(data)
		usa = UserModel.find_by_email(dataDict['EmailId'])
		if usa:
			if check_password_hash(usa.Password, dataDict['Password']):
				return usa.json(), 200
			else:
				return {'message': 'Incorrect username or password'}, 401
		return {'message': 'Email or username not registered'}, 404
