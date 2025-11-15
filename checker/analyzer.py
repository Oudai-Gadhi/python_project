# checker/analyzer.py

from packaging import version

def analyze_dependencies(local_deps, api_module):
    results = []

    for pkg, local_version in local_deps.items():
        latest = api_module.get_latest_version(pkg)
        vulns = api_module.get_vulnerabilities_osv(pkg, local_version)

        if latest is None:
            status = "Not found on PyPI"
        elif version.parse(local_version) < version.parse(latest):
            status = "Outdated"
        else:
            status = "Up-to-date"

        if vulns:
            status = "VULNERABLE"

        results.append({
            "package": pkg,
            "local": local_version,
            "latest": latest,
            "status": status,
            "vulns": vulns
        })

    return results

