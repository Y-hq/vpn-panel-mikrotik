# VPN Panel for Mikrotik

A lightweight and beginner‑friendly VPN user management panel for Mikrotik routers.  
This project provides a simple REST API to create, disable, and delete VPN users, with a clean backend architecture built using **Flask**, **PostgreSQL**, **Docker**, and **Nginx**.

---

## 🚀 Features

- Create VPN users  
- Disable VPN users  
- Delete VPN users  
- Store users in PostgreSQL  
- Ready-to-extend Mikrotik integration (currently simulated)  
- Fully Dockerized (backend + database + nginx)  
- Clean, modular, and easy-to-understand backend structure  

---

## 📂 Project Structure

```
vpn-panel-mikrotik/
├─ backend/
│  ├─ app.py
│  ├─ models.py
│  ├─ mikrotik_client.py
│  ├─ config.py
│  ├─ extensions.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  └─ __init__.py
├─ docker-compose.yml
├─ nginx.conf
├─ .env.example
└─ README.md
```

---

## 🛠 Requirements

To run this project, you only need:

- **Docker**
- **Docker Compose**
- A Mikrotik router (optional — not required for testing)

---

## ⚙️ Getting Started

Follow these steps to run the project on your machine.

---

### **1. Clone the repository**

```bash
git clone https://github.com/Y-hq/vpn-panel-mikrotik.git
cd vpn-panel-mikrotik
```

---

### **2. Create the `.env` file**

Copy the example environment file:

```bash
cp .env.example .env
```

Then open `.env` and fill in your Mikrotik information:

```env
MIKROTIK_HOST=192.168.88.1
MIKROTIK_PORT=8728
MIKROTIK_USER=admin
MIKROTIK_PASSWORD=your-password
```

If you don’t have a Mikrotik device, you can leave the defaults — the backend will still run.

---

### **3. Build and run the project with Docker**

```bash
docker-compose build
docker-compose up -d
```

This will start:

- **backend** → Flask API  
- **db** → PostgreSQL  
- **nginx** → Reverse proxy on port 80  

---

### **4. Health Check**

Open in your browser:

```
http://localhost/health
```

Expected output:

```json
{"status": "ok"}
```

---

## 📡 API Endpoints

### **1. List all users**

```
GET /api/users
```

---

### **2. Create a new user**

```
POST /api/users
Content-Type: application/json

{
  "username": "test",
  "password": "1234"
}
```

---

### **3. Disable a user**

```
POST /api/users/<id>/disable
```

---

### **4. Delete a user**

```
DELETE /api/users/<id>
```

---

## 🧩 Development Notes

### **Mikrotik Integration**
The file:

```
backend/mikrotik_client.py
```

contains placeholder methods (`create_vpn_user`, `disable_vpn_user`, `delete_vpn_user`).  
You can replace these with real RouterOS API calls using libraries such as:

- `routeros-api`
- `librouteros`

---

### **Run backend without Docker (optional)**

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Then open:

```
http://localhost:5000/health
```

---

## 📜 License

This project is open-source and free to use or modify.

---

## ❤️ Author

Created by **Y-hq**  
Feel free to open an issue if you want improvements or new features.
