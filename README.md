# Flask_Web_Application_With_CI-CD_Project (Docker + Jenkins)

This is a simple Flask web application designed to demonstrate basic CI/CD workflows using Docker and Jenkins. The app exposes a few informational routes like name, email, and phone number.

---

## 🐍 Tech Stack

- Python 3
- Flask
- Docker
- Red Hat UBI 8 Base Image

---

## 📁 Project Structure

Flask_Web_Application_With_CI-CD_Project/

├── Dockerfile
├── app.py
└── README.md


---

## 🚀 How to Run This Project

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Flask_Web_Application_With_CI-CD_Project.git
cd Flask_Web_Application_With_CI-CD_Project

### 2. Build the Docker Image
bash
Copy
Edit
docker build -t tarunkohli/wordpress:01 .

3. Run the Docker Container
Make sure port 5000 is free before running:

bash
Copy
Edit
docker run -d -p 5000:5000 --name os1_new tarunkohli/wordpress:01
🌐 API Endpoints
Once the app is running, visit:

Endpoint	Description
/info	Returns origin location
/name	Returns developer name
/email	Returns developer email address
/phone	Returns developer phone number

Example:

bash
Copy
Edit
curl http://localhost:5000/info
# Output: I Am LW From India
⚠️ Notes
The container exposes port 5000. Ensure nothing else is using it.

If the container exits unexpectedly, check the logs using:

bash
Copy
Edit
docker logs os1_new
To remove a conflicting container:

bash
Copy
Edit
docker rm -f os1_new
📧 Author
Tarun Kohli
📧 Email: tarunkohli5555@gmail.com
📞 Phone: 7404650169
