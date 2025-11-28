# Python Dependency Vulnerability Checker 🔍🛡️

A command-line tool that analyzes Python project dependencies for outdated packages and known security vulnerabilities. The tool integrates with PyPI for version checking and OSV (Open Source Vulnerabilities) database for comprehensive vulnerability scanning.

## Features

✨ **Key Capabilities:**
- 📦 Reads dependencies from `requirements.txt`
- 🔄 Checks latest available versions on PyPI
- 🛡️ Scans for known vulnerabilities using OSV database
- 🎨 Color-coded severity ratings (Critical, High, Medium, Low)
- 🔍 Detailed vulnerability information from GitHub Security Advisories
- ⚡ Fast and efficient API-based scanning

## Prerequisites

- Python 3.6+
- GitHub Personal Access Token (for enhanced vulnerability details)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Oudai-Gadhi/python_project.git
cd python_project
```

2. Install required dependencies:
```bash
pip install requests packaging
```

3. Generate a GitHub Personal Access Token:
   - Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - No special permissions needed for public advisory data
   - Copy the token for use with the tool

## Usage

Basic command structure:
```bash
python3 main.py -n <GITHUB_USERNAME> -t <GITHUB_TOKEN> --file <PATH_TO_REQUIREMENTS>
```

### Example

```bash
python3 main.py -n Oudai-Gadhi -t ghp_YourTokenHere --file req.txt
```

### Sample Output

```
[+] Reading dependencies...
[+] Checking online versions and vulnerabilities...

=== Dependency Report ===

📦 django
   Installed : 2.2.0
   Latest    : 5.2.8
   Status    : VULNERABLE
   ⚠️ Vulnerabilities found:
      - GHSA-xxxx-yyyy-zzzz: 9.8 :SQL injection vulnerability in Django admin...: ---> CRITICAL
      - CVE-2023-12345: 7.5 :Cross-site scripting (XSS) vulnerability...: ---> HIGH

📦 requests
   Installed : 2.28.0
   Latest    : 2.31.0
   Status    : Outdated

📦 flask
   Installed : 2.3.0
   Latest    : 2.3.0
   Status    : Up-to-date
```

## Project Structure

```
python_project/
├── main.py                 # Entry point
├── req.txt                 # Sample requirements file
├── checker/
│   ├── reader.py          # Parses requirements.txt
│   ├── api.py             # API integrations (PyPI, OSV, GitHub)
│   ├── analyzer.py        # Dependency analysis logic
│   ├── report.py          # Report generation
│   └── utilities.py       # Utility functions (severity classification)
└── README.md
```

## Severity Levels

The tool classifies vulnerabilities using CVSS scores:

| Score | Severity | Color |
|-------|----------|-------|
| 9.0+ | 🔴 CRITICAL | Red |
| 7.0-8.9 | 🟡 HIGH | Yellow |
| 4.0-6.9 | 🟠 MEDIUM | Orange |
| 0.1-3.9 | 🟢 LOW | Green |

## Command-Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--file` | Yes | Path to your requirements.txt file |
| `-n` | Yes | Your GitHub username |
| `-t` | Yes | Your GitHub Personal Access Token |

## API Integrations

- **PyPI**: Package version information
- **OSV (Open Source Vulnerabilities)**: Comprehensive vulnerability database
- **GitHub Security Advisories**: Detailed severity scores and descriptions

## Requirements File Format

The tool supports standard `requirements.txt` format:

```txt
django==2.2.0
requests==2.28.0
flask==2.3.0

```



## Limitations

- Requires active internet connection for API calls
- GitHub API rate limits apply (60 requests/hour without token, 5000 with token)

## Troubleshooting

### 401 Unauthorized Error
Your GitHub token is invalid or expired. Generate a new one at https://github.com/settings/tokens

### Rate Limited
If you see rate limit warnings, wait a minute or ensure you're using a valid GitHub token for higher limits.

### Package Not Found
The package may not exist on PyPI or the name is misspelled in your requirements file.



## License

This project is open source and available under the MIT License.

## Author

**Oudai Gadhi**

GitHub: [@Oudai-Gadhi](https://github.com/Oudai-Gadhi)

## Acknowledgments

- [OSV](https://osv.dev/) - Open Source Vulnerabilities database
- [PyPI](https://pypi.org/) - Python Package Index
- [GitHub Security Advisories](https://github.com/advisories) - Vulnerability information

---

⭐ If you find this tool useful, please consider giving it a star on GitHub!
