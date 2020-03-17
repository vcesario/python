"""
ALGORITMO (1o rascunho)
1. montar array com o path de todos os arquivos xml
2. definir linguagens em uma array (ex: RU, JA, KO...)
3. definir dictionary (linguagem para set de caracteres)
4. pra cada arquivo xml da array:
    4.1. extrair o prefixo para achar a key do dictionary
    4.2. abrir arquivo
    4.3. extrair todos os caracteres e adicioná-los ao set naquela key
    4.4. fechar arquivo
5. abrir arquivo final
6. printar caracteres do set no arquivo em ordem
7. fechar arquivo
"""
import os

rootpath = ''

if not os.path.exists(rootpath):
    exit()

langtoset = dict()
defaultlangs = {'DE', 'ENAU', 'EN', 'ENGB',
                'ES', 'FRCA', 'FR', 'IT', 'NL', 'PT', 'TR'}

for filename in os.listdir(rootpath):
    if filename.endswith('.xml'):
        splitted = filename.split('_')
        lang = ''.join(splitted[0: len(splitted) - 1])

        xml = open(rootpath + filename, mode='r', encoding='utf8')
        for ch in xml.read():
            if ch == '\n':
                continue

            if lang not in langtoset:
                langtoset[lang] = set()

            langtoset[lang].add(ch)

            if lang in defaultlangs:
                if 'Default' not in langtoset:
                    langtoset['Default'] = set()
                langtoset['Default'].add(ch)
        xml.close()

        langtoset[lang].add('h')
        langtoset[lang].add('m')

uniquesfile = open('uniques-per-language.txt', mode='w', encoding='utf8')
for k, v in langtoset.items():
    print('[' + k + ']', file=uniquesfile)
    for ch in v:
        print(ch, end='', file=uniquesfile)
    print('\n', file=uniquesfile)
uniquesfile.close()
