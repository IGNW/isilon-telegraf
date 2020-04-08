from settings import Settings, SettingsError
import pytest


def test_settings_default():
    s = Settings()
    assert isinstance(s, Settings)
    assert hasattr(s, "name")
    assert hasattr(s, "ip")


def test_settings_with_empty_file(tmp_path):
    d = tmp_path / "settings"
    d.mkdir()
    p = d / "settings.yml"
    p.write_text("")

    s = Settings(p)

    assert isinstance(s, Settings)
    assert s.ip == ""
    assert s.name == ""
    assert not hasattr(s, "missing_property")


def test_settings_with_malformed_settings_file(tmp_path):
    bad_yml = """
    some_key: 'No end quotes is bad yaml
    """
    d = tmp_path / "settings"
    d.mkdir()
    p = d / "settings.yml"
    p.write_text(bad_yml)

    with pytest.raises(SettingsError) as e:
        Settings(settings_file=p)
    error_message = "You have a malformed 'settings.yml' file."
    assert error_message in str(e.value)


def test_settings_with_string_in_yaml(tmp_path):
    test_string = "This is a test string"
    d = tmp_path / "settings"
    d.mkdir()
    p = d / "settings.yml"
    p.write_text(test_string)

    with pytest.raises(AttributeError) as e:
        Settings(settings_file=p)

    assert str(e.value) == "'str' object has no attribute 'items'"


def test_settings_with_valid_yaml(tmp_path):
    test_string = ('---\n'
                   'hostname: test_host\n'
                   'username: "Some User"\n'
                   'undefined_test_param: some_test_value\n'
                   'test param with spaces: "some value with spaces"')

    d = tmp_path / "settings"
    d.mkdir()
    p = d / "settings.yml"
    p.write_text(test_string)

    s = Settings(settings_file=p)

    assert s.hostname == "test_host"
    assert getattr(s, 'test param with spaces') == "some value with spaces"
    assert s.undefined_test_param == "some_test_value"
