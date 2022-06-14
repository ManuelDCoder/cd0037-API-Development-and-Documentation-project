# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```


## API Endpoint Reference

### Overview of the API
- API URL: This is a locally hosted API under port 5000 and URL `http://localhost:5000/api/trivia/v0.1/`
- API Authentication: This API doesn't require any form of authentication or tokens.

### General Error Handling in JSON format
```
  json{
    "success" : false
    "error" : 422
    "message" : "Unprocessable"
  }

```
### 4xx error codes
- 400: `Bad Request`            || The browser (or proxy) sent a request that this server could not understand.
- 404: `Not Found`              || The requested URL was not found on the server.
- 405: `Method Not Allowed`     || The method is not allowed for the requested URL.
- 422: `Unprocessable Entity`   || The request was well-formed but was unable to be followed due to semantic errors

### 5xx error codes
- 500: `internal server error`  || Encounterd an unkown error on the server(Trivia).

### API Endpoints

#### GET `/categories`
##### Returns
- a dictionary of categories with keys(ids) and value(string) of the category.
  - `success` : returns a boolean of true or false
  - `categories`: contains an object of:
    - `id`: `category_string` key:value pairs.
##### Response
- returns the json format as displayed below
###### cURL command
- curl http://127.0.0.1:5000/categories

    ```
      {
        "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
        }, 
        "success": true, 
        "total_categories": 6
      }

    ```

#### GET `/questions`
##### Returns
- a pagination with dictionary of categories and questions
  - categories: a dictionary of categories with keys(ids) and value(string) of the category.
    - `id` : category id 
    - `category` : category text
  - questions: queries a list of paginated questions in json format.
    - `id` : Question id.
    - `question` : Question text.
    - `difficulty` : Question difficulty.
    - `category` : current questions category id.
  - `total_questions` : an integer of total questions
  - `next_page` (url) : link to the next page of questions
  - `success` : true or false

##### Response: 
- returns the json format as displayed below
###### cURL command 
- curl http://127.0.0.1:5000/questions

      ```
        json{
          "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
          }, 
          "next_page": "http://127.0.0.1:5000/questions?page=2", 
          "questions": [
            {
              "answer": "Apollo 13", 
              "category": 5, 
              "difficulty": 4, 
              "id": 2, 
              "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            }, 
            {
              "answer": "Tom Cruise", 
              "category": 5, 
              "difficulty": 4, 
              "id": 4, 
              "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            }, 
            {
              "answer": "Maya Angelou", 
              "category": 4, 
              "difficulty": 2, 
              "id": 5, 
              "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            }, 
            {
              "answer": "Edward Scissorhands", 
              "category": 5, 
              "difficulty": 3, 
              "id": 6, 
              "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            }, 
            {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
            }, 
            {
              "answer": "Brazil", 
              "category": 6, 
              "difficulty": 3, 
              "id": 10, 
              "question": "Which is the only team to play in every soccer World Cup tournament?"
            }, 
            {
              "answer": "Uruguay", 
              "category": 6, 
              "difficulty": 4, 
              "id": 11, 
              "question": "Which country won the first ever soccer World Cup in 1930?"
            }, 
            {
              "answer": "George Washington Carver", 
              "category": 4, 
              "difficulty": 2, 
              "id": 12, 
              "question": "Who invented Peanut Butter?"
            }, 
            {
              "answer": "Lake Victoria", 
              "category": 3, 
              "difficulty": 2, 
              "id": 13, 
              "question": "What is the largest lake in Africa?"
            }, 
            {
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
            }
          ], 
          "success": true, 
          "total_questions": 19
        }

      ```

#### DELETE `/questions/<int:question_id>`
##### Returns
- delete method for the specified question id the URL parameters.
  - `deleted_question` : question_id
  - `success`   returns a boolean of : true or false depending on the delete status
  - `total_questios`  : returns the number of questions available after deletion

##### Response
  ###### cURL command
  -  curl -X DELETE http://127.0.0.1:5000/questions/19

  ```

  json {
    "deleted_question": 19, 
    "success": true, 
    "total_questions": 18
  }

  ```



#### POST `/questions`
##### Returns
- a post method of a new trivia question
##### Request
  - `question` : the question text(string).
  - `answer` :  answer to the question text(string).
  - `difficulty` : a question difficulty ranging from 1 to 5.
  - `category` : An integer that contains the category id.

