

class StorageRoom(object):
    
    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = float(latitude)
        self.longitude = float(longitude)
