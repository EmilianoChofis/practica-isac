import json
from unittest import TestCase
from unittest.mock import patch

from practica import app

"""
connection.cursor
cursor.execute
cursor.fetchone
connection.close"""
class Test(TestCase):

    @patch.dict("os.environ",
                {"DB_HOST": "localhost", "DB_USER": "root", "DB_PASSWORD": "password", "DB_NAME": "practica"})
    @patch("practica.app.pymysql.connect")
    def test_lambda_handler(self, mock_connect):
        mock_connect.return_value = True
        result = app.lambda_handler(None, None)

        self.assertEqual(result['statusCode'], 200)
        body = json.loads(result['body'])
        self.assertIn("data", body)
        self.assertTrue(body["data"])