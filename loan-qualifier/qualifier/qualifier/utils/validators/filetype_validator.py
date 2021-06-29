import os

not_csv_str  = "Please enter a file with extension '.csv' (Ctrl+C to escape)."
not_path_str = "The path is not valid (Ctrl+C to escape)."


def csv_validator(x):
    csvpath_split = os.path.split(x)
    is_path       = path_validator(x)
    is_csv        = os.path.split(x)[-1].endswith(".csv")

    if is_csv and is_path: return True
    elif not is_path:      return not_path_str
    else:                  return not_csv_str


def path_validator(x):
    csvpath_split = os.path.split(x)
    is_path       = os.path.isdir("".join(csvpath_split[0]))

    return is_path