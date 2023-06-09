# NetScape-To-JSON (Not Universial)
A simple script coded in Python 3.11 to convert NetScape 7 Item Arrays into formatted JSON Index [for importing]
# Format
JSON Format
```python
f.write(f'  {{\n'
        f'    "name": "{s[5]}",\n'
        f'    "value": "{s[6]}",\n'
        f'    "domain": "{s[0]}",\n'
        f'    "path": "{s[2]}",\n'
        f'    "expirationDate": {s[4]},\n'
        f'    "secure": {str(s[1]).lower()}\n'
        f'  }}' + (',' if i < len(lines) - 1 else '') + '\n')
```
