import sys
import json
import ast

class Bugs:

    def bugs_today():

        bugs_to_be_solved = []
        arquivo = open('teste.txt', 'r')
        for linha in arquivo.readlines():
            linha_json = json.dumps(linha)
            linha_str = json.loads(linha_json)
            linha_dict = ast.literal_eval(linha_str)
            if(linha_dict['prioridade'] == 'critico'):
                bugs_to_be_solved.append(linha_dict['id'])
            elif(int(linha_dict['idade']) >= 3):
                bugs_to_be_solved.append(linha_dict['id'])
        print(bugs_to_be_solved)            
        return bugs_to_be_solved

if __name__ == "__main__":

    teste = Bugs.bugs_today()
