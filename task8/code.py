
# Manufacturing Quality Control Matrix

quality_threshold = 5.0
products = []

n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")
    raise SystemExit

for i in range(n):
    product_name = input("\nEnter product name: ").strip()
    batches_count = int(input("Enter number of batches: "))

    if not product_name or batches_count <= 0:
        print("Invalid product name or batch count.")
        raise SystemExit

    batches = []

    for j in range(batches_count):
        print(f"Batch {j + 1}")

        quantity = int(input("Enter production quantity: "))
        defective = int(input("Enter defective units: "))

        if quantity <= 0 or defective < 0 or defective > quantity:
            print("Invalid production or defective quantity.")
            raise SystemExit

        batches.append([quantity, defective])

    products.append([product_name, batches])

print("\n======= QUALITY CONTROL REPORT =======")
print("Threshold:", quality_threshold, "%")

inspection_count = 0
total_produced = 0
total_defective = 0

for product in products:
    product_name = product[0]
    batches = product[1]

    print(f"\nProduct: {product_name}")

    for i, batch in enumerate(batches, start=1):
        quantity = batch[0]
        defective = batch[1]

        defect_percentage = defective / quantity * 100
        total_produced += quantity
        total_defective += defective

        if defect_percentage > quality_threshold:
            status = "Needs Inspection"
            inspection_count += 1
        else:
            status = "Acceptable"

        print(
            f"Batch {i}: Produced={quantity}, "
            f"Defective={defective}, "
            f"Defect={defect_percentage:.2f}%, "
            f"Status={status}"
        )

print("\n======= OVERALL SUMMARY =======")
print("Total production:", total_produced)
print("Total defective units:", total_defective)

if total_produced > 0:
    overall_percentage = total_defective / total_produced * 100
    print(f"Overall defect percentage: {overall_percentage:.2f}%")

print("Batches needing inspection:", inspection_count)

