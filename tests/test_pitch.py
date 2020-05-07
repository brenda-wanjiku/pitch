from  app.models import Pitch
from app import db
import unittest

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'brenda',password = 'bread', email = 'bmw@gmail.com')
        self.new_pitch = Pitch(id=1,pitch_title='Test',pitch_content='Pitch',category="interview",name= self.user_brenda,likes=0,dislikes=0)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_title,'Test')
        self.assertEquals(self.new_pitch.pitch_content,'Pitch')
        self.assertEquals(self.new_pitch.category,"Business")
        self.assertEquals(self.new_pitch.user,self.user_brenda)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):
        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitch(1)
        self.assertTrue(got_pitch is not None)

     def test_relationship_user(self):
        user = self.new_pitch.user.username
        self.assertTrue(user == "Brenda")