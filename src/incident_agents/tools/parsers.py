import csv
from typing import List, Dict, Any
from langchain.tools import tool

def read_csv_events(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", newline="") as f:
        return list(csv.DictReader(f))

@tool
def csv_parser_tool(file_path: str) -> List[Dict[str, Any]]:
    """Parse CSV security logs into structured events"""
    try:
        events = read_csv_events(file_path)
        return events
    except Exception as e:
        return [{"error": f"Failed to parse CSV: {str(e)}"}]

@tool
def data_validator_tool(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Validate data quality and completeness of security events"""
    if not events:
        return {"valid": False, "issues": ["No events found"]}
    
    issues = []
    required_fields = ["timestamp", "user", "source_ip", "event_type"]
    
    for i, event in enumerate(events):
        for field in required_fields:
            if field not in event or not event[field]:
                issues.append(f"Event {i}: Missing {field}")
    
    # Check data quality
    valid_count = len([e for e in events if all(field in e for field in required_fields)])
    total_count = len(events)
    
    return {
        "valid": len(issues) == 0,
        "total_events": total_count,
        "valid_events": valid_count,
        "issues": issues,
        "quality_score": valid_count / total_count if total_count > 0 else 0
    }
