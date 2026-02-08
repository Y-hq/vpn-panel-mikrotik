```
  ███████╗ ██████╗ ██╗     
  ██╔════╝██╔═══██╗██║     
  ███████╗██║   ██║██║     
  ╚════██║██║   ██║██║     
  ███████║╚██████╔╝███████╗
  ╚══════╝ ╚═════╝ ╚══════╝
            S0L
```

[🇬🇧 English Version](README.md)

# پنل مدیریت VPN برای Mikrotik

یک پنل سبک، ساده و قابل‌فهم برای مدیریت کاربران VPN روی روترهای Mikrotik.  
این پروژه یک API ساده برای ساخت، غیرفعال‌سازی و حذف کاربران VPN ارائه می‌دهد و با **Flask**, **PostgreSQL**, **Docker**, و **Nginx** ساخته شده است.

---

## 🚀 امکانات

- ساخت کاربر VPN  
- غیرفعال کردن کاربر  
- حذف کاربر  
- ذخیره کاربران در PostgreSQL  
- آماده برای اتصال واقعی به Mikrotik (فعلاً شبیه‌سازی شده)  
- اجرای کامل با Docker  
- ساختار تمیز و قابل توسعه  

---

## 📂 ساختار پروژه

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

## 🛠 پیش‌نیازها

- Docker  
- Docker Compose  
- روتر Mikrotik (اختیاری)

---

## ⚙️ شروع کار

### **۱. کلون کردن ریپو**

```bash
git clone https://github.com/Y-hq/vpn-panel-mikrotik.git
cd vpn-panel-mikrotik
```

---

### **۲. ساخت فایل `.env`**

```bash
cp .env.example .env
```

سپس مقداردهی:

```env
MIKROTIK_HOST=192.168.88.1
MIKROTIK_PORT=8728
MIKROTIK_USER=admin
MIKROTIK_PASSWORD=your-password
```

---

### **۳. اجرای پروژه با Docker**

```bash
docker-compose build
docker-compose up -d
```

---

### **۴. تست سلامت**

```
http://localhost/health
```

خروجی مورد انتظار:

```json
{"status": "ok"}
```

---

## 📡 API ها

### لیست کاربران
```
GET /api/users
```

### ساخت کاربر
```
POST /api/users
{
  "username": "test",
  "password": "1234"
}
```

### غیرفعال کردن کاربر
```
POST /api/users/<id>/disable
```

### حذف کاربر
```
DELETE /api/users/<id>
```

---

## 🧩 نکات توسعه

### اتصال واقعی به Mikrotik  
در فایل زیر می‌توانید API واقعی RouterOS را اضافه کنید:

```
backend/mikrotik_client.py
```

---

### اجرای بدون Docker (اختیاری)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

## ❤️ سازنده

ساخته شده توسط **Y-hq**  
برای پیشنهاد یا توسعه، Issue باز کنید.
