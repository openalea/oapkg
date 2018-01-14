import oapkg


def test_package_exists():
    assert len(oapkg.__version__) > 0
