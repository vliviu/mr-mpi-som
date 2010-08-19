from numpy import *
import sys



argc = len(sys.argv)
if argc != 4:
    print "Usage: "
    sys.exit(1)

outFileName = sys.argv[1]
rows = int(sys.argv[2])
cols = int(sys.argv[3])

mat = random.rand(rows, cols)
outFile = open(outFileName, "w")
for i in range(0, rows):
    for j in range(0, cols):
        outFile.write("%0.3f " % mat[i][j])
    outFile.write("\n")
    
outFile.close()