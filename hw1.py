import re

input_file = open('hw')
regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
code_resoponse_idx = 3
ip_idx = 0
code_resoponse = '404'

result = {}
for line in input_file:
    log = re.match(regex, line).groups()
    if log[code_resoponse_idx] == code_resoponse:
        try:
            result[log[ip_idx]] = result[log[ip_idx]] + 1
        except:
            result[log[ip_idx]] = 1        
            except:
            result[log[ip_idx]] = 1

print(log)

input_file.close()