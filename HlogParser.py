def parseLogs(logs):
    IPs = []
    URIs = []
    AccessMethods = []
    UserAgents = []


    for log in logs:
        IPs.append(log[0])
        AccessMethods.append(log[5])
        URIs.append(log[6])
        UserAgents.append(' '.join(log[11:-1]))
    return IPs, URIs, AccessMethods, UserAgents

def getLogs(fileName):
    f = open(fileName, 'r')
    raw_logs = f.readlines()
    logs = []
    for log in raw_logs:
        logs.append(log.split())
    return logs


if __name__ == "__main__":
    logs = getLogs("test2.txt")
    IPs ,URIs, AccessMethods , UserAgents = parseLogs(logs)

    #Unique#
    UIPs = set(IPs)
    UURIs = set(URIs)
    UAccessMethods = set(AccessMethods)
    UUserAgents = set(UserAgents)
