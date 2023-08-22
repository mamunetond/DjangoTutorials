from abc import ABC, abstractmethod 

from django.http import HttpRequest 

 

class ImageStorage(ABC): 

 

    @abstractmethod # any class that inherits from this one must implement this method 

    def store(self, request: HttpRequest): 

        pass 