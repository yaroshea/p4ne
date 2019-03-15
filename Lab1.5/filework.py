import os

files = os.listdir(path="C:/Users/ea.yarosh/Seafile/p4ne_training/config_files")
fall = []
for i in files:
    file = open("C:/Users/ea.yarosh/Seafile/p4ne_training/config_files/" + i)
    for s in file:
        if s.strip().lower().startswith("ip address: "):
            fall.append(s.strip().lower().replace("ip address: ", ""))
print(set(fall))

