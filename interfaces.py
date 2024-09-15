from abc import ABC, abstractmethod


class Cypher(ABC):
    @property
    @abstractmethod
    def key(self) -> object:
        pass

    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, cyphertext: str) -> str:
        pass
