from django.test import TestCase
import uuid

class TestStorageRoom(TestCase):

    def test_storageroom_model_init(self):
        code = uuid.uuid4()
        storageroom = StorageRoom(code, size=200, price=10,
                           longitude='-0.09998975',
                           latitude='51.75436293')
        self.assertEquals(code,  storageroom.code)
        self.assertEquals(storageroom.size, 200)
        self.assertEquals(storageroom.price, 10)
        self.assertEquals(storageroom.longitude, -0.09998975)
        self.assertEquals(storageroom.latitude, 51.75436293)