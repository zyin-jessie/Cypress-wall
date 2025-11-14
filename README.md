<div align="center">
    <a href="./public/toolkit.png" target="_blank">
        <img src="./public/toolkit.png" alt="PwnStar Toolkit Banner">
    </a>
    <br>
    <img src="https://img.shields.io/badge/Python-3.11.0-%233776AB?style=for-the-badge&logo=python&logoColor=FFFFFF" alt="python"/> 
    <img src="https://img.shields.io/badge/linux-%23000000?style=for-the-badge&logo=linux&logoColor=FFFFFF" alt="Linux"/> 
    <img src="https://img.shields.io/badge/PowerShell-Badge?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAzMiAzMiI+PHBhdGggZD0iTTggMjJsOC02LTgtNk0xOCAyMmg2IiBzdHJva2U9IiNmZmYiIHN0cm9rZS13aWR0aD0iMi4yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGZpbGw9Im5vbmUiLz48L3N2Zz4=&logoSize=auto&23ED8B00&color=%23012456&cacheSeconds=86400)](https://learn.microsoft.com/powershell" alt="PowerShell"/>

# PwnStar-Toolkit

**PwnStar-Toolkit** is a lightweight command-line toolkit designed for **CTF enthusiasts** and security researchers. It helps you quickly **decode classical ciphers**, **crack hashes**, and automate common crypto and reversing tasks.

</div>

## Current Features

- 🖥️ Runs on Windows as a lightweight Python-based CLI toolkit.  
- 🔐 Supports SHA-1 hash cracking with dictionary attacks.  
- 🔢 Provides Vigenère cipher decoding. 

## Upcoming Features

- 🔑 More classical ciphers (Caesar, ROT13, Affine, etc.).  
- 🛡️ More hash types (MD5, SHA-256, NTLM, bcrypt).  
- 🔁 Extra encoders/decoders (Base64, hex, URL, Unicode).  
- ⚡ Faster CLI and auto-solve options.  
- 🔌 Modular extension support.  
- 🧩 Utility tools (endian swap, number conversion, XOR).  
- 🕵️ Basic pattern and frequency analysis.  
- 📂 Workspace mode for saving outputs.

## Installation Guide

### Prerequisites
Ensure you have the following installed on your system:
- **Git** version 2.45.1 or higher
- **Python** version 3.11.0 or higher  
- **Windows OS** (Linux/macOS support coming in future releases)

**Step 1: Open Command Prompt**
- Press `Windows + R`, type `cmd`, and press Enter
- Or search for "Command Prompt" in the Start menu

**Step 2: Navigate to Root Drive**
```bash
cd C:\
```
**Step 3: Clone the Repository**
```bash
git clone https://github.com/zyin-jessie/PwnStar-Toolkit.git
```

**Step 4: Add to System PATH**
- search for "Environment Variable" in the Start menu
- Click "Edit the system environment variables"
- Click "Environment Variables" button
- Under "User variables", select "Path" and click "Edit"
- Click "New" and add the following path:
```bash
C:\PwnStar-Toolkit
```

**Step 5: Launch the Toolkit**
- Open a new Command Prompt window
- Type the following command:
```bash
pwnstar
```
