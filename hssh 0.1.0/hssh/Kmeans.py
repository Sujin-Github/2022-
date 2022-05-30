from hssh.DefClass import *
import random
import pandas as pd
import numpy as np

def K_means(Document,K,analysis_by='제목',*args):
    count=0
    cos_sim=Document.cos_sim(analysis_by).to_numpy()
    num=Document.num
    
    group=[]
    sample = np.random.choice(range(num),K)
    for paper in sample:
        group.append([paper])
    for paper in range(num):
        if paper not in sample:
            cossim=[]
            for samplepaper in sample:
                cossim.append(cos_sim[samplepaper][paper])
            group[cossim.index(max(cossim))].append(paper)
        else:
            pass

    while True:
        count+=1
        newgroup=[]
        sample = np.random.choice(range(num),K)
        for paper in sample:
            newgroup.append([paper])
        for paper in range(num):
            if paper not in sample:
                cossim=[]
                for samplepaper in sample:
                    cossim.append(cos_sim[samplepaper][paper])
                newgroup[cossim.index(max(cossim))].append(paper)
            else:
                pass

        if sorted(group)==sorted(newgroup):
            print('end by',count)
            SSE=0
            for gr in group:
                mean=list(set(gr) & set(sample))[0]
                for paper in gr:
                    if paper != mean: SSE=SSE+((1-cos_sim[paper][mean])**2)
            print('SSE: ',SSE)
            return (group,SSE)
        else:
            group=newgroup
            
def tag(Document,Kmeanslist,K,tag='과목',title='제목',*args):
    taged=[]
    for i in Kmeanslist:
        temp=[]
        for j in i:
            index=list(Document.dataframe[title]).index(j)
            temp.append({j:Document.dataframe[tag].loc[index]})
        taged.append(temp)
    return taged

def tag_name(Document, grouped, title='제목', *args):
  docseries=Document.dataframe[title]
  taged_group=[]
  for group in grouped:
    temp=[]
    for paper in group:
      temp.append(docseries.iloc[paper])
    taged_group.append(temp)
  return taged_group