import sys
import json

f = file('hxh.json')
s = json.load(f)
author=[]
pub=[]
for a in s:
#    print  a['authors'][0].split(',')
    for au in a['authors'][0].split(','):
    	author.append(au.strip())
    pub.append({'title':a['title'][0],'citedby':a['citation'][0],'authors':a['authors'][0].split(',')})
author=set(author)
author.update
author=list(author)
print author
pos =0
links=[]
nodes=[dict({'name':i,'type':'people'}) for i in author]
for p in pub:
    #print p.title
    #nodes.append({'name':p['title'],'type':'pub','cited':p['citedby']})
    #print p['authors']
    for i in p['authors']:
        #print author[0]
    	links.append({'source':author.index(i.strip()),'target':pos,'relation':'coauthor'})
    pos+=1
#print nodes
#print links
fs = open('map/maponly.json','w')
fs.write(json.dumps({'nodes':nodes,'links':links}))
f.close()
fs.close()



