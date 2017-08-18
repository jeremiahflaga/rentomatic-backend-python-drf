
class StorageRoomRepositoryMock(object):
    
    def setup(self, storagerooms):
        self.storagerooms = storagerooms

    def get_all(self):
        return self.storagerooms