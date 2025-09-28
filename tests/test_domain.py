"""Domain management tests for isPanel."""

from pathlib import Path

import pytest


def test_domain_add_creates_structure(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    ispanel_module,
):
    created_commands = []

    def fake_run(cmd: str, check: bool = True):  # type: ignore[override]
        created_commands.append(cmd)
        class Result:
            returncode = 0

        return Result()

    monkeypatch.setattr(ispanel_module, "run", fake_run)
    monkeypatch.setattr(ispanel_module.shutil, "which", lambda _: None)

    domain = "example.com"
    ispanel_module.domain_add(domain)

    docroot = ispanel_module.DOCROOT_BASE / domain / "public_html"
    assert docroot.exists()
    assert (docroot / "index.php").exists()

    vhost_conf = ispanel_module.VHOSTS_DIR / domain / "vhost.conf"
    assert vhost_conf.exists()
    content = vhost_conf.read_text(encoding="utf-8")
    assert "docRoot $VH_ROOT/public_html/" in content


def test_domain_add_rejects_invalid_domain(ispanel_module):
    with pytest.raises(SystemExit):
        ispanel_module.domain_add("not valid")

