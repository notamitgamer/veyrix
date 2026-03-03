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
