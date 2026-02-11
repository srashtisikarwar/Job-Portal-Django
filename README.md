# Job Portal Application

A Django-based Job Portal web application that allows employers to post jobs and candidates to apply for them.  
This project is built as part of learning Django and implementing real-world features.

---

## 🚀 Features

- User authentication (Employer & Candidate)
- Employer profile management
- Job posting and job listing
- Candidate job application
- Admin panel for managing data
- Responsive UI using HTML, CSS, Bootstrap

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (Development)  
- **Tools:** Git, GitHub, VS Code  

---

## 📂 Project Structure

Job_Portal/ # Django project folder
accounts/ # User accounts app
jobs/ # Jobs app
templates/ # HTML templates
static/ # CSS & static files
media/ # Uploaded files (ignored in Git)
manage.py
requirements.txt
screenshots/ # Screenshots folder

---


## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/srashtisikarwar/Job-Portal-Django.git
cd Job_Portal
```

2. **Create & activate virtual environment**

```bash
python -m venv myenv

# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the server**

```bash
python manage.py runserver
```

6. **Open in browser**

```
http://127.0.0.1:8000/
```


👩‍💻 Author
Srashti Sikarwar
Django Developer (Fresher)

GitHub: https://github.com/srashtisikarwar/Job-Portal-Django.git

⭐ Future Improvements
Role-based dashboards

Resume upload functionality

## 🖼️ Screenshots – Light Theme (Thumbnails)

| Home Page | Login Page | Register Page |
|-----------|------------|---------------|
| [<img src="screenshots/light_theme/home.png" width="150">](screenshots/light_theme/home.png) | [<img src="screenshots/light_theme/login.png" width="150">](screenshots/light_theme/login.png) | [<img src="screenshots/light_theme/register.png" width="150">](screenshots/light_theme/register.png) |

| Job Listings | Job Details | Apply Job |
|--------------|------------|-----------|
| [<img src="screenshots/light_theme/jobs.png" width="150">](screenshots/light_theme/jobs.png) | [<img src="screenshots/light_theme/jobs_details.png" width="150">](screenshots/light_theme/jobs_details.png) | [<img src="screenshots/light_theme/jobs_apply.png" width="150">](screenshots/light_theme/jobs_apply.png) |

| Candidate Dashboard | Employer Dashboard | Post Job |
|-------------------|-----------------|---------|
| [<img src="screenshots/light_theme/candidate_dashboard.png" width="150">](screenshots/light_theme/candidate_dashboard.png) | [<img src="screenshots/light_theme/employer_dashboard.png" width="150">](screenshots/light_theme/employer_dashboard.png) | [<img src="screenshots/light_theme/post_jobs.png" width="150">](screenshots/light_theme/post_jobs.png) |

| Admin Dashboard |  |  |
|----------------|--|--|
| [<img src="screenshots/light_theme/admin.png" width="150">](screenshots/light_theme/admin.png) |  |  |

---

## 🖼️ Screenshots – Dark Theme (Thumbnails)

| Home Page | Login Page | Register Page |
|-----------|------------|---------------|
| <img src="screenshots/dark_theme/home.png" width="150"> | <img src="screenshots/dark_theme/login.png" width="150"> | <img src="screenshots/dark_theme/register.png" width="150"> |

| Job Listings | Job Details | Apply Job |
|--------------|------------|-----------|
| <img src="screenshots/dark_theme/jobs.png" width="150"> | <img src="screenshots/dark_theme/job_details.png" width="150"> | <img src="screenshots/dark_theme/jobs_apply.png" width="150"> |

| Candidate Dashboard | Employer Dashboard | Post Job |
|-------------------|-----------------|---------|
| <img src="screenshots/dark_theme/candidate_dashboard.png" width="150"> | <img src="screenshots/dark_theme/employer_dashboard.png" width="150"> | <img src="screenshots/dark_theme/post_job.png" width="150"> |

| Loading Screen |  |  |
|----------------|--|--|
| <img src="screenshots/dark_theme/loading.png" width="150"> |  |  |
