Documentation - https://restful-booker.herokuapp.com/apidoc/index.html

Postman Link - https://ankitkumar-2356106.postman.co/workspace/PYATB5X~6c73ff5a-90de-444d-a0c7-b5326cebbe4c/collection/44694445-eaf55b4b-1bef-4b9a-9bf0-dc79e7e67a44?action=share&creator=44694445

Create Environment
 	Token
	Booking id
	Base url
Create Token
	Post
	{{base_url}} / auth
	Headers
	Body (raw → JSON)
	Test tab 
var jsonData = pm.response.json();
pm.environment.set("token", jsonData.token);

CREATE
Post
{{base_url}} / booking
Headers
Body (raw → JSON)
Test tab 
var jsonData = pm.response.json();
pm.environment.set("booking_id", jsonData.bookingid);

READ
	Get
	{{base_url}} / booking / {{booking_id}}

UPDATE
PUT
{{base_url}} / booking / {{booking_id}}
Headers
	Content-type
	cookie
Body (raw → JSON)

PARTIAL UPDATE
PATCH
{{base_url}} / booking / {{booking_id}}
Headers
	Content-type
	Cookie
Body (raw → JSON)

DELETE
	Delete
{{base_url}} / booking / {{booking_id}}
Headers - only Cookie token={{token}}
