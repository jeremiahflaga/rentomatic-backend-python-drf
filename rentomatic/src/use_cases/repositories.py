
class StorageRoomRepository(object):
    
    def get_all(self):
        storageroom1 = {
            'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'size': 215,
            'price': 39,
            'longitude': '-0.09998975',
            'latitude': '51.75436293',
        }

        return [StorageRoom.from_dict(storageroom1)]