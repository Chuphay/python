def compare_to_zero(func):
    def inner(S,K):
        out = func(S,K)
        if out>0:
            return out
        else:
            return 0
    return inner

@compare_to_zero
def call(S,K):
    return S-K

@compare_to_zero
def put(S,K):
    return K-S


if __name__ == '__main__':
    print put(3,7),3,7
    print put(7,3),7,3
    print call(7,3),7,3
    print call(3,7),3,7
    
