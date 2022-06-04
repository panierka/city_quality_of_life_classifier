import numpy as np

class Fuzzy:
    def __init__(self):
        self.antecedent=[]
        self.consequent=[]
        self.rules=[]
    def triangularFunction(self,x,a,b,c):
        if x<=a:
            return 0
        if x>a and x<=b:
            return (x-a)/(b-a)
        if x>b and x<=c:
            return (c-x)/(c-b)
        if x>c:
            return 0
    def addAntecedent(self,parameter, linguisticValue,a,b,c):
        self.antecedent.append([parameter,linguisticValue,a,b,c])
    def addRule(self,rule):
        self.rules.append(rule)
    def addConsequent(self,linguisticValue,parameters):
        self.consequent.append([linguisticValue,parameters])

    def compute(self,sample):
        #rozmycie
        print(sample)
        fuzzyValues=[]
        for i in self.antecedent:
            fuzzyValues.append([i[0],i[1],self.triangularFunction(sample[i[0]],i[2],i[3],i[4])])
            print(fuzzyValues[-1])

        print(fuzzyValues)
        #wnioskowanie
        rulesResult=[]
        for i in self.rules:
            tmp=1
            for j in fuzzyValues:
                print(j)
                if i[j[0]]==j[1]:
                    tmp*=j[2]
            print(tmp)
            rulesResult.append(tmp)
        print('rulesResult:',rulesResult)
        #wyostrzenie
        res=max (rulesResult)
        decision=''
        print(self.rules)
        decision=self.rules[rulesResult.index(res)]['jakosc zycia']
        print("W miescie",sample['miasto'], "jakosc zycia jest",decision)
        print()


system=Fuzzy()
system.addAntecedent('naslonecznienie','zle',0,0,0.4)
system.addAntecedent('naslonecznienie','srednie',0.3,0.4,0.8)
system.addAntecedent('naslonecznienie','dobre',0.7,1,1)

system.addAntecedent('skazenie','wysokie',0,0,0.4)
system.addAntecedent('skazenie','srednie',0.3,0.4,0.8)
system.addAntecedent('skazenie','niskie',0.7,1,1)

system.addConsequent('jakosc zycia',[['zla',0,0,0.4],['srednia',0.3,0.6,0.8],['dobra',0.7,1,1]])

#regul powinno byc 9
system.addRule({'naslonecznienie':'zle','skazenie':'wysokie','jakosc zycia':'zla'})
system.addRule({'naslonecznienie':'srednie','skazenie':'wysokie','jakosc zycia':'zla'})
system.addRule({'naslonecznienie':'zle','skazenie':'srednie','jakosc zycia':'zla'})
system.addRule({'naslonecznienie':'zle','skazenie':'niskie','jakosc zycia':'srednia'})
system.addRule({'naslonecznienie':'dobre','skazenie':'wysokie','jakosc zycia':'srednia'})
system.addRule({'naslonecznienie':'srednie','skazenie':'srednie','jakosc zycia':'srednia'})
system.addRule({'naslonecznienie':'srednie','skazenie':'niskie','jakosc zycia':'dobra'})
system.addRule({'naslonecznienie':'dobre','skazenie':'srednie','jakosc zycia':'dobra'})
system.addRule({'naslonecznienie':'dobre','skazenie':'niskie','jakosc zycia':'dobra'})

miasta=[]
miasta.append({'naslonecznienie':0.6,'skazenie':0.3,'miasto':'Warszawa'})
miasta.append({'naslonecznienie':1.0,'skazenie':0.1,'miasto':'Krakow'})

for sample in miasta:
    print(sample)
    system.compute(sample)
#%%
