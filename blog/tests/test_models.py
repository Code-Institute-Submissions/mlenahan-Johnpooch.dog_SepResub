from django.test import TestCase
from blog.models import Post, Tag


class PostTestCase(TestCase):

    def test_parsed_content_no_change_if_no_embeds_or_snippets(self):
        post = Post.objects.create(title='python', content='Hello')
        self.assertEqual(post.content, post.parsed_content)

    def test_parsed_content_replaces_single_escaped_gist_script_with_html_script_tags(self):
        escaped_content = '&lt;script src="https://gist.github.com/johnpooch/123"&gt;&lt;/script&gt;'
        expected = '<script src="https://gist.github.com/johnpooch/123"></script>'
        post = Post.objects.create(title='python', content=escaped_content)
        result = post.parsed_content
        self.assertEqual(expected, result)

    def test_parsed_content_replaces_multiple_escaped_gist_script_with_html_script_tags(self):
        escaped_content = '&lt;script src="https://gist.github.com/johnpooch/123"&gt;&lt;/script&gt;text&lt;script src="https://gist.github.com/johnpooch/456"&gt;&lt;/script&gt;'
        expected = '<script src="https://gist.github.com/johnpooch/123"></script>text<script src="https://gist.github.com/johnpooch/456"></script>'
        post = Post.objects.create(title='python', content=escaped_content)
        result = post.parsed_content
        self.assertEqual(expected, result)

    def test_parsed_content_replaces_code_snippet_with_html_tags(self):
        content = "`code snippet`"
        expected = '<span class="inline-code-snippet">code snippet</span>'
        post = Post.objects.create(title='python', content=content)
        result = post.parsed_content
        self.assertEqual(expected, result)
    
    def test_parsed_content_replaces_multiple_code_snippet_with_html_tags(self):
        content = "`code snippet`text`code snippet`"
        expected = '<span class="inline-code-snippet">code snippet</span>text<span class="inline-code-snippet">code snippet</span>'
        post = Post.objects.create(title='python', content=content)
        result = post.parsed_content
        self.assertEqual(expected, result)
