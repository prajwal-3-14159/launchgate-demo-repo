"""Settings must come from the environment, never from the source tree."""
import importlib
import uuid


def test_payments_key_comes_from_environment(monkeypatch):
    expected = uuid.uuid4().hex
    monkeypatch.setenv("PAYMENTS_API_KEY", expected)
    import config
    importlib.reload(config)
    assert config.PAYMENTS_API_KEY == expected
