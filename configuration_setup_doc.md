# Configuration Setup Documentation

This document provides a complete, step-by-step guide for setting up the development environment and running the School Management System project on a Windows machine.

---
## 1. Windows Environment Setup (WSL)

This phase prepares your Windows machine with the necessary Linux environment. All commands should be run in **PowerShell as an Administrator**.

1.  **Install Core WSL Components:**
    ```powershell
    wsl --install --no-distribution
    ```
    **You must reboot your computer** after this step is complete.

2.  **Install Ubuntu via Command Line:**
    ```powershell
    wsl --install Ubuntu-24.04
    ```
3.  **Create Your User Account:** After the command finishes, a new terminal will open. Follow the prompts to create your Linux username and password.

---
## 2. Moving WSL to Drive D: (Optional)

To save space on your C: drive, follow these steps in **PowerShell (Admin)**.

1.  **Exit Ubuntu:** If you are inside the Ubuntu terminal, type `exit`.
2.  **Verify Installation:** Confirm WSL sees your new installation with `wsl --list --all`.
3.  **Create Folders on Drive D:**
    ```powershell
    mkdir D:\WSL; mkdir D:\WSL_Backup
    ```
4.  **Move the Installation:**
    ```powershell
    wsl --shutdown
    wsl --export Ubuntu-24.04 D:\WSL_Backup\ubuntu.tar
    wsl --unregister Ubuntu-24.04
    wsl --import Ubuntu-24.04 D:\WSL\Ubuntu D:\WSL_Backup\ubuntu.tar
    ```
5.  **Set Your Default User:** Launch Ubuntu from the Start Menu. You will be logged in as `root`. Run the following command, replacing `chester` with your actual username:
    ```bash
    echo -e "[user]\ndefault = chester" | sudo tee /etc/wsl.conf > /dev/null
    ```
6.  Type `exit` and then run `wsl --shutdown` in PowerShell to finalize the change.

---
## 3. Installing Developer Tools

1.  **Docker Desktop:** Download from the [official website](https://www.docker.com/products/docker-desktop/). After installing, go to **Settings > Resources > WSL Integration** and ensure the toggle for **`Ubuntu-24.04` is ON**.
2.  **VS Code:** Download from the [official website](https://code.visualstudio.com/) and install these extensions: `WSL`, `Python`, `Volar`, `Docker`.
3.  **Git:** Open your Ubuntu terminal and run `sudo apt update && sudo apt install git`.

---
## 4. Project & Docker Configuration

All commands from this point forward must be run from **inside your Ubuntu terminal**, within your project folder.

1.  **Clone & Navigate:**
    ```bash
    git clone git@github.com:gestaacinc/schoolmanagementv0.1.git school-management-system
    cd school-management-system
    ```
2.  **Create `.env` file:** Open a blank file named `.env.example` with `nano .env.example`, paste the content below, then save and exit (`Ctrl+X`, `Y`, `Enter`).
    ```ini
    # Django Settings
    SECRET_KEY=change-me-in-production-later
    DEBUG=True
    # Database Settings (for Docker)
    POSTGRES_DB=school_db
    POSTGRES_USER=school_user
    POSTGRES_PASSWORD=strongpassword
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```
    Then copy it: `cp .env.example .env`

3.  **Create `docker-compose.yml`:** Open the file with `nano docker-compose.yml`, paste the content below, then save and exit.
    ```yaml
    services:
      backend:
        build: ./backend
        command: python manage.py runserver 0.0.0.0:8000
        environment:
          - PYTHONPATH=/app
        volumes:
          - ./backend:/app
        ports:
          - "8000:8000"
        env_file:
          - ./.env
        depends_on:
          - db
      db:
        image: postgres:16-alpine
        volumes:
          - postgres_data:/var/lib/postgresql/data/
        environment:
          - POSTGRES_DB=${POSTGRES_DB}
          - POSTGRES_USER=${POSTGRES_USER}
          - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
        ports:
          - "5432:5432"
    volumes:
      postgres_data:
    ```
4.  **Create Backend Files:**
    ```bash
    mkdir backend
    nano backend/Dockerfile
    ```
    Paste the following into the Dockerfile, then save and exit:
    ```dockerfile
    FROM python:3.11-slim
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    WORKDIR /app
    COPY requirements.txt /app/
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . /app/
    ```
5.  **Create Python Dependencies File:**
    ```bash
    echo "Django~=5.0" > backend/requirements.txt
    echo "psycopg2-binary" >> backend/requirements.txt
    ```

---
## 5. Building and Initializing the Application

1.  **Build Docker Image:**
    ```bash
    docker compose build
    ```
2.  **Create the Django Project Files:**
    ```bash
    docker compose run --rm backend django-admin startproject school_project .
    ```
3.  **Fix File Permissions:**
    ```bash
    sudo chown -R $USER:$USER backend
    ```
4.  **Configure Django `settings.py`:**
    * Open the settings file: `nano backend/school_project/settings.py`
    * Add `import os` to the very top of the file.
    * Find the `DATABASES` section and replace the entire block with this:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ.get('POSTGRES_DB'),
                'USER': os.environ.get('POSTGRES_USER'),
                'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }
        ```
    * Save and exit (`Ctrl+X`, `Y`, `Enter`).

---
## 6. Final Setup and Execution

1.  **Start Services:**
    ```bash
    docker compose up -d
    ```
2.  **Verify Containers are Running:** Check that `backend` and `db` are both "running".
    ```bash
    docker compose ps
    ```
3.  **Run Database Migrations:**
    ```bash
    docker compose exec backend python manage.py migrate
    ```
4.  **Create Admin Superuser:** Follow the prompts.
    ```bash
    docker compose exec backend python manage.py createsuperuser
    ```
5.  **Access the Application:** Your backend is now running.
    * **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)