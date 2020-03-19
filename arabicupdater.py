"""
IDEIA DO ALGORITMO

1. abrir xml e carregar dict com ids e valores
2. iterar por todos os .xml e substituir #ID pelo valor
"""

import os
import re

rootpath = 'C:\\Mgaia Studio\\Unity Projects\\Skyfish 2\\Assets\\Localization\\Resources\\Languages\\'

if rootpath == '' or not os.path.exists(rootpath):
    exit()

iddict = dict()


def char_reverser(src):
    dst = ''
    for ch in src:
        dst = ch + dst
    return dst


# load xml
with open('log1.txt', mode='w', encoding='utf8') as dump:
    with open('log2.txt', mode='w', encoding='utf8') as dump2:
        for filename in os.listdir(rootpath):
            if (filename.startswith('AR_') and filename.endswith('.xml')):
                print('\n' + filename, file=dump)
                print('==========================================', file=dump)
                with open(rootpath + filename, mode='r', encoding='utf8') as xml:
                    linelist = xml.read().splitlines()
                    pattern = r'<entry name=\"([A-Z_0-9]+)\">([^\<]*)</entry>'
                    for line in linelist:
                        if '#' in line:
                            print(line, file=dump)

                        result = re.search(pattern, line)
                        if result:
                            print(result.group(1) + ' => ' +
                                  result.group(2) + ' // ' + char_reverser(result.group(2)), file=dump2)
                            iddict[result.group(1)] = result.group(2)

# with open('dump2.txt', mode='w', encoding='utf8') as dump2:
#     for filename in os.listdir(rootpath):
#         if (filename.startswith('AR_') and filename.endswith('.xml')):
#             with open(rootpath + filename, mode='r', encoding='utf8') as xml:
#                 data = xml.readlines()
#                 pattern = '#[A-Z_0-9]+'
#                 for i, line in enumerate(data):
#                     result = re.findall(pattern, line)
#                     for token in result:
#                         line = line.replace(
#                             token, iddict[token.replace('#', '')])
#                     data[i] = line
#                     print(line, file=dump2)

            # with open(filename, mode='w', encoding='utf8') as xml:
            #     xml.writelines(data)
