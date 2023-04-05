from import_export import resources
from .models import Productfield

class PersonReource(resources.ModelResource):
    class meta:
        model=Productfield