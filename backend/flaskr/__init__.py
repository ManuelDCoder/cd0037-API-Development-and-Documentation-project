import json
import os
import random
from flask import Flask, request, abort, jsonify
from flask_cors import CORS


from pagination import pagination, nextPage
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    # CORS(app)
    CORS(app, resources={r"*" : {"origins": "*"}})
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,PATCH,POST,DELETE,OPTIONS"
        )
        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route("/categories", methods=["GET"])
    def get_all_categroies():
        try:
            categories = Category.query.order_by(Category.id).all()
            
            return jsonify({
                "success" : True,
                "categories" : {category.id: category.type for category in categories},
                "total_categories" : len(Category.query.all())
            })
        except:
            abort(404)

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route("/questions", methods=["GET"])
    def get_questions():
        try:
            value = Question.query.order_by(Question.id).all()
            trivia_questions = pagination(request, value)

            categories = Category.query.order_by(Category.type).all()
            next_page = get_next_page(trivia_questions)
            
            if len(trivia_questions) == 0:
                abort(404)

            return jsonify({
                "success" : True,
                "questions" : trivia_questions,
                "total_questions" : len(value),
                "categories" : {category.id: category.type for category in categories},
                "next_page" : next_page,
            })  
        except:
            abort(404)

    def get_next_page(trivia_questions):
        paginate = len(trivia_questions) % QUESTIONS_PER_PAGE
        next_page = nextPage(len(trivia_questions), request, paginate)
        return next_page
    
    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            get_question_to_delete = Question.query.filter(Question.id == question_id).one_or_none()
            
            if get_question_to_delete is None:
                abort(404)
                
            get_question_to_delete.delete()

            return jsonify({
                "success" : True,
                "deleted_question" : question_id,
                "total_questions" : len(Question.query.all())
            })
        except:
            abort(422)
    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route("/questions", methods=["POST"])
    def add_a_question():
        body = request.get_json(Question)
        try:
            if body is not None:
                add_question = body.get("question", None)
                add_category = body.get("category", None)
                add_difficulty = body.get("difficulty", None)
                add_answer = body.get("answer", None)

                add_question = Question(question=add_question, category=add_category, difficulty=add_difficulty, answer=add_answer)
                add_question.insert()

                value = Question.query.order_by(Question.id).all()
                trivia_questions = pagination(request, value)

                return jsonify({
                    "success" : True,
                    "new_question" : add_question.question,
                    "new_question_id" : add_question.id,
                    "questions" : trivia_questions,
                    "total_questions" : len(Question.query.all()),
                })
        except:
            abort(422)
    
    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route("/questions/search", methods=['POST'])
    def search_questions():
        searchTerm = request.args.get("search", None)
        if searchTerm is not None:
            if searchTerm == '':
                return jsonify ({
                    "empty_string" : "search requires a string input"
                })
            else:
                value = Question.query.order_by(Question.id).filter(
                Question.question.ilike("%{}%".format(searchTerm))
                )
                searched_items = [search.format() for search in value]
                return jsonify(
                    {
                        "success": True,
                        "questions": searched_items,
                        "total_searched_items" : len(searched_items),
                        "searched_term" : searchTerm,
                    }
                )
        else:
            abort(422)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route("/categories/<int:category_id>/questions")
    def questions_by_categories(category_id):
        get_category = Category.query.get(category_id)
        if category_id is None:
            abort(404)
        try:
            value = Question.query.order_by(Question.id).filter(Question.category == category_id).all()
            get_questions_by_category = pagination(request, value)

            return jsonify({
                "success" : True,
                "questions" : get_questions_by_category,
                "category_id" : get_category.id,
                "category_type" : get_category.type,
                "total_questions" : len(value)
            })
        except:
            abort(422)
    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route("/quizzes", methods=["POST"])
    def quiz():
        body = request.get_json()
        try:
            get_prev_que = body.get('previous_questions')
            get_quiz_category = body.get('quiz_category')['id']
            try:
                get_prev_que is None
            except:
                abort(400)

            return filter_quiz(get_prev_que, get_quiz_category)

        except:
            abort(400)

    def filter_quiz(get_prev_que, get_quiz_category):
        trivia_questions = []
        if get_quiz_category is 0:
            trivia_questions = Question.query.filter(Question.id.notin_(get_prev_que)).all()
        else:
            category = Category.query.get(get_quiz_category)
            if category is None:
                abort(404)
            trivia_questions = Question.query.filter(Question.id.notin_(get_prev_que), Question.category == get_quiz_category).all()
            # retrieved_question = None
        return return_rand_questions(trivia_questions)

    def return_rand_questions(trivia_questions):
        if len(trivia_questions) > 0:
            retrieved_question = get_rand_questions(trivia_questions)
        return jsonify({
                'success': True,
                'question': retrieved_question,
                'total_questions': len(trivia_questions)
            })

    def get_rand_questions(trivia_questions):
        index = random.randrange(0, len(trivia_questions))
        retrieved_question = trivia_questions[index].format()
        return retrieved_question

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success" : False,
            "error" : 400,
            "message" : "Bad Request"
        }), 400
        
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success" : False,
            "error" : 404,
            "message" : "Not Found"
        }), 404
    
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success" : False,
            "error" : 422,
            "message" : "Unprocessable"
        }), 422
        
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error."
        }), 500
        


    return app

