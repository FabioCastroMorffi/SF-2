from animal import Animal

class Bird(Animal):
    def reproduce(self):
        
        text = 'Birds typically reproduce by hatching and incubating their \
eggs.'
        super().reproduce()
        print(text)
    def __repr__(self) -> str:
        text = '\nClass: Bird'
        return super().__repr__() + text