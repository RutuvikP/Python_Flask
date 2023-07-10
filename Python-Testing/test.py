import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_existing_city(client):
    response=client.get('/weather/Austin')
    assert response.status_code == 200
    assert response.json == {'temperature': 32, 'weather': 'Hot'}

def test_nonexisting_city(client):
    response=client.get('/weather/London')
    assert response.status_code == 404
    assert response.json == {'error':'City not found!!'}

def test_add_weather(client):
    data={
        'city':'Latur',
        'temperature':28,
        'weather':'Cloudy'
    }
    response=client.post('/weather',json=data)

    assert response.status_code == 200
    assert response.json == {'msg': 'Data Added Successfully!'}

def test_add_weather_invalid(client):
    data={
        'temperature':28,
        'weather':'Cloudy'
    }
    response=client.post('/weather',json=data)

    assert response.status_code == 400
    assert response.json == {'error':'Incomplete Data'}

def test_update_weather(client):
    city = "Latur"
    data={
        'temperature':28,
        'weather':'Cloudy'
    }
    response=client.put(f'/weather/{city}',json=data)

    assert response.status_code == 200
    assert response.json == {'msg': 'Data updated Successfully!'}

def test_update_weather_invalid(client):
    city = "nonExisting"
    
    response=client.put(f'/weather/{city}')

    assert response.status_code == 400
    assert response.json == {'error':'City not Found'}

def test_delete_weather(client):
    city = "Latur"
    response=client.delete(f'/weather/{city}')

    assert response.status_code == 200
    assert response.json == {'msg': 'City deleted Successfully!'}

def test_delete_weather_invalid(client):
    city = "nonExisting"
    
    response=client.delete(f'/weather/{city}')

    assert response.status_code == 400
    assert response.json == {'error':'City not Found'}

