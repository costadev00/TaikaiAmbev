import nltk
import math
from sklearn.neighbors import KNeighborsClassifier

rad = nltk.stem.RSLPStemmer()

kw = nltk.corpus.stopwords.words('english')

se = nltk.corpus.mac_morpho.tagged_sents()
un = nltk.tag.UnigramTagger(se)

def indiceInvertido(text):
	'''
		função que monta o indice invertido da base de dados, informando a frequncia da palavra por arquivo
	
		@param path string, caminho para o arquivo que contem a lista de arquivos que compõe a base
		
		@return dicionario, com os radicais das palavras e suas respectivas aparições em cada arquivo
	'''

	m = {}

	ca = 1

	for a in text:

		df = a

		pa = []
		for i in df:
			pa += nltk.word_tokenize(i)

		for i in range(len(pa)):
			pa[i] = pa[i].lower()
			
		etq = un.tag(pa)
		
		for i in range(len(etq)):
			if etq[i][1] in ['ART','PREP','KC','KS']:
				pa.remove(etq[i][0])

		aux = list(pa)

		for i in aux:
			if i in kw:
				pa.remove(i)
		
		for i  in pa:
			i = rad.stem(i)
			if i in m:
				if ca in m[i]:
					m[i][ca] += 1
				else:
					m[i][ca] = 1
			else:
				m[i] = {ca: 1}
		ca+=1
	
	return m


def indiceConsulta(text):  # falta remover as stopwords da consulta
	'''
		Função que recebe um arquivo de consulta e retorna o indice invertido referente a ele

		@param path caminho para o arquivo de pesquisa

		@return dicionario de dicionario, indice invertido da consulta
	'''

	con = text.split()
	con = set(con)
	
	# print(con)
	cInd = {}
	
	for i in con:
		i = i.lower()
		if i in kw:
			continue
		
		etq = un.tag([i])
		
		if etq[0][1] in ['ART','PREP','KC','KS']:
			continue
		
		i = rad.stem(i)
		cInd[i] = {1:1}
	
	return cInd


def calcIDF(indIv, nArq):
	'''
		Função que calcula o idf palavra por palavra de uma base de texto apartir de um indice invertido
		
		@param indIV dicionario de dicionario, indice invertido retornado pela função indiceInvertido
		@param nArq número de documentos na base

		@return dicionario onde a chave é a palavra e o valor mapeado é o idf da palavra

	'''
	idf = {}
	for i in indIv:
		idf[i] = math.log10(nArq/float(len(indIv[i])))
	return idf


def calcPeso(indIv,nArq, idf=None):
	'''
		função que recebe um indice invertido e retorna os vetores esparços de pesos tf-idf

		@param indIv dicionario retornado pela função que calcula o indice invertido
		@param nArq número de arquivos na base de documentos
		@param idf dicionario do idf pre-calculado por palavra

		@return dicionario, vetor esparço de pesos de cada arquivo

	'''

	if idf==None:
		idf = calcIDF(indIv,nArq)

	pesoP = {}

	for i in range(1,nArq+1):
		for j in indIv:
			if i in indIv[j]:
				if i in pesoP: 
					if j in idf:
						pesoP[i][j] = (1+math.log10(indIv[j][i]))*idf[j] # math.log10(nArq/float(len(indIv[j])))
					else:
						pesoP[i][j] = 0
				else:
					if j in idf:
						pesoP[i] = {j:(1+math.log10(indIv[j][i]))*idf[j]} #math.log10(nArq/float(len(indIv[j])))}
					else:
						pesoP[i] = {j:0}

	return pesoP


def compConsulta(indIv,indCs):
	'''
		função que calcula a similaridade da consulta para cada arquivo da base de textos

		@param indIv vetor de pesos dos arquivos
		@param indCs vetor de pesos da consulta

		@return dicionario onde a chave é o número do arquivo e seu valor mapeado a similaridade do mesmo com a consulta.
	'''
	sim = {}
	for j in indIv:
		num = 0
		denC = 0
		denB = 0
		for i in indCs[1]:
			if i in indIv[j]:
				num += indIv[j][i] * indCs[1][i]
			denC += indCs[1][i] * indCs[1][i]
		
		for i in indIv[j]:
			denB += indIv[j][i] * indIv[j][i]
		
		sim[j] = num/(math.sqrt(denB)*math.sqrt(denC))
	
	return sim


class Classificador:

	numC = KNeighborsClassifier()

	def __init__(self, numberDatasetX, textDatasetX, numberDatasetY, textDatasetY):
		numC.fit(numberDatasetX,numberDatasetY)
		ind = indiceInvertido(textDatasetX)
		self.textDatasetY = textDatasetY
		self.idf = calcIDF(ind,len(textDatasetX))
		self.pes = calcPeso(ind,len(textDatasetX),self.idf)

	def classifica(self,data):
		if type(data) == str:
			return classStr(data)
		else:
			return classNumber(data)

	def classNumber(self,data):
		return numC.predict([[data]])

	def classStr(self,data):
    cind = indiceConsulta(data)
    cpes = calcPeso(cind,1,self.idf)
    res = compConsulta(sel.pes,cpes)
    ma = [0,0,0]
    for i in res.values():
      if(i>ma[0]):
        ma[2] = ma[1]
        ma[1] = ma[0]
        ma[0] = i
      elif i>m[1]:
        ma[2] = ma[1]
        ma[1] = i
      elif i>m[2]:
        ma[2] = i
		la = {}
		tmp=0
		for i in res:
		  if res[i] in ma:
		    if self.textDatasetY[i] in la:
          la[self.textDatasetY[i]]+=1
        else
		      la[self.textDatasetY[i]]=1
		    if res[i]==ma[0]:
		      tmp = i
		
		if len(la)==3:
		  return self.textDatasetY[tmp]
		else:
		  for i in la:
		    if la[i]==2:
		      return i

