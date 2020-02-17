import tabula, re

df = tabula.read_pdf("ics.pdf", pages="all", output_format="json")
tabula.convert_into("ics.pdf", "ics.csv", output_format="csv", pages="all")

lines = ["Datum Transactie,Datum boeking,Omschrijving-1,Omschrijving-2,Omschrijving-3,Bedrag in vreemde valuta,Bedrag in euro's,Mutatie\n"]

with open("ics.csv", "r") as file:
    for line in file.readlines():
        match = re.match("^\d+.*(Af|Bij)", line)
        if match:
            lines.append(line)

with open("ics.csv", "w") as file:
    for line in lines:
        file.write(line)