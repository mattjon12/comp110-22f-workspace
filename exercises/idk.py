"""Demonstrations of dictionary capabilities."""



schools = dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

print(f"UNC has {schools["UNC"]} students")

schools.pop("Duke")

if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

print(schools["UNCC"])