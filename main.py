# main.py

import argparse
from checker.reader import read_requirements
from checker import api
from checker.analyzer import analyze_dependencies
from checker.report import print_report

def main():
    parser = argparse.ArgumentParser(description="Dependency Checker")
    parser.add_argument("--file", required=True, help="Path to requirements.txt")
    args = parser.parse_args()

    print("[+] Reading dependencies...")
    deps = read_requirements(args.file)

    print("[+] Checking online versions and vulnerabilities...")
    results = analyze_dependencies(deps, api)

    print_report(results)


if __name__ == "__main__":
    main()

