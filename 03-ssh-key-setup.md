# Documentation: GitHub SSH Key Setup

This guide explains how to set up SSH key authentication for GitHub. This method is more secure and convenient than using passwords or Personal Access Tokens over HTTPS, as you won't need to enter your credentials every time you push or pull.

---
## 1. Generate a New SSH Key

All commands should be run from your WSL/Ubuntu terminal.

1.  Run the `ssh-keygen` command. Replace the email address with the one associated with your GitHub account.
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
2.  When prompted, press **Enter** three times to accept the default file location and create a key without a passphrase.

---
## 2. Add the SSH Key to Your GitHub Account

1.  Display your new public SSH key by running this command:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
2.  **Copy the entire output** to your clipboard. It will be a single line of text starting with `ssh-ed25519...`.

3.  In your web browser, go to your GitHub SSH key settings:
    * **[https://github.com/settings/keys](https://github.com/settings/keys)**

4.  Click the **New SSH key** button.

5.  Give it a descriptive **Title** (e.g., `WSL Development Machine`).

6.  In the **Key** box, **paste** the public key you copied from your terminal.

7.  Click **Add SSH key**.

---
## 3. Configure Your Local Project to Use SSH

If your project is currently set up to use HTTPS, you must update its remote URL.

1.  Navigate to your project's root directory in your terminal.
2.  Remove the old HTTPS remote URL:
    ```bash
    git remote remove origin
    ```
3.  Add the new SSH remote URL (replace with your actual repository URL):
    ```bash
    git remote add origin git@github.com:gestaacinc/schoolmanagementv0.1.git
    ```

---
## 4. Test Your Connection

To test if everything is working, you can push a commit or use the `ssh` command. The first time you connect, you will see a host authenticity message.

```bash
# Attempt to authenticate with GitHub
ssh -T git@github.com