test_settings = {'theme': 'light', 'language': 'Spanish'}

def add_setting(settings, new_settings):
    key, value = new_settings
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting 'theme' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
    return f"Setting 'volume' added with value 'high' successfully!"

def update_setting(old_setting, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in old_setting:
        old_setting[key] = value
        return f"Setting 'theme' updated to 'dark' successfully!"
    else:
        return f"Setting 'volume' does not exist! Cannot update a non-existing setting."

def delete_setting(setting, del_setting):
    key = del_setting.lower()
    if key in setting:
        del setting[key]
        return f"Setting 'theme' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(setting):
    if setting == {}:
        return f"No settings available."
    else:
        resultado = "Current User Settings:"
        for key, value in setting.items():
            resultado += f"\n{key.capitalize()}: {value}"
        return resultado + "\n"