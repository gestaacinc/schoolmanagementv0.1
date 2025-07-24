# Documentation: Frontend Setup (Vue.js)

This guide details the steps to set up the Vue.js frontend application using Vite and Docker.

---
## 1. Prepare Docker Configuration

1.  **Enable the `frontend` service:** Open your main `docker-compose.yml` file and uncomment the entire `frontend` section by removing the `#` symbols.

2.  **Create the `frontend` directory:** If it doesn't already exist, create the folder in your project's root.
    ```bash
    mkdir frontend
    ```
---
## 2. Initial Project Scaffolding

We will use a two-step process to create the project files, avoiding a common "chicken-and-egg" problem with Docker.

1.  **Create a Temporary Dockerfile:** The initial project creation requires a very simple Dockerfile. Create the file `frontend/Dockerfile` with `nano frontend/Dockerfile` and add only these two lines:
    ```dockerfile
    FROM node:20-alpine
    WORKDIR /app
    ```
    Save and exit (`Ctrl+X`, `Y`, `Enter`).

2.  **Run the Vite Scaffolding Command:** This command uses the temporary Dockerfile to run the Vite project creator.
    ```bash
    docker compose run --rm frontend npm create vite@latest . -- --template vue
    ```
    Answer the interactive questions in the terminal:
    * `✔ Add TypeScript?` › **No**
    * `✔ Add JSX Support?` › **No**
    * `✔ Add Vue Router for Single Page Application development?` › **Yes**
    * `✔ Add Pinia for state management?` › **Yes**
    * `✔ Add Vitest for Unit Testing?` › **No**
    * `✔ Add an ESLint rule for...?` › **Yes**
    * If asked about a non-empty directory, choose **`Ignore files and continue`**.

---
## 3. Finalize Frontend Configuration

1.  **Restore the Final Dockerfile:** Now that the project files exist, open `frontend/Dockerfile` again (`nano frontend/Dockerfile`) and replace its content with the final, complete version:
    ```dockerfile
    # Use an official Node runtime as the base image
    FROM node:20-alpine

    # Set the working directory in the container
    WORKDIR /app

    # Copy package.json and package-lock.json (or yarn.lock)
    COPY package*.json ./

    # Install application dependencies
    RUN npm install

    # Copy the rest of the application code
    COPY . .

    # Expose the port the app runs on
    EXPOSE 5173

    # Command to run the development server
    CMD ["npm", "run", "dev"]
    ```
    Save and exit.

2.  **Configure Vite for Docker:** Open `frontend/package.json` with `nano frontend/package.json`. Find the `"dev"` script and modify it to be accessible from outside the container.
    * **Change this:** `"dev": "vite"`
    * **To this:** `"dev": "vite --host 0.0.0.0"`
    Save and exit.

---
## 4. Install Dependencies and Run

1.  **Install Node Modules:** This command reads the new `package.json` file and installs all dependencies.
    ```bash
    docker compose run --rm frontend npm install
    ```
2.  **Start the Full Application:**
    ```bash
    docker compose up --build -d
    ```
3.  **Verify:** Check the status with `docker compose ps` and visit your running application in the browser at **`http://localhost:5173`**.