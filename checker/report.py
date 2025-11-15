# checker/report.py
from checker.api import *
from checker.utilities import *
def print_report(results,t,n):
    print("\n=== Dependency Report ===\n")

    for r in results:
        print(f"📦 {r['package']}")
        print(f"   Installed : {r['local']}")
        print(f"   Latest    : {r['latest']}")
        print(f"   Status    : {r['status']}")

        if r["vulns"]:
            print("   ⚠️ Vulnerabilities found:")
            for v in r["vulns"]:
                if 'GHSA' in v['id']:
                    sev= get_github_severity(v['id'],t,n)
                    print(f"      - {v['id']}: {sev} :{v['summary'][:80]}...: ---> {classify(sev)}")
        print("")


