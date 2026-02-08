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

# Mikrotik VPN Panel

A lightweight, modern, and fully‑containerized VPN user management panel for **Mikrotik routers**.

This version is built using:

- **Backend:** Node.js + Express  
- **Frontend:** React + TailwindCSS  
- **Database:** PostgreSQL  
- **Reverse Proxy:** Nginx  
- **Deployment:** Docker Compose  

The panel provides a clean REST API and a simple UI for managing VPN users.

---

## 🚀 Features

- Add VPN users  
- Disable / Enable VPN users  
- Delete VPN users  
- Store users in PostgreSQL  
- Fully Dockerized (frontend + backend + db + nginx)  
- Clean and modular backend structure  
- Modern React UI  

---

## 📂 Project Structure

```
vpn-panel-mikrotik/
├─ backend/
│  ├─ src/
│  │  ├─ app.js
│  │  ├─ routes.js
│  │  ├─ db.js
│  │  └─ controllers/
│  ├─ package.json
│  ├─ Dockerfile
│  └─ .env.example
│
├─ frontend/
│  ├─ public/
│  │  └─ index.html
│  ├─ src/
│  │  ├─ App.js
│  │  ├─ Users.jsx
│  │  ├─ index.js
│  │  └─ index.css
│  ├─ package.json
│  └─ Dockerfile
│
├─ nginx.conf
├─ docker-compose.yml
└─ README.md
```

---

## 🛠 Requirements

You only need:

- **Docker**
- **Docker Compose**
- A Mikrotik router (optional — backend works without it)

---

## ⚙️ Getting Started

### **1. Clone the repository**

```bash
git clone https://github.com/Y-hq/vpn-panel-mikrotik.git
cd vpn-panel-mikrotik
```

---

### **2. Create the backend `.env` file**

```bash
cp backend/.env.example backend/.env
```

Edit it:

```env
DB_HOST=db
DB_USER=vpn_user
DB_PASSWORD=vpn_pass
DB_NAME=vpn_db
```

---

### **3. Build and run with Docker**

```bash
docker-compose up --build
```

Services started:

- **frontend** → React app on port **3000**  
- **backend** → Express API behind Nginx  
- **db** → PostgreSQL  
- **nginx** → reverse proxy on port **80**  

---

### **4. Access the panel**

Frontend:

```
http://localhost:3000
```

Backend API (via Nginx):

```
http://localhost/api/users
```

---

## 📡 API Endpoints

### Get all users
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
PATCH /api/users/:id/disable
```

### Enable user
```
PATCH /api/users/:id/enable
```

### Delete user
```
DELETE /api/users/:id
```

---

## 🧩 Development Notes

### Mikrotik Integration
You can extend real RouterOS API support inside:

```
backend/src/controllers/mikrotik.js
```

---

### Run backend without Docker (optional)

```bash
cd backend
npm install
npm start
```

---

## 📜 License

Open‑source and free to modify.

---

## ❤️ Author

Created by **Y-hq**  
Feel free to open an issue or contribute.
