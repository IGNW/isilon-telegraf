# Settings file for the library
import yaml

from yaml.scanner import ScannerError
from pathlib import Path


class SettingsError(Exception):
    pass


class Settings():
    def __init__(self, settings_file=None):
        if settings_file is None:
            self.settings_file = Path("./settings.yml")
        else:
            self.settings_file = Path(settings_file)

        # Isilon Server Settings and Credentials
        self.hostname = ""
        self.username = ""
        self.password = ""
        self.verify_ssl = True

        # Override the defaults above
        self.load_settings_file()

    # Load data from the settings.yml file
    def load_settings_file(self):
        try:
            with open(self.settings_file, "r") as settings_file:
                data = yaml.safe_load(settings_file)
                for k, v in data.items():
                    setattr(self, k, v)
        except FileNotFoundError:
            # If the settings.yml file is missing, means use defaults
            pass
        except AttributeError as e:
            if str(e) == "'NoneType' object has no attribute 'items'":
                # The settings.yml file exists but is empty, use defaults
                pass
            else:
                raise
        except ScannerError as e:
            raise SettingsError("You have a malformed 'settings.yml' file.  "
                                "Please fix this.  The error can be found in "
                                f"the following message: {e}")
