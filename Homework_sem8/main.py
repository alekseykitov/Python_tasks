from fsinfo import (
    get_entries_info_recoursively,
    save_entries_info_as_pickle,
    save_entries_info_as_json,
    save_entries_info_as_csv,
)


entries = get_entries_info_recoursively('/Users/mac/Desktop/GeekBrains/Погружение в Пайтон')
save_entries_info_as_pickle(entries, 'info.bin')
save_entries_info_as_json(entries, 'info.json')
save_entries_info_as_csv(entries, 'info.csv')
