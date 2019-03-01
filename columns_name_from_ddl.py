# DDL to SQL-table column name

import re

def main():

    handle = open("DDL.txt", "r")
    data = handle.read()

    new_str = re.sub("\w+\(\d+,?\d*\).*\n", ", ", data)                         # Types delete
    new_str = re.sub("-- .*\n", "", new_str)                                    # Comments delete
    new_str = re.sub("CREATE TABLE.*\n", "", new_str)                           # Create table delete
    new_str = re.sub("CREATE INDEX.*\n", "", new_str)                           # Create index delete
    new_str = re.sub("CONSTRAINT SYS_C\d*\sCHECK\s\(\w*\),?\n", "" , new_str)   # Checks delete
    new_str = re.sub("\s*\)\s*;\n", "" , new_str)                               # Braket delete
    new_str = re.sub(" ,\s*", ", ", new_str)                                    # Spaces delete

    handle.close()

    handle = open("result.txt", "w")
    handle.write(new_str)
    handle.close()

main()
