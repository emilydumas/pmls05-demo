'''Demonstrate generating simple curves using twists'''

# The generator code below assumes that twist functions Tab etc have
# been defined and operate on strings.  For this sample we only
# implement Tab, Tbc, and their inverses. 

def Tab(s):
    w = []
    for x in s:
        if x == 'a':
            w.append('b')
        elif x == 'b':
            w.append('Bab')
        elif x == 'A':
            w.append('B')
        elif x == 'B':
            w.append('BAb')
        else:
            w.append(x)
    return ''.join(w)

def Tbc(s):
    w = []
    for x in s:
        if x == 'b':
            w.append('c')
        elif x == 'c':
            w.append('Cbc')
        elif x == 'B':
            w.append('C')
        elif x == 'C':
            w.append('CBc')
        else:
            w.append(x)
    return ''.join(w)

def Tab_inv(s):
    w = []
    for x in s:
        if x == 'a':
            w.append('abA')
        elif x == 'b':
            w.append('a')
        elif x == 'A':
            w.append('aBA')
        elif x == 'B':
            w.append('A')
        else:
            w.append(x)
    return ''.join(w)

def Tbc_inv(s):
    w = []
    for x in s:
        if x == 'b':
            w.append('bcB')
        elif x == 'c':
            w.append('b')
        elif x == 'B':
            w.append('bCB')
        elif x == 'C':
            w.append('B')
        else:
            w.append(x)
    return ''.join(w)


# ---- BEGIN code from presentation slide ----

depth = 5

twists = { Tab, Tab_inv, Tbc, Tbc_inv } # etc
curves = set()
frontier = {'ab', 'bc', 'cd', 'de', 'ea'}

for _ in range(depth):
    latest = \
        { T(x) for x in frontier for T in twists }
    frontier = latest.difference(curves)
    curves.update(frontier)

# ---- END code from presentation slide ----

# Produce output so running this as a script is interesting.
for x in curves:
    print(x)    

