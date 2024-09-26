import pytest
import test_script

def test_leave_organization():
    result = test_script.leave_organization().strip()
    assert result == "Denied to leave the organization. Error: Access Denied"

def test_create_login_profile():
    result = test_script.create_login_profile().strip()
    assert result == "Denied to create login profile. Error: Access Denied"

def test_create_access_key():
    result = test_script.create_access_key().strip()
    assert result == "Denied to create access key. Error: Access Denied"

def test_delete_s3_bucket():
    result = test_script.delete_s3_bucket().strip()
    assert result == "Denied to delete S3 bucket. Error: Access Denied"

def test_stop_cloudtrail_logging():
    result = test_script.stop_cloudtrail_logging().strip()
    assert result == "Denied to stop CloudTrail logging. Error: Access Denied"

def test_delete_config_recorder():
    result = test_script.delete_config_recorder().strip()
    assert result == "Denied to delete configuration recorder. Error: Access Denied"

if __name__ == "__main__":
    pytest.main(["--json-report", "--json-report-file=report.json"])

