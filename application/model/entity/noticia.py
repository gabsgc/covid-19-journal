class Noticia:
    def __init__(self, id: int, title: str, image: str, video: str, text: str, published_at: str, like: int, view: int):

        self._id = id
        self._title = title
        self._imagePath = image
        self._videoPath = video
        self._text = text
        self._publishedAt = published_at
        self._likes = like
        self._views = view

    def getId(self) -> int:
        return self._id

    def getTitle(self) -> str:
        return self._title
    
    def getImagePath(self) -> str:
        return self._imagePath
    
    def getVideoPath(self) -> str:
        return self._videoPath
    
    def getText(self) -> str:
        return self._text

    def getPublishedAt(self) -> str:
        return self._publishedAt

    def getLikes(self) -> int:
        return self._likes

    def getViews(self) -> int:
        return self._views
