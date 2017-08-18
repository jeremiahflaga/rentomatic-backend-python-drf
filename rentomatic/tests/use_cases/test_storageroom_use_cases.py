from unittest import TestCase
from src.use_cases.storageroom_use_cases import StorageRoomListUseCase
from src.domain.storageroom import StorageRoom
from tests.use_cases.fakes import StorageRoomRepositoryMock


class TestStorageRoomListUseCase(TestCase):
    
    def test_storage_room_list_use_case(self):        
        storageroom_1 = StorageRoom(
            code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
            size=215,
            price=39,
            longitude='-0.09998975',
            latitude='51.75436293',
        )

        repository_mock = StorageRoomRepositoryMock()
        repository_mock.setup([storageroom_1])

        storageroom_list_use_case = StorageRoomListUseCase(repository_mock)

        response = storageroom_list_use_case.execute()

        assert response[0].code == storageroom_1.code
        assert response[0].size == storageroom_1.size
        assert response[0].price == storageroom_1.price
        assert response[0].longitude == storageroom_1.longitude
        assert response[0].latitude == storageroom_1.latitude
