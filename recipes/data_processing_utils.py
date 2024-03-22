import pandas as pd

def load_language_mapping(csv_path):
    lang_df = pd.read_csv(csv_path)
    lang_to_iso = pd.Series(lang_df.ISOCode.values, index=lang_df.LanguageName).to_dict()
    return lang_to_iso

def convert_languages_to_iso(languages, lang_to_iso):
    # Split the languages string into a list based on the pipe separator
    languages_list = languages.split('|')
    # Convert each language in the list to its ISO code
    iso_codes_list = [lang_to_iso.get(language.strip(), language.strip()) for language in languages_list]
    # Join the converted ISO codes back into a string separated by pipes
    iso_codes = '|'.join(iso_codes_list)
    return iso_codes
    
# splits up fields that are formatted as a python list. Example: 
# "language": [
#             "French",
#             "Greek, Modern (1453-)",
#             "Latin"
#         ],
def clean_complex_fields(item):
    # Directly return an empty string for None
    if item is None:
        return ''
    # Handle lists specifically
    elif isinstance(item, list):
        # If the list is empty, return an empty string
        if not item:
            return ''
        # Join list items with a pipe, handle semicolon within items
        return '|'.join([str(i) for i in item if pd.notnull(i) and i != ''])
    # Handle singular non-list items, check for NaN separately
    elif pd.isnull(item):
        return ''
    else:
        # For non-list items, clean up as before
        item = str(item).strip()
        return item

        
# splits up fields that are formatted as a string list. Example:
# "country": [
#             "Sweden; Finland; Estonia; Latvia; Lithuania"
#         ],

def replace_with_pipes(column):
    # Replace NaN with empty string and ensure string type
    column = column.fillna('').astype(str)
    # Replace semicolons with pipes and remove surrounding whitespace
    column = column.str.replace(r'\s*;\s*', '|', regex=True)
    # Remove unwanted characters like brackets and quotes
    column = column.str.replace(r"\['", "", regex=True)
    column = column.str.replace(r"'\]", "", regex=True)
    column = column.str.replace(r"[\[\]'\"\"]", "", regex=True)
    return column

