import json
from pathlib import Path


def test_total_requests_count():
    """Instruction criterion: 'how many requests there were'"""
    assert Path("/app/report.json").exists(), "report.json not found"
    with open("/app/report.json") as f:
        data = json.load(f)
    assert "total_requests" in data, "total_requests field missing"
    assert data["total_requests"] == 6, f"Expected 6 total requests, got {data['total_requests']}"


def test_unique_clients():
    """Instruction criterion: 'the clients involved' (unique IPs)"""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert "unique_ips" in data, "unique_ips field missing"
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, got {data['unique_ips']}"


def test_popular_pages():
    """Instruction criterion: 'which pages were popular' (top path)"""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert "top_path" in data, "top_path field missing"
    assert data["top_path"] == "/index.html", f"Expected /index.html as top path, got {data['top_path']}"


def test_findings_saved():
    """Instruction criterion: 'Save your findings so they can be reviewed'"""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json not found at /app/report.json"
    assert report_path.stat().st_size > 0, "report.json is empty"

    # Verify valid JSON structure
    with open(report_path) as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must be a JSON object"
    assert len(data) > 0, "report.json must contain data"
