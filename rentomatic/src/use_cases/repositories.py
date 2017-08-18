
class StorageRoomRepository(object):

    def __init__(self):
        self.storagerooms = []
    
    def get_all(self):
        return self.storagerooms

    def add(self, storageroom):
        self.storagerooms.append(storageroom)