from scm.plams import Molecule, label

m1 = Molecule('xyz/EZ1.xyz')
m2 = Molecule('xyz/EZ2.xyz')

def testYES():
    for i in range(3): assert m1.label(i) == m2.label(i)

def testNO():
    for i in range(3,5): assert m1.label(i) != m2.label(i)