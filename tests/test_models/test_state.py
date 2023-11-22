import unittest
import MySQLdb
import subprocess

class TestCreateState(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def test_create_state(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        original_count = self.cursor.fetchone()[0]

        subprocess.run(['echo', 'create State name="California"', '|', 'HBNB_MYSQL_USER=hbnb_test', 'HBNB_MYSQL_PWD=hbnb_test_pwd', 'HBNB_MYSQL_HOST=localhost', 'HBNB_MYSQL_DB=hbnb_test_db', 'HBNB_TYPE_STORAGE=db', 'python3', 'console.py'], shell=True)

        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        self.assertEqual(new_count, original_count + 1)

    def tearDown(self):
        self.cursor.close()
        self.db.close()