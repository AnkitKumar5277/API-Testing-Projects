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
