
# from models.user.models import base_createTable_users
from models.base import Base
from models.base import base_data

if __name__ == "__main__":
    # base_createTable_users()
    Base.metadata.drop_all(base_data.engine)
    Base.metadata.create_all(base_data.engine)