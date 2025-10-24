from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    

user = User(id=12)
print(user.id)


# Gets the fields that were set during initialization
print(user.model_fields_set)
user = User(id=12, name="Jane Doe")
print(user.model_fields_set)


# Dumping
print(user.model_dump())
print(user.model_dump_json())
print(user.model_json_schema())


from typing import List, Optional
# Nested models
class Food(BaseModel):
    name: str
    price: float
    ingredients: Optional[List[str]] = None
    
class Restaurant(BaseModel):
    name: str
    location: str
    food: List[Food]

resturant = Restaurant(
    name="Good Eats",
    location="123 Main St",
    food=[
        {"name": "Burger", "price": 9.99, "ingredients": ["Beef", "Lettuce", "Tomato"]},
        {"name": "Fries", "price": 2.99}
    ]
)
print(resturant)
print(resturant.model_dump())


# pip install pydantic[email]
from pydantic import EmailStr, PositiveInt, conlist, Field, HttpUrl
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Employee(BaseModel):
    name: str
    position: str
    email: EmailStr
    
class Owner(BaseModel):
    name: str
    email: EmailStr
    
class Restaurant(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$")
    owner: Owner
    address: Address
    # at least 2 employees
    employees: conlist(Employee, min_length=2) # type: ignore
    number_of_seats: PositiveInt
    delivery: bool
    website: HttpUrl

# Creating an instance of the Restaurant class
restaurant_instance = Restaurant(
    name="Tasty Bites",
    owner={
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    address={
        "street": "123, Flavor Street",
        "city": "Tastytown",
        "state": "TS",
        "zip_code": "12345",
    },
    employees=[
        {
            "name": "Jane Doe",
            "position": "Chef",
            "email": "jane.doe@example.com"
        },
        {
            "name": "Mike Roe",
            "position": "Waiter",
            "email": "mike.roe@example.com"
        }
    ],
    number_of_seats=50,
    delivery=True,
    website="http://tastybites.com"
)

# Printing the instance
print(restaurant_instance)