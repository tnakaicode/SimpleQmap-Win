import os
import sys
from ctypes_wrapper import wrapper
import numpy as np
import datetime


def grep(file, key):
    for line in open(file):
        if key in line:
            return line.split()[2]

if len(sys.argv) != 8:
    raise ValueError

file=sys.argv[1]
vqmin=float(sys.argv[2])
vqmax=float(sys.argv[3])
vpmin=float(sys.argv[4])
vpmax=float(sys.argv[5])
row=int(sys.argv[6])
col=int(sys.argv[7])

qmin=float(grep(file, "QMIN"))
qmax=float(grep(file, "QMAX"))
pmin=float(grep(file, "PMIN"))
pmax=float(grep(file, "PMAX"))
dim=int(float(grep(file, "DIM")))
data = np.loadtxt(file).transpose()
qvec = data[2] + 1.j*data[3]
path = os.environ['PYTHONPATH'].split(":")
index = [p.endswith('SimpleQmap') for p in path].index(True)
file_path = path[index] + '/shared/libhsm.so'
cw = wrapper.call_hsm_rep(file_path)
hsm_imag = cw.husimi_rep(qvec, dim, [[qmin,qmax],[pmin,pmax]], [[vqmin,vqmax],[vpmin,vpmax]], [row,col])


x = np.linspace(vqmin, vqmax, row)
y = np.linspace(vpmin, vpmax, col)
X,Y = np.meshgrid(x,y)
data = np.array([X,Y,hsm_imag])

with open(file.replace("qrep","hsm"), "bw") as of:
    def annotate(str=""):
        str += "DATE %s\n" % datetime.datetime.now()
        str += "DIM %d\nQMIN %f\nQMAX %f\n" % (dim, qmin, qmax)
        str += "PMIN %f\nPMAX %f\n" % (pmin, pmax)
        str += "VQMIN %f\nVQMAX %f\nVPMIN %f\nVPMAX %f\n" % (vqmin, vqmax, vpmin,vpmax)
        str += "ROW %d\nCOL %d\n" % (row, col)
        return str
    np.savetxt(of,[],header=annotate())        
    for slice_data in data.transpose():
        np.savetxt(of, slice_data)
        of.write(b"\n")

#        of.write("\n")