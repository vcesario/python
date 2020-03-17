"""
IDEIA DO ALGORITMO

1. abrir xml e carregar dict com ids e valores
2. iterar por todos os .xml e substituir #ID pelo valor
"""

import os
import re

rootpath = ''

if not os.path.exists(rootpath):
    exit()

iddict = dict()

# load xml
with open('dump.txt', mode='w', encoding='utf8') as dump:
    for filename in os.listdir(rootpath):
        if (filename.startswith('AR_') and filename.endswith('.xml')):
            print(filename, file=dump)
            print('==========================================', file=dump)
            with open(rootpath + filename, mode='r', encoding='utf8') as xml:
                linelist = xml.read().splitlines()
                pattern = r'<entry name=\"([A-Z_0-9]+)\">([^\<]*)</entry>'
                for line in linelist:
                    result = re.search(pattern, line)
                    if result:
                        print(result.group(1) + ' => ' +
                              result.group(2), file=dump)
                        iddict[result.group(1)] = result.group(2)

with open('dump2.txt', mode='w', encoding='utf8') as dump2:
    for filename in os.listdir(rootpath):
        if (filename.startswith('AR_') and filename.endswith('.xml')):
            with open(rootpath + filename, mode='r', encoding='utf8') as xml:
                data = xml.readlines()
                pattern = '#[A-Z_0-9]+'
                for i, line in enumerate(data):
                    result = re.findall(pattern, line)
                    for token in result:
                        glyphlesstoken = token[1:len(token)]
                        line = line.replace(token, iddict[glyphlesstoken])
                    data[i] = line
                    print(line, file=dump2)

            with open(rootpath + filename, mode='w', encoding='utf8') as xml:
                xml.writelines(data)
