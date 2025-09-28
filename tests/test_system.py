"""
Tests for system management and monitoring functionality
"""
import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for importing ispanel
sys.path.insert(0, str(Path(__file__).parent.parent))

import ispanel


class TestSystemManagement:
    """Test cases for system management"""
    
    def test_openlitespeed_installation(self, mock_subprocess_run):
        """Test OpenLiteSpeed installation"""
        if hasattr(ispanel, 'install_openlitespeed_only'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Installed", stderr="")
                
                try:
                    ispanel.install_openlitespeed_only()
                    installation_success = True
                except Exception as e:
                    print(f"OpenLiteSpeed installation failed: {e}")
                    installation_success = False
                
                assert installation_success, "OpenLiteSpeed installation should succeed"
    
    def test_mariadb_installation(self, mock_subprocess_run):
        """Test MariaDB installation"""
        if hasattr(ispanel, 'install_mariadb_only'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Installed", stderr="")
                
                try:
                    ispanel.install_mariadb_only()
                    installation_success = True
                except Exception as e:
                    print(f"MariaDB installation failed: {e}")
                    installation_success = False
                
                assert installation_success, "MariaDB installation should succeed"
    
    def test_service_status_check(self, mock_subprocess_run):
        """Test service status checking"""
        if hasattr(ispanel, 'show_service_status'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.print') as mock_print:
                
                mock_run.return_value = MagicMock(returncode=0, stdout="active", stderr="")
                
                try:
                    ispanel.show_service_status()
                    status_success = True
                except Exception as e:
                    print(f"Service status check failed: {e}")
                    status_success = False
                
                assert status_success, "Service status check should succeed"
    
    def test_service_restart(self, mock_subprocess_run):
        """Test service restart functionality"""
        if hasattr(ispanel, 'restart_services'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Restarted", stderr="")
                
                try:
                    ispanel.restart_services()
                    restart_success = True
                except Exception as e:
                    print(f"Service restart failed: {e}")
                    restart_success = False
                
                assert restart_success, "Service restart should succeed"


class TestSystemMonitoring:
    """Test system monitoring functionality"""
    
    def test_system_health_check(self, mock_subprocess_run):
        """Test system health check"""
        if hasattr(ispanel, 'system_health_check'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.print') as mock_print:
                
                # Mock various system commands
                def mock_run_func(cmd, *args, **kwargs):
                    if 'systemctl status' in cmd:
                        return MagicMock(returncode=0, stdout="active", stderr="")
                    elif 'df' in cmd:
                        return MagicMock(returncode=0, stdout="/dev/sda1  100G  10G  85G  11% /", stderr="")
                    elif 'free' in cmd:
                        return MagicMock(returncode=0, stdout="Mem: 8000000 2000000 6000000", stderr="")
                    else:
                        return MagicMock(returncode=0, stdout="OK", stderr="")
                
                mock_run.side_effect = mock_run_func
                
                try:
                    ispanel.system_health_check()
                    health_check_success = True
                except Exception as e:
                    print(f"System health check failed: {e}")
                    health_check_success = False
                
                assert health_check_success, "System health check should succeed"
    
    def test_disk_usage_monitoring(self, mock_subprocess_run):
        """Test disk usage monitoring"""
        if hasattr(ispanel, 'check_disk_usage'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(
                    returncode=0, 
                    stdout="/dev/sda1  100G  10G  85G  11% /", 
                    stderr=""
                )
                
                try:
                    disk_info = ispanel.check_disk_usage()
                    monitoring_success = True
                except Exception as e:
                    print(f"Disk monitoring failed: {e}")
                    monitoring_success = False
                
                assert monitoring_success, "Disk usage monitoring should succeed"
    
    def test_memory_monitoring(self, mock_subprocess_run):
        """Test memory usage monitoring"""
        if hasattr(ispanel, 'check_memory_usage'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(
                    returncode=0,
                    stdout="             total       used       free\nMem:       8000000    2000000    6000000",
                    stderr=""
                )
                
                try:
                    memory_info = ispanel.check_memory_usage()
                    monitoring_success = True
                except Exception as e:
                    print(f"Memory monitoring failed: {e}")
                    monitoring_success = False
                
                assert monitoring_success, "Memory usage monitoring should succeed"


class TestSystemOptimization:
    """Test system optimization functionality"""
    
    def test_openlitespeed_optimization(self, mock_subprocess_run):
        """Test OpenLiteSpeed optimization"""
        if hasattr(ispanel, 'optimize_openlitespeed'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Optimized", stderr="")
                
                try:
                    ispanel.optimize_openlitespeed()
                    optimization_success = True
                except Exception as e:
                    print(f"OpenLiteSpeed optimization failed: {e}")
                    optimization_success = False
                
                assert optimization_success, "OpenLiteSpeed optimization should succeed"
    
    def test_php_optimization(self, mock_subprocess_run):
        """Test PHP optimization"""
        if hasattr(ispanel, 'optimize_php_performance'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Optimized", stderr="")
                
                try:
                    ispanel.optimize_php_performance()
                    optimization_success = True
                except Exception as e:
                    print(f"PHP optimization failed: {e}")
                    optimization_success = False
                
                assert optimization_success, "PHP optimization should succeed"
    
    def test_system_level_optimization(self, mock_subprocess_run):
        """Test system-level optimization"""
        if hasattr(ispanel, 'optimize_system_level'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Optimized", stderr="")
                
                try:
                    ispanel.optimize_system_level()
                    optimization_success = True
                except Exception as e:
                    print(f"System-level optimization failed: {e}")
                    optimization_success = False
                
                assert optimization_success, "System-level optimization should succeed"


class TestBackupSystem:
    """Test backup and recovery functionality"""
    
    def test_emergency_backup(self, mock_subprocess_run):
        """Test emergency backup creation"""
        if hasattr(ispanel, 'emergency_backup'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Backup created", stderr="")
                
                try:
                    ispanel.emergency_backup()
                    backup_success = True
                except Exception as e:
                    print(f"Emergency backup failed: {e}")
                    backup_success = False
                
                assert backup_success, "Emergency backup should succeed"
    
    def test_domain_backup(self, mock_subprocess_run):
        """Test domain backup functionality"""
        if hasattr(ispanel, 'backup_domain'):
            domain = "testdomain.com"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Domain backed up", stderr="")
                
                try:
                    ispanel.backup_domain(domain)
                    backup_success = True
                except Exception as e:
                    print(f"Domain backup failed: {e}")
                    backup_success = False
                
                assert backup_success, "Domain backup should succeed"
    
    def test_auto_backup_system(self, mock_subprocess_run):
        """Test automatic backup system setup"""
        if hasattr(ispanel, 'auto_backup_system'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='y'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Cron job added", stderr="")
                
                try:
                    ispanel.auto_backup_system()
                    auto_backup_success = True
                except Exception as e:
                    print(f"Auto backup setup failed: {e}")
                    auto_backup_success = False
                
                assert auto_backup_success, "Auto backup setup should succeed"


class TestSecurityFeatures:
    """Test security features"""
    
    def test_firewall_management(self, mock_subprocess_run):
        """Test firewall management"""
        if hasattr(ispanel, 'manage_firewall'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='1'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Firewall configured", stderr="")
                
                try:
                    ispanel.manage_firewall()
                    firewall_success = True
                except Exception as e:
                    print(f"Firewall management failed: {e}")
                    firewall_success = False
                
                assert firewall_success, "Firewall management should succeed"
    
    def test_ssl_support_installation(self, mock_subprocess_run):
        """Test SSL support installation"""
        if hasattr(ispanel, 'install_ssl_support'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="SSL support installed", stderr="")
                
                try:
                    ispanel.install_ssl_support()
                    ssl_success = True
                except Exception as e:
                    print(f"SSL support installation failed: {e}")
                    ssl_success = False
                
                assert ssl_success, "SSL support installation should succeed"


class TestUpdateSystem:
    """Test update functionality"""
    
    def test_ispanel_update(self, mock_subprocess_run):
        """Test isPanel update functionality"""
        if hasattr(ispanel, 'update_ispanel'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='n'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Already up to date", stderr="")
                
                try:
                    ispanel.update_ispanel()
                    update_success = True
                except Exception as e:
                    print(f"isPanel update failed: {e}")
                    update_success = False
                
                assert update_success, "isPanel update should succeed"


if __name__ == "__main__":
    pytest.main([__file__])
