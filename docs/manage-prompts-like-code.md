# Systematically Manage Your Prompts Like Code

> **A comprehensive guide for leaders and professionals to organize, version, and share AI prompts using professional development tools**

By James Gray | [JamesGray.AI](https://jamesgray.ai) | [Hands-on AI for Leaders Course](https://handsonai.info)

> 📎 **Optional Resource**: This tutorial was adapted from a comprehensive presentation. <a href="https://docs.google.com/presentation/d/1bcRtVw8X3hotEJYovJe3IzyL7Ap5NY6fMoWAR5TXllg/edit?usp=sharing" target="_blank">View the slide deck</a> for a visual walkthrough of these concepts.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Why Manage Prompts Like Code?](#why-manage-prompts-like-code)
3. [Core Concepts](#core-concepts)
4. [Setting Up Your Environment](#setting-up-your-environment)
5. [Creating Your Prompt Repository](#creating-your-prompt-repository)
6. [Working with Markdown Prompts](#working-with-markdown-prompts)
7. [Integrating with AI Platforms](#integrating-with-ai-platforms)
8. [Version Control and Collaboration](#version-control-and-collaboration)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## 🚀 Introduction

Your prompts are competitive moats and intellectual property. As a leader working with AI, you've likely accumulated dozens—perhaps hundreds—of effective prompts scattered across chat windows, documents, and notes. This guide shows you how to transform that ad-hoc collection into a systematic, professional prompt management system using the same tools software developers use to manage code.

### 🎯 What You'll Learn

By the end of this guide, you will:

- **Design and implement** a personal prompt management system that increases your AI workflow efficiency
- **Use Markdown** to enhance AI prompt clarity with well-structured formatting
- **Establish cloud backup** with automated synchronization for your prompt library
- **Manage prompts with GitHub** for version control, change tracking, and team sharing
- **Integrate your prompts** seamlessly across multiple AI platforms (Claude, ChatGPT, Gemini)

### Who This Guide Is For

This tutorial is designed for **professionals and leaders** who:
- Work regularly with AI assistants but lack coding experience
- Want to organize and reuse their best prompts systematically
- Need to share prompts across teams or organizations
- Seek a professional approach to managing their AI intellectual property
- Are comfortable learning new tools with step-by-step guidance

**No coding experience required.** We'll walk through everything step by step.

---

## 💡 Why Manage Prompts Like Code?

### ❌ The Problem with Ad-Hoc Prompt Management

Most professionals manage their prompts informally:
- Scattered across multiple chat windows
- Saved in random documents or notes
- Lost when chat history is deleted
- Impossible to find when needed
- No way to track what works and what doesn't
- Can't easily share with team members

### ✅ The Solution: Treat Prompts as Source Code

Software developers have spent decades perfecting systems to manage, version, and collaborate on code. These same systems work brilliantly for AI prompts.

### 🔑 Four Key Benefits

#### 1. Version Control & Traceability

Just like code, prompts evolve. With version control, you can:
- Track what worked, when, and why
- See the history of iterations for any prompt
- Roll back to previous versions if needed
- Understand which changes improved results

**Example:** You tweak a prompt for generating board updates. GitHub records both versions, so you can see whether version A or B produced clearer output.

#### 2. Reusability & Standardization

A well-written prompt is a valuable asset. By storing prompts in repositories:
- Reuse proven prompts across projects
- Share standardized prompts across teams
- Maintain consistency in AI-generated outputs
- Build a library of organizational knowledge

**Example:** A "Quarterly Business Review Drafting Prompt" can be standardized for all directors, ensuring consistent update formats regardless of who writes them.

#### 3. Collaboration & Peer Review

Prompts can be reviewed and improved like code:
- Team members can suggest improvements
- Best practices emerge through collaboration
- Avoid reinventing the wheel
- Build on colleagues' expertise

**Example:** A marketing VP and product VP co-develop a "Go-to-Market Playbook Prompt," ensuring it works for both product specs and press releases.

#### 4. Scalability Across Tools

Your prompts aren't locked to one AI platform:
- Markdown + GitHub = portable prompts
- Use the same prompt in ChatGPT, Claude, or Gemini
- Import into internal copilots or custom tools
- Future-proof your prompt library

**Example:** A company-wide "Customer Objection Handling Prompt" can run in Microsoft Teams Copilot, Claude, or a custom helpdesk bot.

### Your Prompts Are Strategic Assets

Systematic prompt management transforms ad-hoc AI use into strategic intellectual property. **Prompts managed as source code become productivity multipliers** that save hours weekly, ensure consistent quality, and scale instantly across teams—turning accumulated AI expertise into sustainable business advantage.

---

## Core Concepts

Before diving into the setup process, let's understand the key concepts and tools you'll be using.

### What Is "Managing Prompts Like Code"?

Managing prompts like code means applying software development best practices to AI prompt workflows:

1. **Version Control & History**
   - Track prompt iterations with Git
   - See what changed and when
   - Roll back to previous versions
   - Understand evolution over time

2. **Structured Organization**
   - Store prompts as Markdown files
   - Organize by function, team, or use case
   - Enable easy search and reuse
   - Maintain clear file structures

3. **Collaborative Development**
   - Share prompt repositories across teams
   - Enable peer review and standardization
   - Build institutional AI knowledge
   - Learn from collective experience

4. **Cross-Platform Portability**
   - Write once, use everywhere (Claude, ChatGPT, Gemini)
   - Import seamlessly into any AI platform
   - No vendor lock-in
   - Future-proof your investment

### Key Tools Overview

**Markdown (*.md files)**
- Plain text format with simple formatting
- AI models parse it excellently
- Human-readable and editable
- Universal compatibility

**Git**
- Version control software
- Tracks all changes to your files
- Enables collaboration
- Industry-standard tool

**GitHub**
- Cloud platform for Git repositories
- Backs up your files automatically
- Enables sharing and collaboration
- Integrates with AI platforms

**AI Code Editors (Cursor or VS Code)**
- Professional text editors
- Built-in AI assistance
- Git integration
- Enhanced productivity features

**Claude Code / Codex**
- AI assistants integrated into your editor
- Can reference your GitHub prompts
- Provide contextual help
- Streamline your workflow

### The Workflow at a Glance

```
Create Prompt → Save as Markdown → Commit to Git → Push to GitHub
                                                          ↓
                                      ← Use in Claude/ChatGPT/etc.
```

Your local folder on your machine is your **master prompt library**. It syncs to:
- **GitHub** (version control with change history)
- **Google Drive / OneDrive** (simple file backup)
- **AI Platforms** (Claude, ChatGPT) via integrations

---

## 🛠️ Setting Up Your Environment

Let's set up all the tools you need. Follow these steps carefully, and you'll have everything configured in about 30-45 minutes.

### ✅ Step 1: Install an AI Code Editor

You'll need a modern code editor with AI capabilities. Choose one:

#### Option A: Cursor (Recommended for Beginners)
- **Website:** [cursor.com](https://cursor.com)
- **Cost:** Free with upgrade options
- **Best for:** Those new to code editors, includes built-in AI

**Installation Steps:**

**macOS:**
1. Open your web browser and go to https://cursor.com
2. Click "Download for Mac"
3. Open the downloaded .dmg file
4. Drag the Cursor icon into your Applications folder
5. Launch Cursor from Launchpad or Applications
6. Navigate to Extensions (left sidebar) and search for "Python extension for Visual Studio Code"
7. Install the Python extension from Microsoft

**Windows:**
1. Open your web browser and go to https://cursor.com
2. Click "Download for Windows"
3. Run the downloaded .exe file and follow the installation prompts
4. Launch Cursor from the Start menu
5. Navigate to Extensions (left sidebar) and search for "Python extension for Visual Studio Code"
6. Install the Python extension from Microsoft

#### Option B: Visual Studio Code
- **Website:** [code.visualstudio.com](https://code.visualstudio.com)
- **Cost:** Free
- **Best for:** Those comfortable with more technical tools

**Installation:** Download from the website and follow standard installation procedures for your operating system.

**💡 Pro Tip:** Both editors are free and work similarly. Cursor is designed specifically for AI-assisted coding, which may be more intuitive for beginners.

---

### ✅ Step 2: Install Git

Git is version control software that tracks changes to your files.

**Check if Git is already installed:**

1. Open your terminal (command prompt):
   - **macOS:** Press `Cmd + Space`, type "Terminal", press Enter
   - **Windows:** Press `Windows key`, type "PowerShell", press Enter

2. Type this command and press Enter:
   ```bash
   git --version
   ```

3. If you see a version number (like `git version 2.39.0`), Git is already installed. **Skip to Step 3.**

**Install Git if needed:**

**macOS:**
```bash
brew install git
```
(If you don't have Homebrew, download Git from https://git-scm.com/downloads)

**Windows:**
1. Go to https://git-scm.com/downloads
2. Download the Windows installer
3. Run the installer with default settings
4. Verify installation by opening PowerShell and typing `git --version`

---

### ✅ Step 3: Create a GitHub Account

GitHub is where you'll store your prompts in the cloud with version control.

**Steps:**

1. Go to https://github.com
2. Click "Sign up" in the top-right corner
3. Follow the prompts to create your free account:
   - Enter your email address
   - Create a password
   - Choose a username (this will be public)
   - Verify you're human
   - Check your email for verification

4. Once logged in, you'll see your GitHub dashboard

**💡 Pro Tip:** Choose a professional username—you may share repositories with colleagues or clients.

---

### ✅ Step 4: Configure Your Git Identity

Git needs to know who you are for tracking changes.

**Steps:**

1. Open your terminal (Terminal on macOS, PowerShell on Windows)

2. Set your name (replace "Your Name" with your actual name):
   ```bash
   git config --global user.name "Your Name"
   ```

3. Set your email (use the same email as your GitHub account):
   ```bash
   git config --global user.email "you@example.com"
   ```

4. Verify your configuration:
   ```bash
   git config --list
   ```

You should see your name and email in the output.

---

### 🔑 Step 5: Create a GitHub Personal Access Token (PAT)

GitHub requires a Personal Access Token (PAT) instead of your password when pushing or pulling via HTTPS.

**⚠️ Why you need this:** Without a PAT, GitHub will block authentication when you try to sync your files.

**Steps:**

1. **Go to GitHub Settings:**
   - Sign in to GitHub
   - Click your avatar (top right) → **Settings**
   - Scroll down the left menu → **Developer settings**
   - Click **Personal access tokens** → **Tokens (classic)**

2. **Generate a new token:**
   - Click **Generate new token (classic)**
   - Give it a descriptive name (e.g., "Cursor Prompt Management Token")
   - Choose an expiration:
     - **30 days** (recommended for testing)
     - **90 days** (for regular use)
     - **No expiration** (use with caution)

3. **Select scopes (permissions):**
   - Check the **repo** box (gives full control of private and public repos)
   - Optionally check **workflow** if you plan to use GitHub Actions later
   - Leave other boxes unchecked for now

4. **Save the token:**
   - Scroll down and click **Generate token**
   - **GitHub shows the token only once**—copy it immediately
   - **Save it in a password manager** (1Password, Bitwarden, LastPass, etc.)
   - You'll need this token later when pushing files to GitHub

**⚠️ Important:** Treat this token like a password. Anyone with this token can access your repositories.

---

## 📦 Creating Your Prompt Repository

Now that your tools are installed, let's create your first prompt repository.

### ✅ Step 6: Create a GitHub Repository

A repository (or "repo") is like a project folder that lives on GitHub.

**Steps:**

1. **Navigate to GitHub:**
   - Go to https://github.com and sign in
   - Click your profile picture (top right)
   - Click **Your repositories**

2. **Create a new repository:**
   - Click the green **New** button
   - You'll see the "Create a new repository" form

3. **Configure your repository:**

   **Repository name:**
   - Enter a name with no spaces (use dashes if needed)
   - Example: `my-ai-prompts`, `prompt-library`, or `leadership-prompts`

   **Description (optional):**
   - Add a brief description like "My personal AI prompt library"

   **Visibility:**
   - **Private**: Only you can see it (recommended to start)
   - **Public**: Anyone can see it (use if you want to share publicly)

   **Initialize repository:**
   - ✅ Check "Add a README file"
   - If you'll store Python code later, set .gitignore to "Python"
   - Leave License as "No license" for now

4. **Create the repository:**
   - Click the green **Create repository** button
   - You'll see your new repository page

**🎉 Congratulations!** Your repository is now live on GitHub.

---

### ✅ Step 7: Clone the Repository to Your Local Machine

"Cloning" creates a local copy of your GitHub repository on your computer so you can work with files directly.

**Steps:**

1. **Get the repository URL:**
   - On your repository's GitHub page, click the green **Code** button
   - Make sure "HTTPS" is selected (not SSH)
   - Click the copy icon to copy the repository URL
   - It looks like: `https://github.com/your-username/your-repo-name.git`

2. **Choose a parent directory:**
   - Decide where you want your prompt library to be stored
   - The clone operation will create a folder with your repository name in this location
   - Recommended locations: `Documents`, `Projects`, or `AI-Projects` folder in your user directory
   - Example: If you clone to `Documents`, Git will create `Documents/your-repo-name/`

3. **Clone using your code editor (Cursor/VS Code):**

   **In Cursor:**
   - Open Cursor
   - Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows) to open Command Palette
   - Type "Git: Clone" and select it
   - Paste your repository URL
   - Choose the folder where you want to save it
   - When prompted, choose **Open** to open the cloned repository

   **You may be prompted to authenticate:**
   - Enter your GitHub username
   - For the password, **paste your Personal Access Token** (from Step 5)
   - Check "Remember my credentials" if offered

4. **Verify the clone:**
   - You should now see your repository files in the editor's file explorer (left sidebar)
   - You should see at least a `README.md` file
   - At the bottom of the editor, you'll see the branch name (usually "main")

**What just happened?** You now have a synchronized copy of your GitHub repository on your local machine. Changes you make locally can be "pushed" to GitHub, and changes on GitHub can be "pulled" to your local machine.

---

### ✅ Step 8: Verify Your Setup

Let's make sure Git is working correctly in your project.

**Steps:**

1. **Open the terminal in your code editor:**
   - **Cursor/VS Code:** Menu → Terminal → New Terminal
   - A terminal panel will appear at the bottom of your editor

2. **Check Git status:**
   - In the terminal, type:
     ```bash
     git status
     ```
   - Press Enter

3. **Expected output:**
   ```
   On branch main
   Your branch is up to date with 'origin/main'.

   nothing to commit, working tree clean
   ```

   This means:
   - You're on the "main" branch
   - Everything is synchronized with GitHub
   - No uncommitted changes

**If you see errors:** Make sure you're in the correct directory. The terminal should show the path to your cloned repository.

---

## 📝 Working with Markdown Prompts

Now let's create and manage actual prompts using Markdown.

### 💡 Why Markdown for Prompts?

**Markdown** is a simple text format that AI models understand exceptionally well. [Learn more about Markdown syntax →](https://www.markdownguide.org/basic-syntax/)

✅ **Maintains semantic structure natively**
- Headers, lists, and formatting are preserved as intended
- Hierarchical structure (H1, H2, etc.) remains clear
- AI models parse it without conversion overhead

✅ **Plain text with explicit markup**
- What you see is exactly what the AI receives
- No conversion artifacts or unexpected changes
- Immediately readable without processing

✅ **Superior to Google Docs**
- Google Docs undergo format conversion that can introduce parsing errors
- Markdown has no latency or potential failure points
- The semantic markup provides clear structural cues to AI

### Basic Markdown Syntax

Here's what you need to know:

```markdown
# Heading 1 (use for main title)
## Heading 2 (use for sections)
### Heading 3 (use for subsections)

**Bold text** for emphasis
*Italic text* for slight emphasis

- Bullet point
- Another bullet point

1. Numbered item
2. Another numbered item

[Link text](https://example.com)

> Quote or callout box

`inline code` or inline variable

```
code block
```
```

### Prompt Structure Example

Here's a well-structured prompt in Markdown:

```markdown
# Role & Expertise

You are a senior marketing strategist with 15+ years of experience creating audience-specific style guides.

# Task

Create a comprehensive audience style guide in markdown format that enables consistent communication.

# Required Inputs

You will be provided with:
- Target audience demographics and psychographics
- Business context and goals
- Brand positioning (if available)
- Communication objectives

# Style Guide Structure

Your output must include these sections:

## 1. Audience Profile Summary
- Key demographics and psychographics
- Pain points and motivations
- Communication preferences
- Trust factors and credibility signals

## 2. Voice & Tone Guidelines
- Primary voice characteristics (3-5 key attributes)
- Tone variations for different contexts
- Words to use vs. words to avoid

## 3. Communication Framework
- Key messaging pillars
- Content structure preferences
- Examples of effective communication

# Output Format

Provide the style guide as a well-formatted markdown document ready for immediate use.
```

**Why this structure works:**
- Clear headings guide the AI
- Explicit requirements leave no ambiguity
- Well-organized sections make it reusable
- Markdown formatting is preserved perfectly

---

### ✅ Step 9: Create Your First Prompt

Let's create a prompt file and save it to your repository.

**Steps:**

1. **Create a new file:**
   - In Cursor/VS Code, right-click in the file explorer (left sidebar)
   - Select **New File**
   - Name it with a `.md` extension (e.g., `audience-style-guide-creator.md`)

2. **Write your prompt:**
   - Type or paste your prompt content
   - Use Markdown formatting (headings, lists, bold, etc.)
   - Save the file (`Cmd+S` on macOS, `Ctrl+S` on Windows)

3. **Alternative - Import from Claude:**
   - If you've already created a good prompt in Claude, click the **Download as Markdown** button
   - Drag the downloaded file into your editor's file explorer

4. **Alternative - Use AI to author your prompt:**
   - If you have Claude Code, Cursor Agent, or Codex installed in your editor
   - Create a new `.md` file
   - Open the AI chat panel (Claude Code: `Cmd+L` / `Ctrl+L`, Cursor: `Cmd+K` / `Ctrl+K`, or Codex: click the icon)
   - Describe your intent in plain language:
     - Example: "Create a prompt that helps me write professional emails with different tones"
     - Example: "Build a prompt for analyzing business strategies and identifying gaps"
   - The AI will generate a well-structured Markdown prompt for you
   - Review and refine the generated prompt
   - Save to your file

**Example starter prompts to create:**
- `prompt-improver.md` - Analyzes and improves your prompts
- `meeting-notes-summarizer.md` - Converts meeting notes to action items
- `email-drafter.md` - Drafts professional emails
- `strategy-analyzer.md` - Analyzes business strategies

---

### ✅ Step 10: Push Your Prompt to GitHub

Now let's sync your local changes to GitHub.

#### Option A: Use AI Assistant (Easiest for Beginners)

If you have Claude Code, Cursor Agent, or Codex installed, they can handle the git operations for you:

**Steps:**

1. **Save your new prompt file** (`Cmd+S` / `Ctrl+S`)

2. **Open your AI assistant:**
   - Claude Code: `Cmd+L` / `Ctrl+L`
   - Cursor: `Cmd+K` / `Ctrl+K` or click the chat icon
   - Codex: Click the Codex icon

3. **Ask the AI to commit and push your changes:**
   - Example: "Please commit my new prompt file to git with a descriptive message and push it to GitHub"
   - Example: "Add my audience-style-guide-creator.md file to git and sync it to GitHub"
   - Example: "Commit the changes I made and push them to my remote repository"

4. **Review what the AI does:**
   - The AI will stage your file
   - Create a commit with an appropriate message
   - Push to GitHub
   - You'll see the git commands it runs in the output

5. **Verify on GitHub:**
   - Go to your repository on GitHub.com
   - Refresh the page
   - Your new file should appear

**💡 Pro Tip:** This is often the fastest and least error-prone method, especially when you're starting out. The AI handles all the git commands for you.

---

#### Option B: Manual Method (Good to Understand)

If you prefer to understand the process or don't have an AI assistant installed:

**Steps:**

1. **Stage your changes:**
   - Look at the left sidebar in your editor
   - You'll see a Source Control icon (looks like a branch) with a number badge
   - Click the Source Control icon
   - You'll see your new file listed under "Changes"
   - Click the **+** icon next to the file to "stage" it

2. **Commit your changes:**
   - At the top of the Source Control panel, you'll see a text box labeled "Message"
   - Enter a brief commit message describing your change:
     - Good: "Add audience style guide creator prompt"
     - Bad: "update" or "changes"
   - Click the **✓ Commit** button (or press `Cmd+Enter` / `Ctrl+Enter`)

3. **Push to GitHub:**
   - Click the **Sync Changes** button (it may have an up arrow)
   - If prompted for credentials:
     - Username: Your GitHub username
     - Password: **Paste your Personal Access Token** (not your GitHub password)
   - Wait for the sync to complete (you'll see a success notification)

4. **Verify on GitHub:**
   - Go to your repository on GitHub.com
   - Refresh the page
   - You should see your new file listed!
   - Click on it to view the contents

**What just happened?** You've successfully saved a version of your prompt to GitHub with a message describing the change. This is now part of your prompt library's history.

---

## 🔗 Integrating with AI Platforms

Now let's connect your GitHub prompt repository to Claude and ChatGPT so you can use your prompts seamlessly.

### ✅ Step 11: Connect Claude to GitHub

Claude can read files directly from your GitHub repositories.

**Steps:**

1. **Open Claude Settings:**
   - Go to https://claude.ai and sign in
   - Click your profile picture (bottom left)
   - Select **Settings**

2. **Navigate to Connectors:**
   - In settings, click **Connectors** in the left menu
   - You'll see a list of available integrations

3. **Connect GitHub:**
   - Find **GitHub** in the list
   - Click **Connect** or **Configure**
   - You'll be redirected to GitHub to authorize the connection

4. **Authorize Claude:**
   - Review the permissions Claude is requesting
   - Click **Authorize Claude**
   - You'll be redirected back to Claude

5. **Configure Repository Access:**
   - Go to your GitHub Settings (github.com → Settings)
   - Navigate to **Applications** in the left menu
   - Find **Claude for GitHub**
   - Click **Configure**
   - Under "Repository access", select:
     - **All repositories** (simplest option), OR
     - **Only select repositories** (choose your prompt repository)
   - Click **Save**

6. **Test the Connection:**
   - Open a new chat in Claude
   - Click the **attachment icon** (📎)
   - Select **Add from GitHub**
   - You should see your repository listed
   - Browse and select a prompt file
   - Click **Add files**

**✅ Success!** Claude can now access your prompts directly from GitHub.

**💡 Pro Tip:** In Claude Projects, you can add GitHub files and set them to **Sync** automatically, ensuring you always have the latest version.

---

### ✅ Step 12: Connect ChatGPT to GitHub

ChatGPT can also integrate with GitHub through Codex Connector.

**Steps:**

1. **Open ChatGPT Settings:**
   - Go to https://chatgpt.com and sign in
   - Click your profile picture (bottom left)
   - Select **Settings**

2. **Navigate to Connectors:**
   - Click **Personalization** in the left menu
   - Click **Connectors**

3. **Install GitHub Connector:**
   - Find **GitHub** in the available connectors
   - Click to install the connector
   - You may need to install **ChatGPT Codex Connector** specifically
   - Follow the authorization prompts

4. **Configure Repository Access:**
   - Similar to Claude, authorize ChatGPT to access your GitHub account
   - Select which repositories to share
   - Save your configuration

5. **Use in ChatGPT:**
   - In a chat, click **Connected apps**
   - Select **GitHub** → **Repositories**
   - Click **Configure Repositories**
   - Choose your prompt repository
   - Select specific files to add to the conversation

**Alternative Method - Manual Copy:**
If you prefer not to connect GitHub directly:
1. Open your prompt file on GitHub.com
2. Click the **Raw** button
3. Copy the contents
4. Paste into ChatGPT

---

### ✅ Step 13: Reference Prompts in Your Workflow

Now that everything is connected, here's how to use your prompts effectively:

**In Claude:**

1. **For one-time use:**
   - Start a new chat
   - Click 📎 (attachment icon)
   - Select **Add from GitHub**
   - Choose your repository and file
   - Type your specific request referencing the attached prompt
   - Example: "Using the attached audience style guide creator, create a guide for tech startup founders"

2. **For repeated use (Projects):**
   - Create a Claude Project (click **Projects** in sidebar)
   - Click **Add content** → **Add from GitHub**
   - Select your prompt files
   - Enable **Sync now** for automatic updates
   - Every chat in this project will have access to these prompts

**In ChatGPT:**

1. Start a chat
2. Click **Connected apps** or the attachment icon
3. Select **GitHub** → navigate to your file
4. Reference it in your request

**In Cursor/VS Code with Claude Code:**

1. Install the Claude Code extension (if not already installed)
2. Open your prompt file locally
3. Select text or the whole file
4. Press `Cmd+L` or `Ctrl+L` to open Claude Code chat
5. Claude Code automatically includes selected text as context

---

## 🔄 Version Control and Collaboration

Understanding version control unlocks the full power of managing prompts like code.

### Understanding Version History

Every time you commit a change to GitHub, it's saved in history permanently. This allows you to:

- **Compare versions** to see exactly what changed
- **Restore old versions** if a change made things worse
- **Understand evolution** by reading commit messages
- **Track improvements** over time

**Viewing History on GitHub:**

1. Go to your repository on GitHub.com
2. Click on any file
3. Click **History** (clock icon) in the top right
4. You'll see all commits that changed this file
5. Click any commit to see exactly what changed:
   - **Green lines** = additions
   - **Red lines** = deletions

**Example Use Case:**
You iterate on a "board update generator" prompt. After several versions, you realize version 3 was actually better than version 5. You can view version 3's content and restore it if needed.

---

### ✅ Step 14: Making Updates to Existing Prompts

As you refine your prompts, you'll update them frequently. Here's the workflow:

**Steps:**

1. **Edit your prompt file:**
   - Open the file in your code editor
   - Make your improvements
   - Save the file (`Cmd+S` / `Ctrl+S`)

2. **Review your changes:**
   - Open Source Control panel (left sidebar)
   - Click on the modified file
   - You'll see a **diff view** showing:
     - Old version on left
     - New version on right
     - Changes highlighted

3. **Commit your changes:**
   - Stage the file (click + icon)
   - Write a descriptive commit message:
     - Good: "Improve clarity in audience definition section"
     - Good: "Add example outputs to style guide prompt"
     - Bad: "update"
   - Click **Commit**

4. **Push to GitHub:**
   - Click **Sync Changes**
   - Your updates are now backed up and versioned

5. **Sync in Claude Projects:**
   - If you're using Claude Projects, click **Sync now**
   - Claude will fetch the latest version from GitHub

**Best Practice:** Commit after each meaningful improvement. Don't wait until you have dozens of changes—small, frequent commits with clear messages are better than large, unclear ones.

---

### Collaboration Best Practices

If you're working with a team:

**Sharing Your Repository:**

1. Go to your repository on GitHub.com
2. Click **Settings** (top right)
3. Click **Collaborators** in the left menu
4. Click **Add people**
5. Enter their GitHub username or email
6. They'll receive an invitation

**Reviewing Changes:**

- Use **Pull Requests** for team review (advanced topic, see GitHub docs)
- Team members can suggest changes before merging
- Maintain quality through peer review

**Organizational Repositories:**

For larger teams:
1. Create a GitHub Organization
2. Create repositories under the organization
3. Set up teams with different access levels
4. Establish contribution guidelines

---

## ⭐ Best Practices

### 📁 Organizing Your Prompt Library

**Recommended Folder Structure:**

```
my-prompts/
├── README.md                          # Overview of your library
├── prompts/
│   ├── writing/
│   │   ├── email-drafter.md
│   │   ├── blog-post-outliner.md
│   │   └── social-media-creator.md
│   ├── analysis/
│   │   ├── strategy-analyzer.md
│   │   ├── data-interpreter.md
│   │   └── trend-researcher.md
│   ├── leadership/
│   │   ├── meeting-facilitator.md
│   │   ├── feedback-generator.md
│   │   └── goal-setter.md
│   └── templates/
│       ├── prompt-improver.md
│       └── style-guide-creator.md
├── workflows/
│   └── content-creation-pipeline.md
└── examples/
    └── successful-outputs.md
```

**Naming Conventions:**
- Use lowercase
- Use hyphens, not spaces (`my-prompt.md`, not `My Prompt.md`)
- Be descriptive (`audience-style-guide-creator.md`, not `prompt1.md`)
- Include version numbers if needed (`v2-email-drafter.md`)

---

### Writing Effective Commit Messages

Good commit messages help you (and your team) understand changes later.

**Format:**
```
Brief summary (50 chars or less)

Optional detailed explanation:
- What changed
- Why you changed it
- Any important notes
```

**Examples:**

✅ **Good:**
```
Add context examples to email drafter prompt

Included 3 example emails showing different tones
to help AI better understand desired output format.
```

❌ **Bad:**
```
update
```

```
changes to prompt
```

**Commit Message Tips:**
- Start with a verb (Add, Update, Fix, Remove, Improve)
- Be specific about what changed
- Explain why if not obvious
- Keep the first line short

---

### 🔒 Security Best Practices

**Protecting Sensitive Information:**

1. **Never commit API keys or passwords**
   - Store these in `.env` files (add to `.gitignore`)
   - Use GitHub Secrets for automation

2. **Review before committing**
   - Check diffs in Source Control panel
   - Make sure no personal info is included
   - Remove any client-specific details

3. **Use private repositories** for:
   - Proprietary prompts
   - Client work
   - Competitive advantage IP

4. **Use public repositories** for:
   - General-purpose prompts
   - Open-source contributions
   - Community sharing

**Adding a .gitignore file:**

Create a file named `.gitignore` in your repository root:

```
# Environment variables
.env
.env.local

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/

# Personal notes
NOTES.md
scratch/
```

This prevents specified files from being tracked by Git.

---

## 🤖 Integrating Models into Your IDE

Take your workflow to the next level by bringing AI directly into your code editor.

### Option 1: Claude Code in VS Code/Cursor

**What is Claude Code?**
Claude Code is an agentic coding tool that lives in your terminal and integrates with your editor. It can read your files, understand your codebase, and help you work faster.

**Installation:**

1. **Install Claude Code:**
   - Go to Claude Settings (claude.ai → Settings)
   - Click **Claude Code** in the left menu
   - Follow the installation instructions for your OS:

   **macOS/Linux:**
   ```bash
   curl -fsSL claude.ai/install.sh | bash
   ```

   **Windows PowerShell:**
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```

2. **Start Claude Code:**
   - Open terminal in your project directory
   - Type:
     ```bash
     claude
     ```
   - Claude Code launches and can access your project files

3. **Install VS Code Extension:**
   - Open Extensions in VS Code/Cursor
   - Search for "Claude Code for VS Code"
   - Click **Install**
   - Click **Enable**

**Using Claude Code:**
- Type in the Claude Code chat to ask questions about your files
- Claude can read, edit, and create files
- Reference your prompt library directly
- Get AI assistance without leaving your editor

**Documentation:** [Claude Code Documentation](https://docs.claude.com/claude-code)

---

### Option 2: ChatGPT Codex in Cursor

**What is Codex?**
OpenAI's Codex is a coding agent that integrates with Cursor and can help with writing, reviewing, and improving code (and prompts!).

**Installation:**

1. **Install Cursor** (if not already done)

2. **Enable Codex:**
   - In ChatGPT, go to Settings → **Codex**
   - Click "Try in your IDE" or "Try in your terminal"

3. **Install in Cursor:**
   - Open Cursor
   - Go to Extensions marketplace (left sidebar)
   - Search for "Codex – OpenAI's coding agent"
   - Click **Install**

4. **Authenticate:**
   - Click the Codex icon in Cursor
   - Sign in with your ChatGPT account
   - Allow Cursor to connect

**Using Codex:**
- Press `Cmd+K` (macOS) or `Ctrl+K` (Windows) to open Codex inline
- Type your request
- Codex can read your repository and suggest changes
- Works in chat mode or inline with your files

---

### Option 3: Google Gemini CLI

**What is Gemini CLI?**
A command-line interface for Google's Gemini model with free tier access and powerful features.

**Benefits:**
- 60 requests/min and 1,000 requests/day (free tier)
- Powerful Gemini 2.5 Pro with 1M token context window
- Built-in tools: Google Search, file operations, shell commands, web fetching
- MCP (Model Context Protocol) support
- Terminal-first design

**Installation:**

**Quick Install (No Installation Required):**
```bash
npx https://github.com/google-gemini/gemini-cli
```

**Install Globally with npm:**
```bash
npm install -g @google/gemini-cli
```

**Install with Homebrew (macOS/Linux):**
```bash
brew install gemini-cli
```

**Usage:**
1. Navigate to your project directory in terminal
2. Type `gemini` to start
3. Ask questions, edit files, or run commands
4. Gemini has access to your local file context

**Documentation:** [Gemini CLI on GitHub](https://github.com/google-gemini/gemini-cli)

---

## ⚠️ Troubleshooting

### Common Issues and Solutions

#### Issue: "Permission denied" when pushing to GitHub

**Cause:** Your Personal Access Token may be incorrect or expired.

**Solution:**
1. Generate a new token (see Step 5)
2. When prompted for password, paste the new token
3. Make sure "repo" scope is checked when creating the token

---

#### Issue: Can't see my repository in Claude

**Cause:** Repository access may not be configured correctly.

**Solution:**
1. Go to GitHub Settings → Applications
2. Find "Claude for GitHub"
3. Click Configure
4. Ensure your repository is included in the access list
5. Go back to Claude and refresh

---

#### Issue: Changes aren't syncing to GitHub

**Cause:** You may have committed but not pushed.

**Solution:**
1. Check Source Control panel in your editor
2. Look for the "Sync Changes" button with a number
3. Click it to push your commits
4. Verify on GitHub.com that changes appear

---

#### Issue: Git says "working tree is dirty"

**Cause:** You have uncommitted changes.

**Solution:**
1. Review changes in Source Control panel
2. Stage all changes (click + icon)
3. Write commit message and commit
4. Push to GitHub

---

#### Issue: Merge conflicts

**Cause:** Changes made in two places conflict with each other.

**Solution:**
1. If you're working alone, this is rare
2. Open the file with conflicts
3. Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Manually choose which version to keep
5. Remove conflict markers
6. Save, commit, and push

---

## 🎯 Next Steps

Congratulations! You've now set up a professional prompt management system. Here's what to do next:

### ✅ Immediate Actions

1. **Create 5-10 of your best prompts**
   - Convert your most-used prompts to Markdown
   - Organize them in folders by category
   - Commit and push them to GitHub

2. **Test the workflow**
   - Use a prompt from GitHub in Claude
   - Make an improvement and commit it
   - View the version history on GitHub

3. **Set up cloud backup**
   - Enable Google Drive or OneDrive sync on your local prompt folder
   - This provides an extra layer of backup

### Building Your Library

**Week 1-2:**
- Document your existing prompts
- Organize them by use case
- Create a README explaining your library structure

**Month 1:**
- Develop 20-30 core prompts
- Establish naming conventions
- Start building prompt templates

**Ongoing:**
- Refine prompts based on results
- Share with team members
- Contribute to open-source prompt libraries

### Advanced Topics to Explore

1. **GitHub Actions** - Automate testing and validation of prompts
2. **Prompt Templates** - Create reusable templates with variables
3. **Team Collaboration** - Set up Pull Request workflows
4. **Prompt Analytics** - Track which prompts perform best
5. **Integration Automation** - Auto-sync prompts to internal tools

---

## 📚 Resources

### Official Documentation

- **GitHub Guides:** [guides.github.com](https://guides.github.com)
- **Git Handbook:** [guides.github.com/introduction/git-handbook](https://guides.github.com/introduction/git-handbook)
- **Claude Code Docs:** [docs.claude.com/claude-code](https://docs.claude.com/claude-code)
- **Markdown Guide:** [markdownguide.org](https://markdownguide.org)
- **Cursor Documentation:** [cursor.com/docs](https://cursor.com/docs)
- **VS Code Git Guide:** [code.visualstudio.com/docs/sourcecontrol/overview](https://code.visualstudio.com/docs/sourcecontrol/overview)

### Learning More

- **Pro Git Book (Free):** [git-scm.com/book](https://git-scm.com/book)
- **GitHub Skills:** [skills.github.com](https://skills.github.com)
- **Markdown Tutorial:** [markdowntutorial.com](https://markdowntutorial.com)

### Community and Support

- **Hands-on AI for Leaders Course:** [maven.com/james-gray/hands-on-ai-for-leaders](https://maven.com/james-gray/hands-on-ai-for-leaders)
- **Course Community:** Available through Maven platform

---

## 🎉 Conclusion

You've just learned to manage your AI prompts like professional software developers manage code. This system will:

- **Save you time** by making prompts easy to find and reuse
- **Improve quality** through version control and iteration tracking
- **Enable collaboration** with team members
- **Protect your intellectual property** with proper backups and organization
- **Scale effortlessly** as your prompt library grows

Remember: **Your prompts are strategic assets.** By managing them systematically, you're building intellectual property that compounds in value over time.

Start small, be consistent, and watch your prompt library become one of your most valuable professional tools.

---

**About the Author**

James Gray is a former Microsoft Data Scientist and Berkeley Haas AI Strategy Instructor who teaches leaders how to leverage AI for strategic advantage. Through the [Hands-on AI for Leaders course](https://maven.com/james-gray/hands-on-ai-for-leaders), he helps professionals master AI tools and build autonomous systems.

Connect: [JamesGray.AI](https://jamesgray.ai) | [handsonai.info](https://handsonai.info)

---

*© 2025 James Gray Innovations LLC. This guide is provided as an educational resource.*
