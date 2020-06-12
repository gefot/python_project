import modules
import pprint
import pandas

### Main
xls = "export_list.xlsx"
all_entries = modules.create_list_of_dicts_from_xls(xls)

### Normalize entries
all_entries = modules.normalize_shoretel_entries(all_entries)
print(len(all_entries))
# for my_entry in all_entries:
#     pprint.pprint(my_entry)

modules.create_xls_from_list_of_dicts(all_entries)
