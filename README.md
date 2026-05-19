# AKGEC Faculty Recruitment Form Backend

This is a production-grade Django backend for the AKGEC Faculty Recruitment Form.

## Prerequisites

- Python 3.8+
- MySQL Server

## Setup Instructions

Choose one of the setup methods below:

### Option A: Running with Docker (Recommended)

1. **Create the environment file:**
   Create a `.env` file in the project root folder. Example configuration:
   ```env
   # Django Settings
   DJANGO_SECRET_KEY=your_secure_secret_key
   DJANGO_DEBUG=False
   DJANGO_ALLOWED_HOSTS=*
   CSRF_TRUSTED_ORIGINS=http://localhost:8001,http://127.0.0.1:8001

   # Database Settings (Docker network config)
   DB_NAME=recruitment_db
   DB_USER=recruitment_user
   DB_PASSWORD=your_secure_password
   DB_ROOT_PASSWORD=your_root_password
   DB_HOST=db
   DB_PORT=3306
   ```

2. **Start the containers:**
   ```bash
   docker-compose up --build -d
   ```

3. **Run database migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Collect static files (required when DEBUG=False):**
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

5. **Create a superuser (for admin access):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

The application will be accessible at:
- Web App / API: `http://localhost:8001/`
- Admin Panel: `http://localhost:8001/admin/`

---

### Option B: Running Locally (Manual)

1. **Activate virtual environment:**
   ```powershell
   .\venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Database Configuration:**
   - Create a local MySQL database named `recruitment_db`.
   - Setup a local `.env` file or environment variables with your MySQL credentials (ensuring `DB_HOST` is set to `localhost` or `127.0.0.1`).
4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Collect Static Files:**
   ```bash
   python manage.py collectstatic --noinput
   ```
6. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the Server:**
   ```bash
   python manage.py runserver
   ```


## API Endpoints

- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Applications API:** `http://127.0.0.1:8000/api/applications/`
  - `GET`: List all applications.
  - `POST`: Submit a new application.
  - `GET <id>`: Retrieve a specific application.

## Form Sections Covered

- Section 1: Basic Details (including photograph upload)
- Section 2: Educational Qualifications (10th, 12th, Diploma, UG, PG, PhD)
- Section 3: Additional Qualifications (NET, GATE, Certifications)
- Section 4: Experience Details (Teaching, Industry, Research, Current & Previous Employment)
- Section 5: Research & Academic Contributions (Publications, Metrics, Patents, Projects, Consultancy, PhD Guidance)
- Section 6: Teaching Details
- Section 7: FDP / STTP / Workshops
- Section 8: Administrative & Professional
- Section 9: Statement Section
- Section 10: Institutional Suitability (Why AKGEC, Suitability Statement)
- Section 11: Document Uploads (CV, Certificates, Experience, Awards)
- Section 12: Declaration
- Section 13: Final Submission (handled via standard POST)
