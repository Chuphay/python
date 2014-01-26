alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
craze = "OIVDCQZWFMKTGSNPRAHJUXBEYL"


def encrypt(s,key):
    s = s.replace("\n", "")
    s = s.lower()
    output = ""
    for i in s:
        try:
            j = (alpha.index(i)+key)%len(alpha)
            output += ALPHA[j]
        except ValueError:
            output += i 
    if key<0:
        output = output.lower()
        return output
    else:           
        return output
def main():        
    jedi = open("/home/chuphay/python/projects/codes/text/clueless.txt").read()
    space = """Space... the Final Frontier. These are the voyages of the starship Enterprise. Its continuing mission: to explore strange new worlds, to seek out new life and new civilizations, to boldly go where no one has gone before."""
    print encrypt(space,3)
    import random        
    message = list(ALPHA) 
    random.shuffle(message)
    message = ''.join(message)
    #print message 
    
if __name__ == "__main__":
    main()           
       
