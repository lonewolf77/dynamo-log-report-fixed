import json
from pathlib import Path

def load_report():
    report_path = Path("/app/report.json")
    assert report_path.exists(), "/app/report.json does not exist"
    with open(report_path, "r") as f:
        return json.load(f)

def test_criterion_1_total_requests():
    """Criterion 1: The report contains a 'total_requests' key with the exact integer value of the total HTTP requests in the log."""
    data = load_report()
    assert "total_requests" in data, "Missing key: total_requests"
    assert data["total_requests"] == 6, f"Expected 6 total_requests, got {data['total_requests']}"

def test_criterion_2_unique_ips():
    """Criterion 2: The report contains a 'unique_ips' key with the exact integer value of the total unique client IP addresses."""
    data = load_report()
    assert "unique_ips" in data, "Missing key: unique_ips"
    assert data["unique_ips"] == 3, f"Expected 3 unique_ips, got {data['unique_ips']}"

def test_criterion_3_top_path():
    """Criterion 3: The report contains a 'top_path' key with the exact string value of the most frequently requested path."""
    data = load_report()
    assert "top_path" in data, "Missing key: top_path"
    assert data["top_path"] == "/index.html", f"Expected '/index.html' for top_path, got {data['top_path']}"
