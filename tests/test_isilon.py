from isilon import (
    Isilon,
    IsilonNoHostException,
    IsilonInvalidClassException,
    IsilonConnectionException,
    IsilonInvalidArgumentException,
    IsilonInvalidMethodException
)
import pytest


@pytest.fixture
def bad_settings_file(tmp_path):
    text = ('ip: "10.20.30.40"\n'
            'port: "8080"\n'
            'username: "admin"\n'
            'password: "bad_password"\n'
            'verify_ssl: False\n'
            )
    file_name = tmp_path / "test_settings.yml"
    with open(file_name, "w") as f:
        f.write(text)

    return file_name


def test_isilon_can_be_created():
    i = Isilon(api_class="StatisticsApi")

    assert isinstance(i, Isilon)


def test_isilon_with_invalid_class():
    with pytest.raises(IsilonInvalidClassException) as e:
        Isilon(api_class="InvalidClass")

    assert str(e.value) == "There is no class called 'InvalidClass' in the Isilon SDK"


def test_isilon_no_host_specified():
    i = Isilon(api_class="StatisticsApi", settings_file="fake.yml")
    with pytest.raises(IsilonNoHostException) as e:
        i.call_method(method='get_summary_system', nodes='1,2,3,4')

    assert str(e.value) == "No host is defined in the settings file"


def test_isilon_bad_host_ip(bad_settings_file):
    i = Isilon(api_class="StatisticsApi", settings_file=bad_settings_file)
    with pytest.raises(IsilonConnectionException) as e:
        i.call_method(method='get_summary_system', nodes='1,2,3,4')

    assert str(e.value) == "Unable to connect to the the host 10.20.30.40"


def test_isilon_bad_method(bad_settings_file):
    i = Isilon(api_class="StatisticsApi", settings_file=bad_settings_file)
    with pytest.raises(IsilonInvalidMethodException) as e:
        i.call_method(method='get_bad_method', nodes='1,2,3,4')

    assert str(e.value) == "The method `get_bad_method` does not exist on the Class Object."


def test_isilon_bad_arguement_in_good_method(bad_settings_file):
    i = Isilon(api_class="StatisticsApi", settings_file=bad_settings_file)
    with pytest.raises(IsilonInvalidArgumentException) as e:
        i.call_method(method='get_summary_system', bad_param='1,2,3,4')

    assert str(e.value) == "One of the arguements you passed in is invalid.  Arguments are: {'bad_param': '1,2,3,4'}"
