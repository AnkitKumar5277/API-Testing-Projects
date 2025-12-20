Here’s a **clean, interview-ready `README.md` format** you can directly use in your GitHub project for this **Postman API Automation Mini Project**.

---

```md
# 🧪 Mini Project: Automating API Test Flow with Postman

## 📌 Project Overview
This project demonstrates **end-to-end API automation** using **Postman Collections, Environments, and Collection Runner**.  
A complete **User Management API workflow** is automated with dynamic data handling and request chaining.

---

## 🔁 Automated API Flow
1. **Login** → Extract authentication token  
2. **Create User** → Use token → Extract userId  
3. **Update User** → Use extracted userId  
4. **Delete User** → Validate deletion  

All requests are executed **in one flow** using Postman Runner.

---

## 🗂 Project Structure
```

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

```

---

## 🌍 Environment Setup

**Environment Name:** `User_API_Env`

| Variable | Initial Value | Current Value |
|--------|---------------|---------------|
| baseUrl | https://reqres.in | https://reqres.in |
| token | | |
| userId | | |

---

## 🔐 API Requests Details

### 1️⃣ Login – Extract Token
**Method:** POST  
**Endpoint:**  
```

{{baseUrl}}/api/login

````

**Request Body:**
```json
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
````

**Tests Script:**

```javascript
pm.test("Login successful", function () {
    pm.response.to.have.status(200);
});

let response = pm.response.json();
pm.environment.set("token", response.token);
```

---

### 2️⃣ Create User – Extract userId

**Method:** POST
**Endpoint:**

```
{{baseUrl}}/api/users
```

**Headers:**

```
Authorization: Bearer {{token}}
Content-Type: application/json
```

**Request Body:**

```json
{
  "name": "Ankit",
  "job": "QA Engineer"
}
```

**Tests Script:**

```javascript
pm.test("User created successfully", function () {
    pm.response.to.have.status(201);
});

let response = pm.response.json();
pm.environment.set("userId", response.id);
```

---

### 3️⃣ Update User

**Method:** PUT
**Endpoint:**

```
{{baseUrl}}/api/users/{{userId}}
```

**Request Body:**

```json
{
  "name": "Ankit Kumar",
  "job": "Senior QA Engineer"
}
```

**Tests Script:**

```javascript
pm.test("User updated successfully", function () {
    pm.response.to.have.status(200);
});
```

---

### 4️⃣ Delete User

**Method:** DELETE
**Endpoint:**

```
{{baseUrl}}/api/users/{{userId}}
```

**Tests Script:**

```javascript
pm.test("User deleted successfully", function () {
    pm.response.to.have.status(204);
});
```

---

## ▶ Running the Collection

1. Open **Postman**
2. Click **Collection Runner**
3. Select Collection → `User Management API Automation`
4. Select Environment → `User_API_Env`
5. Set Iterations → `1`
6. Click **Run**

---

## 📊 Test Execution Report

* All requests executed successfully ✅
* Token and userId passed dynamically
* Full API workflow completed in a single run

Reports can be exported in:

* JSON
* HTML

---

## 🎯 Key Learnings

✔ API workflow automation
✔ Environment variable handling
✔ Dynamic request chaining
✔ Postman test scripting
✔ CI/CD ready automation approach

---

## 🛠 Tools Used

* Postman
* REST APIs
* JavaScript (Postman Tests)

---

## 📌 Ideal For

* QA Freshers
* API Testing Practice
* Automation Portfolio
* Interview Demonstrations

```

---

If you want, I can also:
- 📸 Add **screenshots section**
- 🧠 Convert this into **resume bullet points**
- 🚀 Prepare **CI/CD + Newman README**

Just tell me 👍
```
