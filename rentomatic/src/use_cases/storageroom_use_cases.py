from src.domain.storageroom import StorageRoom

class StorageRoomListUseCase(object):

    def __init__(self, repository):
        self.repository = repository
        
    def execute(self):
        return self.repository.get_all()

    