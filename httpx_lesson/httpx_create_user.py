import httpx
from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(url="http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response_data)
print(create_user_response.status_code)