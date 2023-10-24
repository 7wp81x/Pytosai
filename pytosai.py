import re, os
import shutil
import zipfile
import binascii


def replace_strings(match):
    string_value = match.group(0)
    if '\\' in string_value or ('{' in string_value and '}' in string_value):
        return string_value
    replaced_value = ''
    for char in string_value[1:-1]:  # Exclude the quotes
        ascii_code = ord(char)
        replaced_value += f'\\x{ascii_code:02X}'
    return f'"{replaced_value}"'


def encode_variable_name(match):
    variable_name = match.group(1)
    variable_value = match.group(2)
    encoded_name = ''.join(format(ord(char), '02X') for char in variable_name)
    return f'globals()[bytes.fromhex("{encoded_name}").decode()] = {variable_value}'

def main():
    print("""\033[0;92m
     _____     _               _
    |  _  |_ _| |_ ___ ___ ___|_|
    |   __| | |  _| . |_ -| .'| |
    |__|  |_  |_| |___|___|__,|_|
          |___|

 \033[0m[\033[0;92m+\033[0m] Github: \033[4;92mhttps://github.com/MrP1r4t3\033[0m\n [\033[0;92m+\033[0m] Author: \033[4;92m7wp81x\033[0m\n""")
    file_name = input(" \033[0m[\033[0;92m?\033[0m] Enter Python file name: ")
    try:

        with open(file_name, 'r') as file:
            content = file.read()

        string_pattern = r'(?<!\\)(\'[^\']*\'|"[^"]*")'
        content_with_replaced_strings = re.sub(string_pattern, replace_strings, content)

        pattern = r'(\w+) = ([^=\n]+)'
        content_with_replaced_variables = re.sub(pattern, encode_variable_name, content_with_replaced_strings)

        output_script = f"""exec('import binascii');exec(binascii.a2b_hex('{binascii.b2a_hex(content_with_replaced_variables.encode()).decode()}').decode())"""
        print('\n \033[0m[\033[0;94m*\033[0m] Obfuscating...')
        with open("tmp.py", 'w') as output_file:
            output_file.write(output_script)


        shutil.move('tmp.py','__main__.py')
        print(' \033[0m[\033[0;94m*\033[0m] Compressing...')
        with zipfile.ZipFile('obfuscated.py', 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write('__main__.py')
        print(' \033[0m[\033[0;94m*\033[0m] Cleaning...')
        os.remove('__main__.py')
        print('\n \033[0m[\033[0;92m+\033[0m] Output: \033[4mobfuscated.py\033[0m')

    except FileNotFoundError:
        print(f"\n \033[0m[\033[0;91m!\033[0m] The file '{file_name}' was not found.")

if __name__ == '__main__':
    main()
