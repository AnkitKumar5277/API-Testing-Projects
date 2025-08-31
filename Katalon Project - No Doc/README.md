Project Link : https://ankitkumar-2356106.postman.co/workspace/PYATB5X~6c73ff5a-90de-444d-a0c7-b5326cebbe4c/collection/44694445-a3d0ad0f-8cef-4ff5-96a2-aefd33942351?action=share&source=copy-link&creator=44694445

# 🏥 Katalon Demo Healthcare API Testing Project

This project demonstrates **API testing using Postman** on the [Katalon Demo Healthcare App](https://katalon-demo-cura.herokuapp.com/).  
It covers **Authentication, Appointment Management, User Management, and Security Testing** with **15 core API requests**.

---

## 🔹 Project Overview
- **Base URL:** `https://katalon-demo-cura.herokuapp.com`
- **Tool Used:** Postman
- **Focus Areas:**  
  - Authentication (Login/Logout)  
  - CRUD Operations on Appointments  
  - User Management (Register, Profile, Password)  
  - Security & Negative Testing  

---

## 🔑 **Top 15 API Requests**

### 1. Login (Valid Credentials)
- **POST** `/authenticate.php`
- **Headers:** `Content-Type: application/x-www-form-urlencoded`
- **Body:**
username: John Doe
password: ThisIsNotAPassword

yaml
Copy code
- ✅ Expected: 200 OK with success message

---

### 2. Login with Invalid Credentials
- **POST** `/authenticate.php`
- Wrong username/password
- ✅ Expected: 401 Unauthorized

---

### 3. Login with Blank Fields
- **POST** `/authenticate.php`
- Empty username & password
- ✅ Expected: Validation error

---

### 4. Logout
- **GET** `/logout.php`
- ✅ Expected: Session cleared

---

### 5. Make Appointment (Valid Data)
- **POST** `/appointment.php`
- **Headers:** `Content-Type: application/x-www-form-urlencoded`
- **Body:**
facility: Tokyo CURA Healthcare Center
hospital_readmission: Yes
healthcare_program: Medicaid
visit_date: 2025-09-10
comment: First appointment

yaml
Copy code
- ✅ Expected: Appointment created

---

### 6. Get All Appointments
- **GET** `/appointments.php`
- ✅ Expected: List of appointments (JSON)

---

### 7. Get Appointment by ID
- **GET** `/appointments.php?id=1`
- ✅ Expected: Appointment details (ID=1)

---

### 8. Update Appointment
- **PUT** `/appointments.php?id=1`
- **Headers:** `Content-Type: application/json`
- **Body:**
```json
{
  "facility": "Hongkong CURA Center",
  "visit_date": "2025-09-15",
  "comment": "Updated appointment"
}
✅ Expected: Appointment updated

9. Cancel Appointment
DELETE /appointments.php?id=1

✅ Expected: Appointment deleted

10. Register New User
POST /register.php

Headers: Content-Type: application/json

Body:

json
Copy code
{
  "name": "Ankit",
  "email": "ankit@test.com",
  "password": "Test@123"
}
✅ Expected: User created

11. Register with Existing Email
POST /register.php

Duplicate email

✅ Expected: "Email already exists"

12. Update User Profile
PUT /user.php?id=1

Body:

json
Copy code
{
  "phone": "9876543210",
  "address": "India"
}
✅ Expected: Profile updated

13. Change Password
PUT /user/password.php?id=1

Body:

json
Copy code
{
  "old_password": "Test@123",
  "new_password": "New@123"
}
✅ Expected: Password updated

14. Get User Profile
GET /user.php?id=1

✅ Expected: User details in JSON

15. Access Appointments Without Login
GET /appointments.php

No authentication

✅ Expected: 401 Unauthorized

📌 How to Use
Clone or download this repo.

Import the Postman Collection (Katalon_Healthcare_APIs.json) into Postman.

Run requests individually or via Postman Runner.

Validate responses with Postman Tests.

📝 Key Learnings
Hands-on with Postman API Testing

Performed CRUD Operations

Implemented Positive & Negative Scenarios

Explored Security Tests (Unauthorized access, invalid login)

Practiced Real-World API testing skills

💼 Resume Highlight
"Developed and executed API testing project using Postman for Katalon Healthcare Demo application covering 15+ APIs including authentication, CRUD, user management, and security testing scenarios."

yaml
Copy code

Ask ChatGPT
