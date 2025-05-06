import unittest
import json
from app import app
from models import db, User

class UserApiTestCase(unittest.TestCase):

    # setup the test environment before each test
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:checkmysql@localhost:3306/practice'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.client = app.test_client()
        print(f"client inside test {self.client}")
        with app.app_context():
            db.create_all()

    def tearDown(self) -> None:
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        new_user_data = {'name':'Subha Arun', 'email': 'subha@gmail.com'}

        response = self.client.post("/api/users", json=new_user_data)

        self.assertEqual(response.status_code, 201)

        data = json.loads(response.data)
        self.assertEqual(data['message'], 'User Created')

        with app.app_context():
            user = User.query.filter_by(email='subha@gmail.com').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.name, 'Subha Arun')


if __name__=="__main__":
    unittest.main()


