from settings import Settings, SettingsError
import pytest


def test_settings_default():
    s = Settings()
    assert isinstance(s, Settings)


def test_settings_with_empty_file(tmp_path):
    d = tmp_path / "settings"
    d.mkdir()
    p = d / "settings.yml"
    p.write_text("")

    s = Settings(p)

    assert isinstance(s, Settings)


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
