from django.test import TestCase
from blog.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_post(self):
        post = Post.objects.create(title='python')
        self.assertEqual(post, Post)

    def test_created_at_auto_now_add(self):
        # just test that it is a date
        post = Post.objects.create(title='python')
        self.assertEqual(post.DateTimeField, DateTimeField)

    def test_updated_at_auto_now(self):
        # changes anytime its saved
        # create post and then change value and save post
        # assert updated at is not same as created at
        pass

    def test_published_at_not_auto_now(self):
        # mistake in model
        # when you create a post the published at is None
        pass

    def test_auto_generate_slug(self):
        # add method to auto generate slug
        # create post with title and assert that slug is correct
        pass

    def test_str(self):
        # create post then call str(post) and check that its the same as post.title
        post = Post.objects.create(title='python')
        str_post = Post.__str__()
        self.assertEqual(post.title, str_post)

    def test_publish(self):
        # add method to post called publish which should set published at to now
        # and sets status to live
        # and saves
        # create post then do post.publish
        # then find that status should be live
        # and that published at should be set
        pass

    def test_add_tag(self):
        # create many-to-many relationship(add to post)
        # create a post, create a tag
        # then do post.tags.add(tag)
        post = Post.objects.create(title='python')
        tag = Tag.objects.create(title='flask')
        post.tags.add('flask')
        self.assertEqual(post.tags, 'flask')

    def test_get_tags(self):
        post = Post.objects.create(title='python')
        tag = Tag.objects.create(title='flask')
        post.tags.add('flask')
        self.assertEqual(post.tags, tag)

    def test_parsed_content_no_change_if_no_embeds_or_snippets(self):
        post = Post.objects.create(title='python', content='Hello')
        self.assertEqual(post.content, post.parsed_content)

    def test_parsed_content_replaces_single_escaped_gist_script_with_html_script_tags(self):
        post = Post.objects.create(title='python', content='<script src="https://gist.github.com/johnpooch/123"></script>')
        self.assertEqual(post.content, post.parsed_content)

    def test_parsed_content_replaces_multiple_escaped_gist_script_with_html_script_tags(self):
        post = Post.objects.create(title='python', content='<script src="https://gist.github.com/johnpooch/123"></script>, <script src="https://gist.github.com/johnpooch/123"></script>')
        self.assertEqual(post.content, post.parsed_content)

    def test_parsed_content_replaces_code_snippet_with_html_tags(self):
        post = Post.objects.create(title='python', content='`code snippet`')
        self.assertEqual(post.content, post.parsed_content)
    
    def test_parsed_content_replaces_multiple_code_snippet_with_html_tags(self):
        post = Post.objects.create(title='python', content='`code snippet`, `code snippet 2`')
        self.assertEqual(post.content, post.parsed_content)
