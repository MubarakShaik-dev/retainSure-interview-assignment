## ✅ Prerequisites

Before you begin, ensure you have the following software installed on your machine:

- **Visual Studio Code**: The code editor. [Download here](https://code.visualstudio.com/).
- **Git**: For cloning the repository. [Download here](https://git-scm.com/).
- **[Language Runtime, e.g., Node.js or Python 3.10+]**: The environment your code runs in. [Add download link].



1.  **Open VS Code**.

2.  **Open the Integrated Terminal**. You can do this by pressing `` `Ctrl` + `~` `` or by navigating to `View` > `Terminal` in the menu bar.

3.  **Clone the repository**. In the terminal, run the following command. Replace `[your-repository-url]` with the actual Git URL.
    ```bash
    git clone [your-repository-url]
    ```

4.  **Navigate into the project directory**.
    ```bash
    cd messy-migration
    ```

5.  **Open the project in VS Code**. This command opens the folder in your current VS Code window.
    ```bash
    code .
    ```
    > **Note:** A new VS Code window will open with the project loaded. You can close the old window. All subsequent commands should be run in the **new window's integrated terminal**.

6.  **Install dependencies**. This command will install all the necessary packages for the project to run.
    -  
    -   *For Python projects (using a virtual environment is recommended):*
        ```bash
        # Create a virtual environment
        python -m venv venv
        
        # Activate it
        # On Windows: .\venv\Scripts\activate
        # On macOS/Linux: source venv/bin/activate
        
        # Install packages from the requirements file
        pip install -r requirements.txt
        ```

---Run the start command directly in the VS Code integrated terminal.

python init_db.py

python app.py

### for test cases

pytest 