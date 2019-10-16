land = input("Ein Land bitte")
betrag = int(input("Wie viel Euro hast du?"))

laender = {
  "England":  {"waerung": "Pfund", "waechselkurs": 1.2},
  "Schweiz":  {"waerung": "Schweizer Franken", "waechselkurs": 1.3},
  "USA":      {"waerung": "US-Dollar", "waechselkurs": 1.4},
  "Norwegen": {"waerung": "Norwegische Kronen", "waechselkurs": 1.4},
  "Polen":    {"waerung": "Zloty", "waechselkurs": 1.6},
  "Japan":    {"waerung": "Yen", "waechselkurs": 1.7}
}

print(str(betrag*laender[land]["waechselkurs"]) + " " + laender[land]["waerung"] )