def caliconcatenate(S):
    if S.startswith("calico"):
        return "CALICO" + S[6:]
    elif S.startswith("alico"):
        return "CALICO" + S[5:]
    elif S.startswith("lico"):
        return "CALICO" + S[4:]
    elif S.startswith("ico"):
        return "CALICO" + S[3:]
    elif S.startswith("co"):
        return "CALICO" + S[2:]
    elif S.startswith("o"):
        return "CALICO" + S[1:]
    else:
        return S


T = int(input().strip())
results = []
for _ in range(T):
    S = input().strip()
    results.append(caliconcatenate(S))

print("\n".join(results))
