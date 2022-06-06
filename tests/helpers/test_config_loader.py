"""Tests for the `new_project_name.helpers.config_loader` module."""

from pytest import LogCaptureFixture

from new_project_name.helpers.config_loader import Config, ConfigSection


def test_config_loader(caplog: LogCaptureFixture) -> None:
    """Tests the `Config` class."""
    config_ok = Config("tests/helpers/.files/config_ok.yml")

    assert getattr(config_ok, "test_key") == "test value"

    assert isinstance(getattr(config_ok, "test_section"), ConfigSection)

    test_section = getattr(config_ok, "test_section")
    assert test_section.test_subkey == 12345

    new_config_ok = Config("tests/helpers/.files/config_ok.yml")
    assert config_ok == new_config_ok

    config_ok_2 = Config("tests/helpers/.files/config_ok_2.yml")
    assert config_ok_2 != config_ok

    try:
        Config("tests/helpers/.files/config_bad.yml")
    except BaseException as e:
        assert "Error in configuration file" in caplog.text
        assert isinstance(e, SystemExit)