##### Response 
- returns a json object with the required keys:
  - `new_question` : text(string) for the new question created.
  - `new_question_id` : integer(ID) of the new question created.
  - `questions` : a list that contains paginated questions objects.
    - `id` : Question id.
    - `question` : Question text.
    - `difficulty` : Question difficulty.
    - `category` : question category id.
  - `total_questions` : an integer that contains total questions.
  - `success` : true or false

###### cURL command
- curl -X POST -d '{"question": "What! Is POST method working?", "category": "2", "difficulty": "1", "answer": "Yes"}' http://127.0.0.1:5000/questions

    ```    {
      "new_question": "Is POST method working", 
      "new_question_id": 26, 
      "questions": [
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "Lake Victoria", 
          "category": 3, 
          "difficulty": 2, 
          "id": 13, 
          "question": "What is the largest lake in Africa?"
        }, 
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ], 
      "success": true, 
      "total_questions": 20
    }
    ```



#### POST `/questions/search`
##### Returns
- a search result for matched questions.
##### Request
  - `search` : a string of the searched term.
##### Response
- `questions` : a list of paginated questions in json with reference to the searched term.
  - `id` : question id.
    - `question` : question text.
    - `difficulty` : question difficulty.
    - `category` : question category id.
  - `success` :  true or false
  - `total_searched_items` : the total number of items matched by searched term

###### cURL command
- curl -X POST 'http://127.0.0.1:5000/questions/search?search=POST'

  searched term: POST

      ```json
      {
          "search_term" : "POST"
      }
      ```
  response to searched term "POST":

    ```

    json {
  "questions": [
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 24, 
      "question": "Is POST method working"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 25, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 26, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 27, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 28, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 29, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 30, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 31, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 32, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 33, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 34, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 35, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 36, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 37, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 38, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 39, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 40, 
      "question": "What! Is POST method working?"
    }, 
    {
      "answer": "Yes", 
      "category": 2, 
      "difficulty": 1, 
      "id": 41, 
      "question": "What! Is POST method working?"
    }
  ], 
  "searched_term": "POST", 
  "success": true, 
  "total_searched_items": 18


    ```

#### GET `/categories/<int:category_id>/questions`
##### Returns
  - a pagination with dictionary of questions specified in the categories URL parameters.
  - `category_id`  : the id of the current category
  - `category_type` : the type(string) of the current category selected.
    - `questions` : a list that contains paginated questions objects, that correspond to the page query.
      - `id` : Question id.
      - `question` : Question text.
      - `difficulty` : Question difficulty.
      - `category` : question category id.
    - `total_questions` : an integer that contains total questions in the selected category.
    - `success` true or false
##### Response
  - returns the json format as displayed below
###### cURL command
- curl http://127.0.0.1:5000/categories/2/questions

    ```
      json {
        "category_id": 2, 
        "category_type": "Art", 
        "questions": [
          {
            "answer": "Escher", 
            "category": 2, 
            "difficulty": 1, 
            "id": 16, 
            "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }, 
          {
            "answer": "Mona Lisa", 
            "category": 2, 
            "difficulty": 3, 
            "id": 17, 
            "question": "La Giaconda is better known as what?"
          }, 
          {
            "answer": "One", 
            "category": 2, 
            "difficulty": 4, 
            "id": 18, 
            "question": "How many paintings did Van Gogh sell in his lifetime?"
          }, 
          {
            "answer": "Jackson Pollock", 
            "category": 2, 
            "difficulty": 2, 
            "id": 19, 
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
          }
        ], 
        "success": true, 
        "total_questions": 4
      }

    ```

#### POST `/quizzes`
##### Returns
- a random set of questions for users to play quiz game each time without repeating the previous set of questions.
##### Request
  - `quiz_category`: A dictionary that contains the category id.
    - `id` : the category id to get the random question from. use 0 to get a random question from all categories.
    - `previous_questions` : A list that contains the IDs of the previous questions.
  - `question` (dict) that has the following data:
    - `id` : question ID.
    - `question` : question text.
    - `answer` : question answer.
    - `difficulty` : question's difficulty
    - `category` : category's ID.
  - `success` : returns a boolean of  true or false

##### Response: returns the json format below :
###### cURL command  
  - curl http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":{"id":"2"}}

    ```
      json {
          "question": {
            "answer": "Yes", 
            "category": 2, 
            "difficulty": 1, 
            "id": 40, 
            "question": "What! Is POST method working?"
          }, 
          "success": true, 
          "total_questions": 34
        }

    ```



#### Author:
Emmanuel Larbi - Udacity FullStack Nanodegree Student.

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
  