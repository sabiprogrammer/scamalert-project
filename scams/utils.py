def db_string_to_list(string):
    if string:
        a = string.replace("[", "").replace("]", "").replace("'", "")
        return a.split(", ")
        # invalid = ["[", "]"]
        # return [i for i in string if i not in invalid]
    return []
