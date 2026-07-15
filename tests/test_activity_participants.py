from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    original_participants = list(activities[activity_name]["participants"])

    response = client.delete(f"/activities/{activity_name}/participants/{original_participants[0]}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {original_participants[0]} from {activity_name}"
    assert original_participants[0] not in activities[activity_name]["participants"]

    activities[activity_name]["participants"] = original_participants
