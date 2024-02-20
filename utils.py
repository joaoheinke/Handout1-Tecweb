import json

def extract_route(request):
    return request.split()[1][1:]

def read_file(filepath):
    with open(filepath, 'rb') as file:
        return file.read()
    
def load_data(doc):
    with open("data/{0}".format(doc), 'r') as file:
        conteudo = file.read()
        return json.loads(conteudo)
    