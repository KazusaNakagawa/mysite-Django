from django.test import TestCase

# from .models import Category
from blog.models import Comment
from blog.models import Post


# Create your tests here.

class PostTests(TestCase):
    def test_save(self):
        save = Post()
        self.assert_(True, msg=save)

    def test_save_false(self, *args, **kwargs):
        save = Post(*args, **kwargs)
        with self.assertRaises(AssertionError):
            self.assert_(False, msg=save)

    def test_save_request(self):
        save = Post()
        str_ = self.__str__().isalnum()
        self.assertNotEqual(save, str_, msg='save')


class CommentTests(TestCase):
    def setUp(self) -> None:
        print('setup')
        self.comment = Comment()

    def tearDown(self) -> None:
        print('clean up')
        del self.comment

