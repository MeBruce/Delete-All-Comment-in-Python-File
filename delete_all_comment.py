import re

def remove_comments(source_code):
    # Regex pattern สำหรับ single-line และ multi-line comments
    pattern = r"""
        # Single-line comment
        (?:\#.*?$) |
        # Multi-line comment
        (?:\'\'\'(?:.|\n)*?\'\'\') |
        (?:\"\"\"(?:.|\n)*?\"\"\")
    """

    # ลบคอมเมนต์ออกจาก source code
    cleaned_code = re.sub(pattern, '', source_code, flags=re.MULTILINE | re.VERBOSE)
    return cleaned_code

def main(input_file, output_file):
    # อ่านไฟล์ Python
    with open(input_file, 'r', encoding='utf-8') as file:
        source_code = file.read()

    # ลบคอมเมนต์
    cleaned_code = remove_comments(source_code)

    # บันทึกไฟล์ใหม่
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_code)

if __name__ == "__main__":
    input_file = 'input.py'   # ไฟล์ต้นฉบับ
    output_file = 'output.py' # ไฟล์ที่ลบคอมเมนต์แล้ว
    main(input_file, output_file)
