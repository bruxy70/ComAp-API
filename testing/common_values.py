"""Demonstration of the ComAp API library

This is just a helper that list the stored constants for most common value guids.
This is a local example - this does not talk to the API - so it does not need to authenticate.
"""


from comap.constants import VALUE_GUID

print("These common values GUIDs are stored in the constant VALUE_GUID[value], available in module comap.constants.")
print("------------------------------------------------------------------------------------------------------------")
for value in VALUE_GUID:
    print(f'{value:<16} {VALUE_GUID[value]}')
