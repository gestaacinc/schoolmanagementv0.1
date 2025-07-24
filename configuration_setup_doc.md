# Configuration Setup Documentation

This document provides a complete, step-by-step guide for setting up the development environment and running the School Management System project on a Windows machine.

---
## 1. Windows Environment Setup (WSL)

This phase prepares your Windows machine with the necessary Linux environment. All commands should be run in **PowerShell as an Administrator**.

1.  **Install Core WSL Components:** This prepares your system for WSL.
    ```powershell
    wsl --install --no-distribution
    ```
    **You must reboot your computer** after this step is complete.

2.  **Install Ubuntu via Command Line:** This is the most reliable method.
    ```powershell
    wsl --install Ubuntu-24.04
    ```
3.  **Create Your User Account:** After the command finishes, a new terminal will open. Follow the prompts to create your Linux username and password. **Note:** You will not see characters as you type your password. This is normal.

---
## 2. Moving WSL to Drive D: (Optional)

To save space on your C: drive, follow these steps in **PowerShell (Admin)**.

1.  **Exit Ubuntu:** If you are inside the Ubuntu terminal, type `exit` and press Enter.
2.  **Verify Installation:** Confirm WSL sees your new installation.
    ```powershell
    wsl --list --all
    ```
3.  **Create Folders on Drive D:**
    ```powershell
    mkdir D:\WSL
    mkdir D:\WSL_Backup
    ```
4.  **Move the Installation:** Run these commands one by one to move the system.
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

1.  **VS Code:** Download from the [official website](https://code.visualstudio.com/) and install these extensions: `WSL`, `Python`, `Volar`, `Docker`, `Prettier - Code formatter`.
2.  **Docker Desktop:** Download from the [official website](https://www.docker.com/products/docker-desktop/) and ensure it's configured to use the WSL 2 backend in its settings.
3.  **Git:** Open your Ubuntu terminal (by typing `wsl` in PowerShell) and run `sudo apt update && sudo apt install git`.

---
## 4. Project Setup

All commands from this point forward must be run from **inside your Ubuntu terminal**.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/gestaacinc/schoolmanagementv0.1.git](https://github.com/gestaacinc/schoolmanagementv0.1.git) school-management-system
    ```
2.  **Navigate into the Project Directory:**
    ```bash
    cd school-management-system
    ```
3.  **Create the Environment File Template:** This file might not exist in the repo, so create it.
    ```bash
    cat << EOF > .env.example
    # Django Settings
    SECRET_KEY=change-me-in-production-later
    DEBUG=True

    # Database Settings (for Docker)
    POSTGRES_DB=school_db
    POSTGRES_USER=school_user
    POSTGRES_PASSWORD=strongpassword
    DATABASE_HOST=db
    DATABASE_PORT=5432
    EOF
    ```
4.  **Create Your Local Environment File:**
    ```bash
    cp .env.example .env
    ```

---
## 5. Running the Application

1.  **Start Docker Services:** This command builds and starts the database and backend services.
    ```bash
    docker-compose up -d --build
    ```
2.  **Run Database Migrations:** This sets up the project's tables in the database.
    ```bash
    docker-compose exec backend python manage.py migrate
    ```
3.  **Create an Admin Superuser:** This creates your account for the admin panel. Follow the prompts.
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```
4.  **Run Development Servers:** You need two terminals for this.
    * **Terminal 1 (Backend):**
        ```bash
        docker-compose exec backend python manage.py runserver 0.0.0.0:8000
        ```
    * **Terminal 2 (Frontend):**
        ```bash
        docker-compose exec frontend npm install
        docker-compose exec frontend npm run dev
        ```
5.  **Access the Application:**
    * **Frontend:** [http://localhost:5173](http://localhost:5173)
    * **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)