import random

class Simulador():
    """
    Classe destinada a simulação de dados de voo
    """
    def __init__(self):
        """
        Construtor da classe Simulador
        """
        # Gerando lista de dados
        self._altitude = [x for x in range(3000)] + [3000-x for x in range(3000)] # Simulando dados de altitude entre 0 e 3000.
        self._latitude = [10+random.randrange(-2,2) for x in range(6000)]         # Simulando dados de latitude entre 8 e 12.
        self._longitude = [20+random.randrange(-4,4) for x in range(6000)]        # Simulando dados de longitude entre 16 e 24.
        self._acionamentoPPE = [0]*2999 + [1] + [1]*3000                          # Simulando a confirmação do acionamento principal do paraquedas estabilizador
        self._acionamentoRPE = [0]*3004 + [1] + [1]*2995                          # Simulando a confirmação do acionamento redundante do paraquedas estabilizador
        self._acionamentoPPP = [0]*3449 + [1] + [1]*2500                          # Simulando a confirmação do acionamento principal do paraquedas principal
        self._acX = [2+random.uniform(-.2, .2) for x in range(6000)]              # Simulando a aceleração no eixo x
        self._acY = [3+random.uniform(-.3, .3) for x in range(6000)]              # Simulnado a aceleração no eixo y
        self._acZ = [35+random.randrange(-5, 5) for x in range(6000)]             # Simulando a aceleração no eixo z
        self._gyX = [100+random.randrange(-10,10) for x in range(6000)]           # Simulando a angulação no eixo x
        self._gyY = [0+random.randrange(-30,30) for x in range(6000)]           # Simulando a angulação no eixo y
        self._gyZ = [-75+random.randrange(-15,15) for x in range(6000)]           # Simulando a angulação no eixo z
        self._RSSI = [60+random.randrange(-30,30) for x in range(6000)]           # Simulando os dados de RSSI
