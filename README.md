# 🔐 API Security Testing Framework

## 📌 Project Overview

This project is an **Automated API Security Testing Framework** designed to identify common vulnerabilities in web APIs. It simulates real-world penetration testing techniques and provides automated scanning with report generation.

---

## 🎯 Objectives

* Develop a secure API using Flask
* Implement authentication using **JWT and OAuth (simulated)**
* Identify and exploit API vulnerabilities
* Automate security testing using Python scripts
* Generate structured vulnerability reports

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Authentication:** JWT (flask-jwt-extended), OAuth (simulated)
* **Testing Tools:** Postman, Burp Suite, OWASP ZAP
* **Automation:** Python Requests
* **Environment:** Kali Linux (VMware Fusion)

---

## 🔑 Features

* ✅ JWT-based authentication
* ✅ OAuth login simulation
* ✅ Protected API endpoints
* ✅ Vulnerable endpoints for testing
* ✅ Secure (fixed) endpoints
* ✅ Automated vulnerability scanner
* ✅ Report generation (report.txt)

---

## 🧪 Vulnerabilities Tested

### 1. Broken Object Level Authorization (BOLA)

* Users can access other users' data by modifying IDs
* Demonstrated in `/profile/<id>` and `/orders/<id>`

### 2. Rate Limiting Issues

* Weak rate limiting implementation
* Demonstrated in `/limited`

### 3. Authentication Checks

* Ensures protected endpoints require valid JWT tokens

---

## 📂 Project Structure

```
api-security-testing-framework/
│
├── api_server.py        
├── api_scanner.py       
├── report.txt           
├── README.md
```

---

## 🚀 Setup & Installation

### 1. Clone Repository

```
git clone https://github.com/shaunAngel/api-security-testing-framework.git
cd api-security-testing-framework
```

---

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install flask flask-jwt-extended requests authlib
```

---

## ▶️ Running the Project

### Start API Server

```
python api_server.py
```

API runs on:

```
http://<KALI_IP>:5000
```

---

### Run Automated Scanner

```
python api_scanner.py
```

---

## 🔐 Authentication Flow

1. User logs in using `/login`
2. Server generates JWT token
3. Token is used to access protected endpoints
4. Unauthorized requests are blocked

---

## 🧪 Example API Requests

### Login

```
POST /login
```

```json
{
  "username": "user",
  "password": "password"
}
```

---

### Access Protected Endpoint

```
GET /users
Authorization: Bearer <TOKEN>
```

---

## 💥 BOLA Attack Demonstration

1. Login as normal user
2. Access:

```
GET /profile/2   (own data)
GET /profile/1   (other user data)
```

👉 If both succeed → **BOLA vulnerability confirmed**

---

## 🛡️ Secure Implementation

```
GET /secure/orders
```

✔ Ensures users can only access their own data
✔ Fixes BOLA vulnerability

---

## 📊 Sample Output

```
API SECURITY REPORT
==============================
Target: http://192.168.185.129:5000

Login: SUCCESS
BOLA: Accessed user 1
Rate Limit: Blocked at request 5
Auth: Protected endpoint secured

=== SUMMARY ===
BOLA: VULNERABLE
Rate Limiting: ENFORCED
Auth Protection: SECURE
```

---

## 🧠 Key Learnings

* API authentication vs authorization
* JWT token handling
* Common API vulnerabilities
* Automation in security testing
* Real-world pentesting workflow

---

## ⚠️ Disclaimer

This project is created for **educational and ethical testing purposes only**.
Do not use these techniques on unauthorized systems.

---

## 👨‍💻 Author

* Developed as part of API Security Testing Project
* Tools inspired by real-world penetration testing practices

---

## 🚀 Future Enhancements

* Add real OAuth (Google login)
* JWT attack simulations
* Multi-threaded scanning
* GUI-based dashboard
* PDF report generation
