from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestCourierLocation:
    def test_create_courier(self):
        new_courier_data = {
            "name": "John Doe",
            "location": {"latitude": 40.7128, "longitude": -74.0060},
        }
        response = client.post("/b_courier", json=new_courier_data)
        assert response.status_code == 200
        assert response.json() == {"message": "Courier created successfully"}

    def test_get_courier_location(self):
        response = client.get("/b_courier?courier_id=1")
        assert response.status_code == 200
        assert response.json() == {"location": "test_location"}

    def test_change_courier_location(self):
        new_location = {"latitude": 40.7128, "longitude": -74.0060}
        response = client.post("/b_courier?courier_id=1", json=new_location)
        assert response.status_code == 200
        assert response.json() == {"message": "Location updated successfully"}


class TestCourierLocationNotFound:
    def test_get_courier_location_not_found(self):
        response = client.get(
            "/b_courier?courier_id=100"
        )  # Assuming courier with ID 100 doesn't exist
        assert response.status_code == 404
        assert response.json() == {"detail": "Courier not found"}

    def test_change_courier_location_not_found(self):
        new_location = {"latitude": 40.7128, "longitude": -74.0060}
        response = client.post(
            "/b_courier?courier_id=100", json=new_location
        )  # Assuming courier with ID 100 doesn't exist
        assert response.status_code == 404
        assert response.json() == {"detail": "Courier not found"}
