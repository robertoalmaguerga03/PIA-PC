import nmap

def puertos(ip):
    target = ip

    scanner = nmap.PortScanner()

    for i in range(100):
        res = scanner.scan(target,str(i))
        res = res['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {res}.')
        if (f'{res}' == 'open'):
            with open('.' + '/output.csv', 'w') as output:
                output.write(f'port {i} is {res}.\n')
