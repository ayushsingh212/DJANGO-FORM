# AKGEC Faculty Recruitment Form Backend

This is a production-grade Django backend for the AKGEC Faculty Recruitment Form.

## Prerequisites

- Python 3.8+
- MySQL Server

## Setup Instructions

1.  **Clone the repository and enter the directory.**
2.  **Activate the virtual environment:**
    ```powershell
    .\venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration:**
    - Create a MySQL database named `recruitment_db`.
    - Update `config/settings.py` with your MySQL `USER`, `PASSWORD`, `HOST`, and `PORT`.

5.  **Run Migrations:**
    ```bash
    python manage.py makemigrations recruitment
    python manage.py migrate
    ```

6.  **Create Superuser (for Admin access):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Server:**
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
