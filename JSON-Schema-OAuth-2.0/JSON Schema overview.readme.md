### 🧩 1. What is JSON Schema (Simple Explanation)
JSON Schema is a rulebook for your JSON data.
It defines how the data should look — what keys are allowed, what data types (string, number, boolean, etc.), and whether fields are required.

Example:
```
{
  "name": "Ankit",
  "age": 25,
  "email": "ankit@test.com"
}
```

JSON Schema for this:
```
{
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "integer" },
    "email": { "type": "string", "format": "email" }
  },
    "required": ["name", "age", "email"]
}
```

### This schema checks:
  ✅ All keys exist
  ✅ Data types match
  ✅ Email format is valid

### 🚀 2. Project Idea: “User API Validation”
API Endpoint (use public test API)
We’ll use this free API:
``` https://reqres.in/api/users/2 ```
If you send a GET request here, you’ll get:

```
{
  "data": {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
  },
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```

### 🧪 3. Steps to Test in Postman
Step 1️⃣: Create a New Request
Open Postman → New → Request
Name: Get User Data
Method: GET
URL: https://reqres.in/api/users/2
Click Send
You’ll see the above JSON response.

Step 2️⃣: Add JSON Schema Validation in Tests Tab
Go to Tests tab in Postman and paste:
```
const schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": { "type": "integer" },
        "email": { "type": "string", "format": "email" },
        "first_name": { "type": "string" },
        "last_name": { "type": "string" },
        "avatar": { "type": "string" }
      },
      "required": ["id", "email", "first_name", "last_name", "avatar"]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": { "type": "string" },
        "text": { "type": "string" }
      },
      "required": ["url", "text"]
    }
  },
  "required": ["data", "support"]
};

// Validate using Postman's built-in Ajv validator
pm.test("Validate JSON Schema", function () {
  pm.response.to.have.jsonSchema(schema);
});
```
Step 3️⃣: Run & Validate
Click Send
Go to the Tests tab (below response) → You’ll see
✅ Test Passed: Validate JSON Schema
If the response changes or a field is missing →
❌ Test will fail and tell you what doesn’t match.

🧠 4. Practice Ideas for You
Try these to learn more:
Remove "email" from required → see if validation still passes
Change "email" type to "number" → watch test fail
Use another endpoint like https://reqres.in/api/users?page=2 and design your own schema
