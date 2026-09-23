#Task 4 - Consolidate parcel labels
# list, distinct label once, preserving the order, 
# splitting, loops, normalization, memberships checks, ordered output

scanned_labels = input("Scanned labels: ")
scanned_labels = scanned_labels.split(",")

unique_labels = []

for label in scanned_labels:
    label = label.upper()
    label = label.strip()
    if label not in unique_labels:
        unique_labels.append(label)

print(f"Unique load list:")

for number, label in enumerate(unique_labels, start = 1):
    print(f"{number}. {label}")

print(f"Total unique parcels: {len(unique_labels)}")
     


