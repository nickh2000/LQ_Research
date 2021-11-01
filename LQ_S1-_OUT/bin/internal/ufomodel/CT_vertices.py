# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 5, 2011)
# Date: Sat 2 Dec 2017 14:04:28


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_166_44,(0,0,1):C.R2GC_166_45,(0,1,0):C.R2GC_169_46,(0,1,1):C.R2GC_169_47,(0,2,0):C.R2GC_169_46,(0,2,1):C.R2GC_169_47,(0,3,0):C.R2GC_166_44,(0,3,1):C.R2GC_166_45,(0,4,0):C.R2GC_166_44,(0,4,1):C.R2GC_166_45,(0,5,0):C.R2GC_169_46,(0,5,1):C.R2GC_169_47})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_117_9,(2,0,1):C.R2GC_117_10,(0,0,0):C.R2GC_117_9,(0,0,1):C.R2GC_117_10,(4,0,0):C.R2GC_115_5,(4,0,1):C.R2GC_115_6,(3,0,0):C.R2GC_115_5,(3,0,1):C.R2GC_115_6,(8,0,0):C.R2GC_116_7,(8,0,1):C.R2GC_116_8,(7,0,0):C.R2GC_122_16,(7,0,1):C.R2GC_175_52,(6,0,0):C.R2GC_121_14,(6,0,1):C.R2GC_176_53,(5,0,0):C.R2GC_115_5,(5,0,1):C.R2GC_115_6,(1,0,0):C.R2GC_115_5,(1,0,1):C.R2GC_115_6,(11,0,0):C.R2GC_119_12,(11,0,1):C.R2GC_119_13,(10,0,0):C.R2GC_119_12,(10,0,1):C.R2GC_119_13,(9,0,1):C.R2GC_118_11,(2,1,0):C.R2GC_117_9,(2,1,1):C.R2GC_117_10,(0,1,0):C.R2GC_117_9,(0,1,1):C.R2GC_117_10,(6,1,0):C.R2GC_173_49,(6,1,1):C.R2GC_173_50,(4,1,0):C.R2GC_115_5,(4,1,1):C.R2GC_115_6,(3,1,0):C.R2GC_115_5,(3,1,1):C.R2GC_115_6,(8,1,0):C.R2GC_116_7,(8,1,1):C.R2GC_177_54,(7,1,0):C.R2GC_122_16,(7,1,1):C.R2GC_122_17,(5,1,0):C.R2GC_115_5,(5,1,1):C.R2GC_115_6,(1,1,0):C.R2GC_115_5,(1,1,1):C.R2GC_115_6,(11,1,0):C.R2GC_119_12,(11,1,1):C.R2GC_119_13,(10,1,0):C.R2GC_119_12,(10,1,1):C.R2GC_119_13,(9,1,1):C.R2GC_118_11,(2,2,0):C.R2GC_117_9,(2,2,1):C.R2GC_117_10,(0,2,0):C.R2GC_117_9,(0,2,1):C.R2GC_117_10,(4,2,0):C.R2GC_115_5,(4,2,1):C.R2GC_115_6,(3,2,0):C.R2GC_115_5,(3,2,1):C.R2GC_115_6,(8,2,0):C.R2GC_116_7,(8,2,1):C.R2GC_174_51,(6,2,0):C.R2GC_121_14,(6,2,1):C.R2GC_121_15,(7,2,0):C.R2GC_172_48,(7,2,1):C.R2GC_117_10,(5,2,0):C.R2GC_115_5,(5,2,1):C.R2GC_115_6,(1,2,0):C.R2GC_115_5,(1,2,1):C.R2GC_115_6,(11,2,0):C.R2GC_119_12,(11,2,1):C.R2GC_119_13,(10,2,0):C.R2GC_119_12,(10,2,1):C.R2GC_119_13,(9,2,1):C.R2GC_118_11})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_186_58,(0,1,0):C.R2GC_187_59})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_160_39})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_159_38})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_189_61})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_190_62})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_188_60,(0,1,0):C.R2GC_185_57})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.g, P.S1tm43__star__, P.S1tm43 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1 ],
               loop_particles = [ [ [P.g, P.S1tm43] ] ],
               couplings = {(0,0,0):C.R2GC_134_25})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.g, P.g, P.S1tm43__star__, P.S1tm43 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(2,0,0):C.R2GC_135_26,(2,0,1):C.R2GC_135_27,(1,0,0):C.R2GC_135_26,(1,0,1):C.R2GC_135_27,(0,0,0):C.R2GC_119_13,(0,0,1):C.R2GC_132_23})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.e__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_146_30})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.e__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_146_30})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.mu__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_147_31})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.mu__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_147_31})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.ta__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_148_32})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.ta__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_148_32})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s, P.e__minus__, P.S1tm43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_149_33})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.e__plus__, P.S1tm43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_149_33})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s, P.mu__minus__, P.S1tm43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_150_34})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.mu__plus__, P.S1tm43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_150_34})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.ta__minus__, P.s, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_151_35})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.ta__plus__, P.s__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_151_35})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.e__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_161_40})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.e__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_161_40})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.mu__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_162_41})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.mu__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_162_41})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.ta__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_163_42})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.ta__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_163_42})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_125_20})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_125_20})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_125_20})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_18})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_18})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_123_18})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_124_19})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_145_29})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_4,(0,1,0):C.R2GC_184_56})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_104_4,(0,1,0):C.R2GC_184_56})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_104_4,(0,1,0):C.R2GC_184_56})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_158_37})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_158_37})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_158_37})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_141_28})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_141_28})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_181_55,(0,1,0):C.R2GC_141_28})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_141_28})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_141_28})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_36,(0,1,0):C.R2GC_141_28})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.S1tm43__star__, P.S1tm43 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.R2GC_164_43,(0,1,0):C.R2GC_133_24})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_81_63,(0,0,0):C.R2GC_89_64,(0,0,3):C.R2GC_89_65,(0,1,1):C.R2GC_92_70})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_90_66,(0,0,1):C.R2GC_90_67})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_3})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_95_75,(0,0,1):C.R2GC_95_76})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_98_81,(0,0,1):C.R2GC_98_82})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_93_71,(0,0,1):C.R2GC_93_72})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_97_79,(1,0,1):C.R2GC_97_80,(0,1,0):C.R2GC_96_77,(0,1,1):C.R2GC_96_78})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_94_73,(0,0,1):C.R2GC_94_74})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_91_68,(0,0,1):C.R2GC_91_69})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_91_68,(0,0,1):C.R2GC_91_69})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_102_2})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.S1tm43__star__, P.S1tm43__star__, P.S1tm43, P.S1tm43 ],
                color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.SSSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(1,0,0):C.R2GC_131_21,(1,0,1):C.R2GC_131_22,(0,0,0):C.R2GC_131_21,(0,0,1):C.R2GC_131_22})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_166_95,(0,0,1):C.UVGC_166_96,(0,0,2):C.UVGC_166_97,(0,0,3):C.UVGC_120_17,(0,0,4):C.UVGC_166_98,(0,0,5):C.UVGC_166_99,(0,1,0):C.UVGC_169_105,(0,1,1):C.UVGC_169_106,(0,1,2):C.UVGC_170_110,(0,1,3):C.UVGC_170_111,(0,1,4):C.UVGC_170_112,(0,1,5):C.UVGC_169_109,(0,3,0):C.UVGC_169_105,(0,3,1):C.UVGC_169_106,(0,3,2):C.UVGC_169_107,(0,3,3):C.UVGC_114_7,(0,3,4):C.UVGC_169_108,(0,3,5):C.UVGC_169_109,(0,5,0):C.UVGC_166_95,(0,5,1):C.UVGC_166_96,(0,5,2):C.UVGC_168_102,(0,5,3):C.UVGC_168_103,(0,5,4):C.UVGC_168_104,(0,5,5):C.UVGC_166_99,(0,6,0):C.UVGC_166_95,(0,6,1):C.UVGC_166_96,(0,6,2):C.UVGC_167_100,(0,6,3):C.UVGC_167_101,(0,6,4):C.UVGC_166_98,(0,6,5):C.UVGC_166_99,(0,7,0):C.UVGC_169_105,(0,7,1):C.UVGC_169_106,(0,7,2):C.UVGC_171_113,(0,7,3):C.UVGC_171_114,(0,7,4):C.UVGC_170_112,(0,7,5):C.UVGC_169_109,(0,2,2):C.UVGC_114_6,(0,2,3):C.UVGC_114_7,(0,4,2):C.UVGC_120_16,(0,4,3):C.UVGC_120_17,(0,4,4):C.UVGC_120_18})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.S1tm43], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                couplings = {(2,0,4):C.UVGC_116_11,(2,0,5):C.UVGC_116_10,(0,0,4):C.UVGC_116_11,(0,0,5):C.UVGC_116_10,(4,0,4):C.UVGC_115_8,(4,0,5):C.UVGC_115_9,(3,0,4):C.UVGC_115_8,(3,0,5):C.UVGC_115_9,(8,0,4):C.UVGC_116_10,(8,0,5):C.UVGC_116_11,(7,0,0):C.UVGC_175_129,(7,0,3):C.UVGC_135_47,(7,0,4):C.UVGC_175_130,(7,0,5):C.UVGC_175_131,(7,0,6):C.UVGC_175_132,(7,0,7):C.UVGC_175_133,(6,0,0):C.UVGC_175_129,(6,0,3):C.UVGC_135_47,(6,0,4):C.UVGC_176_134,(6,0,5):C.UVGC_176_135,(6,0,6):C.UVGC_175_132,(6,0,7):C.UVGC_175_133,(5,0,4):C.UVGC_115_8,(5,0,5):C.UVGC_115_9,(1,0,4):C.UVGC_115_8,(1,0,5):C.UVGC_115_9,(11,0,4):C.UVGC_119_14,(11,0,5):C.UVGC_119_15,(10,0,4):C.UVGC_119_14,(10,0,5):C.UVGC_119_15,(9,0,4):C.UVGC_118_12,(9,0,5):C.UVGC_118_13,(2,1,4):C.UVGC_116_11,(2,1,5):C.UVGC_116_10,(0,1,4):C.UVGC_116_11,(0,1,5):C.UVGC_116_10,(6,1,0):C.UVGC_172_115,(6,1,4):C.UVGC_173_120,(6,1,5):C.UVGC_173_121,(6,1,6):C.UVGC_173_122,(6,1,7):C.UVGC_172_119,(4,1,4):C.UVGC_115_8,(4,1,5):C.UVGC_115_9,(3,1,4):C.UVGC_115_8,(3,1,5):C.UVGC_115_9,(8,1,0):C.UVGC_177_136,(8,1,3):C.UVGC_177_137,(8,1,4):C.UVGC_177_138,(8,1,5):C.UVGC_177_139,(8,1,6):C.UVGC_177_140,(8,1,7):C.UVGC_177_141,(7,1,1):C.UVGC_121_19,(7,1,4):C.UVGC_122_22,(7,1,5):C.UVGC_122_23,(5,1,4):C.UVGC_115_8,(5,1,5):C.UVGC_115_9,(1,1,4):C.UVGC_115_8,(1,1,5):C.UVGC_115_9,(11,1,4):C.UVGC_119_14,(11,1,5):C.UVGC_119_15,(10,1,4):C.UVGC_119_14,(10,1,5):C.UVGC_119_15,(9,1,4):C.UVGC_118_12,(9,1,5):C.UVGC_118_13,(2,2,4):C.UVGC_116_11,(2,2,5):C.UVGC_116_10,(0,2,4):C.UVGC_116_11,(0,2,5):C.UVGC_116_10,(4,2,4):C.UVGC_115_8,(4,2,5):C.UVGC_115_9,(3,2,4):C.UVGC_115_8,(3,2,5):C.UVGC_115_9,(8,2,0):C.UVGC_174_123,(8,2,3):C.UVGC_174_124,(8,2,4):C.UVGC_174_125,(8,2,5):C.UVGC_174_126,(8,2,6):C.UVGC_174_127,(8,2,7):C.UVGC_174_128,(6,2,2):C.UVGC_121_19,(6,2,4):C.UVGC_121_20,(6,2,5):C.UVGC_118_12,(6,2,6):C.UVGC_121_21,(7,2,0):C.UVGC_172_115,(7,2,4):C.UVGC_172_116,(7,2,5):C.UVGC_172_117,(7,2,6):C.UVGC_172_118,(7,2,7):C.UVGC_172_119,(5,2,4):C.UVGC_115_8,(5,2,5):C.UVGC_115_9,(1,2,4):C.UVGC_115_8,(1,2,5):C.UVGC_115_9,(11,2,4):C.UVGC_119_14,(11,2,5):C.UVGC_119_15,(10,2,4):C.UVGC_119_14,(10,2,5):C.UVGC_119_15,(9,2,4):C.UVGC_118_12,(9,2,5):C.UVGC_118_13})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_186_153,(0,0,2):C.UVGC_186_154,(0,0,1):C.UVGC_186_155,(0,1,0):C.UVGC_187_156,(0,1,2):C.UVGC_187_157,(0,1,1):C.UVGC_187_158})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_160_81})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_159_80})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_189_162})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_190_163})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_188_159,(0,0,2):C.UVGC_188_160,(0,0,1):C.UVGC_188_161,(0,1,0):C.UVGC_185_150,(0,1,2):C.UVGC_185_151,(0,1,1):C.UVGC_185_152})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.g, P.S1tm43__star__, P.S1tm43 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S1tm43] ], [ [P.S1tm43] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_134_39,(0,0,1):C.UVGC_134_40,(0,0,2):C.UVGC_134_41,(0,0,3):C.UVGC_134_42,(0,0,5):C.UVGC_134_43,(0,0,6):C.UVGC_134_44,(0,0,4):C.UVGC_134_45})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.g, P.g, P.S1tm43__star__, P.S1tm43 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S1tm43] ], [ [P.S1tm43] ], [ [P.t] ] ],
                couplings = {(2,0,0):C.UVGC_135_46,(2,0,1):C.UVGC_135_47,(2,0,2):C.UVGC_135_48,(2,0,3):C.UVGC_135_49,(2,0,5):C.UVGC_135_50,(2,0,6):C.UVGC_135_51,(2,0,4):C.UVGC_135_52,(1,0,0):C.UVGC_135_46,(1,0,1):C.UVGC_135_47,(1,0,2):C.UVGC_135_48,(1,0,3):C.UVGC_135_49,(1,0,5):C.UVGC_135_50,(1,0,6):C.UVGC_135_51,(1,0,4):C.UVGC_135_52,(0,0,2):C.UVGC_132_36,(0,0,4):C.UVGC_132_37})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.e__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_146_56,(0,0,2):C.UVGC_146_57,(0,0,1):C.UVGC_146_58})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.e__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_146_56,(0,0,2):C.UVGC_146_57,(0,0,1):C.UVGC_146_58})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.mu__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_147_59,(0,0,2):C.UVGC_147_60,(0,0,1):C.UVGC_147_61})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.mu__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_147_59,(0,0,2):C.UVGC_147_60,(0,0,1):C.UVGC_147_61})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.ta__minus__, P.d, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_148_62,(0,0,2):C.UVGC_148_63,(0,0,1):C.UVGC_148_64})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.ta__plus__, P.d__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_148_62,(0,0,2):C.UVGC_148_63,(0,0,1):C.UVGC_148_64})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.s, P.e__minus__, P.S1tm43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_149_65,(0,0,1):C.UVGC_149_66,(0,0,2):C.UVGC_149_67})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.s__tilde__, P.e__plus__, P.S1tm43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_149_65,(0,0,1):C.UVGC_149_66,(0,0,2):C.UVGC_149_67})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s, P.mu__minus__, P.S1tm43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_150_68,(0,0,1):C.UVGC_150_69,(0,0,2):C.UVGC_150_70})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.s__tilde__, P.mu__plus__, P.S1tm43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_150_68,(0,0,1):C.UVGC_150_69,(0,0,2):C.UVGC_150_70})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.ta__minus__, P.s, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_151_71,(0,0,1):C.UVGC_151_72,(0,0,2):C.UVGC_151_73})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.ta__plus__, P.s__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S1tm43] ], [ [P.g, P.s, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_151_71,(0,0,1):C.UVGC_151_72,(0,0,2):C.UVGC_151_73})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.e__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_161_82,(0,0,2):C.UVGC_161_83,(0,0,1):C.UVGC_161_84})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.e__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_161_82,(0,0,2):C.UVGC_161_83,(0,0,1):C.UVGC_161_84})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.mu__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_162_85,(0,0,2):C.UVGC_162_86,(0,0,1):C.UVGC_162_87})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.mu__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_162_85,(0,0,2):C.UVGC_162_86,(0,0,1):C.UVGC_162_87})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.ta__minus__, P.b, P.S1tm43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_163_88,(0,0,2):C.UVGC_163_89,(0,0,1):C.UVGC_163_90})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.ta__plus__, P.b__tilde__, P.S1tm43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S1tm43] ], [ [P.g, P.S1tm43] ] ],
                couplings = {(0,0,0):C.UVGC_163_88,(0,0,2):C.UVGC_163_89,(0,0,1):C.UVGC_163_90})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_125_26,(0,1,0):C.UVGC_106_2,(0,2,0):C.UVGC_106_2})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_125_26,(0,1,0):C.UVGC_179_143,(0,2,0):C.UVGC_179_143})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_125_26,(0,1,0):C.UVGC_106_2,(0,2,0):C.UVGC_106_2})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_154_75,(0,2,0):C.UVGC_154_75})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_108_3,(0,2,0):C.UVGC_108_3})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_108_3,(0,2,0):C.UVGC_108_3})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,1):C.UVGC_126_28,(0,1,3):C.UVGC_126_29,(0,1,4):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,2):C.UVGC_126_33,(0,2,0):C.UVGC_126_27,(0,2,1):C.UVGC_126_28,(0,2,3):C.UVGC_126_29,(0,2,4):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,2):C.UVGC_126_33})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,1):C.UVGC_126_28,(0,1,2):C.UVGC_126_29,(0,1,3):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,4):C.UVGC_180_144,(0,2,0):C.UVGC_126_27,(0,2,1):C.UVGC_126_28,(0,2,2):C.UVGC_126_29,(0,2,3):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,4):C.UVGC_180_144})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,1):C.UVGC_126_28,(0,1,2):C.UVGC_126_29,(0,1,3):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,4):C.UVGC_126_33,(0,2,0):C.UVGC_126_27,(0,2,1):C.UVGC_126_28,(0,2,2):C.UVGC_126_29,(0,2,3):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,4):C.UVGC_126_33})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,2):C.UVGC_126_28,(0,1,3):C.UVGC_126_29,(0,1,4):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,1):C.UVGC_155_76,(0,2,0):C.UVGC_126_27,(0,2,2):C.UVGC_126_28,(0,2,3):C.UVGC_126_29,(0,2,4):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,1):C.UVGC_155_76})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,1):C.UVGC_126_28,(0,1,3):C.UVGC_126_29,(0,1,4):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,2):C.UVGC_126_33,(0,2,0):C.UVGC_126_27,(0,2,1):C.UVGC_126_28,(0,2,3):C.UVGC_126_29,(0,2,4):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,2):C.UVGC_126_33})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_124_25,(0,1,0):C.UVGC_126_27,(0,1,1):C.UVGC_126_28,(0,1,2):C.UVGC_126_29,(0,1,3):C.UVGC_126_30,(0,1,5):C.UVGC_126_31,(0,1,6):C.UVGC_126_32,(0,1,4):C.UVGC_126_33,(0,2,0):C.UVGC_126_27,(0,2,1):C.UVGC_126_28,(0,2,2):C.UVGC_126_29,(0,2,3):C.UVGC_126_30,(0,2,5):C.UVGC_126_31,(0,2,6):C.UVGC_126_32,(0,2,4):C.UVGC_126_33})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_145_54,(0,0,1):C.UVGC_145_55})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_182_146,(0,0,2):C.UVGC_182_147,(0,0,1):C.UVGC_145_55})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_145_54,(0,0,1):C.UVGC_145_55})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_182_146,(0,0,2):C.UVGC_182_147,(0,0,1):C.UVGC_145_55})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_145_54,(0,0,1):C.UVGC_145_55})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_145_54,(0,0,1):C.UVGC_145_55})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_183_148,(0,1,0):C.UVGC_184_149})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_157_78,(0,1,0):C.UVGC_158_79})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_141_53,(0,1,0):C.UVGC_105_1,(0,2,0):C.UVGC_105_1})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_105_1})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_181_145,(0,1,0):C.UVGC_178_142})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_105_1})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_105_1})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_156_77,(0,1,0):C.UVGC_153_74})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.S1tm43__star__, P.S1tm43 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S1tm43] ] ],
                 couplings = {(0,0,0):C.UVGC_164_91,(0,1,0):C.UVGC_133_38})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.S1tm43] ], [ [P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_165_92,(0,1,3):C.UVGC_165_93,(0,1,4):C.UVGC_165_94,(0,0,1):C.UVGC_113_4,(0,0,2):C.UVGC_113_5})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.S1tm43__star__, P.S1tm43__star__, P.S1tm43, P.S1tm43 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.S1tm43] ] ],
                 couplings = {(1,0,0):C.UVGC_131_34,(1,0,1):C.UVGC_131_35,(0,0,0):C.UVGC_131_34,(0,0,1):C.UVGC_131_35})

