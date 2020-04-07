import urllib3
from urllib3.exceptions import MaxRetryError, LocationValueError

import isi_sdk_8_2_1 as isi_sdk
from settings import Settings


class IsilonConnectionException(Exception):
    pass


class IsilonNoHostException(Exception):
    pass


class IsilonInvalidClassException(Exception):
    pass


class IsilonInvalidArgumentException(Exception):
    pass


class IsilonInvalidMethodException(Exception):
    pass


class Isilon:
    def __init__(self, api_class=None, settings_file=None):
        self.config = Settings(settings_file)
        urllib3.disable_warnings()

        # Configuration Settings
        url = f"https://{self.config.hostname}:{self.config.port}"
        configuration = isi_sdk.Configuration()
        configuration.host = url
        configuration.username = self.config.username
        configuration.password = self.config.password
        configuration.verify_ssl = self.config.verify_ssl

        self.create_client(api_class=api_class, configuration=configuration)

    def create_client(self, api_class=None, configuration=None):
        # Create an instance of the API class
        client = isi_sdk.ApiClient(configuration)

        try:
            api_class = getattr(isi_sdk, api_class)
        except AttributeError:
            raise IsilonInvalidClassException(f"There is no class called '{api_class}' in the Isilon SDK")
        except Exception:
            raise

        self.api_client = api_class(client)

    def call_method(self, method=None, **kwargs):
        # This allows the calling of Class Methods using a variable
        try:
            to_call = getattr(self.api_client, method)
        except AttributeError:
            raise IsilonInvalidMethodException(f"The method `{method}` does not exist on the Class Object.")
        except Exception:
            print("An unknown error occured when trying to access the Instance Method")
            raise

        try:
            # Calling the function and passing in all the args
            output = to_call(**kwargs)
        except MaxRetryError:
            raise IsilonConnectionException(f"Unable to connect to the the host {self.config.hostname}")
        except LocationValueError:
            raise IsilonNoHostException("No host is defined in the settings file")
        except TypeError:
            raise IsilonInvalidArgumentException(f"One of the arguements you passed in is invalid.  Arguments are: {kwargs}")
        except Exception:
            print("An unknown error occured when trying to call the method")
            raise

        return output
