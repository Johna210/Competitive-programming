class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime+self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if currentTime < self.tokens[tokenId]:
                self.tokens[tokenId] =  currentTime+self.time
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        values = 0
        for token in self.tokens:
            if currentTime < self.tokens[token]:
                values+=1
        return values


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)