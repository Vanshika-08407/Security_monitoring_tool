
from datetime import datetime

def parse_logs(logs):
    parsed_logs = []

    for log in logs:
        log = log.strip()
        if not log or log.startswith("TIMESTAMP"):
            continue
        try:
            parts = log.strip().split(" | ")

            timestamp = datetime.strptime(
                parts[0].strip(),
                "%Y-%m-%d %H:%M:%S"
            )
            username = parts[1].strip().lower()
            ip = parts[2].strip()
            status = parts[3].strip().upper()

            parsed_logs.append({
                "timestamp": timestamp,
                "username": username,
                "ip": ip,
                "status": status
            })

        except Exception as e:
            print("PARSER ERROR:", e)
            print("BAD LINE:", log)

    return parsed_logs
