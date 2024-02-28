SEC_S = input()
SEC = int(SEC_S)

HORA = SEC//3600 #PARA HORA
MIN = SEC//60  
SEGUNDO = SEC%60

print('{}:{}:{}'.format(HORA,MIN,SEGUNDO))