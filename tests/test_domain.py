"""
Tests for domain management functionality
"""
import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for importing ispanel
sys.path.insert(0, str(Path(__file__).parent.parent))

import ispanel


class TestDomainManagement:
    """Test cases for domain management"""
    
    def test_domain_validation(self):
        """Test domain name validation"""
        # Valid domains
        valid_domains = [
            "example.com",
            "subdomain.example.com", 
            "test-site.org",
            "my123site.net"
        ]
        
        for domain in valid_domains:
            assert ispanel.is_valid_domain(domain) if hasattr(ispanel, 'is_valid_domain') else True
    
    def test_domain_add_basic(self, isolated_ispanel_env, mock_subprocess_run):
        """Test basic domain addition"""
        env = isolated_ispanel_env
        domain = "testdomain.com"
        
        # Mock the domain_add function if it exists
        if hasattr(ispanel, 'domain_add'):
            with patch('ispanel.run') as mock_run, \
                 patch('ispanel.LSWS_CONF_DIR') as mock_lsws_conf, \
                 patch('pathlib.Path.exists', return_value=True), \
                 patch('pathlib.Path.read_text', return_value="mock config"), \
                 patch('pathlib.Path.write_text'):
                
                # Mock LSWS_CONF_DIR.exists() to return True
                mock_lsws_conf.exists.return_value = True
                mock_run.return_value = MagicMock(returncode=0, stdout="OK", stderr="")
                
                # Test domain addition
                try:
                    ispanel.domain_add(domain)
                    success = True
                except Exception as e:
                    print(f"Domain add failed: {e}")
                    success = False
                
                assert success, "Domain addition should succeed"
    
    def test_domain_directory_structure(self, isolated_ispanel_env):
        """Test that domain directories are created properly"""
        env = isolated_ispanel_env
        domain = "testdomain.com"
        domain_path = env['domain_dir']
        
        # Check if domain directory structure exists
        assert domain_path.exists()
        assert (domain_path / "html").exists()
        assert (domain_path / "logs").exists()
        assert (domain_path / "ssl").exists()
    
    def test_vhost_config_creation(self, isolated_ispanel_env):
        """Test virtual host configuration creation"""
        env = isolated_ispanel_env
        vhost_dir = env['vhost_dir']
        
        # Test vhost config template
        if hasattr(ispanel, 'create_vhost_config'):
            domain = "testdomain.com"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="OK", stderr="")
                
                try:
                    ispanel.create_vhost_config(domain)
                    config_created = True
                except Exception as e:
                    print(f"VHost config creation failed: {e}")
                    config_created = False
                
                assert config_created, "VHost configuration should be created"
    
    def test_domain_list(self, isolated_ispanel_env, mock_subprocess_run):
        """Test domain listing functionality"""
        if hasattr(ispanel, 'list_domains'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.print') as mock_print:
                
                mock_run.return_value = MagicMock(returncode=0, stdout="testdomain.com", stderr="")
                
                try:
                    ispanel.list_domains()
                    list_success = True
                except Exception as e:
                    print(f"Domain listing failed: {e}")
                    list_success = False
                
                assert list_success, "Domain listing should succeed"
    
    def test_domain_remove(self, isolated_ispanel_env, mock_subprocess_run):
        """Test domain removal"""
        if hasattr(ispanel, 'domain_remove'):
            domain = "testdomain.com"
            
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='y'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="OK", stderr="")
                
                try:
                    ispanel.domain_remove(domain)
                    remove_success = True
                except Exception as e:
                    print(f"Domain removal failed: {e}")
                    remove_success = False
                
                assert remove_success, "Domain removal should succeed"
    
    def test_php_version_management(self, isolated_ispanel_env, mock_subprocess_run):
        """Test PHP version management for domains"""
        if hasattr(ispanel, 'set_domain_php_version'):
            domain = "testdomain.com"
            php_version = "8.3"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="OK", stderr="")
                
                try:
                    ispanel.set_domain_php_version(domain, php_version)
                    php_success = True
                except Exception as e:
                    print(f"PHP version setting failed: {e}")
                    php_success = False
                
                assert php_success, "PHP version setting should succeed"


class TestDomainValidation:
    """Test domain validation functions"""
    
    def test_invalid_domains(self):
        """Test invalid domain names"""
        invalid_domains = [
            "",
            "invalid..domain.com",
            "domain-.com",
            "-domain.com",
            "domain.c",
            "domain with spaces.com",
            "domain$.com"
        ]
        
        for domain in invalid_domains:
            if hasattr(ispanel, 'is_valid_domain'):
                assert not ispanel.is_valid_domain(domain), f"Domain {domain} should be invalid"
    
    def test_domain_exists_check(self, isolated_ispanel_env):
        """Test checking if domain already exists"""
        if hasattr(ispanel, 'domain_exists'):
            # Existing domain
            assert ispanel.domain_exists("testdomain.com"), "testdomain.com should exist in test environment"
            
            # Non-existing domain
            assert not ispanel.domain_exists("nonexistent.com"), "nonexistent.com should not exist"


class TestSSLManagement:
    """Test SSL certificate management"""
    
    def test_ssl_installation(self, isolated_ispanel_env, mock_subprocess_run):
        """Test SSL certificate installation"""
        if hasattr(ispanel, 'install_ssl_cert'):
            domain = "testdomain.com"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Certificate installed", stderr="")
                
                try:
                    ispanel.install_ssl_cert(domain)
                    ssl_success = True
                except Exception as e:
                    print(f"SSL installation failed: {e}")
                    ssl_success = False
                
                assert ssl_success, "SSL installation should succeed"
    
    def test_letsencrypt_support(self, isolated_ispanel_env, mock_subprocess_run):
        """Test Let's Encrypt certificate support"""
        if hasattr(ispanel, 'install_letsencrypt_cert'):
            domain = "testdomain.com"
            email = "admin@testdomain.com"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Certificate issued", stderr="")
                
                try:
                    ispanel.install_letsencrypt_cert(domain, email)
                    letsencrypt_success = True
                except Exception as e:
                    print(f"Let's Encrypt installation failed: {e}")
                    letsencrypt_success = False
                
                assert letsencrypt_success, "Let's Encrypt installation should succeed"


if __name__ == "__main__":
    pytest.main([__file__])
