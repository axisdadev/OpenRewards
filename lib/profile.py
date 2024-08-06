import lib.logging as logging, yaml
from tinydb import TinyDB, Query

with open("config.yaml") as conf:
    config = yaml.safe_load(conf)
    
class Profile:
    def __init__(self) -> None:
        with open("config.yaml") as conf:
          config = yaml.safe_load(conf)
        
        self.db = TinyDB(config['USER_DB'])
        self.config = config
        pass
    
    def create_profile(self,userId: str):
        db = self.db
        profile = {"user": userId, "points": 0}
        status = db.insert(profile)
        logging.Logging.info(f"Created profile for {userId} with an index of {status}.")
        return status
    
    def delete_profle(self, userId: str):
        db = self.db
        data = Query()
        status = db.remove(data.user == userId)
        logging.Logging.warn(f"Deleted profile for {userId}.")

        return status
    
    def fetch_profile(self, userId: str):
        db = self.db
        data = Query()
        status = db.search(data.user == userId)
        return status
    
    def profile_exists(self, userId: str):
        db = self.db
        data = Query()
        status = db.search(data.user == userId)
        
        if status == []:
            return False
        else:
            return True
    