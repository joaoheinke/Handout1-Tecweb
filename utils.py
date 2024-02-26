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
    
def load_template(doc):
    with open("templates/{0}".format(doc), 'r') as file:
        return file.read()

def save_data(doc, data):
    with open("data/{0}".format(doc), 'w') as file:
        file.write(json.dumps(data))

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    response += f'Content-Length: {len(body)}\n'
    response += 'Content-Type: text/html\n'
    response += headers
    response += '\n\n'
    response = response + body
    return response.encode()
