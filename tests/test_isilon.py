from isilon import Isilon

def test_isilon_can_be_created():
    i = Isilon(api_class="StatisticsApi")

    assert isinstance(i, Isilon)
