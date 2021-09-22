# number <- question number
# title <- question title
# is_correct <- answer to the question True/False

class Question:
    def __init__(self, number, title, is_correct):
        self.number = number
        self.title = title
        self.is_correct = is_correct