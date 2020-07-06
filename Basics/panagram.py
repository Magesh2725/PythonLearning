import string
def ispangaram(sentence):
    sentence=sentence.lower().strip().replace(" ", "")
    alpha='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    alphabets=list(alpha.split(','))
    print(alphabets)
    for item in sentence:
        print(f'removing {item}')
        if item in alphabets:
            alphabets.remove(item)
    print(alphabets)
    print(len(alphabets))
    print(string.ascii_lowercase)

ispangaram('The Quick brown fox jumps over the lazy dog')