#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask, request
from tulip import *
import json

import numpy as np
import pandas as pd

app = Flask('A la une')

@app.route('/',methods = ['GET'])
def index():

	df = pd.read_csv('C:/Users/Mehdi/Desktop/M1/Visualisation/data/montant_annee.txt',sep ='\t' , encoding='latin-1')
	
	montant_par_annee = montant_annee(df)
	pie = pie_chart(montant_par_annee)
	#graph = generate()
	#graph2json(graph)

	# generer un graphe avec tulip
	# on stocke un fichier json qui le decrit
	# on renvois un fichier html qui contient le code d3 qui affiche le graphe

	#return app.send_static_file('graphe.html')
	return pie

#@app.route('/')
#def dessin():
#	return  "je calcule un graphe avec un algo (option formulaire, "


#@app.route('/')
#def dessin_color():
#	return 


def generate():
	graph = tlp.newGraph()
	n1 = graph.addNode()
	graph['viewLayout'][n1] = tlp.Coord(1,15,0)
	n2 = graph.addNode()
	graph['viewLayout'][n2] = tlp.Coord(6,1,0)
	n3 = graph.addNode()
	graph['viewLayout'][n3] = tlp.Coord(10,1,2)
	n4 = graph.addNode()
	graph['viewLayout'][n4] = tlp.Coord(10,1,2)
	graph.addEdge(n1,n2)
	graph.addEdge(n2,n3)
	graph.addEdge(n3,n1)
	graph.addEdge(n3,n4)
	return graph

def graph2json(graph):
	nodes = [{'index':0},{'index': 1}]
	links = [{'source':0,'target':1}]

	json_object = {}
	nodes = []
	for n in graph.getNodes():
		nodes.append({'index' : n.id , 'x' : graph['viewLayout'][n][0] ,'y' : graph['viewLayout'][n][1]  })
	json_object['nodes'] = nodes
	links = []
	for e in graph.getEdges():
		links.append({'source':graph.source(e).id,'target': graph.target(e).id})
	json_object['links'] = links
	with open('static/graph.json','w') as fp:
		json.dump(json_object,fp)



def montant_annee(df):

	df = df.dropna()
	df = df.reset_index(drop=True)

	montant = {}
	montant[2006] = 0
	montant[2007] = 0
	montant[2008] = 0
	montant[2009] = 0
	montant[2010] = 0
	montant[2011] = 0
	montant[2012] = 0
	montant[2013] = 0
	montant[2014] = 0
	montant[2015] = 0

	for i in range(0,len(df)):
		montant[df['Annee de financement'][i]] = montant[df['Annee de financement'][i]] + df['Montant'][i]

	return montant



def pie_chart(cmots):
  html = ''
  html += '<!DOCTYPE html><html><head><script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script><meta charset="utf-8">'
  #html += '<title>A la une</title><link rel="stylesheet" href="http://127.0.0.1/alaune/style.css" media="screen" title="no title" charset="utf-8"><link rel="icon" type="image/jpg" href="http://127.0.0.1/alaune/image3.jpg" /></head><body><div class="banniere"><img src="http://127.0.0.1/alaune/image3.jpg" alt="banniere_alaune" /></div><ul id="menu"><li><a href="/">Accueil</a></li><li><a href="trouverjournal.php">Trouvez votre journal </a></li><li><a href="choixdumot.php"> Je choisis mon mot </a></li><li><a href="journalmot.php"> Filtrez vos actualités </a></li><li><a href="#"> Comparez</a><ul><li><a href="cinqmotsjournal.php"> 5 mots </a></li></ul></li><li><a href="#"> Et pour finir .. </a><ul><li><a href="bubble1.php">Bubble Chart</a></li><li><a href="bubble2.php"> Bubble Chart 2</a></li></ul></li></ul>'
  html += '<h2 align="center"> Argent distribué par l ANR entre 2006 et 2015 </h2>'
  html += '<body>'
  html += '<script>'
  html += 'var data =['+str(cmots[2006])+','+str(cmots[2007])+','+str(cmots[2008])+','+str(cmots[2009])+','+str(cmots[2010])+','+str(cmots[2011])+','+str(cmots[2012])+','+str(cmots[2013])+','+str(cmots[2014])+','+str(cmots[2015])+'];'
  html += 'var r= 200;'
  html += 'var color = d3.scale.ordinal()'
  html += '.range(["#FF7F00","blue","yellow","#00FF00","#DE3163","#b40000","#1844a5","#f344a5","#f3e206","#04e9ca"]);'
  html += 'var canvas=d3.select("body").append("svg")'
  html += '.attr("width",2000)'
  html += '.attr("height",500);'
  html += 'var group= canvas.append("g")'
  html += '.attr("transform", "translate(1075,200)");'
  html += 'var arc = d3.svg.arc()'
  html += '.innerRadius(75)'
  html += '.outerRadius(r);'
  html += 'var pie = d3.layout.pie()'
  html += '.value(function (d) {return d; });'
  html += 'var arcs = group.selectAll(".arc")'
  html += '.data(pie(data))'
  html += '.enter()'
  html += '.append("g")'
  html += '.attr("class","arc");'
  html += 'arcs.append("path")'
  html += '.attr("d",arc)'
  html += '.attr("fill", function(d) {return color(d.data); });'
  html += 'arcs.append("text")'
  html += '.attr("transform", function (d) { return "translate(" + arc.centroid(d) + ")";})'
  html += '.text(function (d) { return d.data; });'
  html += '</script>'

  html += '<h2 align="center">  '+str(cmots[2006])+' euros on été distribués en '+str(2006)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2007])+' euros on été distribués en '+str(2007)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2008])+' euros on été distribués en '+str(2008)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2009])+' euros on été distribués en '+str(2009)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2010])+' euros on été distribués en '+str(2010)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2011])+' euros on été distribués en '+str(2011)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2012])+' euros on été distribués en '+str(2012)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2013])+' euros on été distribués en '+str(2013)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2014])+' euros on été distribués en '+str(2014)+'  </h2>'
  html += '<h2 align="center">  '+str(cmots[2015])+' euros on été distribués en '+str(2015)+'  </h2>'


  html += '</body>'
  html += '</html>'
  return html


if __name__ == '__main__':
  app.run(debug=True)