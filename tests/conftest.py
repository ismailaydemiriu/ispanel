"""
pytest configuration and fixtures for isPanel testing
"""
import pytest
import tempfile
import shutil
from pathlib import Path
import os
import sys

# Add the parent directory to sys.path to import ispanel
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing"""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def mock_ols_config_dir(temp_dir):
    """Create a mock OpenLiteSpeed configuration directory"""
    ols_config = temp_dir / "usr" / "local" / "lsws" / "conf"
    ols_config.mkdir(parents=True, exist_ok=True)
    
    # Create mock configuration files
    (ols_config / "httpd_config.conf").write_text("""
docRoot                   $VH_ROOT/html/
index  {
  useServer               0
  indexFiles              index.php, index.html
}

errorlog $SERVER_ROOT/logs/error.log {
  useServer               0
  logLevel                WARN
  rollingSize             10M
}

accesslog $SERVER_ROOT/logs/access.log {
  useServer               0
  logFormat               "%h %l %u %t \\"%r\\" %>s %b"
  logHeaders              5
  rollingSize             10M
  keepDays                10  
  compressArchive         1
}
""")
    
    return ols_config


@pytest.fixture
def mock_vhost_dir(temp_dir):
    """Create a mock virtual host directory"""
    vhost_dir = temp_dir / "usr" / "local" / "lsws" / "conf" / "vhosts"
    vhost_dir.mkdir(parents=True, exist_ok=True)
    return vhost_dir


@pytest.fixture
def mock_domain_dir(temp_dir):
    """Create a mock domain directory"""
    domain_dir = temp_dir / "home" / "testdomain.com"
    domain_dir.mkdir(parents=True, exist_ok=True)
    
    # Create domain structure
    (domain_dir / "html").mkdir()
    (domain_dir / "logs").mkdir()
    (domain_dir / "ssl").mkdir()
    
    # Create index.php
    (domain_dir / "html" / "index.php").write_text("""<?php
echo "Hello from testdomain.com!";
phpinfo();
?>""")
    
    return domain_dir


@pytest.fixture
def mock_mysql_config():
    """Mock MySQL configuration"""
    return {
        'host': 'localhost',
        'user': 'root',
        'password': 'test_password',
        'database': 'test_db'
    }


@pytest.fixture
def isolated_ispanel_env(temp_dir, mock_ols_config_dir, mock_vhost_dir, mock_domain_dir, monkeypatch):
    """
    Create an isolated environment for ispanel testing
    """
    # Mock environment variables and paths
    monkeypatch.setenv('ISPANEL_TEST_MODE', '1')
    monkeypatch.setenv('ISPANEL_OLS_CONFIG_PATH', str(mock_ols_config_dir))
    monkeypatch.setenv('ISPANEL_VHOST_PATH', str(mock_vhost_dir))
    monkeypatch.setenv('ISPANEL_DOMAIN_PATH', str(temp_dir / "home"))
    
    # Mock common paths in ispanel module
    import ispanel
    if hasattr(ispanel, 'OLS_CONFIG_PATH'):
        monkeypatch.setattr(ispanel, 'OLS_CONFIG_PATH', str(mock_ols_config_dir))
    if hasattr(ispanel, 'VHOST_PATH'):
        monkeypatch.setattr(ispanel, 'VHOST_PATH', str(mock_vhost_dir))
    if hasattr(ispanel, 'DOMAIN_PATH'):
        monkeypatch.setattr(ispanel, 'DOMAIN_PATH', str(temp_dir / "home"))
    
    return {
        'temp_dir': temp_dir,
        'ols_config': mock_ols_config_dir,
        'vhost_dir': mock_vhost_dir,
        'domain_dir': mock_domain_dir
    }


@pytest.fixture
def mock_subprocess_run(monkeypatch):
    """Mock subprocess.run to avoid executing actual system commands"""
    import subprocess
    
    def mock_run(command, *args, **kwargs):
        """Mock subprocess run with common command responses"""
        
        # Mock successful responses
        if isinstance(command, str):
            if 'systemctl status' in command:
                return subprocess.CompletedProcess(
                    args=command,
                    returncode=0,
                    stdout="active",
                    stderr=""
                )
            elif 'mysql' in command and '-e' in command:
                return subprocess.CompletedProcess(
                    args=command,
                    returncode=0,
                    stdout="Query OK",
                    stderr=""
                )
            elif 'git' in command:
                return subprocess.CompletedProcess(
                    args=command,
                    returncode=0,
                    stdout="main",
                    stderr=""
                )
            elif 'df' in command:
                return subprocess.CompletedProcess(
                    args=command,
                    returncode=0,
                    stdout="/dev/sda1  100G  10G  85G  11% /",
                    stderr=""
                )
            elif 'free' in command:
                return subprocess.CompletedProcess(
                    args=command,
                    returncode=0,
                    stdout="             total       used       free\nMem:       8000000    2000000    6000000",
                    stderr=""
                )
        
        # Default successful response
        return subprocess.CompletedProcess(
            args=command,
            returncode=0,
            stdout="OK",
            stderr=""
        )
    
    monkeypatch.setattr(subprocess, 'run', mock_run)
    return mock_run
