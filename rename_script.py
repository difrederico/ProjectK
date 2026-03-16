import os
import re

search_dir = r'c:\Users\fredericolemes.ps\.gemini\antigravity\scratch\CogniKids'

patterns = [
    (re.compile(r'CogniKids'), 'Project-CK'),
    (re.compile(r'cognikids'), 'project-ck'),
    (re.compile(r'COGNIKIDS'), 'PROJECT-CK')
]

for root, dirs, files in os.walk(search_dir):
    if '.git' in root or '.gemini' in root:
        continue
        
    for file in files:
        if file.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.gif', '.pyc')):
            continue
            
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            for pattern, replacement in patterns:
                new_content = pattern.sub(replacement, new_content)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filepath}')
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='latin-1') as f:
                    content = f.read()
                new_content = content
                for pattern, replacement in patterns:
                    new_content = pattern.sub(replacement, new_content)
                if new_content != content:
                    with open(filepath, 'w', encoding='latin-1') as f:
                        f.write(new_content)
                    print(f'Updated (latin-1) {filepath}')
            except Exception as e:
                print(f'Failed completely on {filepath}: {e}')
        except Exception as e:
            print(f'Could not process {filepath}: {e}')
