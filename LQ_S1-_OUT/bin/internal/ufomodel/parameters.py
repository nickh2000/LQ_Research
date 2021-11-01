# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 5, 2011)
# Date: Sat 2 Dec 2017 14:04:28



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

yRR1x1 = Parameter(name = 'yRR1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR1x1}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 1, 1 ])

yRR1x2 = Parameter(name = 'yRR1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR1x2}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 1, 2 ])

yRR1x3 = Parameter(name = 'yRR1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR1x3}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 1, 3 ])

yRR2x1 = Parameter(name = 'yRR2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR2x1}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 2, 1 ])

yRR2x2 = Parameter(name = 'yRR2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR2x2}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 2, 2 ])

yRR2x3 = Parameter(name = 'yRR2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR2x3}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 2, 3 ])

yRR3x1 = Parameter(name = 'yRR3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR3x1}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 3, 1 ])

yRR3x2 = Parameter(name = 'yRR3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR3x2}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 3, 2 ])

yRR3x3 = Parameter(name = 'yRR3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{yRR3x3}',
                   lhablock = 'YUKS1tRR',
                   lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MS1t = Parameter(name = 'MS1t',
                 nature = 'external',
                 type = 'real',
                 value = 650,
                 texname = '\\text{MS1t}',
                 lhablock = 'MASS',
                 lhacode = [ 9000005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WS1t = Parameter(name = 'WS1t',
                 nature = 'external',
                 type = 'real',
                 value = 12.931339,
                 texname = '\\text{WS1t}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

