import json

dictionary = {"debian": "apt", "ubuntu": "apt", "fedora": "dnf"}
data = json.dumps(dictionary, sort_keys=1, indent=4)
print(data)
