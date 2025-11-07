# Mini Project: Token-based Authentication Flow in Postman
  https://ankitkumar-2356106.postman.co/workspace/PYATB5X~6c73ff5a-90de-444d-a0c7-b5326cebbe4c/folder/44694445-d87b1369-3ea3-42c4-a5c4-4353bdf9cbae?action=share&creator=44694445&ctx=documentation&active-environment=44694445-22065ceb-dd55-4311-8a88-cd8bcd22e1b8

#Scenario Overview:
  You log in to an API using credentials
  The API returns a token in the response
  You store that token in an environment variable
  You use the token in another API request to access protected data

#Project Goals
  Automate token retrieval through a login request
  Store token dynamically in an environment variable
  Use the token in headers for authenticated requests
  Add test validations for successful login and token presence

#Tools Used
  Postman

#Deliverables
  ✅ Postman Collection containing authenticated API requests
  ✅ Environment file with dynamic token storage
  ✅ Working Pre-request and Tests scripts for token management

#End Result
  🟩 A real-world project with authentication and API chaining
  Real-world confidence to automate a complete login →
  token extraction → data request flow using Postman variables and scripts

#Tips / Common Mistakes:
  ✅ Make sure environment is selected or variables won’t resolve
  🚫 Don’t hardcode tokens; always extract dynamically
  ⚠️ Token may expire in real APIs — handle re-login accordingly
  ✏️ Use console.log() to debug scripts easily
  🔒 Never share sensitive tokens publicly

Step 1 – Create new Environment

Step 2 – Add a variable: baseUrl → https://reqres.in

Step 3 – Save and select the environment

Step 4 – Create a new POST request:
{{baseUrl}}/api/login

Step 5 – In Body (raw → JSON):

{
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

Step 6 – In Tests tab, add:

const response = pm.response.json();
pm.environment.set("token", response.token);
console.log("Token saved:", response.token);


Step 7 – Click Send → Response should contain a token

Step 8 – Check Environment Variables → token should be stored

Step 9 – Create a new GET request:
{{baseUrl}}/api/users?page=2

Step 10 – Go to Headers:
Authorization → Bearer {{token}}

Step 12 – Go to the Pre-request Script tab in the GET request

pm.environment.set("timestamp", Date.now());
console.log("Current Timestamp:", pm.environment.get("timestamp"));


Step 13 – Run and turn on the Postman Console (View → Show Postman Console) to verify
