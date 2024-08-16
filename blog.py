# blog.py

from post import Post

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            post = self.posts[index]
            if new_title:
                post.title = new_title
            if new_content:
                post.content = new_content
            return True
        return False

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            return True
        return False

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        
        for idx, post in enumerate(self.posts):
            print(f"Post {idx + 1}:\n{post}")
