import socket # Biblioteca responsavel pela comunicação socket
import json   # Biblioteca usada para envio de Json
import time   # Biblioteca usada para parar o codigo
from simulador import Simulador

class Servidor():
    """
    Classe servidor - Servidor para o simulador de dados de voo de um minifogute - API Socket
    """

    def __init__(self, host, port):
        """
        Construtor da classe Servidor
        """
        self._host = host
        self._port = port
        self._tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def start(self):
        """
        Inicia a execução do serviço
        """
        endpoint = (self._host, self._port)
        try:
            self._tcp.bind(endpoint)
            self._tcp.listen(1)
            print(f'Servidor foi iniciado em {self._host}:{self._port}')
            while True:
                con, client = self._tcp.accept()
                self._service(con, client)
        except Exception as e:
            print(f"Erro ao inicializar o servidor: {e.args}")



    def _service(self, con, client):
        """
        Metodo que implementa o serviçõ de simulador de dados de voo
        :param con: objeto socket utilizado para enviar e receber os dados
        :param client: é o endereço e porta do cliente
        """
        dados = Simulador()
        
        print(f'Atendendo cliente {client}')
        try:
            msg = con.recv(1024)
            if str(msg.decode('ascii')) == 'y':
                for i in range(len(dados._altitude)):
                    self._data = {"Altitude" : dados._altitude[i],
                                    "Latitude" : dados._latitude[i],
                                    "Longitude" : dados._longitude[i],
                                    "Principal Paraquedas Estabilizador" : dados._acionamentoPPE[i],
                                    "Redundancia Paraquedas Estabilizador" : dados._acionamentoPPP[i],
                                    "Comercial Paraquedas Estabilizador" : dados._acionamentoCPE[i],
                                    "Principal Paraquedas Principal" : dados._acionamentoPPP[i],
                                    "Comercial Paraquedas Principal" : dados._acionamentoCPP[i],
                                    "Acelerometro" : {"x" : dados._acX[i] , "y" : dados._acY[i] , "z" : dados._acZ[i]},
                                    "Giroscopio" : {"x" : dados._gyX[i] , "y" : dados._gyY[i] , "z" : dados._gyZ[i]},
                                    "RSSI" : dados._RSSI[i]
                                    }
                    self._data = json.dumps(self._data)
                    con.send(self._data.encode())
                    print("Dados enviados.")
                    time.sleep(0.3)
        except OSError as e:
            print(f'Erro na conexao {client} : {e.args}')
            return
        except Exception as e:
            print(f'Erro na palavra de conexao recebida do client {client} : {e.args}')              