import numpy as np
plaintext="ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
frequency = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228, "G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025, "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987, "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150, "Y": .01974, "Z": .00074 }
frequency_val= frequency.values()
#print(frequency_val)
main_mean=(sum(frequency_val)/len(frequency_val))
print(main_mean)

#def population_variance(text):
    

# Calcualte the population variance for the english language:
counter=0
print(np.square(2))
for i in frequency_val:
    counter= counter+ np.square(main_mean -counter)


