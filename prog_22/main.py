from comments import Comment
from posts import Post, TextPost, PhotoPost
from users import User
from social_media_platform import SocialMediaPlatform

if __name__ == "__main__":
    platform = SocialMediaPlatform()

    user1 = platform.create_user("Alice", "alice@example.com")
    user2 = platform.create_user("Bob", "bob@example.com")

    post1 = platform.create_text_post(user1, "Hello, world!")
    post2 = platform.create_photo_post(user2, "A beautiful sunset", "sunset.jpg")

    platform.add_comment(post1, user2, "Nice post, Alice!")
    platform.add_comment(post2, user1, "I love sunsets!")

    print("User Posts:")
    for post in platform.posts:
        print(post.display())
        if isinstance(post, TextPost):
            for comment in post.comments:
                print(f"  - {comment.user.name}: {comment.content}")
        print()
