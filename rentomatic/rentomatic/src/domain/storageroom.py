

class StorageRoom(object):
    
    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    @classmethod
    def from_dict(cls, dict):
        room = StorageRoom(
            code = dict['code'],
            size = dict['size'],
            price = dict['price'],
            latitude = dict['latitude'],
            longitude = dict['longitude']
        )

        return room