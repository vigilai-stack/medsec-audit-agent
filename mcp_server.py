import os
import sys
import json
import re
import hashlib
import time
from typing import Dict, Any, Tuple
from mcp.server.fastmcp import FastMCP

# Define central configuration
class Config:
    WORKSPACE_DIR = "./medsec_sandbox"
    ENCRYPTION_ENABLED = True
    PII_MASKING_ENABLED = True
    AUDIT_LOG_ENABLED = True
    
    PHI_PATTERNS = {
        "name": r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
        "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
        "dob": r'\b\d{2}/\d{2}/\d{4}\b',
        "phone": r'\b\d{3}-\d{3}-\d{4}\b',
        "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "mrn": r'\bMRN-\d{6,}\b',
        "address": r'\b\d{1,5}\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln|Court|Ct)\b'
    }

class SecurityUtils:
    @staticmethod
    def mask_phi(text: str) -> Tuple[str, Dict]:
        masked_text = text
        phi_found = {}
        for phi_type, pattern in Config.PHI_PATTERNS.items():
            matches = re.findall(pattern, masked_text)
            if matches:
                phi_found[phi_type] = matches
                for match in matches:
                    placeholder = f"[[{phi_type.upper()}_{hashlib.md5(match.encode()).hexdigest()[:8]}]]"
                    masked_text = masked_text.replace(match, placeholder)
        return masked_text, phi_found

    @staticmethod
    def validate_input_safety(text: str) -> bool:
        dangerous_patterns = [r'<script', r'javascript:', r'DROP TABLE', r';--', r'--', r'/\*', r'\*/']
        for pattern in dangerous_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return False
        return True

# Initialize FastMCP
mcp = FastMCP("Med-Sec Audit Agent Tools")

@mcp.tool()
def anonymize_patient_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymize patient records by masking all PHI fields (name, ssn, dob, phone, email, mrn, address).
    """
    start_time = time.perf_counter()
    try:
        result = {"status": "success", "anonymized_record": {}, "phi_found": {}, "original_phi_count": 0}
        for key, value in record.items():
            if isinstance(value, str):
                masked_value, phi_found = SecurityUtils.mask_phi(value)
                result["anonymized_record"][key] = masked_value
                if phi_found:
                    result["phi_found"].update(phi_found)
                    result["original_phi_count"] += len(phi_found)
            else:
                result["anonymized_record"][key] = value
        result["runtime_ms"] = (time.perf_counter() - start_time) * 1000
        return result
    except Exception as e:
        return {"status": "error", "error": str(e), "runtime_ms": (time.perf_counter() - start_time) * 1000}

@mcp.tool()
def detect_threat(log_data: str) -> Dict[str, Any]:
    """
    Scan system log data for security threats such as SQL injection, unusual PHI accesses, or other anomalies.
    """
    start_time = time.perf_counter()
    try:
        threats = []
        risk_score = 0.0

        phi_accesses = re.findall(r'access.*PHI|view.*patient|read.*record', log_data, re.IGNORECASE)
        if len(phi_accesses) > 10:
            threats.append(f"Unusual PHI access pattern: {len(phi_accesses)} accesses")
            risk_score += 0.3

        injection_patterns = ["' OR '1'='1", "; DROP TABLE", "UNION SELECT"]
        for pattern in injection_patterns:
            if pattern in log_data:
                threats.append(f"Potential SQL injection attempt: {pattern}")
                risk_score += 0.5

        return {
            "status": "success",
            "threats_found": threats,
            "risk_score": min(1.0, risk_score),
            "threat_count": len(threats),
            "severity": "HIGH" if risk_score > 0.7 else "MEDIUM" if risk_score > 0.3 else "LOW",
            "runtime_ms": (time.perf_counter() - start_time) * 1000
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

@mcp.tool()
def compliance_check(record: Dict[str, Any], standard: str = "HIPAA") -> Dict[str, Any]:
    """
    Validate a patient record compliance level against HIPAA security and privacy rules.
    """
    start_time = time.perf_counter()
    try:
        compliance_issues = []
        passed_checks = 0
        total_checks = 0

        record_str = json.dumps(record)
        masked, phi_found = SecurityUtils.mask_phi(record_str)
        if phi_found:
            compliance_issues.append(f"PHI detected in record: {list(phi_found.keys())}")
        else:
            passed_checks += 1
        total_checks += 1

        if Config.ENCRYPTION_ENABLED:
            passed_checks += 1
        else:
            compliance_issues.append("Encryption disabled")
        total_checks += 1

        if Config.AUDIT_LOG_ENABLED:
            passed_checks += 1
        else:
            compliance_issues.append("Audit logging disabled")
        total_checks += 1

        compliance_score = passed_checks / max(total_checks, 1)
        return {
            "status": "success",
            "standard": standard,
            "compliance_score": compliance_score,
            "passed_checks": passed_checks,
            "total_checks": total_checks,
            "issues_found": compliance_issues,
            "compliant": compliance_score >= 0.8,
            "runtime_ms": (time.perf_counter() - start_time) * 1000
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    mcp.run()
