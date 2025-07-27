# 📦 Flask_Web_Application_With_CI-CD_Project (Docker + Jenkins)

This project is a basic Flask web application containerized with Docker, intended to demonstrate core DevOps concepts including CI/CD integration, containerization, and endpoint testing.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Framework:** Flask
- **Containerization:** Docker
- **Base Image:** Red Hat UBI 8
- **Deployment Tool:** Jenkins (CI/CD)

---

## ⚙️ CI/CD Pipeline Overview

The project is configured for Continuous Integration and Continuous Deployment using **Jenkins**:

1. **Source Code Management:** GitHub
2. **Build Stage:** Docker image is built using `Dockerfile`.
3. **Test Stage:** (Optional) You can add unit tests using `pytest` or similar.
4. **Push to Registry:** Docker image is pushed to Docker Hub.
5. **Deployment:** Container is run on a Docker host with port `5000` exposed.

---

## ✅ Test Coverage

> 🔧 *Test coverage integration is currently a placeholder.*

To add tests:

1. Create a `tests/` directory.
2. Use `pytest` or `unittest` modules.
3. Optionally integrate with Jenkins using `pytest --junitxml=result.xml`.

---

## 🐳 Docker Details

### 📄 Dockerfile Summary

```Dockerfile
FROM redhat/ubi8
RUN yum install python3 -y
RUN pip3 install flask
COPY app.py /app.py
EXPOSE 5000
CMD [ "python3", "/app.py" ]
🏗️ Build Docker Image
bash
Copy
Edit
docker build -t tarunkohli/wordpress:01 .
🚀 Run Docker Container
bash
Copy
Edit
docker run -d -p 5000:5000 --name os1_new tarunkohli/wordpress:01
Ensure port 5000 is not already in use.

### **🌐 API Endpoints**
Route	Description	Sample Output
/info	Returns developer location	"I Am LW From India"
/name	Returns developer name	"My Name Is TARUN KOHLI"
/email	Returns developer email address	"My Email ID Is tarunkohli5555@gmail.com"
/phone	Returns developer phone number	"My Phone Number Is 7404650169"

Example:
bash
Copy
Edit
curl http://localhost:5000/info

## **📁 Project Structure**
bash
Copy
Edit
Flask_Web_Application_With_CI-CD_Project/
│
├── app.py          # Main Flask application
├── Dockerfile      # Docker configuration
├── README.md       # Project documentation
└── Jenkinsfile     # (Optional) Jenkins pipeline script

## **✍️ Author**
Tarun Kohli
📧 Email: tarunkohli5555@gmail.com
📞 Phone: 7404650169
🐙 GitHub: TarunKohli1362


