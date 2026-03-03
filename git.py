import os

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Generated {filename}")

def main():
    # README.md
    readme_content = """
# Veyrix IDE

Veyrix IDE is a lightweight, privacy-first, Progressive Web App (PWA) code editor that runs entirely in the browser. It features local IndexedDB storage, offline capabilities, real-time syntax highlighting, and dual sharing mechanics. Built for developers who need a fast, zero-setup scratchpad.

## Features

* In-Browser Execution: No server setup required. Everything runs locally.
* Local Storage: Files are saved securely in your browser's IndexedDB.
* Offline Support: Install as a PWA and use it completely offline.
* Snapshot System: Save up to 5 versioned snapshots per file to track your progress.
* Dual Sharing Mechanics:
  * Fast Local Share: Compresses code directly into a URL using LZ-String. No servers involved.
  * Cloud Share: Generates short links by uploading to an anonymous Firebase Firestore instance. Includes optional password protection.
* Native Web Share Integration: Share code directly to mobile apps or desktop environments.

## Getting Started

Visit the live site to start using Veyrix IDE immediately. No installation is required.
To install as a PWA, click the "Settings" icon and select "Install Web App".

## Architecture

* UI/Styling: Tailwind CSS
* Editor: Ace Editor
* Compression: LZ-String
* Cloud Sharing: Firebase (Firestore, Anonymous Auth)

## Support and Contact

For general inquiries: mail@amit.is-a.dev
For important matters: amitdutta4255@gmail.com
Developer Portfolio: https://amit.is-a.dev

## Disclaimer

Use of this tool is at your own risk. The creator is not responsible for any data loss, misuse, or damages caused by using this application. The creator holds full rights to modify or permanently discontinue this project at any time without prior notice.
    """

    # CONTRIBUTING.md
    contributing_content = """
# Contributing to Veyrix IDE

We welcome contributions to Veyrix IDE! Whether it is a bug report, a new feature, or a documentation update, your help is appreciated.

## How to Contribute

1. Fork the Repository
Navigate to the GitHub repository and fork the project to your personal account.

2. Clone Your Fork
Clone your forked repository to your local machine.
`git clone https://github.com/your-username/veyrix.git`

3. Create a Branch
Create a new branch for your specific feature or bugfix.
`git checkout -b feature/your-feature-name`

4. Make Your Changes
Implement your changes. Please ensure your code adheres to the existing style and architecture of the project.

5. Commit and Push
Commit your changes with clear, descriptive commit messages.
`git commit -m "Add descriptive message here"`
`git push origin feature/your-feature-name`

6. Submit a Pull Request
Go to the original repository on GitHub and open a Pull Request. Provide a detailed description of the changes you have made and the problem they solve.

## Reporting Bugs

If you find a bug, please open an issue in the repository. Include clear steps to reproduce the issue, your browser version, and your operating system.
    """

    # CODE_OF_CONDUCT.md
    coc_content = """
# Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:
* Using welcoming and inclusive language.
* Being respectful of differing viewpoints and experiences.
* Gracefully accepting constructive criticism.
* Focusing on what is best for the community.
* Showing empathy towards other community members.

Examples of unacceptable behavior by participants include:
* The use of sexualized language or imagery and unwelcome sexual attention or advances.
* Trolling, insulting/derogatory comments, and personal or political attacks.
* Public or private harassment.
* Publishing others' private information, such as a physical or electronic address, without explicit permission.
* Other conduct which could reasonably be considered inappropriate in a professional setting.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at mail@amit.is-a.dev. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident.
    """

    # SECURITY.md
    security_content = """
# Security Policy

## Supported Versions

Currently, only the latest version of Veyrix IDE is supported with security updates. Because Veyrix operates entirely within the browser (client-side), security updates are automatically applied upon refreshing the application or fetching the latest PWA service worker cache.

## Reporting a Vulnerability

We take the security of Veyrix IDE seriously. If you discover a security vulnerability within this project, please send an e-mail to Amit Dutta at amitdutta4255@gmail.com. 

Please provide the following information in your report:
* A detailed description of the vulnerability.
* Steps to reproduce the issue.
* Any potential impact or risk you have identified.

All security vulnerabilities will be promptly addressed. We ask that you do not disclose the vulnerability publicly until a fix has been released.
    """

    # Write files
    write_file('README.md', readme_content)
    write_file('CONTRIBUTING.md', contributing_content)
    write_file('CODE_OF_CONDUCT.md', coc_content)
    write_file('SECURITY.md', security_content)

if __name__ == "__main__":
    main()