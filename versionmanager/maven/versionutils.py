def increase_version_minor(version, by=1):
    return __modify_minor_version__(version, True, by)

def decrease_version_minor(version, by=1):
    return __modify_minor_version__(version, False, by)

def __modify_minor_version__(version, addition, by=1):
    minor = __get_minor_version__(version)
    minor = minor + by if addition else minor - by
    v_strings, _ = __split__(version)
    v_strings = v_strings.split(".")
    v_strings[1] = str(minor)
    return ".".join(v_strings) + "-" + _

def __get_minor_version__(version):
    base_version, _ = __split__(version)
    return int(base_version.split(".")[1])

def __split__(version):
    return version.split("-")
