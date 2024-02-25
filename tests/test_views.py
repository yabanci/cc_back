from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestCourierLocation:
    def test_create_courier(self):
        new_courier_data = {
            "name": "John Doe",
            "location": {"latitude": 40.7128, "longitude": -74.0060},
        }
        response = client.post("/courier", json=new_courier_data)
        assert response.status_code == 200
        assert response.json() == {"message": "Courier created successfully"}

    def test_get_courier_location(self):
        response = client.get("/courier?courier_id=1")
        assert response.status_code == 200
        assert response.json() == {"latitude": 40.7128, "longitude": -74.0060}

    def test_change_courier_location(self):
        new_location = {"latitude": 40.7128, "longitude": -74.0060}
        response = client.post("/courier/1/location", json=new_location)
        assert response.status_code == 200
        assert response.json() == {"message": "Location updated successfully"}


class TestCourierLocationNotFound:
    def test_get_courier_location_not_found(self):
        response = client.get("/courier?courier_id=100")
        assert response.status_code == 404
        assert response.json() == {"detail": "Courier not found"}

    def test_change_courier_location_not_found(self):
        new_location = {"latitude": 40.7128, "longitude": -74.0060}
        response = client.post("/courier/100/location", json=new_location)
        assert response.status_code == 404
        assert response.json() == {"detail": "Courier not found"}
