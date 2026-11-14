"""Settings must come from the environment, never from the source tree."""
import importlib


def test_payments_key_comes_from_environment(monkeypatch):
    monkeypatch.setenv("PAYMENTS_API_KEY", "value-from-env")
    import config
    importlib.reload(config)
    assert config.PAYMENTS_API_KEY == "value-from-env"
