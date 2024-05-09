import unittest
from main import app, User, Note

class TestNoteApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        User('test_user', 'test_password').save()

    def tearDown(self):
        test_user = User.get_by_username_and_password('test_user', 'test_password')
        if test_user:
            test_user.delete()

    def test_login(self):
        response = self.app.post('/login', data=dict(
            username='test_user',
            password='test_password'
        ), follow_redirects=True)
        self.assertIn(b'Notes', response.data)

    def test_signup(self):
        response = self.app.post('/signup', data=dict(
            username='new_test_user',
            password='new_test_password'
        ), follow_redirects=True)
        self.assertIn(b'Log In', response.data)

    def test_add_note(self):
        with self.app.session_transaction() as sess:
            sess['user_id'] = 1
        response = self.app.post('/add_note', data=dict(
            title='Test Note',
            content='Test content',
            folder='Test Folder'
        ), follow_redirects=True)
        self.assertIn(b'Test Note', response.data)

    def test_edit_note(self):
        with self.app.session_transaction() as sess:
            sess['user_id'] = 1  
        response = self.app.post('/edit_note/1', data=dict(
            title='Updated Note',
            content='Updated content',
            folder='Updated Folder'
        ), follow_redirects=True)
        self.assertIn(b'Updated Note', response.data)

    def test_delete_note(self):
        with self.app.session_transaction() as sess:
            sess['user_id'] = 1  
        response = self.app.post('/delete_note/1', follow_redirects=True)
        self.assertNotIn(b'Updated Note', response.data)


if __name__ == '__main__':
    unittest.main()
