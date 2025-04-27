import requests

def test_create_new_user():
    payload = {
        "name": "Saikiran",
        "job": "QA Engineer"
    }

    # Send POST request to jsonplaceholder
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

    # Print Status Code
    print("Status Code:", response.status_code)

    # Print Response Body
    print("Response Body:", response.json())

    # Assertions
    assert response.status_code == 201
    assert response.json()['name'] == 'Saikiran'
    assert response.json()['job'] == 'QA Engineer'

if __name__ == "__main__":
    test_create_new_user()

