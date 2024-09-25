import json


def add_server(sn):
    # Nome do servidor como variável
    server_name = sn


    data = {
        "server_list": {
            server_name: {  # Aqui a variável server_name substitui "server1"
            "p0": {
            },
            }
        }
    }

    # Escrever no arquivo JSON
    with open('servers.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)