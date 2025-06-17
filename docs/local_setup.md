# 🚀 Setting Up Your Python & Cursor Development Environment

- Welcome! This guide walks you through installing Python, Cursor, Visual Studio Code and scaffolding a brand-new Python project with best practices in place.
---

## 🎯 Learning Objectives

By the end of this lesson, you’ll be able to:

1. Install Python on macOS and Windows  
2. Install and launch an AI-powered code editor (Cursor or Visual Studio Code)
3. Scaffold a local Python project folder with:
   - a virtual environment  
   - Git initialization  
   - requirements pinning  
   - a clean `src/` layout  
   - essential config files  

## Understanding GUI vs. Terminal
**How to open:**

- **macOS Terminal**  
  - Click the **Spotlight** icon (🔍) in the top-right → type `Terminal` → press **Enter**  
  - Or open **Finder → Applications → Utilities → Terminal**

- **Windows PowerShell / Windows Terminal**  
  - Click **Start** → type `PowerShell` or `Windows Terminal` → press **Enter**  
  - To install software, right-click it and choose **Run as administrator**

---

## 📥 Prerequisites

**Git** (version control)
   Git is a distributed version-control system that tracks changes in your code and lets you collaborate safely. This step is only required if you plan to manage a backup of your code on [Github.com.](https://www.github.com). You can go there to create a free account.  

   See the [official GitHub Git Guide](https://github.com/git-guides/install-git) for installing Git on Windows and MacOS.
   <details>
   <summary>How to install Git</summary>

   **macOS (in Terminal):**
   ```bash
   # If you have Homebrew:
   brew install git

   # Otherwise, first install Homebrew:
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   brew install git
   ```
   Verify:
   ```bash
   git --version   # should print something like git version 2.x.x
```
**Windows (in PowerShell as Administrator)**

1. Open your web browser → go to https://github.com/git-guides/install-git
2.	Download and run the installer (keep default options)
3.	After install, open PowerShell (not plain “Command Prompt”) and run:

  ```powershell
   git --version   # should print git version 2.x.x
   ```
   </details>

**Administrator Rights**
- macOS: You may be prompted for your password when installing software.
- Windows: Right-click PowerShell/Terminal → Run as administrator for installs.

---
## ✅ Install Python

Check if Python is already installed
- macOS/Linux (Terminal):
```
python3 --version    # look for "Python 3.x.x"
```
- Windows (PowerShell):
```
python --version     # look for "Python 3.x.x"
```

If you see a 3.x version, you can skip straight to "Install Cursor". Otherwise, follow the installation steps below.

<details>
<summary>macOS (in Terminal)</summary>

1. Install Python 3 via Homebrew:
```bash
brew install python
```
2. Verify
```
python3 --version   # e.g. Python 3.11.x
```
</details>

<details>
<summary>Windows (in web browser & PowerShell)</summary>

1. In your web browser, go to https://python.org → Downloads → Windows  
2. Download the Windows installer (.exe) and run it.
    - Check “Add Python to PATH”
	- Click Install Now
3.	Open PowerShell (not Command Prompt) and verify:
```
python --version   # e.g. Python 3.11.x
```
</details>

## ✅ Install Cursor or Visual Studio Code
Cursor is an AI-powered code editor. These steps use your browser and the OS installer.   
Cursor is a fork of Visual Studio Code that also include AI-powered development with Github Copilot.   
You can download [VS Code](https://code.visualstudio.com/) for free and follow similar steps. 
<details>
<summary>macOS</summary>

1. Open your web browser → go to https://cursor.com
2.	Click Download for Mac
3.	Open the downloaded .dmg, drag the Cursor icon into Applications
4.	Launch Cursor from Launchpad
5. Navigate to "Marketplace" in the UI and install "Python extension for Visual Studio" from Microsoft.
</details>

<details>
<summary>Windows</summary>
	
1.	Open your web browser → go to https://cursor.so
2.	Click Download for Windows
3.	Run the downloaded .exe, follow prompts
4.	Launch Cursor from the Start menu
5. Navigate to "Marketplace" in the UI and install "Python extension for Visual Studio" from Microsoft.
</details>

Tip: Sign in or create a free Cursor account to unlock AI code completions.

## ✅ Scaffold Your Local Project Folder

From here on out, you’ll work in the Terminal (macOS) or PowerShell (Windows).

You can also create a project folder in macOS and Windows like you normally would.

**Step 1: Create your project folder**
```
mkdir my_project
cd my_project
```

**Step 2: Initialize Git (start version control)**
```
git init
```
- This creates a hidden .git/ folder.
- You’ll use Git commands (git add, git commit) to save snapshots.

**Step 3: Create a Python virtual environment**
- macOS
```
python3 -m venv .venv
source .venv/bin/activate
```
- Windows (Powershell)
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
If PowerShell complains:
```
File …\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```
Run **once**:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Confirm you’re inside the env
```
where python            # should point to …\.venv\Scripts\python.exe
python -m pip list      # shows packages inside the env
```

- What you see: Your prompt should change to (.venv).
- Why: Keeps this project’s packages isolated from your system.

**Step 4: Upgrade pip & install Python libraries**
This will install Python libaries requires to build code with OpenAI APIs and the OpenAI Agents SDK.
```
pip install --upgrade pip
pip install openai
pip install openai-agents
pip install requests
pip install python-dotenv
```

**Step 5: Save (“pin”) your dependencies**
```
pip freeze > requirements.txt
```
- Runs Python’s package manager (pip) and asks it to “freeze” all currently installed libraries in your active environment.Takes whatever pip freeze prints to the screen and writes it into the file named on the right.
- Outputs a list in requirement.txt like:
```
openai==1.76.2
openai-agents==0.0.14
pydantic==2.11.4
pydantic-settings==2.9.1
pydantic_core==2.33.2
python-dotenv==1.1.0
requests==2.32.3
```

**Step 6: Open the folder in Cursor**
- In Cursor or VS Code: File → Open Folder… → select my_project
- Cursor auto-detects .venv and uses the right Python interpreter.

## ✅ Add Recommended Best-Practice Files

> All commands below run in Terminal (macOS) or PowerShell (Windows).

Step 1: Navigate to your project folder ("my_project")

Step 2:	Create your source folder structure. This is where you will store your "source files" - the code you develop. You can create the folder from the command line below, or use explorer view in Cursor to create a folder under the my_project folder.
```
MacOS:
mkdir -p src/my_project

Windows PowerShell:
mkdir src\my_project
```

Step 3: Create an empty __init__.py  
This tells Python “this is a package”:
```
MacOS:
touch src/my_project/__init__.py

Windows PowerShell:
New-Item -Path src\my_project\__init__.py -ItemType File
```

Step 4: Create your docs & config files
```
MacOS:
touch README.md LICENSE

Windows PowerShell:
New-Item -Path README.md, LICENSE -ItemType File
```
Step 5: Open your editor (Cursor or VS Code) on this folder so you can edit those files.

Step 6: Add a .env file to the root folder in Cursor/VS Code. You can right-mouse click in the left explorer pane or click File > New File from the menu. Add your API keys to the .env file like:
```
OPENAI_API_KEY='sk-long-key-here'
```

Step 7: Initialize Git
```
git init
```
At this point your tree looks like:
```
my_project/
├── .gitignore
├── .git/               ← (auto)
├── .venv/              ← (auto)
├── requirements.txt    ← (you’ll generate this)
├── README.md           ← (you create/edit)
├── LICENSE             ← (you add license text)
└── src/
    └── my_project/
        └── __init__.py

```
On Windows:
```
C:\Users\you\projects\my_project\
├─ .gitignore
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ src\
│   └─ my_project\
│       └─ __init__.py
└─ .venv\
```

## ✅ Verify Your Setup

Step 1: click on the "src" folder in Cursor and create a new file "hello.py" with the following contents:
```
def main():
    print("✅ Your environment is ready!")

if __name__ == "__main__":
    main()
```

Step 2: run your script
```
python src/my_project/hello.py
```
You should see:
✅ Your environment is ready!

## 🤔 FAQ
- **What is .venv?**  
A folder containing a self-contained Python environment for this project only.
- **Why use Git?**  
To track changes, revert mistakes, and collaborate with others safely.
- **Can I choose different names?**  
Yes—if you rename .venv, update the activation command accordingly.

___