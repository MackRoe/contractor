from bson.objectid import ObjectId
from app import app, db_client

def test_products_index(self):
        """Test the playlists homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'products', result.data)