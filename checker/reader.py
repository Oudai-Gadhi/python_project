# checker/reader.py

def read_requirements(path):
    deps = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if "==" in line:
                name, version = line.split("==")
                deps[name.strip()] = version.strip()
            else:
                # Format non géré
                print(f"[!] Format inconnu ignoré : {line}")

    return deps

