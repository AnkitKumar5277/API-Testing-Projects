Mini Project : Automating API Test Flow with Postman Collections & Runner

Scenario Overview:
● You have a simple User Management API
● The test flow involves:
   a. Login → extract token
   b. Create a user → use token → extract user ID
   c. Update user using the extracted ID
   d. Delete the user
● You’ll run all these steps as one automated flow using Postman Runner

Deliverables
✅ Postman Collection with at least 4 requests
✅ Environment file for base URL and dynamic variables
✅ Automated run report (via Collection Runner)

End Result
🟩 You can run a complete API workflow in one go
🟩 You can pass variables dynamically and chain requests
🟩 Builds a foundation for data-driven and CI/CD testing

ask ai -> For this request create script in post-response section to extract token from response and store it in environment variable `token`

🧪 Mini Project: Automating API Test Flow using Postman
📌 Scenario

Automate a User Management API flow using Postman Collection + Environment + Runner

Flow:

Login → extract token

Create User → use token → extract userId

Update User → use userId

Delete User

🗂 Project Structure
Postman
│
├── Collection
│   ├── 1_Login
│   ├── 2_Create_User
│   ├── 3_Update_User
│   └── 4_Delete_User
│
├── Environment
│   ├── baseUrl
│   ├── token
│   └── userId
│
└── Collection Runner Report

🌍 Step 1: Create Environment

Environment Name: User_API_Env

Add variables:

Variable	Initial Value	Current Value
baseUrl	https://reqres.in
	https://reqres.in

token		
userId		

✅ Save Environment

📦 Step 2: Create Collection

Collection Name:
User Management API Automation

🔐 Request 1: Login (Extract Token)

Request Name: 1_Login
Method: POST
URL:

{{baseUrl}}/api/login


Body (JSON):

{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}

✅ Tests Script
pm.test("Login successful", function () {
    pm.response.to.have.status(200);
});

let response = pm.response.json();
pm.environment.set("token", response.token);


✔ Token stored dynamically

👤 Request 2: Create User (Extract userId)

Request Name: 2_Create_User
Method: POST
URL:

{{baseUrl}}/api/users


Headers:

Authorization: Bearer {{token}}
Content-Type: application/json


Body (JSON):

{
  "name": "Ankit",
  "job": "QA Engineer"
}

✅ Tests Script
pm.test("User created", function () {
    pm.response.to.have.status(201);
});

let response = pm.response.json();
pm.environment.set("userId", response.id);


✔ userId extracted and saved

✏ Request 3: Update User

Request Name: 3_Update_User
Method: PUT
URL:

{{baseUrl}}/api/users/{{userId}}


Headers:

Authorization: Bearer {{token}}
Content-Type: application/json


Body (JSON):

{
  "name": "Ankit Kumar",
  "job": "Senior QA Engineer"
}

✅ Tests Script
pm.test("User updated", function () {
    pm.response.to.have.status(200);
});

🗑 Request 4: Delete User

Request Name: 4_Delete_User
Method: DELETE
URL:

{{baseUrl}}/api/users/{{userId}}


Headers:

Authorization: Bearer {{token}}

✅ Tests Script
pm.test("User deleted", function () {
    pm.response.to.have.status(204);
});

▶ Step 3: Run Using Collection Runner

Click Runner

Select Collection → User Management API Automation

Select Environment → User_API_Env

Iterations → 1

Click Run

📊 Deliverable: Automated Run Report

After run:

All requests PASS (🟢)

Token & userId passed automatically

Full workflow executed in one go

You can export report as:

JSON

HTML

🎯 End Result (For Interview / Resume)

✔ Automated complete API workflow
✔ Dynamic variable handling
✔ Request chaining
✔ Ready for CI/CD integration
✔ Real-world API automation exposure



