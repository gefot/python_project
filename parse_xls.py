import modules
import pprint
import pandas

### Main
xls = "export_list.xlsx"
all_entries = modules.create_list_of_dicts_from_xls(xls)
print(len(all_entries))

### Normalize entries
all_entries = modules.normalize_shoretel_entries(all_entries)
for my_entry in all_entries:
    pprint.pprint(my_entry)

