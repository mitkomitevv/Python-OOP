from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia("Name1", "Twitter", 1000, "books")

    def test_init(self):
        self.assertEqual("Name1", self.social_media._username)
        self.assertEqual("Twitter", self.social_media._platform)
        self.assertEqual(1000, self.social_media._followers)
        self.assertEqual("books", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_wrong_platform_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "wrong platform"

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_negative_followers_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post(self):
        result = self.social_media.create_post("Hello")

        self.assertEqual({'content': 'Hello', 'likes': 0, 'comments': []}, self.social_media._posts[0])
        self.assertEqual("New books post created by Name1 on Twitter.", result)

    def test_like_post_where_post_liked(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 0, 'comments': []},
                                    {'content': 'Bye', 'likes': 0, 'comments': []}]

        result = self.social_media.like_post(0)
        self.assertEqual("Post liked by Name1.", result)
        self.assertEqual({'content': 'Hello', 'likes': 1, 'comments': []}, self.social_media._posts[0])
        self.assertEqual(
            [{'content': 'Hello', 'likes': 1, 'comments': []}, {'content': 'Bye', 'likes': 0, 'comments': []}],
            self.social_media._posts)

        result2 = self.social_media.like_post(1)
        self.assertEqual("Post liked by Name1.", result2)
        self.assertEqual({'content': 'Bye', 'likes': 1, 'comments': []}, self.social_media._posts[1])
        self.assertEqual(
            [{'content': 'Hello', 'likes': 1, 'comments': []}, {'content': 'Bye', 'likes': 1, 'comments': []}],
            self.social_media._posts)

    def test_like_post_where_post_max_liked(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 10, 'comments': []},
                                    {'content': 'Bye', 'likes': 10, 'comments': []}]

        result = self.social_media.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", result)
        self.assertEqual({'content': 'Hello', 'likes': 10, 'comments': []}, self.social_media._posts[0])
        self.assertEqual(
            [{'content': 'Hello', 'likes': 10, 'comments': []}, {'content': 'Bye', 'likes': 10, 'comments': []}],
            self.social_media._posts)

        result2 = self.social_media.like_post(1)
        self.assertEqual("Post has reached the maximum number of likes.", result2)
        self.assertEqual({'content': 'Bye', 'likes': 10, 'comments': []}, self.social_media._posts[1])
        self.assertEqual(
            [{'content': 'Hello', 'likes': 10, 'comments': []}, {'content': 'Bye', 'likes': 10, 'comments': []}],
            self.social_media._posts)

    def test_like_post_where_invalid_index(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 5, 'comments': []},
                                    {'content': 'Bye', 'likes': 10, 'comments': []}]

        result = self.social_media.like_post(-1)
        self.assertEqual("Invalid post index.", result)
        self.assertEqual([{'content': 'Hello', 'likes': 5, 'comments': []}, {'content': 'Bye', 'likes': 10, 'comments': []}], self.social_media._posts)

    def test_like_post_where_invalid_index2(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 5, 'comments': []},
                                    {'content': 'Bye', 'likes': 10, 'comments': []}]

        result = self.social_media.like_post(2)
        self.assertEqual("Invalid post index.", result)
        self.assertEqual(
            [{'content': 'Hello', 'likes': 5, 'comments': []}, {'content': 'Bye', 'likes': 10, 'comments': []}],
            self.social_media._posts)

    def test_comment_on_post_where_valid(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 5, 'comments': []},
                                    {'content': 'Bye', 'likes': 10, 'comments': []}]

        result = self.social_media.comment_on_post(0, "test1test11")
        self.assertEqual("Comment added by Name1 on the post.", result)
        self.assertEqual(
            [{'comments': [{'comment': 'test1test11', 'user': 'Name1'}],
              'content': 'Hello',
              'likes': 5},
             {'comments': [], 'content': 'Bye', 'likes': 10}],
            self.social_media._posts
        )

    def test_comment_on_post_where_invalid(self):
        self.social_media._posts = [{'content': 'Hello', 'likes': 5, 'comments': []},
                                    {'content': 'Bye', 'likes': 10, 'comments': []}]

        result = self.social_media.comment_on_post(0, "test1test2")
        self.assertEqual("Comment should be more than 10 characters.", result)
        self.assertEqual(
            [{'content': 'Hello', 'likes': 5, 'comments': []},
             {'content': 'Bye', 'likes': 10, 'comments': []}],
            self.social_media._posts
        )


if __name__ == '__main__':
    main()
