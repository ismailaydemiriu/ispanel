"""Shared pytest fixtures for isPanel tests."""

import os
import sys
import importlib
import textwrap
from importlib.machinery import SourceFileLoader
from pathlib import Path
from typing import Iterator

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_ispanel_module():
    path = str(PROJECT_ROOT / "ispanel")
    loader = SourceFileLoader("ispanel_module", path)
    spec = importlib.util.spec_from_loader("ispanel_module", loader)
    if spec is None:
        raise RuntimeError("ispanel modülü yüklenemedi")
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    sys.modules["ispanel_module"] = module
    return module


@pytest.fixture()
def tmp_ispanel_home(tmp_path: Path) -> Path:
    """Return a temporary /home replacement for domain operations."""
    home = tmp_path / "home"
    home.mkdir()
    return home


@pytest.fixture()
def fake_lsws_conf(tmp_path: Path) -> Iterator[Path]:
    """Provide a fake /usr/local/lsws/conf directory with defaults."""
    conf_dir = tmp_path / "lsws_conf"
    conf_dir.mkdir()
    httpd = conf_dir / "httpd_config.conf"
    httpd.write_text(
        textwrap.dedent(
            """
            # Test httpd config
            listener Default {
                address                 *:80
                secure                  0
            }

            # HTTPS listener intentionally absent
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    vhosts = conf_dir / "vhosts"
    vhosts.mkdir()
    original_conf = os.environ.get("ISPANEL_TEST_LSWS_CONF")
    os.environ["ISPANEL_TEST_LSWS_CONF"] = str(conf_dir)

    try:
        yield conf_dir
    finally:
        if original_conf is not None:
            os.environ["ISPANEL_TEST_LSWS_CONF"] = original_conf
        else:
            os.environ.pop("ISPANEL_TEST_LSWS_CONF", None)


@pytest.fixture()
def ispanel_module(monkeypatch: pytest.MonkeyPatch, tmp_ispanel_home: Path, fake_lsws_conf: Path):
    module = load_ispanel_module()
    monkeypatch.setattr(module, "DOCROOT_BASE", tmp_ispanel_home)
    monkeypatch.setattr(module, "LSWS_CONF_DIR", fake_lsws_conf)
    monkeypatch.setattr(module, "VHOSTS_DIR", fake_lsws_conf / "vhosts")
    monkeypatch.setattr(module, "HTTPD_CONF", fake_lsws_conf / "httpd_config.conf")
    monkeypatch.setattr(module, "DEFAULT_LSPHP_VERSION", "83")
    monkeypatch.setenv("ISPANEL_SKIP_CERTBOT", "1")
    monkeypatch.setenv("ISPANEL_SYMLINK_TARGET", str(fake_lsws_conf / "ispanel-symlink"))
    return module


