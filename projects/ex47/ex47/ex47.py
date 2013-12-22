words = {
"direction":['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
"verb":['go', 'stop', 'kill', 'eat'],
"stop":['the', 'in', 'of', 'from', 'at', 'it'],
"noun":['door', 'bear', 'princess', 'cabinet']
}
class lexicon:
    @staticmethod
    def scan(s):
        the_words = s.split()
        output = []
        for m in the_words:
            error = True
            try:
                num = int(m)
                output.append(('number',num))
                error = False
            except ValueError:
                pass
            for x in words:
                if m in words[x]:
                    output.append((x,m))
                    error = False
            if error:
                output.append(('error',m)) 
        return output


