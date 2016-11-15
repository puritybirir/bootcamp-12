class StringSplosion:

    def __init__(self, arg):
        self.word=arg

    def manipulate(self):
        fragments=[]
        i=1
        while i <= len(self.word):
            fragments.append(self.word[0:i])
            i+=1

        j=1
        result=fragments[0]
        while j < len(fragments):
            result=result+fragments[j]
            j+=1

        return result