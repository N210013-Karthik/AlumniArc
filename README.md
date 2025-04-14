# Alumni Arc

Alumni Arc is a Django-based web application designed to connect alumni with their alma mater and foster a strong alumni network.

## Features

- User authentication and profile management.
- Alumni directory with search and filter functionality.
- Event management and RSVP system.
- Job postings and career opportunities.
- Messaging system for alumni communication.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd alumni_arc
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://127.0.0.1:8000/`.

7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up a username, email, and password for the superuser.