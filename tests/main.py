from models.base_model import BaseModel
from models.city import City
from models.place import Place

if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)


