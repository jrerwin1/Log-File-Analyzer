# 🔍 Log File Analyzer

A Python-based tool that scans system log files to detect failed login attempts, extract IP addresses, and identify error messages. Outputs results to both the console and an `output.txt` file.

## 📁 Project Overview

This project simulates a simplified log monitoring system often used in cybersecurity and system administration roles. The code was designed to help detect signs of unauthorized access, failed login attempts, and errors within a system log.

## 👨‍💻 Created By

**Joshua Erwin**  
April 2025  

## 🛠️ Features

- Detects and lists failed SSH login attempts  
- Extracts and displays unique IP addresses from suspicious activity  
- Identifies system error messages  
- Saves all results to a clean, formatted `output.txt` file  
- Accepts any plain-text log file as input via the command line

## 🧪 Sample Log Format

```text
Feb 12 08:01:23 server sshd[1234]: Failed password for invalid user admin from 192.168.1.15 port 22 ssh2  
Feb 12 08:05:12 server sshd[1237]: error: PAM: Authentication failure  

