class APIError(BaseException):
    def __init__(self, *, code: int, msg: str) -> None:
        self.code = code
        self.msg = msg
