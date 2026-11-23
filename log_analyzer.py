
# Cybersecurity Log Analysis Tool

def analyze_logs():
    logs = [
        "INFO: User login successful",
        "WARNING: Failed login attempt",
        "INFO: System started",
        "WARNING: Failed login attempt",
        "ERROR: Unauthorized access detected"
    ]

    print("Cybersecurity Log Analysis Report")
    print("--------------------------------")

    for log in logs:
        if "Failed login" in log or "Unauthorized" in log:
            print("SECURITY ALERT:", log)

    print("Log analysis completed.")


if __name__ == "__main__":
    analyze_logs()
