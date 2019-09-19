from comap.constants import VALUE_GUID

print("These common values GUIDs are stored in the constant VALUE_GUID[value], available in module comap.constants.")
print("------------------------------------------------------------------------------------------------------------")
for value in VALUE_GUID:
    print(f'{value:<16} {VALUE_GUID[value]}')