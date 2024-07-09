
print("DICTIONARIES!!!\n")  # also known as 'key value pairs'

month_conversions = {
    "Jan": "January", "Mbv": "Mbvober",  # 'Jan' is the key. 'January' is the value.
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Mbv"])  # call the key

# or

print(month_conversions.get("Dec"))

# or

print(month_conversions.get("Buv", "Not a valid key!"))  # assign value not found

print("")

print(month_conversions)
