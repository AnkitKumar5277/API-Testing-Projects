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

Step 1 – Create new Environment
Step 2 – Add a variable:
baseUrl → https://reqres.in
token → (empty)
userId → (empty)
Step 3 – Save and select the environment
Step 4 – Click “New” → Collection → Name it User Flow Automation
Step 5 – Create a new POST request Login (Extract Token)
{{baseUrl}}/api/login
Step 6 – Add body
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
