import os
p = "C:/Users/ea.yarosh/Seafile/p4ne_training/config_files/"
files = os.listdir(path="C:/Users/ea.yarosh/Seafile/p4ne_training/config_files")
fall = []
for i in files:
    file = open("C:/Users/ea.yarosh/Seafile/p4ne_training/config_files/" + i)
    for s in file:
        if s.strip().lower().startswith("ip address"):
            f = s.strip().lower().replace("ip address", "")
            if not f.strip().startswith(":"): fall.append(f.strip())
            else: fall.append(f.strip().replace(": ", ""))

print(set(fall))

