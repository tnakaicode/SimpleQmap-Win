import sys
from qmap import Qmap
from maps import StandardMap
import numpy as np


if len(sys.argv) != 7:
    raise ValueError("\nusage: python %s dim k qmin qmax pmin pmax " % sys.argv[0])

dim = int(sys.argv[1])
k = float(sys.argv[2])
qmin = float(sys.argv[3])
qmax = float(sys.argv[4])
pmin = float(sys.argv[5])
pmax = float(sys.argv[6])
domain = [[qmin,qmax],[pmin,pmax]]

#dim = 10
#domain=[[0.0, 1.0],[-0.5,0.5]]
#k=1.0

map = StandardMap(k=k)
qmap = Qmap(map, dim, domain)

evals, evecs = qmap.eigen()
for i, evec in enumerate(evecs):
    evec.savetxt("eigen_qrep_%i.dat" % i)


sample=300
tmax=300
q = np.random.random(sample)
p = (np.random.random(sample) -0.5) * (pmax - pmin) * 2
with open("trajectories.dat", "w") as f:
    for i in range(tmax):
        pp = p - map.func0(q)
        qq = q + map.func1(pp)
        q = qq - np.floor(qq)
        p = pp
        [ f.write("%.16e %.16e\n" % (q[i],p[i])) for i in range(sample)  ] 
        #np.savetxt(f, np.array([q, p]).transpose())
