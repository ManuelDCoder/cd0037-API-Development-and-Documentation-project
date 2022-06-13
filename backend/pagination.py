QUESTIONS_PER_PAGE = 10

"""Defined function for pagination"""
def pagination(request, value):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    question_format = [question.format() for question in value]
    trivia = question_format[start:end]

    return trivia


def nextPage(page, request, paginate):
    if paginate < page:
        nextpage = request.args.get('page', 1, type=int) + 1
        return str(request.url_root + 'questions?page=') + str(nextpage)
    else:
        return str(request.url_root + 'questions?page=1')
