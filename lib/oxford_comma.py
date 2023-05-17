
def oxford_comma(items):
    if len(items) <= 2:
        return ' and '.join(items)
    else:
        last_item = items[-1]
        remaining_items = ', '.join(items[:-1])
        return f"{remaining_items}, and {last_item}"

print(oxford_comma(["fiddleheads", "okra", "disk", "not a disk", "kohlrabi"]))