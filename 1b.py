import pandas as pd
data = pd.read_csv("1weather_dataset.csv")

data.head(10)
print (data);
def package_hypothesis(hypothesis, outcome):
    ln = dict()
    ln['hypothesis'] = hypothesis
    ln['outcome'] = outcome
    return ln

#Test hypothesises
h1 = package_hypothesis(["?","?","normal","?","?"],"yes")
h2 = package_hypothesis(["sunny","high","?","?","?"],"yes")
h3 = package_hypothesis(["rainy","?","ok","?","?"],"no")
h4 = package_hypothesis(["rainy","warm","high","?","?"],"yes")
h5 = package_hypothesis(["?","cold","?","cool","?"],"no")
h6 = package_hypothesis(["?","?","?","cool","?"],"yes")
def compare(values, hypo):
    for i in range(len(values)):
        if(hypo[i] != "?"):
            if(values[i] != hypo[i]):
                return False
    return True

def list_then_eliminate(data, *hypothesis):
    consistent_space = []
    inconsistent_space = []
    
    for hyp in hypothesis:
        state = True
        for i in range(data.shape[0]):
            if(hyp['outcome'] == data.iloc[i,-1]):
                if(not compare(hypo = hyp['hypothesis'], values = list(data.iloc[i,:-1])[:-1])):
                    inconsistent_space.append(hyp)
                    state = False
                    break
        if(state):
            consistent_space.append(hyp)
            
    return (inconsistent_space, consistent_space)
print (list_then_eliminate(data, h1,h2,h3,h4,h5,h6));
