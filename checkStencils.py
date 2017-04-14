import json

fn = 'stencils-20170414.json'

with open(fn) as json_data:
    d = json.load(json_data)

o = d.keys()
num_stencils = len(o)

num_assets = []
for ii in range(0,num_stencils):
	a = len(d[o[ii]])
	num_assets.append(a)

print str(num_stencils) + ' stencils!'
print 'Between ' + str(min(num_assets)) + '-' + str(max(num_assets)) + ' assets per stencil!'