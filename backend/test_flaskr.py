import os
import random
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from requests import request
from sqlalchemy import func

from flaskr import create_app
from models import Category, setup_db, Question


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.environ['DB_TEST']
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            os.environ['POSTGRES_USER'], os.environ['PASSWORD'], os.environ['DB_HOST'], self.database_name
        )
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_all_categories(self):
        """test categories endpoint"""
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_get_questions(self):
        """test questions endpoint without arguments"""
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_get_valid_questions_pagination(self):
        """testing valid pagination"""
        res = self.client().get("/questions?page=2")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_get_invalid_questions_pagination(self):
        """testing invalid pagination request"""
        res = self.client().get("/questions?page=100")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_delete_question_with_valid_id(self):
        """testing question deletion with valid id"""
        question = Question.query.order_by(self.db.desc(Question.id)).first()
        self.assertNotEqual(question, None)
        res = self.client().delete("/questions/"+str(question.id))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])

    def test_delete_question_with_invalid_id(self):
        """testing question deletion with invalid id"""
        res = self.client().delete("/questions/5933")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")
        
    def test_create_valid_question(self):

        """request creation with valid data"""
        new_que = {
            "question": "testing question","answer": "test passed", 
            "difficulty": 1, "category": 1
            }
        res = self.client().post("/questions", json=new_que)
        data = json.loads(res.data)
        
        valid_que_post = Question.query.order_by(
            self.db.desc(Question.id)).first()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["new_question_id"], valid_que_post.id)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
        
    def test_create_invalid_question(self):
        """testing incomplete question post """
        new_question = {"answer": "answer", "difficulty": 1, "category": 1}
        res = self.client().post("/questions", json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_search_question_with_existing_data(self):
        """test search questions with existing results"""
        res = self.client().post("/questions", json={"search": "validsearch"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))

    def test_search_question_with_non_existing_data(self):
        """test question search with no results"""
        res = self.client().post("/questions", json={"search": "sdamcc@wqs!qw#"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))


    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()