# utils.py
# Miscellaneous helper functions

def get_path_with_different_extension(path, ext):
    paths = path.split("/")
    return "/".join(paths[0:-1]) + "/" + paths[-1].split(".")[0] + ext