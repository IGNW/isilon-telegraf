from settings import Settings

def test_settings_default():
    s = Settings()
    assert isinstance(s, Settings)