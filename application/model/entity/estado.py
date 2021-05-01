from typing import List
from application.model.entity.noticia import Noticia

class Estado:
    def __init__(self, id: int, nome: str, sigla: str, bandeira: str, noticia_list: List[Noticia]):
        self._id = id
        self._nome = nome
        self._sigla = sigla
        self._bandeira = bandeira
        self._noticiaList = noticia_list

    def getId(self) -> int:
        return self._id

    def getNome(self) -> str:
        return self._nome

    def getSigla(self) -> str:
        return self._sigla
    
    def getBandeira(self) -> str:
        return self._bandeira
    
    def getNoticiaList(self) -> List[Noticia]:
        return self._noticiaList