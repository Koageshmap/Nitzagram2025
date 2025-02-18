class Post:
    def __init__(self, likes_counter, comments, username, location, description):
        self.description = description
        self.location = location
        self.username = username
        self.likes_counter = 0
        self.comments = []
    def add_like(self):
        self.likes_counter += 1
    def add_comment(self, comment):
        self.comments.append(comment)
    def image(self):