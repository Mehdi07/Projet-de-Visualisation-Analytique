# Powered by Python 3.6

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import tlp
import numpy as np
from tulip import tlp
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# The main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
  Acronyme = graph.getStringProperty("Acronyme")
  Année_de_financement = graph.getIntegerProperty("Année de financement")
  Code_du_programme = graph.getStringProperty("Code du programme")
  Code_du_projet = graph.getStringProperty("Code du projet")
  Code_du_type_de_partenaire = graph.getStringVectorProperty("Code du type de partenaire")
  Coordinateur_du_projet = graph.getStringProperty("Coordinateur du projet")
  Date_de_début = graph.getIntegerProperty("Date de début")
  Durée_en_mois = graph.getIntegerProperty("Durée en mois")
  Identifiant_de_partenaire = graph.getStringVectorProperty("Identifiant de partenaire")
  Libellé_de_partenaire = graph.getStringVectorProperty("Libellé de partenaire")
  Lien_Programme = graph.getStringProperty("Lien Programme")
  Lien_Projet = graph.getStringProperty("Lien Projet")
  Montant = graph.getDoubleProperty("Montant")
  Perspectives = graph.getStringProperty("Perspectives")
  Programme = graph.getStringProperty("Programme")
  Publications_et_brevets = graph.getStringProperty("Publications et brevets")
  Résultats = graph.getStringProperty("Résultats")
  Résumé = graph.getStringProperty("Résumé")
  Résumé_de_la_soumission = graph.getStringProperty("Résumé de la soumission")
  Sigle_de_partenaire = graph.getStringVectorProperty("Sigle de partenaire")
  Titre = graph.getStringProperty("Titre")
  Type_didentifiant = graph.getStringVectorProperty("Type d'identifiant")
  Type_de_partenaire = graph.getStringVectorProperty("Type de partenaire")
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
  viewLabel = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  viewLabelColor = graph.getColorProperty("viewLabelColor")
  viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
  viewLayout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  viewShape = graph.getIntegerProperty("viewShape")
  viewSize = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")

  G = graph.addSubGraph()
  
  df = pd.read_csv('C:/Users/Mehdi/Desktop/M1/Visualisation/abstracts.txt',sep ='\t' , encoding='latin-1')
  
  resume = df['Résumé']
  acronyme = df['Acronyme']
  
  stop_words = ['alors','au','aucuns','aussi','autre','avant','avec','avoir','bon','car','ce','cela','ces','ceux','chaque','ci','comme','comment','dans','des','du','dedans','dehors','depuis','devrait','doit','donc','dos','début','elle','elles','en','encore','essai','est','et','eu','fait','faites','fois','font','hors','ici','il','ils','je','juste','la','le','les','leur','là','ma','maintenant','mais','mes','mine','moins','mon','mot','même','ni','nommés','notre','nous','ou','où','par','parce','pas','peut','peu','plupart','pour','pourquoi','quand','que','quel','quelle','quelles','quels','qui','sa','sans','plus','trois','donc','cette','sera','ses','chez','ainsi','afin','afin de','seulement','si','sien','son','sont','sous','soyez','sur','ta','tandis','tellement','tels','tes','ton','tous','tout','trop','très','tu','voient','vont','votre','vous','vu','ça','étaient','état','étions','été','être']
  
  vectorizer = CountVectorizer(stop_words=stop_words, min_df=0.025, max_df=0.03, ngram_range=(1,1))

  
  resume = resume.dropna()
  
  test = resume[0:200]
  
  X = vectorizer.fit_transform(test)
  
  transformer = TfidfTransformer(smooth_idf=False)
  
  tfidf = transformer.fit_transform(X)
  
  
  binarizer = preprocessing.Binarizer(threshold = 0.004)
  
  Y = binarizer.transform(tfidf)
  
  Z = Y.toarray()
  
  A = np.asmatrix(Z)
  
  B = np.transpose(A)
  
  dd = np.dot(A,B)
  
  R = pd.DataFrame(dd)
  len(R)
  dic = {}
  
  for i in range(0,len(R)):
    R = R.rename(index=int,columns={i : acronyme[i]})
  
  b = 0;
  
  for a in range(0,len(dd)):
    a = G.addNode()
    viewLabel[a] = R.columns[b]
  
    dic[R.columns[b]] = a
    b = b+1
    
  o = 0
    
  for c in range(0,len(R)):
      for d in range(c+1,len(R)):
        if R[acronyme[c]][d] == 1:
          o = o +1
          G.addEdge(dic[R.columns[c]],dic[R.columns[d]])
          

  print(o)
