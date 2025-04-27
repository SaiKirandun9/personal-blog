import requests

def test_get_single_user():
    # Send GET request to the new API
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")

    # Print Status Code
    print("Status Code:", response.status_code)

    # Print Response Body
    print("Response Body:", response.json())

    # Assertions (Validation)
    assert response.status_code == 200
    assert response.json()['name'] == 'Ervin Howell'

if __name__ == "__main__":
    test_get_single_user()

