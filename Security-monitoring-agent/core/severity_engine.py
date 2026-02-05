def assign_severity(alerts):

    for alert in alerts:
        if alert["type"]=="Bruteforce":
            alert["severity"] = "HIGH"
        elif alert["type"]=="User_Attack":
            alert["severity"] = "MEDIUM"
        else:
            alert["severity"] = "LOW"    
    return alerts