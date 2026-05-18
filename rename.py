import os
import sys

replacements = {
    "Connect AI Lab": "Os Studio",
    "connect-ai-lab": "os-studio",
    "connectAiLab": "osStudio",
    "ConnectAiLab": "OsStudio",
    "connectailab": "osstudio",
    "Connect AI": "Os Studio",
    "Connect-AI": "Os-Studio",
    "connect-ai": "os-studio",
    "ConnectAI": "OsStudio",
    "Connectai": "Osstudio",
    "CONNECT_AI": "OS_STUDIO"
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for k, v in replacements.items():
            new_content = new_content.replace(k, v)
            
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}", flush=True)
    except UnicodeDecodeError:
        # Not a text file, skip
        pass
    except Exception as e:
        print(f"Error reading {filepath}: {e}", flush=True)

print("Starting replacement...", flush=True)

for root, dirs, files in os.walk('.'):
    # skip .git, node_modules, and assets
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if 'assets' in dirs:
        dirs.remove('assets')
        
    for file in files:
        if file == "rename.py":
            continue
        filepath = os.path.join(root, file)
        replace_in_file(filepath)

print("Finished replacement.", flush=True)
