import shodan


def api(api):
    sites = []
    objShodan = shodan.Shodan(api)
    resultados = objShodan.search("port: 21 Anonymous user logged in")
    print("Numero de host encontrados: ", len(resultados['matches']))
    for match in resultados['matches']:
        if match['ip_str'] is not None:
            print(match['ip_str'])
            sites.append(match['ip_str'])
    
