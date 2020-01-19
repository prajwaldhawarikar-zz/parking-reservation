# parking-reservation

Parking reservation exposes REST APIs to
- See available parking spots on a map
 - Search for an address and find nearby parking spot. (input: lat, lng, radius in meters. Output - list of
parking spots within the radius).
-  Reserve a parking spot
-  View existing reservations
-  Cancel an existing reservation

The REST APIs are built using Flask and MongoDB.

API description:

- Fetch all parking slots<br>
    *GET*  http://localhost:5000/api/v1/parking_spots
    <br>
    Sample response: <br>
    [
    {
        "_id": "5e2423d01c9d440000413fec",
        "address": "Ring Rd, Vyankatesh Nagar, Kotwal Nagar, Tatya Tope Nagar, Khamla, Nagpur, Maharashtra 440022",
        "location": {
            "coordinates": [
                79.062645,
                21.112567
            ],
            "type": "Point"
        }
    },
    {
        "_id": "5e24246b1c9d440000413fed",
        "address": "Wardha Rd, Somalwada Square, Somalwada, Nagpur, Maharashtra 440005",
        "location": {
            "coordinates": [
                79.067004,
                21.09847
            ],
            "type": "Point"
        }
    }
    ]
    
- Search nearby parking spots
    *GET* http://localhost:5000/api/v1/parking_spots/search?lat=21.113738&lng=79.056776&radius=626
    <br>
    Sample response: <br>
    [
    {
        "_id": "5e2423d01c9d440000413fec",
        "address": "Ring Rd, Vyankatesh Nagar, Kotwal Nagar, Tatya Tope Nagar, Khamla, Nagpur, Maharashtra 440022",
        "location": {
            "coordinates": [
                79.062645,
                21.112567
            ],
            "type": "Point"
        }
    }
    ]
- Reserve a parking spot: <br>
    *POST* http://localhost:5000/api/v1/bookings
    <br>
    Sample request body:
    <br>
    {
	"user": "5e241bac1c9d44000051f251",
	"parking_spot": "5e2423d01c9d440000413fec"
    }
    <br>
    Sample response:
    <br>
    {
    "_id": "5e2442ee5f95925ea6994935",
    "created_at": "Sun, 19 Jan 2020 17:22:14 GMT",
    "parking_spot": "5e2423d01c9d440000413fec",
    "state": "CONFIRMED",
    "updated_at": "Sun, 19 Jan 2020 17:22:14 GMT",
    "user": "5e241bac1c9d44000051f251"
    }
   <br>
- Fetch existing reservations
    <br>
    *GET* http://localhost:5000/api/v1/bookings
    <br>
    Sample response:
    <br>
    [
    {
        "_id": "5e2426081c005cdba801d563",
        "created_at": "Sun, 19 Jan 2020 15:18:56 GMT",
        "parking_spot": {
            "_id": "5e2423d01c9d440000413fec",
            "address": "Ring Rd, Vyankatesh Nagar, Kotwal Nagar, Tatya Tope Nagar, Khamla, Nagpur, Maharashtra 440022",
            "location": {
                "coordinates": [
                    79.062645,
                    21.112567
                ],
                "type": "Point"
            }
        },
        "state": "CONFIRMED",
        "updated_at": "Sun, 19 Jan 2020 15:18:56 GMT",
        "user": {
            "_id": "5e241b811c9d44000051f24f",
            "name": "Prajwal"
        }
    },
    {
        "_id": "5e24264d1c005cdba801d564",
        "created_at": "Sun, 19 Jan 2020 15:20:05 GMT",
        "parking_spot": {
            "_id": "5e24246b1c9d440000413fed",
            "address": "Wardha Rd, Somalwada Square, Somalwada, Nagpur, Maharashtra 440005",
            "location": {
                "coordinates": [
                    79.067004,
                    21.09847
                ],
                "type": "Point"
            }
        },
        "state": "CONFIRMED",
        "updated_at": "Sun, 19 Jan 2020 15:20:05 GMT",
        "user": {
            "_id": "5e241bac1c9d44000051f251",
            "name": "Niharika"
        }
    }]

- Cancel an existing reservation
    <br>
    *PATCH* http://localhost:5000/api/v1/bookings/<booking_id>/cancel
    <br>
    
    Sample request body:
    <br>
    {
	"_id": "5e2439ff9f27ecaa731c53b9",
	"state": "CANCELLED"
    }
    <br>
    Sample response:
    <br>
    {
    "_id": "5e2439ff9f27ecaa731c53b9",
    "message": "booking cancelled"
    }

Heroku app url: https://tranquil-eyrie-82395.herokuapp.com/

