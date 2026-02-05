from collections import defaultdict
from datetime import timedelta
def detect_threats(parsed_logs):
    alerts = []
    failed_by_ip = defaultdict(list)
    failed_by_user = defaultdict(list)

    for log in parsed_logs:
        if log["status"]=="FAILED":
          failed_by_ip[log['ip']].append(log)
          failed_by_user[log['username']].append(log)

    '''BRUTE FORCE ATTACK DETECTION'''
    for ip,log in failed_by_ip.items():
        log.sort(key = lambda x: x["timestamp"])

        for i in range(len(log)):
            window = log[i:i+5]

            if len(window)==5:
                time_diff = window[-1]["timestamp"] - window[0]["timestamp"]
        
                if time_diff < timedelta(minutes=1):
                    alerts.append({
                    "type":"Bruteforce",
                    "ip"  : ip,
                    "failed_attempts" : 5,
                    "window_time" : "1 minute"
                })
                break
    for user,log in failed_by_user.items():
        log.sort(key = lambda x: x["timestamp"])

        for i in range(len(log)):
            window = log[i:i+3]

            if len(window)==3:
                time_diff = window[-1]["timestamp"] - window[0]["timestamp"]
        
                if time_diff < timedelta(minutes=2):
                    alerts.append({
                    "type":"User_Attack",
                    "username" : user,
                    "failed_attempts" : 3,
                    "window_time" : "2 minutes"
                })
                break
        return alerts