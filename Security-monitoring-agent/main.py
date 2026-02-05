from core.log_reader import read_logs 
from core.log_parser import parse_logs
from core.detector   import detect_threats
from core.severity_engine import assign_severity


def main():
    print("MAIN.PY IS RUNNING")

    log_filepath = "logs/logs_login.txt"
    raw_logs = read_logs(log_filepath)

    print("RAW LOGS TYPE:", type(raw_logs))
    print("RAW LOGS LEN:", len(raw_logs))

    parsed_logs = parse_logs(raw_logs)

    print("PARSED LOGS TYPE:", type(parsed_logs))
    print("PARSED LOGS LEN:", len(parsed_logs))

    for log in parsed_logs:
        print(log)
    alerts = detect_threats(parsed_logs)
    alerts = assign_severity(alerts)
    print("---Alerts with severity---")
    print(alerts)

if __name__ == "__main__":
    main()
    