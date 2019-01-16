import pandas as pd

df = pd.read_csv('C:/Users/Mehdi/Desktop/M1/Visualisation/data/data_selected2.txt',sep ='\t' , encoding='utf-8')

df = df.dropna()
df = df.reset_index(drop=True)

#on importe les données, on enlève les lignes qui comporte des Nan, ensuite on reindex les lignes

titre = df['Titre']
Libelle = df['Libellé de partenaire']

new_df = pd.DataFrame(columns=['Code du projet','Titre','Centre','Résumé','Montant','Année de financement','Date de début','Durée en mois'])

for j in range(0,len(titre)):
    montant = 0;
    list = []
    centre = ''
    for i in Libelle[j]:
        if i == ';':
            list.append(centre)
            #new_df = new_df.append({'Titre' : titre, 'Centre' : centre },ignore_index=True)
            centre = ''
        else:
            centre = centre + i
    list.append(centre)
    
    
    list = set(list)
    montant = len(list)
    for i in list:
        new_df = new_df.append({ 'Code du projet' : df['Code du projet'][j] ,'Titre' : titre[j], 'Centre' : i, 'Résumé' : df['Résumé'][j]  ,'Montant' : (df['Montant'][j])/montant, 'Année de financement' : df['Année de financement'][j] , 'Date de début' : df['Date de début'][j] , 'Durée en mois' : df['Durée en mois'][j] },ignore_index=True)
        
        
new_df  

#new_df est un nouveau tableau, tiré du premier, ou chaque ligne comporte un partenaire pour un projet, contrairement au tableau initial, df, ou on pouvais lire tout les partenaire d'un projet sur la meme lignes. Ici, bien sur, le tableau est plus grand que le premier  

city = ['Paris','Lyon','Toulouse','Marseille','Montpellier','Bordeaux','Strasbourg','Nantes','Lille','Nice']
city_df = pd.DataFrame(columns=['Code du projet','Titre','Centre','Résumé','Montant','Année de financement','Date de début','Durée en mois','Ville'])

for i in range(0,9):
    for j in range(0,len(new_df['Centre'])):
        if city[i] in new_df['Centre'][j]:
            city_df = city_df.append({'Code du projet' : new_df['Code du projet'][j] ,'Titre' : new_df['Titre'][j], 'Centre' : new_df['Centre'][j], 'Résumé' : new_df['Résumé'][j]  ,'Montant' : new_df['Montant'][j] , 'Année de financement' : new_df['Année de financement'][j] , 'Date de début' : new_df['Date de début'][j] , 'Durée en mois' : new_df['Durée en mois'][j] , 'Ville' : city[i] },ignore_index=True)
            
city_df

#city_df est un tableau ou nous avons pu identifier la ville d'apartenance d'un partenaires, c'est donc un sous-tableau de new_df

word = ['chimie','chimique','bio','données','climat','élec','informatique','algorithmes','energie','molécule']


city_df['Domaine'] = ''
city_df['Domaine2'] = False 


for i in range(0,len(city_df['Domaine'])):
    if (city_df['Domaine'][i] == '' and city_df['Domaine2'][i] == True):
        city_df['Domaine2'][i] = False


#On va associer à une ligne du tableau une ville et un domaine

data_sankey = city_df
data_sankey = data_sankey[data_sankey.Domaine != '']



for i in range(0,len(sankey)):
    if sankey['Domaine'][i] == 'génome' or sankey['Domaine'][i] == 'vaccin' or sankey['Domaine'][i] == 'cellul' or sankey['Domaine'][i] == 'plante':
        sankey['Domaine'][i] = 'biologie'

for i in range(0,len(sankey)):
    if sankey['Domaine'][i] == 'cognit':
        sankey['Domaine'][i] = 'santé'

for i in range(0,len(sankey)):
    if sankey['Domaine'][i] == 'climat' or sankey['Domaine'][i] == 'séisme' or sankey['Domaine'][i] == 'environn' or sankey['Domaine'][i] == 'sol' or sankey['Domaine'][i] == 'toxi' or sankey['Domaine'][i] == 'terre' or sankey['Domaine'][i] == 'océan':
        sankey['Domaine'][i] = 'environnement'

for i in range(0,len(sankey)):
    if sankey['Domaine'][i] == 'math' or sankey['Domaine'][i] == 'arithmé' or sankey['Domaine'][i] == 'géométri'  :
        sankey['Domaine'][i] = 'mathématiques'

for i in range(0,len(sankey)):
    if sankey['Domaine'][i] == 'internet' or sankey['Domaine'][i] == 'algorithmes' or sankey['Domaine'][i] == 'data' or sankey['Domaine'][i] == 'données':
        sankey['Domaine'][i] = 'informatique'

sankey.to_csv('C:/Users/Mehdi/Desktop/M1/Visualisation/data/data_sankey.txt', sep = '\t', index = False)

sankey2 = sankey['Ville']
for i in range(0,len(sankey2)):
    sankey2[i] = sankey2[i] + ',' + sankey['Domaine'][i]


sankey3 = pd.DataFrame()
sankey3['V_D'] = ''
sankey3['Nombre'] = ''
list = []
a = 0
for i in range (0,len(sankey2)):
    if sankey2[i] not in list:
        list.append(sankey2[i])

list

list2 = []
for i in range(0,75):
    list2.append(0)
list2


d = { 'V_D' : list , 'Nombre' : list2}

sankey3 = pd.DataFrame(data = d)


for i in range(0,len(sankey3)):
    for j in range(0,len(sankey2)):
        if sankey2[j] == sankey3['V_D'][i]:
            sankey3['Nombre'][i] = sankey3['Nombre'][i] + 1


for i in range(0,len(sankey3)):
    a = 0
    for j in sankey3['V_D'][i]:
        if j == ',':
            sankey4['Ville'][i] = sankey3['V_D'][i][0:a]
            sankey4['Domaine'][i] = sankey3['V_D'][i][a+1:]
        a = a + 1

sankey4

#la sortie de sankey4 nous renvois un tableau a 3 colonnes (Ville, Domaine, Nombre de projet entre la ville et le domaine), c'est ce tableau que nous allons utiliser pour notre sankey diagramm

def domaine(domain):
    a = 0
    for i in range(0,len(city_df)):
        if domain in city_df['Résumé'][i].lower() and city_df['Domaine2'][i] == False:
            city_df['Domaine2'][i] = True
            city_df['Domaine'][i] = domain
            a = a + 1
    j = 0;
    for i in range(0,len(city_df)):
        if(city_df['Domaine2'][i] == False):
            j = j +1;
    return j
        


