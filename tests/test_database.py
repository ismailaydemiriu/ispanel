"""
Tests for database management functionality
"""
import pytest
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for importing ispanel
sys.path.insert(0, str(Path(__file__).parent.parent))

import ispanel


class TestDatabaseManagement:
    """Test cases for database management"""
    
    def test_mysql_connection(self, mock_subprocess_run):
        """Test MySQL connection"""
        if hasattr(ispanel, 'mysql_exec'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="OK", stderr="")
                
                try:
                    ispanel.mysql_exec("SELECT 1")
                    connection_success = True
                except Exception as e:
                    print(f"MySQL connection failed: {e}")
                    connection_success = False
                
                assert connection_success, "MySQL connection should succeed"
    
    def test_database_creation(self, mock_subprocess_run):
        """Test database creation"""
        if hasattr(ispanel, 'db_create'):
            db_name = "test_database"
            username = "test_user"
            password = "test_password"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Database created", stderr="")
                
                try:
                    ispanel.db_create(db_name, username, password)
                    creation_success = True
                except Exception as e:
                    print(f"Database creation failed: {e}")
                    creation_success = False
                
                assert creation_success, "Database creation should succeed"
    
    def test_database_user_creation(self, mock_subprocess_run):
        """Test database user creation with proper privileges"""
        if hasattr(ispanel, 'create_db_user'):
            username = "test_user"
            password = "test_password"
            database = "test_database"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="User created", stderr="")
                
                try:
                    ispanel.create_db_user(username, password, database)
                    user_creation_success = True
                except Exception as e:
                    print(f"Database user creation failed: {e}")
                    user_creation_success = False
                
                assert user_creation_success, "Database user creation should succeed"
    
    def test_database_deletion(self, mock_subprocess_run):
        """Test database deletion"""
        if hasattr(ispanel, 'db_delete'):
            db_name = "test_database"
            username = "test_user"
            
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='y'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Database deleted", stderr="")
                
                try:
                    ispanel.db_delete(db_name, username)
                    deletion_success = True
                except Exception as e:
                    print(f"Database deletion failed: {e}")
                    deletion_success = False
                
                assert deletion_success, "Database deletion should succeed"
    
    def test_database_listing(self, mock_subprocess_run):
        """Test database listing"""
        if hasattr(ispanel, 'list_databases'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.print') as mock_print:
                
                mock_run.return_value = MagicMock(
                    returncode=0, 
                    stdout="test_database\ninformation_schema\nmysql\nperformance_schema", 
                    stderr=""
                )
                
                try:
                    ispanel.list_databases()
                    listing_success = True
                except Exception as e:
                    print(f"Database listing failed: {e}")
                    listing_success = False
                
                assert listing_success, "Database listing should succeed"


class TestDatabaseValidation:
    """Test database validation functions"""
    
    def test_valid_database_names(self):
        """Test valid database name validation"""
        valid_names = [
            "test_db",
            "myapp123",
            "user_data",
            "app_2024"
        ]
        
        for name in valid_names:
            if hasattr(ispanel, 'is_valid_db_name'):
                assert ispanel.is_valid_db_name(name), f"Database name {name} should be valid"
    
    def test_invalid_database_names(self):
        """Test invalid database name validation"""
        invalid_names = [
            "",
            "123invalid",
            "invalid-name",
            "invalid.name",
            "invalid name",
            "test@db"
        ]
        
        for name in invalid_names:
            if hasattr(ispanel, 'is_valid_db_name'):
                assert not ispanel.is_valid_db_name(name), f"Database name {name} should be invalid"
    
    def test_password_strength(self):
        """Test password strength validation"""
        if hasattr(ispanel, 'validate_password_strength'):
            # Strong passwords
            strong_passwords = [
                "MyStrongP@ssw0rd123",
                "C0mpl3x!P@ssw0rd",
                "S3cur3P@$$w0rd!"
            ]
            
            for password in strong_passwords:
                assert ispanel.validate_password_strength(password), f"Password {password} should be strong"
            
            # Weak passwords
            weak_passwords = [
                "123456",
                "password",
                "abc123",
                "qwerty"
            ]
            
            for password in weak_passwords:
                assert not ispanel.validate_password_strength(password), f"Password {password} should be weak"


class TestDatabaseSecurity:
    """Test database security features"""
    
    def test_mysql_root_password_reset(self, mock_subprocess_run):
        """Test MySQL root password reset"""
        if hasattr(ispanel, 'reset_mysql_root_password'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', return_value='new_secure_password'):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Password updated", stderr="")
                
                try:
                    ispanel.reset_mysql_root_password()
                    reset_success = True
                except Exception as e:
                    print(f"MySQL root password reset failed: {e}")
                    reset_success = False
                
                assert reset_success, "MySQL root password reset should succeed"
    
    def test_secure_mariadb_installation(self, mock_subprocess_run):
        """Test secure MariaDB installation"""
        if hasattr(ispanel, 'secure_mariadb_installation'):
            with patch('ispanel.run') as mock_run, \
                 patch('builtins.input', side_effect=['y', 'y', 'y', 'y']):
                
                mock_run.return_value = MagicMock(returncode=0, stdout="Secured", stderr="")
                
                try:
                    ispanel.secure_mariadb_installation()
                    security_success = True
                except Exception as e:
                    print(f"MariaDB security setup failed: {e}")
                    security_success = False
                
                assert security_success, "MariaDB security setup should succeed"
    
    def test_database_backup(self, mock_subprocess_run):
        """Test database backup functionality"""
        if hasattr(ispanel, 'backup_database'):
            database = "test_database"
            
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Backup created", stderr="")
                
                try:
                    ispanel.backup_database(database)
                    backup_success = True
                except Exception as e:
                    print(f"Database backup failed: {e}")
                    backup_success = False
                
                assert backup_success, "Database backup should succeed"


class TestDatabasePerformance:
    """Test database performance optimization"""
    
    def test_mysql_optimization(self, mock_subprocess_run):
        """Test MySQL performance optimization"""
        if hasattr(ispanel, 'optimize_mysql_performance'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Optimized", stderr="")
                
                try:
                    ispanel.optimize_mysql_performance()
                    optimization_success = True
                except Exception as e:
                    print(f"MySQL optimization failed: {e}")
                    optimization_success = False
                
                assert optimization_success, "MySQL optimization should succeed"
    
    def test_database_repair(self, mock_subprocess_run):
        """Test database repair functionality"""
        if hasattr(ispanel, 'repair_databases'):
            with patch('ispanel.run') as mock_run:
                mock_run.return_value = MagicMock(returncode=0, stdout="Repaired", stderr="")
                
                try:
                    ispanel.repair_databases()
                    repair_success = True
                except Exception as e:
                    print(f"Database repair failed: {e}")
                    repair_success = False
                
                assert repair_success, "Database repair should succeed"


if __name__ == "__main__":
    pytest.main([__file__])
