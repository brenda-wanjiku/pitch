from app.models import Comment
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'brenda',password = 'bread', email = 'bmw@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='Pitch',category="Business",name = self.user_brenda,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_brenda,pitch=self.new_pitch)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()



    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_brenda)
        self.assertEquals(self.new_comment.pitch,self.

    def test_get_comments(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(2)
        self.assertEqual(len(get_comments) == 2)

    def test_save_comments(self):
            self.new_review.save_review()
            self.assertTrue(len(Review.query.all())>0)