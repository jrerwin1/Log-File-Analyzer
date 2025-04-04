# =====================================================
# Author: Joshua Erwin
# Project: Log File Analyzer
# Description: Parses log files to detect failed logins,
#              error messages, and extracts IP addresses.
# Date: April 2025
# =====================================================

import re

def analyze_log(file_path):
    failed_logins = []
    error_messages = []
    ip_addresses = set()

    with open(file_path, 'r') as file:
        for line in file:
            if "Failed password" in line:
                failed_logins.append(line.strip())
                ip_matching = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_matching:
                    ip_addresses.add(ip_matching.group(1))
            elif "error" in line.lower():
                error_messages.append(line.strip())

    print("\n📌 Failed Login Attempts:")
    for entry in failed_logins:
        print(entry)

    print("\n📌 Error Messages:")
    for entry in error_messages:
        print(entry)

    print("\n📌 Unique IP Addresses Detected:")
    for ip in ip_addresses:
        print(ip)

if __name__ == "__main__":
    analyze_log('sample_log.txt')
