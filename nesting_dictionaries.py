"""
Module to manage user data with address information.
This module contains a list of users and prints their details in a formatted manner.
"""

USERS = [
    {
        "user_id": 1,
        "full_name": "Jean Carlos",
        "address": {
            "street": "1890 Park Ave",
            "apartment": "5C",
            "zip_code": "10024"
        },
        "is_active": True
    },
    {
        "user_id": 2,
        "full_name": "Maria Lopez",
        "address": {
            "street": "2200 Broadway",
            "apartment": "10A",
            "zip_code": "10025"
        },
        "is_active": False
    },
    {
        "user_id": 3,
        "full_name": "David Kim",
        "address": {
            "street": "155 W 72nd St",
            "apartment": "2B",
            "zip_code": "10023"
        },
        "is_active": True
    }
]

for user in USERS:
    print(f"id: {user["user_id"]}")
    print(f"full_name: {user["full_name"]}")
    print(f"is_active: {user["is_active"]}")
    print(f"street: {user["address"]["street"]}")
    print(f"apartment: {user["address"]["apartment"]}")
    print(f"zip_code: {user["address"]["zip_code"]}")
    print("-----------------------------")
