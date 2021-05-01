from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

class EstadoDAO:
    def __init__(self):
        noticia1 = Noticia(1, "Aplicação da segunda dose da vacina contra covid está suspensa em Duque de Caxias", "img/rj_noticia_1.png", "video/rj-noticia-1.mp4", "Em Duque de Caxias, a aplicação da segunda dose contra a covid está suspensa. Tem vacinação apenas para pessoas com 57 anos ou mais e também pra quem tem obesidade mórbida. O problema é que a prefeitura de Caxias faz a convocação sem seguir o Plano Nacional de Imunizações. Desde as primeiras horas do dia, as filas em alguns posto estão enormes, os moradores estão perdidos quanto ao calendário e isso impacta a campanha de imunização no município. A Secretaria Estadual de Saúde notificou Caxias e quer que a prefeitura siga com os grupos prioritários de vacinação. Segundo o governo do estado, o desrespeito ao plano de imunizações pode levar à perda de credibilidade no programa de vacinação.", "29/04/2021", 250, 400)
        noticia2 = Noticia(2, "Rio começa a vacinação de grupos prioritários para pessoas com 59 anos", "img/rj_noticia_2.png", "video/rj_noticia2.mp4", "Começa no Rio de Janeiro a vacinação contra a covid-19 dos grupos prioritários, para as pessoas de 59 anos. O calendário vai seguir a divisão por idade e gênero. Hoje é a vez das mulheres.", "26/04/2021", 300, 445)
        noticia3 = Noticia(3, "Mensagens de carinho levam esperança aos impactados pela covid em BH", "img/mg_noticia_1.png", "video/mg_noticia1.mp4", "O afeto nunca foi tão necessário como nesses tempos de pandemia. Uma intervenção artística realizada pelo Sesi e pela CBTU (Companhia Brasileira de Trens Urbanos) faz uma homenagem cheia de carinho aos impactados pela covid-19. A partir de segunda feira (26), serão centenas de corações e mensagens pela cidade.", "26/04/2021", 320, 650)
        noticia4 = Noticia(4, "Minas Gerais investiga 150 casos de reinfecção pela Covid 19", "img/mg_noticia_2.png", "video/mg_noticia2.mp4", "O estado de Minas Gerais investiga 150 casos de reinfecção pela Covid-19. Mais de 300 casos já foram notificados.", "28/04/2021", 120, 300)
        noticia5 = Noticia(5, "SP identifica caso de variante suíça da COVID 19 e novo caso da variante sul africana", "img/sp_noticia_1.png", "video/sp_noticia1.mp4", "Pesquisadores do Instituto Buntatan identificaram, pela primeira vez no estado de São Paulo, a presença da variante suíça da COVID-19. a B.1.1.38, em Itapecerica da Serra. A rede de monitoramento identificou também um novo caso da variante sul-africana, a B.1.351, e uma mutação da cepa originalmente identificada em Manaus, P1.", "27/04/2021", 222, 540)
        estado1 = Estado(1, "Rio de Janeiro", "RJ", "img/bandeira-rj.png", [noticia1, noticia2])
        estado2 = Estado(2, "Minas Gerais", "MG", "img/bandeira-mg.png", [noticia3, noticia4])
        estado3 = Estado(3, "São Paulo", "SP", "img/bandeira_sp.jpg", [noticia5])
        self._estados = [estado1, estado2, estado3]

    def findAll(self):
        return self._estados

    def findNoticiaById(self, id:int):
        for estado in self._estados:
            for noticia in estado.getNoticiaList():
                if noticia.getId() == id:
                    return noticia
        return None