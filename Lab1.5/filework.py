import os
# путь к директории с файлами
p = "C:/Users/ea.yarosh/Seafile/p4ne_training/config_files/"

files = os.listdir(path=p)
fall = []
for i in files:
    file = open(p + i)
    for s in file:
        if s.strip().lower().startswith("ip address"):
            f = s.strip().lower().replace("ip address", "")
            if not f.strip().startswith(":"): fall.append(f.strip())
            else: fall.append(f.strip().replace(": ", ""))

print(set(fall))

