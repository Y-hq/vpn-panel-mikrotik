```
  ███████╗ ██████╗ ██╗     
  ██╔════╝██╔═══██╗██║     
  ███████╗██║   ██║██║     
  ╚════██║██║   ██║██║     
  ███████║╚██████╔╝███████╗
  ╚══════╝ ╚═════╝ ╚══════╝
            S0L
```

[🇮🇷 Persian Version](README_FA.md)

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

You only need:

- **Docker**
- **Docker Compose**
- A Mikrotik router (optional — not required for testing)

---

## ⚙️ Getting Started

Follow these steps to run the project.

---

### **1. Clone the repository**

```bash
git clone https://github.com/Y-hq/vpn-panel-mikrotik.git
cd vpn-panel-mikrotik
```

---

### **2. Create the `.env` file**

```bash
cp .env.example .env
```

Then edit `.env`:

```env
MIKROTIK_HOST=192.168.88.1
MIKROTIK_PORT=8728
MIKROTIK_USER=admin
MIKROTIK_PASSWORD=your-password
```

---

### **3. Build and run with Docker**

```bash
docker-compose build
docker-compose up -d
```

Services started:

- backend (Flask API)  
- db (PostgreSQL)  
- nginx (reverse proxy on port 80)  

---

### **4. Health Check**

```
http://localhost/health
```

Expected:

```json
{"status": "ok"}
```

---

## 📡 API Endpoints

### List users
```
GET /api/users
```

### Create user
```
POST /api/users
{
  "username": "test",
  "password": "1234"
}
```

### Disable user
```
POST /api/users/<id>/disable
```

### Delete user
```
DELETE /api/users/<id>
```

---

## 🧩 Development Notes

### Mikrotik Integration
Edit:

```
backend/mikrotik_client.py
```

Replace placeholder methods with real RouterOS API calls if needed.

---

### Run backend without Docker (optional)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

## 📜 License

Open-source and free to modify.

---

## ❤️ Author

Created by **Y-hq**  
Feel free to open an issue for improvements.
