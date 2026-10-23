
# Text-Based Invoice Data Extraction

invoices = [
    "P101,2,500.00",
    "P102,5,1250.00",
    "P103,abc,300.00",
    "P104,3,invalid",
    "P105,0,200.00",
    "P106,4,800.00"
]

valid_records = []
malformed_records = []

print("===== INVOICE DATA EXTRACTION =====")

for invoice in invoices:
    fields = invoice.split(",")

    if len(fields) != 3:
        malformed_records.append(invoice)
        continue

    code = fields[0].strip()
    quantity_text = fields[1].strip()
    amount_text = fields[2].strip()

    # Validate product code
    if (len(code) < 2 or code[0] != "P"
            or not code[1:].isdigit()):
        malformed_records.append(invoice)
        continue

    # Validate quantity and amount
    try:
        quantity = int(quantity_text)
        amount = float(amount_text)

        if quantity <= 0 or amount < 0:
            malformed_records.append(invoice)
            continue

    except ValueError:
        malformed_records.append(invoice)
        continue

    valid_records.append((code, quantity, amount))

    print("\nProduct Code:", code)
    print("Quantity:", quantity)
    print("Amount: Rs.", format(amount, ".2f"))

print("\n===== VALIDATION SUMMARY =====")

print("\nValid Invoice Records:")
for code, quantity, amount in valid_records:
    print(code, quantity, format(amount, ".2f"))

print("\nMalformed Invoice Records:")
if malformed_records:
    for record in malformed_records:
        print(record)
else:
    print("None")

print("\nTotal Valid Records:", len(valid_records))
print("Total Malformed Records:", len(malformed_records))

total_amount = sum(record[2] for record in valid_records)
print("Total Invoice Amount: Rs.", format(total_amount, ".2f"))
