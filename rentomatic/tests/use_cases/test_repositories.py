from unittest import TestCase
from src.domain.storageroom import StorageRoom
from src.use_cases.repositories import StorageRoomRepository

class TestStorageRoomRepository(TestCase):

    def test_get_all_one_item(self):
        storageroom_1 = StorageRoom(
            code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
            size=215,
            price=39,
            longitude='-0.09998975',
            latitude='51.75436293',
        )

        repo = StorageRoomRepository()

        repo.add(storageroom_1)

        storagerooms = repo.get_all()
        
        assert storagerooms[0].code == storageroom_1.code
        assert storagerooms[0].size == storageroom_1.size
        assert storagerooms[0].price == storageroom_1.price
        assert storagerooms[0].longitude == storageroom_1.longitude
        assert storagerooms[0].latitude == storageroom_1.latitude
    
    def test_get_all_two_items(self):
        storageroom_1 = StorageRoom(
            code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
            size=215,
            price=39,
            longitude='-0.09998975',
            latitude='51.75436293',
        )

        storageroom_2 = StorageRoom(
            code='fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
            size=405,
            price=66,
            longitude='0.18228006',
            latitude='51.74640997',
        )

        repo = StorageRoomRepository()

        repo.add(storageroom_1)
        repo.add(storageroom_2)

        storagerooms = repo.get_all()
        
        assert storagerooms[0].code == storageroom_1.code
        assert storagerooms[0].size == storageroom_1.size
        assert storagerooms[0].price == storageroom_1.price
        assert storagerooms[0].longitude == storageroom_1.longitude
        assert storagerooms[0].latitude == storageroom_1.latitude
        
        assert storagerooms[1].code == storageroom_2.code
        assert storagerooms[1].size == storageroom_2.size
        assert storagerooms[1].price == storageroom_2.price
        assert storagerooms[1].longitude == storageroom_2.longitude
        assert storagerooms[1].latitude == storageroom_2.latitude
    