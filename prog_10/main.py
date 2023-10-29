from users import User
from comments import Comment
from posts import Post, TextPost, ImagePost

def main():
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    post1 = user1.create_post("Hello, world!", TextPost)
    post2 = user2.create_post("Check out this cool image!", ImagePost)

    user1.leave_comment(post2, "Nice image, Bob!")
    user2.leave_comment(post1, "Hello, Alice!")

    user1.view_posts()
    user2.view_posts()

    user1.update_profile("Alicia", "alicia@example.com")
    user1.view_posts()

    user2.view_posts()

if __name__ == "__main__":
    main()
