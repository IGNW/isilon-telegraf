from isilon import Isilon, IsilonNoHostException, IsilonInvalidClassException
import pytest


def test_isilon_can_be_created():
    i = Isilon(api_class="StatisticsApi")

    assert isinstance(i, Isilon)


def test_isilon_with_invalid_class():
    with pytest.raises(IsilonInvalidClassException) as e:
        Isilon(api_class="InvalidClass")

    assert str(e.value) == "There is no class called 'InvalidClass' in the Isilon SDK"


def test_isilon_no_host_specified():
    i = Isilon(api_class="StatisticsApi", settings_file="s.yml")
    with pytest.raises(IsilonNoHostException) as e:
        i.call_method(method='get_summary_system', nodes='1,2,3,4')

    assert str(e.value) == "No host is defined in the settings file"
