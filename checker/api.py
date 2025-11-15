# checker/api.py

import requests

def get_package_info(pkg_name):
    url = f"https://pypi.org/pypi/{pkg_name}/json"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None


def get_latest_version(pkg_name):
    data = get_package_info(pkg_name)
    if not data:
        return None
    return data["info"]["version"]


# ---------------------------
# NEW: Vulnerability scanning via OSV
# ---------------------------
def get_vulnerabilities_osv(pkg_name, version):
    url = "https://api.osv.dev/v1/query"

    payload = {
        "version": version,
        "package": {
            "name": pkg_name,
            "ecosystem": "PyPI"
        }
    }

    try:
        r = requests.post(url, json=payload, timeout=5)
        data = r.json()
    except:
        return []

    vulns = []
    for v in data.get("vulns", []):
        vulns.append({
            "id": v.get("id", "N/A"),
            "summary": v.get("summary", "No summary available."),
            "details": v.get("details", ""),
            "severity": v.get("severity", [])
        })

    return vulns

import requests
import time

def get_github_severity(ghsa_id,t,n):
    """Get severity from GitHub Security Advisories with proper authentication"""
    url = f"https://api.github.com/advisories/{ghsa_id}"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": str(n),  # Required by GitHub
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    # Optional: Add GitHub token for higher rate limits
    # Get a token from: https://github.com/settings/tokens (no special scopes needed)
    github_token = str(t)  # Optional but recommended
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            # Get CVSS score
            if 'cvss' in data and 'score' in data['cvss']:
                return data['cvss']['score']
            # Or get severity level
            elif 'severity' in data:
                return data['severity']
            return "N/A"
            
        elif response.status_code == 403:
            # Rate limited
            print(f"⚠️ Rate limited for {ghsa_id}. Waiting...")
            time.sleep(60)  # Wait 1 minute
            return "Rate Limited"
            
        else:
            print(f"❌ GitHub API error for {ghsa_id}: {response.status_code}")
            return "N/A"
            
    except Exception as e:
        print(f"❌ Error fetching {ghsa_id}: {e}")
        return "N/A"
