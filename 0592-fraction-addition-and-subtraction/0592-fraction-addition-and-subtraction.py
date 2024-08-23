class Solution:
    def fractionAddition(self, expression: str) -> str:
        def convert(exp):
            fraction=[]
            x, sgn, prev=0, 1, 0
            c=exp[0]
            if c=='-': sgn=-1
            elif c=='+': pass
            else: x=ord(c)-ord('0')

            i, sz= 1, len(exp)
            while i<sz:
                c=exp[i]
                while ord(c)>=ord('0'):
                    x=10*x+(ord(c)-ord('0'))
                    if i==sz-1: break
                    i+=1
                    c=exp[i]

                if c=='+':
                    fraction+=[(prev, x)]
                    sgn=1
                    x=0
                elif c=='-':
                    fraction+=[(prev, x)]
                    sgn=-1
                    x=0
                elif c=='/':
                    prev=x*sgn
                    x=0
                i+=1
            fraction+=[(prev, x)]
            return fraction

        def add(x, y):
            q=x[1]*y[1]
            p=x[0]*y[1]+x[1]*y[0]
            g=gcd(p, q)
            return (p//g, q//g)

        fraction=convert(expression)
        ans=(0, 1)
        for f in fraction:
            ans=add(ans, f)
        return str(ans[0])+'/'+str(ans[1])
            

        