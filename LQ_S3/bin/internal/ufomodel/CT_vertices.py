# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 5, 2011)
# Date: Sun 3 Dec 2017 09:36:59


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
               couplings = {(0,0,0):C.R2GC_309_178,(0,0,1):C.R2GC_309_179,(0,1,0):C.R2GC_312_180,(0,1,1):C.R2GC_312_181,(0,2,0):C.R2GC_312_180,(0,2,1):C.R2GC_312_181,(0,3,0):C.R2GC_309_178,(0,3,1):C.R2GC_309_179,(0,4,0):C.R2GC_309_178,(0,4,1):C.R2GC_309_179,(0,5,0):C.R2GC_312_180,(0,5,1):C.R2GC_312_181})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_181_33,(2,0,1):C.R2GC_181_34,(0,0,0):C.R2GC_181_33,(0,0,1):C.R2GC_181_34,(4,0,0):C.R2GC_179_29,(4,0,1):C.R2GC_179_30,(3,0,0):C.R2GC_179_29,(3,0,1):C.R2GC_179_30,(8,0,0):C.R2GC_180_31,(8,0,1):C.R2GC_180_32,(7,0,0):C.R2GC_186_40,(7,0,1):C.R2GC_318_186,(6,0,0):C.R2GC_185_38,(6,0,1):C.R2GC_319_187,(5,0,0):C.R2GC_179_29,(5,0,1):C.R2GC_179_30,(1,0,0):C.R2GC_179_29,(1,0,1):C.R2GC_179_30,(11,0,0):C.R2GC_183_36,(11,0,1):C.R2GC_183_37,(10,0,0):C.R2GC_183_36,(10,0,1):C.R2GC_183_37,(9,0,1):C.R2GC_182_35,(2,1,0):C.R2GC_181_33,(2,1,1):C.R2GC_181_34,(0,1,0):C.R2GC_181_33,(0,1,1):C.R2GC_181_34,(6,1,0):C.R2GC_316_183,(6,1,1):C.R2GC_316_184,(4,1,0):C.R2GC_179_29,(4,1,1):C.R2GC_179_30,(3,1,0):C.R2GC_179_29,(3,1,1):C.R2GC_179_30,(8,1,0):C.R2GC_180_31,(8,1,1):C.R2GC_320_188,(7,1,0):C.R2GC_186_40,(7,1,1):C.R2GC_186_41,(5,1,0):C.R2GC_179_29,(5,1,1):C.R2GC_179_30,(1,1,0):C.R2GC_179_29,(1,1,1):C.R2GC_179_30,(11,1,0):C.R2GC_183_36,(11,1,1):C.R2GC_183_37,(10,1,0):C.R2GC_183_36,(10,1,1):C.R2GC_183_37,(9,1,1):C.R2GC_182_35,(2,2,0):C.R2GC_181_33,(2,2,1):C.R2GC_181_34,(0,2,0):C.R2GC_181_33,(0,2,1):C.R2GC_181_34,(4,2,0):C.R2GC_179_29,(4,2,1):C.R2GC_179_30,(3,2,0):C.R2GC_179_29,(3,2,1):C.R2GC_179_30,(8,2,0):C.R2GC_180_31,(8,2,1):C.R2GC_317_185,(6,2,0):C.R2GC_185_38,(6,2,1):C.R2GC_185_39,(7,2,0):C.R2GC_315_182,(7,2,1):C.R2GC_181_34,(5,2,0):C.R2GC_179_29,(5,2,1):C.R2GC_179_30,(1,2,0):C.R2GC_179_29,(1,2,1):C.R2GC_179_30,(11,2,0):C.R2GC_183_36,(11,2,1):C.R2GC_183_37,(10,2,0):C.R2GC_183_36,(10,2,1):C.R2GC_183_37,(9,2,1):C.R2GC_182_35})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_329_191,(0,1,0):C.R2GC_336_195})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_298_170})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_297_169})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_338_197})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_339_198})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_337_196,(0,1,0):C.R2GC_328_190})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.a, P.S3m13__star__, P.S3m13 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               loop_particles = [ [ [P.g, P.S3m13] ] ],
               couplings = {(0,0,0):C.R2GC_195_46,(0,1,0):C.R2GC_196_47})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.a, P.a, P.S3m13__star__, P.S3m13 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_197_48})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.a, P.S3m43__star__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_208_58,(0,1,0):C.R2GC_209_59})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.a, P.a, P.S3m43__star__, P.S3m43 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_210_60})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.a, P.S3p23__star__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_222_67,(0,1,0):C.R2GC_221_66})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.a, P.a, P.S3p23__star__, P.S3p23 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_223_68})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.g, P.S3m13__star__, P.S3m13 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_199_50,(0,1,0):C.R2GC_198_49})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.a, P.g, P.S3m13__star__, P.S3m13 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_200_51})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.g, P.S3m43__star__, P.S3m43 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_199_50,(0,1,0):C.R2GC_198_49})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.a, P.g, P.S3m43__star__, P.S3m43 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_213_61})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.g, P.S3p23__star__, P.S3p23 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_199_50,(0,1,0):C.R2GC_198_49})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.a, P.g, P.S3p23__star__, P.S3p23 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_226_69})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.g, P.g, P.S3m13__star__, P.S3m13 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.S3m13] ] ],
                couplings = {(2,0,0):C.R2GC_201_52,(2,0,1):C.R2GC_201_53,(1,0,0):C.R2GC_201_52,(1,0,1):C.R2GC_201_53,(0,0,0):C.R2GC_183_37,(0,0,1):C.R2GC_193_44})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.g, P.g, P.S3m43__star__, P.S3m43 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.S3m43] ] ],
                couplings = {(2,0,0):C.R2GC_201_52,(2,0,1):C.R2GC_201_53,(1,0,0):C.R2GC_201_52,(1,0,1):C.R2GC_201_53,(0,0,0):C.R2GC_183_37,(0,0,1):C.R2GC_193_44})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.g, P.g, P.S3p23__star__, P.S3p23 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.S3p23] ] ],
                couplings = {(2,0,0):C.R2GC_201_52,(2,0,1):C.R2GC_201_53,(1,0,0):C.R2GC_201_52,(1,0,1):C.R2GC_201_53,(0,0,0):C.R2GC_183_37,(0,0,1):C.R2GC_193_44})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.W__minus__, P.S3m13__star__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_255_90,(0,1,0):C.R2GC_256_91})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.W__minus__, P.S3m13, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_255_90})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.S3m13, P.S3m43__star__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_257_92})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.a, P.W__minus__, P.S3m13__star__, P.S3p23 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_265_97})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.g, P.W__minus__, P.S3m13, P.S3m43__star__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_258_93,(0,0,1):C.R2GC_258_94})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.g, P.W__minus__, P.S3m13__star__, P.S3p23 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_266_98,(0,0,1):C.R2GC_266_99})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.W__minus__, P.W__minus__, P.S3m43__star__, P.S3p23 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23] ] ],
                couplings = {(0,0,1):C.R2GC_283_120,(0,0,0):C.R2GC_283_121})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.W__plus__, P.S3m13__star__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_256_91})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.W__plus__, P.S3m13, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_256_91})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.S3m13__star__, P.S3m43 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_257_92})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.a, P.W__plus__, P.S3m13, P.S3p23__star__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_265_97})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.S3m13__star__, P.S3m43 ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_258_93,(0,0,1):C.R2GC_258_94})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.g, P.W__plus__, P.S3m13, P.S3p23__star__ ],
                color = [ 'T(1,3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_266_98,(0,0,1):C.R2GC_266_99})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.S3m13__star__, P.S3m13 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43], [P.g, P.S3m13, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_260_95,(0,0,1):C.R2GC_253_88})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.S3m43__star__, P.S3m43 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                couplings = {(0,0,1):C.R2GC_253_87,(0,0,0):C.R2GC_253_88})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.S3p23__star__, P.S3p23 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                couplings = {(0,0,1):C.R2GC_253_87,(0,0,0):C.R2GC_253_88})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.W__plus__, P.W__plus__, P.S3m43, P.S3p23__star__ ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23] ] ],
                couplings = {(0,0,1):C.R2GC_283_120,(0,0,0):C.R2GC_283_121})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.ve, P.d, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_247_81})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u, P.e__minus__, P.S3m13__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_247_81})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.ve__tilde__, P.d__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_247_81})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.u__tilde__, P.e__plus__, P.S3m13 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_247_81})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.e__minus__, P.d, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_250_84})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.e__plus__, P.d__tilde__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_250_84})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.ve, P.u, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_277_103})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.ve__tilde__, P.u__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_277_103})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.vm, P.d, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_248_82})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.u, P.mu__minus__, P.S3m13__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_248_82})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.vm__tilde__, P.d__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_248_82})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.u__tilde__, P.mu__plus__, P.S3m13 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_248_82})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.mu__minus__, P.d, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_251_85})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.mu__plus__, P.d__tilde__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_251_85})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.vm, P.u, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_278_104})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.vm__tilde__, P.u__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_278_104})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.vt, P.d, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_249_83})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.u, P.ta__minus__, P.S3m13__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_249_83})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.vt__tilde__, P.d__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_249_83})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.u__tilde__, P.ta__plus__, P.S3m13 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3m13, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_249_83})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.ta__minus__, P.d, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_252_86})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.ta__plus__, P.d__tilde__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_252_86})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.vt, P.u, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_279_105})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.vt__tilde__, P.u__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3p23, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_279_105})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.ve, P.s, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_240_74})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.e__minus__, P.c, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_240_74})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.ve__tilde__, P.s__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_240_74})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.e__plus__, P.c__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_240_74})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.s, P.e__minus__, P.S3m43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_270_100})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.s__tilde__, P.e__plus__, P.S3m43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_270_100})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.ve, P.c, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_243_77})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.ve__tilde__, P.c__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_243_77})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.vm, P.s, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_241_75})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.mu__minus__, P.c, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_241_75})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.vm__tilde__, P.s__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_241_75})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.mu__plus__, P.c__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_241_75})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.s, P.mu__minus__, P.S3m43__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_271_101})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.s__tilde__, P.mu__plus__, P.S3m43 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_271_101})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.vm, P.c, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_244_78})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.vm__tilde__, P.c__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_244_78})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.vt, P.s, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_242_76})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.ta__minus__, P.c, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_242_76})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.vt__tilde__, P.s__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_242_76})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.ta__plus__, P.c__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_242_76})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.ta__minus__, P.s, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_272_102})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.ta__plus__, P.s__tilde__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_272_102})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.vt, P.c, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_245_79})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.vt__tilde__, P.c__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.S3p23] ] ],
                couplings = {(0,0,0):C.R2GC_245_79})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.ve, P.b, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_299_171})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.t, P.e__minus__, P.S3m13__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_299_171})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.ve__tilde__, P.b__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_299_171})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.t__tilde__, P.e__plus__, P.S3m13 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_299_171})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.e__minus__, P.b, P.S3m43__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_300_172})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.e__plus__, P.b__tilde__, P.S3m43 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                couplings = {(0,0,0):C.R2GC_300_172})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.ve, P.t, P.S3p23__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_331_192})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.ve__tilde__, P.t__tilde__, P.S3p23 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_331_192})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.vm, P.b, P.S3m13__star__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_301_173})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.t, P.mu__minus__, P.S3m13__star__ ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_301_173})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.vm__tilde__, P.b__tilde__, P.S3m13 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                couplings = {(0,0,0):C.R2GC_301_173})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.mu__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_301_173})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.mu__minus__, P.b, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_302_174})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.mu__plus__, P.b__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_302_174})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.vm, P.t, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_333_193})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.vm__tilde__, P.t__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_333_193})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.vt, P.b, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_303_175})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.ta__minus__, P.t, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_175})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.vt__tilde__, P.b__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_303_175})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.ta__plus__, P.t__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_303_175})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.ta__minus__, P.b, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_304_176})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.ta__plus__, P.b__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_304_176})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.vt, P.t, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_335_194})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.vt__tilde__, P.t__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_335_194})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_202_54})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_203_55})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_215_62})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_216_63})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_228_70})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_229_71})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_204_56})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_217_64})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_230_72})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.S3m13, P.S3m43__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_254_89})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.S3m13__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_261_96})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.S3m13__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_254_89})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.S3m13, P.S3p23__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_261_96})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_205_57})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_218_65})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_231_73})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_139_3})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_139_3})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_139_3})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_187_42})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_187_42})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_187_42})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_188_43})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_246_80})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_157_25,(0,1,0):C.R2GC_140_4})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_157_25,(0,1,0):C.R2GC_140_4})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_157_25,(0,1,0):C.R2GC_140_4})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_158_26,(0,1,0):C.R2GC_142_5})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_158_26,(0,1,0):C.R2GC_142_5})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_158_26,(0,1,0):C.R2GC_142_5})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_138_2})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_138_2})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_324_189,(0,1,0):C.R2GC_138_2})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_138_2})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_138_2})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_294_168,(0,1,0):C.R2GC_138_2})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.R2GC_305_177,(0,1,0):C.R2GC_194_45})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.R2GC_305_177,(0,1,0):C.R2GC_194_45})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.R2GC_305_177,(0,1,0):C.R2GC_194_45})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                 couplings = {(0,2,2):C.R2GC_137_1,(0,0,0):C.R2GC_147_6,(0,0,3):C.R2GC_147_7,(0,1,1):C.R2GC_150_12})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_148_8,(0,0,1):C.R2GC_148_9})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_151_13,(0,0,1):C.R2GC_151_14})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_153_17,(0,0,1):C.R2GC_153_18})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_156_23,(0,0,1):C.R2GC_156_24})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_161_28})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_152_15,(0,0,1):C.R2GC_152_16})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV7 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,0,0):C.R2GC_155_21,(1,0,1):C.R2GC_155_22,(0,1,0):C.R2GC_154_19,(0,1,1):C.R2GC_154_20})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_149_10,(0,0,1):C.R2GC_149_11})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_149_10,(0,0,1):C.R2GC_149_11})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_160_27})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.S3p23__star__, P.S3p23__star__, P.S3p23, P.S3p23 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_280_106,(1,0,0):C.R2GC_282_116,(1,0,3):C.R2GC_280_108,(1,0,5):C.R2GC_282_117,(1,0,1):C.R2GC_282_118,(1,0,4):C.R2GC_282_119,(0,0,2):C.R2GC_280_106,(0,0,0):C.R2GC_282_116,(0,0,3):C.R2GC_280_108,(0,0,5):C.R2GC_282_117,(0,0,1):C.R2GC_282_118,(0,0,4):C.R2GC_282_119})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.S3m13__star__, P.S3m13, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13], [P.a, P.g, P.S3p23] ], [ [P.a, P.g, P.S3m13, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.S3p23, P.Z] ], [ [P.g, P.S3m13, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.Z], [P.g, P.S3p23, P.Z] ], [ [P.g, P.W__plus__] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_286_138,(1,0,0):C.R2GC_288_152,(1,0,4):C.R2GC_286_140,(1,0,10):C.R2GC_283_120,(1,0,11):C.R2GC_288_153,(1,0,1):C.R2GC_288_154,(1,0,5):C.R2GC_286_143,(1,0,8):C.R2GC_286_144,(1,0,9):C.R2GC_288_155,(1,0,2):C.R2GC_288_156,(1,0,6):C.R2GC_284_125,(1,0,7):C.R2GC_288_157,(0,0,3):C.R2GC_285_126,(0,0,0):C.R2GC_280_107,(0,0,4):C.R2GC_285_128,(0,0,10):C.R2GC_285_129,(0,0,11):C.R2GC_287_148,(0,0,1):C.R2GC_151_13,(0,0,5):C.R2GC_285_132,(0,0,8):C.R2GC_285_133,(0,0,9):C.R2GC_287_149,(0,0,2):C.R2GC_287_150,(0,0,6):C.R2GC_285_136,(0,0,7):C.R2GC_287_151})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.S3m13__star__, P.S3m13__star__, P.S3m13, P.S3m13 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13] ], [ [P.g] ], [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_280_106,(1,0,0):C.R2GC_280_107,(1,0,3):C.R2GC_280_108,(1,0,5):C.R2GC_280_109,(1,0,1):C.R2GC_280_110,(1,0,4):C.R2GC_280_111,(0,0,2):C.R2GC_280_106,(0,0,0):C.R2GC_280_107,(0,0,3):C.R2GC_280_108,(0,0,5):C.R2GC_280_109,(0,0,1):C.R2GC_280_110,(0,0,4):C.R2GC_280_111})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.S3m13__star__, P.S3m13__star__, P.S3m43, P.S3p23 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.W__plus__], [P.g, P.S3m13, P.S3p23, P.W__plus__], [P.g, P.S3m43, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.W__plus__] ], [ [P.g, P.S3m43, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.W__plus__] ] ],
                 couplings = {(1,0,3):C.R2GC_284_122,(1,0,1):C.R2GC_284_123,(1,0,2):C.R2GC_284_124,(1,0,0):C.R2GC_284_125,(0,0,3):C.R2GC_284_122,(0,0,1):C.R2GC_284_123,(0,0,2):C.R2GC_284_124,(0,0,0):C.R2GC_284_125})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.S3m13, P.S3m13, P.S3m43__star__, P.S3p23__star__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.W__plus__], [P.g, P.S3m13, P.S3p23, P.W__plus__], [P.g, P.S3m43, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.W__plus__] ], [ [P.g, P.S3m43, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.W__plus__] ] ],
                 couplings = {(1,0,3):C.R2GC_284_122,(1,0,1):C.R2GC_284_123,(1,0,2):C.R2GC_284_124,(1,0,0):C.R2GC_284_125,(0,0,3):C.R2GC_284_122,(0,0,1):C.R2GC_284_123,(0,0,2):C.R2GC_284_124,(0,0,0):C.R2GC_284_125})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.S3m43__star__, P.S3m43, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m43], [P.a, P.g, P.S3p23] ], [ [P.a, P.g, P.S3m43, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3m43], [P.g, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23, P.Z] ], [ [P.g, P.S3m43, P.Z], [P.g, P.S3p23, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_286_138,(1,0,0):C.R2GC_290_162,(1,0,4):C.R2GC_286_140,(1,0,8):C.R2GC_290_163,(1,0,1):C.R2GC_290_164,(1,0,5):C.R2GC_286_143,(1,0,7):C.R2GC_290_165,(1,0,2):C.R2GC_290_166,(1,0,6):C.R2GC_290_167,(0,0,3):C.R2GC_285_126,(0,0,0):C.R2GC_282_116,(0,0,4):C.R2GC_285_128,(0,0,8):C.R2GC_289_158,(0,0,1):C.R2GC_151_14,(0,0,5):C.R2GC_285_132,(0,0,7):C.R2GC_289_159,(0,0,2):C.R2GC_289_160,(0,0,6):C.R2GC_289_161})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.S3m13__star__, P.S3m13, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13], [P.a, P.g, P.S3m43] ], [ [P.a, P.g, P.S3m13, P.S3m43] ], [ [P.g] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43, P.W__plus__] ], [ [P.g, P.S3m13, P.S3m43, P.Z] ], [ [P.g, P.S3m13, P.W__plus__], [P.g, P.S3m43, P.W__plus__] ], [ [P.g, P.S3m13, P.Z], [P.g, P.S3m43, P.Z] ], [ [P.g, P.W__plus__] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_286_138,(1,0,0):C.R2GC_286_139,(1,0,4):C.R2GC_286_140,(1,0,10):C.R2GC_283_120,(1,0,11):C.R2GC_286_141,(1,0,1):C.R2GC_286_142,(1,0,5):C.R2GC_286_143,(1,0,8):C.R2GC_286_144,(1,0,9):C.R2GC_286_145,(1,0,2):C.R2GC_286_146,(1,0,6):C.R2GC_284_125,(1,0,7):C.R2GC_286_147,(0,0,3):C.R2GC_285_126,(0,0,0):C.R2GC_285_127,(0,0,4):C.R2GC_285_128,(0,0,10):C.R2GC_285_129,(0,0,11):C.R2GC_285_130,(0,0,1):C.R2GC_285_131,(0,0,5):C.R2GC_285_132,(0,0,8):C.R2GC_285_133,(0,0,9):C.R2GC_285_134,(0,0,2):C.R2GC_285_135,(0,0,6):C.R2GC_285_136,(0,0,7):C.R2GC_285_137})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.S3m43__star__, P.S3m43__star__, P.S3m43, P.S3m43 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m43] ], [ [P.g] ], [ [P.g, P.S3m43] ], [ [P.g, P.S3m43, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_280_106,(1,0,0):C.R2GC_281_112,(1,0,3):C.R2GC_280_108,(1,0,5):C.R2GC_281_113,(1,0,1):C.R2GC_281_114,(1,0,4):C.R2GC_281_115,(0,0,2):C.R2GC_280_106,(0,0,0):C.R2GC_281_112,(0,0,3):C.R2GC_280_108,(0,0,5):C.R2GC_281_113,(0,0,1):C.R2GC_281_114,(0,0,4):C.R2GC_281_115})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_309_300,(0,0,1):C.UVGC_309_301,(0,0,2):C.UVGC_309_302,(0,0,3):C.UVGC_184_21,(0,0,4):C.UVGC_309_303,(0,0,5):C.UVGC_309_304,(0,1,0):C.UVGC_312_310,(0,1,1):C.UVGC_312_311,(0,1,2):C.UVGC_313_315,(0,1,3):C.UVGC_313_316,(0,1,4):C.UVGC_313_317,(0,1,5):C.UVGC_312_314,(0,3,0):C.UVGC_312_310,(0,3,1):C.UVGC_312_311,(0,3,2):C.UVGC_312_312,(0,3,3):C.UVGC_178_11,(0,3,4):C.UVGC_312_313,(0,3,5):C.UVGC_312_314,(0,5,0):C.UVGC_309_300,(0,5,1):C.UVGC_309_301,(0,5,2):C.UVGC_311_307,(0,5,3):C.UVGC_311_308,(0,5,4):C.UVGC_311_309,(0,5,5):C.UVGC_309_304,(0,6,0):C.UVGC_309_300,(0,6,1):C.UVGC_309_301,(0,6,2):C.UVGC_310_305,(0,6,3):C.UVGC_310_306,(0,6,4):C.UVGC_309_303,(0,6,5):C.UVGC_309_304,(0,7,0):C.UVGC_312_310,(0,7,1):C.UVGC_312_311,(0,7,2):C.UVGC_314_318,(0,7,3):C.UVGC_314_319,(0,7,4):C.UVGC_313_317,(0,7,5):C.UVGC_312_314,(0,2,2):C.UVGC_178_10,(0,2,3):C.UVGC_178_11,(0,4,2):C.UVGC_184_20,(0,4,3):C.UVGC_184_21,(0,4,4):C.UVGC_184_22})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.S3m13], [P.S3m43], [P.S3p23], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(2,0,4):C.UVGC_180_15,(2,0,5):C.UVGC_180_14,(0,0,4):C.UVGC_180_15,(0,0,5):C.UVGC_180_14,(4,0,4):C.UVGC_179_12,(4,0,5):C.UVGC_179_13,(3,0,4):C.UVGC_179_12,(3,0,5):C.UVGC_179_13,(8,0,4):C.UVGC_180_14,(8,0,5):C.UVGC_180_15,(7,0,0):C.UVGC_318_334,(7,0,3):C.UVGC_201_58,(7,0,4):C.UVGC_318_335,(7,0,5):C.UVGC_318_336,(7,0,6):C.UVGC_318_337,(7,0,7):C.UVGC_318_338,(6,0,0):C.UVGC_318_334,(6,0,3):C.UVGC_201_58,(6,0,4):C.UVGC_319_339,(6,0,5):C.UVGC_319_340,(6,0,6):C.UVGC_318_337,(6,0,7):C.UVGC_318_338,(5,0,4):C.UVGC_179_12,(5,0,5):C.UVGC_179_13,(1,0,4):C.UVGC_179_12,(1,0,5):C.UVGC_179_13,(11,0,4):C.UVGC_183_18,(11,0,5):C.UVGC_183_19,(10,0,4):C.UVGC_183_18,(10,0,5):C.UVGC_183_19,(9,0,4):C.UVGC_182_16,(9,0,5):C.UVGC_182_17,(2,1,4):C.UVGC_180_15,(2,1,5):C.UVGC_180_14,(0,1,4):C.UVGC_180_15,(0,1,5):C.UVGC_180_14,(6,1,0):C.UVGC_315_320,(6,1,4):C.UVGC_316_325,(6,1,5):C.UVGC_316_326,(6,1,6):C.UVGC_316_327,(6,1,7):C.UVGC_315_324,(4,1,4):C.UVGC_179_12,(4,1,5):C.UVGC_179_13,(3,1,4):C.UVGC_179_12,(3,1,5):C.UVGC_179_13,(8,1,0):C.UVGC_320_341,(8,1,3):C.UVGC_320_342,(8,1,4):C.UVGC_320_343,(8,1,5):C.UVGC_320_344,(8,1,6):C.UVGC_320_345,(8,1,7):C.UVGC_320_346,(7,1,1):C.UVGC_185_23,(7,1,4):C.UVGC_186_26,(7,1,5):C.UVGC_186_27,(5,1,4):C.UVGC_179_12,(5,1,5):C.UVGC_179_13,(1,1,4):C.UVGC_179_12,(1,1,5):C.UVGC_179_13,(11,1,4):C.UVGC_183_18,(11,1,5):C.UVGC_183_19,(10,1,4):C.UVGC_183_18,(10,1,5):C.UVGC_183_19,(9,1,4):C.UVGC_182_16,(9,1,5):C.UVGC_182_17,(2,2,4):C.UVGC_180_15,(2,2,5):C.UVGC_180_14,(0,2,4):C.UVGC_180_15,(0,2,5):C.UVGC_180_14,(4,2,4):C.UVGC_179_12,(4,2,5):C.UVGC_179_13,(3,2,4):C.UVGC_179_12,(3,2,5):C.UVGC_179_13,(8,2,0):C.UVGC_317_328,(8,2,3):C.UVGC_317_329,(8,2,4):C.UVGC_317_330,(8,2,5):C.UVGC_317_331,(8,2,6):C.UVGC_317_332,(8,2,7):C.UVGC_317_333,(6,2,2):C.UVGC_185_23,(6,2,4):C.UVGC_185_24,(6,2,5):C.UVGC_182_16,(6,2,6):C.UVGC_185_25,(7,2,0):C.UVGC_315_320,(7,2,4):C.UVGC_315_321,(7,2,5):C.UVGC_315_322,(7,2,6):C.UVGC_315_323,(7,2,7):C.UVGC_315_324,(5,2,4):C.UVGC_179_12,(5,2,5):C.UVGC_179_13,(1,2,4):C.UVGC_179_12,(1,2,5):C.UVGC_179_13,(11,2,4):C.UVGC_183_18,(11,2,5):C.UVGC_183_19,(10,2,4):C.UVGC_183_18,(10,2,5):C.UVGC_183_19,(9,2,4):C.UVGC_182_16,(9,2,5):C.UVGC_182_17})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_329_358,(0,0,2):C.UVGC_329_359,(0,0,1):C.UVGC_329_360,(0,1,0):C.UVGC_336_373,(0,1,2):C.UVGC_336_374,(0,1,1):C.UVGC_336_375})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_275})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_297_274})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_338_379})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_339_380})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_337_376,(0,0,2):C.UVGC_337_377,(0,0,1):C.UVGC_337_378,(0,1,0):C.UVGC_328_355,(0,1,2):C.UVGC_328_356,(0,1,1):C.UVGC_328_357})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.a, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_195_39,(0,1,0):C.UVGC_196_40})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.a, P.a, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_197_41})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.a, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_208_74,(0,1,0):C.UVGC_209_75})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.a, P.a, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_210_76})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.a, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_222_95,(0,1,0):C.UVGC_221_94})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.a, P.a, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_223_96})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.g, P.S3m13__star__, P.S3m13 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_199_43,(0,0,1):C.UVGC_199_44,(0,0,2):C.UVGC_199_45,(0,0,3):C.UVGC_199_46,(0,0,5):C.UVGC_199_47,(0,0,6):C.UVGC_199_48,(0,0,4):C.UVGC_199_49,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_198_42})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.a, P.g, P.S3m13__star__, P.S3m13 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_200_50,(0,0,1):C.UVGC_200_51,(0,0,2):C.UVGC_200_52,(0,0,3):C.UVGC_200_53,(0,0,5):C.UVGC_200_54,(0,0,6):C.UVGC_200_55,(0,0,4):C.UVGC_200_56})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.g, P.S3m43__star__, P.S3m43 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_199_43,(0,0,1):C.UVGC_199_44,(0,0,2):C.UVGC_199_45,(0,0,3):C.UVGC_199_46,(0,0,5):C.UVGC_199_47,(0,0,6):C.UVGC_199_48,(0,0,4):C.UVGC_199_49,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_198_42})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.a, P.g, P.S3m43__star__, P.S3m43 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_213_77,(0,0,1):C.UVGC_213_78,(0,0,2):C.UVGC_213_79,(0,0,3):C.UVGC_213_80,(0,0,5):C.UVGC_213_81,(0,0,6):C.UVGC_213_82,(0,0,4):C.UVGC_213_83})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.g, P.S3p23__star__, P.S3p23 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_199_43,(0,0,1):C.UVGC_199_44,(0,0,2):C.UVGC_199_45,(0,0,3):C.UVGC_199_46,(0,0,5):C.UVGC_199_47,(0,0,6):C.UVGC_199_48,(0,0,4):C.UVGC_199_49,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_198_42})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.a, P.g, P.S3p23__star__, P.S3p23 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_226_97,(0,0,1):C.UVGC_226_98,(0,0,2):C.UVGC_226_99,(0,0,3):C.UVGC_226_100,(0,0,5):C.UVGC_226_101,(0,0,6):C.UVGC_226_102,(0,0,4):C.UVGC_226_103})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.g, P.g, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(2,0,0):C.UVGC_201_57,(2,0,1):C.UVGC_201_58,(2,0,2):C.UVGC_201_59,(2,0,3):C.UVGC_201_60,(2,0,5):C.UVGC_201_61,(2,0,6):C.UVGC_201_62,(2,0,4):C.UVGC_201_63,(1,0,0):C.UVGC_201_57,(1,0,1):C.UVGC_201_58,(1,0,2):C.UVGC_201_59,(1,0,3):C.UVGC_201_60,(1,0,5):C.UVGC_201_61,(1,0,6):C.UVGC_201_62,(1,0,4):C.UVGC_201_63,(0,0,2):C.UVGC_193_36,(0,0,4):C.UVGC_193_37})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.g, P.g, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(2,0,0):C.UVGC_201_57,(2,0,1):C.UVGC_201_58,(2,0,2):C.UVGC_201_59,(2,0,3):C.UVGC_201_60,(2,0,5):C.UVGC_201_61,(2,0,6):C.UVGC_201_62,(2,0,4):C.UVGC_201_63,(1,0,0):C.UVGC_201_57,(1,0,1):C.UVGC_201_58,(1,0,2):C.UVGC_201_59,(1,0,3):C.UVGC_201_60,(1,0,5):C.UVGC_201_61,(1,0,6):C.UVGC_201_62,(1,0,4):C.UVGC_201_63,(0,0,2):C.UVGC_193_36,(0,0,4):C.UVGC_193_37})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.g, P.g, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(2,0,0):C.UVGC_201_57,(2,0,1):C.UVGC_201_58,(2,0,2):C.UVGC_201_59,(2,0,3):C.UVGC_201_60,(2,0,5):C.UVGC_201_61,(2,0,6):C.UVGC_201_62,(2,0,4):C.UVGC_201_63,(1,0,0):C.UVGC_201_57,(1,0,1):C.UVGC_201_58,(1,0,2):C.UVGC_201_59,(1,0,3):C.UVGC_201_60,(1,0,5):C.UVGC_201_61,(1,0,6):C.UVGC_201_62,(1,0,4):C.UVGC_201_63,(0,0,2):C.UVGC_193_36,(0,0,4):C.UVGC_193_37})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.W__minus__, P.S3m13__star__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_262_177,(0,0,2):C.UVGC_255_158,(0,0,1):C.UVGC_255_159,(0,1,0):C.UVGC_256_160,(0,1,2):C.UVGC_264_178,(0,1,1):C.UVGC_256_161})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.W__minus__, P.S3m13, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,1,1):C.UVGC_255_158,(0,1,2):C.UVGC_255_159,(0,0,0):C.UVGC_169_6,(0,2,3):C.UVGC_168_5})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.S3m13, P.S3m43__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_257_162,(0,0,2):C.UVGC_257_163,(0,0,1):C.UVGC_257_164})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.S3m13__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_265_179,(0,0,2):C.UVGC_265_180,(0,0,1):C.UVGC_265_181})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.S3m13, P.S3m43__star__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_258_165,(0,0,1):C.UVGC_258_166,(0,0,2):C.UVGC_258_167,(0,0,3):C.UVGC_258_168,(0,0,6):C.UVGC_258_169,(0,0,7):C.UVGC_258_170,(0,0,4):C.UVGC_258_171,(0,0,5):C.UVGC_258_172})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.S3m13__star__, P.S3p23 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_266_182,(0,0,1):C.UVGC_266_183,(0,0,2):C.UVGC_266_184,(0,0,3):C.UVGC_266_185,(0,0,6):C.UVGC_266_186,(0,0,7):C.UVGC_266_187,(0,0,4):C.UVGC_266_188,(0,0,5):C.UVGC_266_189})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__minus__, P.S3m43__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43], [P.g, P.S3m13, P.S3p23], [P.g, P.S3m43, P.S3p23] ], [ [P.g, P.S3m13, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43], [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_283_222,(0,0,3):C.UVGC_283_223,(0,0,1):C.UVGC_283_224,(0,0,2):C.UVGC_283_225})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.W__plus__, P.S3m13__star__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,1,1):C.UVGC_256_160,(0,1,2):C.UVGC_256_161,(0,0,0):C.UVGC_168_5,(0,2,3):C.UVGC_169_6})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.W__plus__, P.S3m13, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,1,1):C.UVGC_256_160,(0,1,2):C.UVGC_256_161,(0,0,0):C.UVGC_168_5,(0,2,3):C.UVGC_169_6})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.S3m13__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_257_162,(0,0,2):C.UVGC_257_163,(0,0,1):C.UVGC_257_164})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.S3m13, P.S3p23__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_265_179,(0,0,2):C.UVGC_265_180,(0,0,1):C.UVGC_265_181})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.S3m13__star__, P.S3m43 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_258_165,(0,0,1):C.UVGC_258_166,(0,0,2):C.UVGC_258_167,(0,0,3):C.UVGC_258_168,(0,0,6):C.UVGC_258_169,(0,0,7):C.UVGC_258_170,(0,0,4):C.UVGC_258_171,(0,0,5):C.UVGC_258_172})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.S3m13, P.S3p23__star__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_266_182,(0,0,1):C.UVGC_266_183,(0,0,2):C.UVGC_266_184,(0,0,3):C.UVGC_266_185,(0,0,6):C.UVGC_266_186,(0,0,7):C.UVGC_266_187,(0,0,4):C.UVGC_266_188,(0,0,5):C.UVGC_266_189})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43], [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3m43], [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_260_173,(0,0,2):C.UVGC_253_152,(0,0,1):C.UVGC_253_154})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_253_152,(0,0,2):C.UVGC_253_153,(0,0,1):C.UVGC_253_154})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_253_152,(0,0,2):C.UVGC_253_153,(0,0,1):C.UVGC_253_154})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.W__plus__, P.W__plus__, P.S3m43, P.S3p23__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43], [P.g, P.S3m13, P.S3p23], [P.g, P.S3m43, P.S3p23] ], [ [P.g, P.S3m13, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43], [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_283_222,(0,0,3):C.UVGC_283_223,(0,0,1):C.UVGC_283_224,(0,0,2):C.UVGC_283_225})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.ve, P.d, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_247_134,(0,0,2):C.UVGC_247_135,(0,0,1):C.UVGC_247_136})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.u, P.e__minus__, P.S3m13__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_247_135,(0,0,2):C.UVGC_247_134,(0,0,1):C.UVGC_247_136})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.d__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_247_134,(0,0,2):C.UVGC_247_135,(0,0,1):C.UVGC_247_136})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.e__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_247_135,(0,0,2):C.UVGC_247_134,(0,0,1):C.UVGC_247_136})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.e__minus__, P.d, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_250_143,(0,0,2):C.UVGC_250_144,(0,0,1):C.UVGC_250_145})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.e__plus__, P.d__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_250_143,(0,0,2):C.UVGC_250_144,(0,0,1):C.UVGC_250_145})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.ve, P.u, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_277_199,(0,0,2):C.UVGC_277_200,(0,0,1):C.UVGC_277_201})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.u__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_277_199,(0,0,2):C.UVGC_277_200,(0,0,1):C.UVGC_277_201})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.vm, P.d, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_248_137,(0,0,2):C.UVGC_248_138,(0,0,1):C.UVGC_248_139})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.u, P.mu__minus__, P.S3m13__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_248_138,(0,0,2):C.UVGC_248_137,(0,0,1):C.UVGC_248_139})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.d__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_248_137,(0,0,2):C.UVGC_248_138,(0,0,1):C.UVGC_248_139})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.mu__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_248_138,(0,0,2):C.UVGC_248_137,(0,0,1):C.UVGC_248_139})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.mu__minus__, P.d, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_251_146,(0,0,2):C.UVGC_251_147,(0,0,1):C.UVGC_251_148})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.d__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_251_146,(0,0,2):C.UVGC_251_147,(0,0,1):C.UVGC_251_148})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.vm, P.u, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_278_202,(0,0,2):C.UVGC_278_203,(0,0,1):C.UVGC_278_204})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.u__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_278_202,(0,0,2):C.UVGC_278_203,(0,0,1):C.UVGC_278_204})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.vt, P.d, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_249_140,(0,0,2):C.UVGC_249_141,(0,0,1):C.UVGC_249_142})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.u, P.ta__minus__, P.S3m13__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_249_141,(0,0,2):C.UVGC_249_140,(0,0,1):C.UVGC_249_142})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.d__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_249_140,(0,0,2):C.UVGC_249_141,(0,0,1):C.UVGC_249_142})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.ta__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_249_141,(0,0,2):C.UVGC_249_140,(0,0,1):C.UVGC_249_142})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.ta__minus__, P.d, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_252_149,(0,0,2):C.UVGC_252_150,(0,0,1):C.UVGC_252_151})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.d__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_252_149,(0,0,2):C.UVGC_252_150,(0,0,1):C.UVGC_252_151})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.vt, P.u, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_279_205,(0,0,2):C.UVGC_279_206,(0,0,1):C.UVGC_279_207})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.u__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_279_205,(0,0,2):C.UVGC_279_206,(0,0,1):C.UVGC_279_207})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.ve, P.s, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_240_114,(0,0,1):C.UVGC_240_115,(0,0,2):C.UVGC_240_116})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.e__minus__, P.c, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_240_114,(0,0,2):C.UVGC_240_115,(0,0,1):C.UVGC_240_116})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.s__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_240_114,(0,0,1):C.UVGC_240_115,(0,0,2):C.UVGC_240_116})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.e__plus__, P.c__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_240_114,(0,0,2):C.UVGC_240_115,(0,0,1):C.UVGC_240_116})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.s, P.e__minus__, P.S3m43__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_270_190,(0,0,1):C.UVGC_270_191,(0,0,2):C.UVGC_270_192})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.e__plus__, P.S3m43 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_270_190,(0,0,1):C.UVGC_270_191,(0,0,2):C.UVGC_270_192})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.ve, P.c, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_243_123,(0,0,2):C.UVGC_243_124,(0,0,1):C.UVGC_243_125})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.c__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_243_123,(0,0,2):C.UVGC_243_124,(0,0,1):C.UVGC_243_125})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.vm, P.s, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_241_117,(0,0,1):C.UVGC_241_118,(0,0,2):C.UVGC_241_119})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.mu__minus__, P.c, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_241_117,(0,0,2):C.UVGC_241_118,(0,0,1):C.UVGC_241_119})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.s__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_241_117,(0,0,1):C.UVGC_241_118,(0,0,2):C.UVGC_241_119})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.c__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_241_117,(0,0,2):C.UVGC_241_118,(0,0,1):C.UVGC_241_119})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.s, P.mu__minus__, P.S3m43__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_271_193,(0,0,1):C.UVGC_271_194,(0,0,2):C.UVGC_271_195})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.mu__plus__, P.S3m43 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_271_193,(0,0,1):C.UVGC_271_194,(0,0,2):C.UVGC_271_195})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.vm, P.c, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_244_126,(0,0,2):C.UVGC_244_127,(0,0,1):C.UVGC_244_128})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.c__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_244_126,(0,0,2):C.UVGC_244_127,(0,0,1):C.UVGC_244_128})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.vt, P.s, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_242_120,(0,0,1):C.UVGC_242_121,(0,0,2):C.UVGC_242_122})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.ta__minus__, P.c, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_242_120,(0,0,2):C.UVGC_242_121,(0,0,1):C.UVGC_242_122})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.s__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m13] ], [ [P.g, P.s, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_242_120,(0,0,1):C.UVGC_242_121,(0,0,2):C.UVGC_242_122})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.c__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_242_120,(0,0,2):C.UVGC_242_121,(0,0,1):C.UVGC_242_122})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.ta__minus__, P.s, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_272_196,(0,0,1):C.UVGC_272_197,(0,0,2):C.UVGC_272_198})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.s__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.S3m43] ], [ [P.g, P.s, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_272_196,(0,0,1):C.UVGC_272_197,(0,0,2):C.UVGC_272_198})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.vt, P.c, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_245_129,(0,0,2):C.UVGC_245_130,(0,0,1):C.UVGC_245_131})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.c__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_245_129,(0,0,2):C.UVGC_245_130,(0,0,1):C.UVGC_245_131})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.ve, P.b, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_299_276,(0,0,2):C.UVGC_299_277,(0,0,1):C.UVGC_299_278})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.t, P.e__minus__, P.S3m13__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_299_277,(0,0,2):C.UVGC_330_361,(0,0,1):C.UVGC_299_278})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.b__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_299_276,(0,0,2):C.UVGC_299_277,(0,0,1):C.UVGC_299_278})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.e__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_299_277,(0,0,2):C.UVGC_330_361,(0,0,1):C.UVGC_299_278})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.e__minus__, P.b, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_300_279,(0,0,2):C.UVGC_300_280,(0,0,1):C.UVGC_300_281})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.e__plus__, P.b__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_300_279,(0,0,2):C.UVGC_300_280,(0,0,1):C.UVGC_300_281})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.ve, P.t, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_331_362,(0,0,2):C.UVGC_331_363,(0,0,1):C.UVGC_331_364})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.ve__tilde__, P.t__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_331_362,(0,0,2):C.UVGC_331_363,(0,0,1):C.UVGC_331_364})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.vm, P.b, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_301_282,(0,0,2):C.UVGC_301_283,(0,0,1):C.UVGC_301_284})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.t, P.mu__minus__, P.S3m13__star__ ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_301_283,(0,0,2):C.UVGC_332_365,(0,0,1):C.UVGC_301_284})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.b__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_301_282,(0,0,2):C.UVGC_301_283,(0,0,1):C.UVGC_301_284})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.mu__plus__, P.S3m13 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_301_283,(0,0,2):C.UVGC_332_365,(0,0,1):C.UVGC_301_284})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.mu__minus__, P.b, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_302_285,(0,0,2):C.UVGC_302_286,(0,0,1):C.UVGC_302_287})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.mu__plus__, P.b__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_302_285,(0,0,2):C.UVGC_302_286,(0,0,1):C.UVGC_302_287})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.vm, P.t, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_333_366,(0,0,2):C.UVGC_333_367,(0,0,1):C.UVGC_333_368})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.vm__tilde__, P.t__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_333_366,(0,0,2):C.UVGC_333_367,(0,0,1):C.UVGC_333_368})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.vt, P.b, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_303_288,(0,0,2):C.UVGC_303_289,(0,0,1):C.UVGC_303_290})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.ta__minus__, P.t, P.S3m13__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_303_289,(0,0,2):C.UVGC_334_369,(0,0,1):C.UVGC_303_290})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.b__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m13] ], [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_303_288,(0,0,2):C.UVGC_303_289,(0,0,1):C.UVGC_303_290})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.t__tilde__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_303_289,(0,0,2):C.UVGC_334_369,(0,0,1):C.UVGC_303_290})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.ta__minus__, P.b, P.S3m43__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_304_291,(0,0,2):C.UVGC_304_292,(0,0,1):C.UVGC_304_293})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.ta__plus__, P.b__tilde__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_304_291,(0,0,2):C.UVGC_304_292,(0,0,1):C.UVGC_304_293})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.vt, P.t, P.S3p23__star__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_335_370,(0,0,2):C.UVGC_335_371,(0,0,1):C.UVGC_335_372})

V_292 = CTVertex(name = 'V_292',
                 type = 'UV',
                 particles = [ P.vt__tilde__, P.t__tilde__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_335_370,(0,0,2):C.UVGC_335_371,(0,0,1):C.UVGC_335_372})

V_293 = CTVertex(name = 'V_293',
                 type = 'UV',
                 particles = [ P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_202_64})

V_294 = CTVertex(name = 'V_294',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_203_65})

V_295 = CTVertex(name = 'V_295',
                 type = 'UV',
                 particles = [ P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_215_84})

V_296 = CTVertex(name = 'V_296',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_216_85})

V_297 = CTVertex(name = 'V_297',
                 type = 'UV',
                 particles = [ P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_228_104})

V_298 = CTVertex(name = 'V_298',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_229_105})

V_299 = CTVertex(name = 'V_299',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m13] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_204_66,(0,0,1):C.UVGC_204_67,(0,0,2):C.UVGC_204_68,(0,0,3):C.UVGC_204_69,(0,0,5):C.UVGC_204_70,(0,0,6):C.UVGC_204_71,(0,0,4):C.UVGC_204_72})

V_300 = CTVertex(name = 'V_300',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3m43] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_217_86,(0,0,1):C.UVGC_217_87,(0,0,2):C.UVGC_217_88,(0,0,3):C.UVGC_217_89,(0,0,5):C.UVGC_217_90,(0,0,6):C.UVGC_217_91,(0,0,4):C.UVGC_217_92})

V_301 = CTVertex(name = 'V_301',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.S3p23] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_230_106,(0,0,1):C.UVGC_230_107,(0,0,2):C.UVGC_230_108,(0,0,3):C.UVGC_230_109,(0,0,5):C.UVGC_230_110,(0,0,6):C.UVGC_230_111,(0,0,4):C.UVGC_230_112})

V_302 = CTVertex(name = 'V_302',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.S3m13, P.S3m43__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_254_155,(0,0,2):C.UVGC_254_156,(0,0,1):C.UVGC_254_157})

V_303 = CTVertex(name = 'V_303',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.S3m13__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_261_174,(0,0,2):C.UVGC_261_175,(0,0,1):C.UVGC_261_176})

V_304 = CTVertex(name = 'V_304',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.S3m13__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_254_155,(0,0,2):C.UVGC_254_156,(0,0,1):C.UVGC_254_157})

V_305 = CTVertex(name = 'V_305',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.S3m13, P.S3p23__star__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_261_174,(0,0,2):C.UVGC_261_175,(0,0,1):C.UVGC_261_176})

V_306 = CTVertex(name = 'V_306',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13] ] ],
                 couplings = {(0,0,0):C.UVGC_205_73})

V_307 = CTVertex(name = 'V_307',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3m43] ] ],
                 couplings = {(0,0,0):C.UVGC_218_93})

V_308 = CTVertex(name = 'V_308',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_231_113})

V_309 = CTVertex(name = 'V_309',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_164_2})

V_310 = CTVertex(name = 'V_310',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_164_2,(0,1,0):C.UVGC_322_348,(0,2,0):C.UVGC_322_348})

V_311 = CTVertex(name = 'V_311',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_164_2,(0,1,0):C.UVGC_176_7,(0,2,0):C.UVGC_176_7})

V_312 = CTVertex(name = 'V_312',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_187_28,(0,1,0):C.UVGC_292_269,(0,2,0):C.UVGC_292_269})

V_313 = CTVertex(name = 'V_313',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_187_28,(0,1,0):C.UVGC_167_4,(0,2,0):C.UVGC_167_4})

V_314 = CTVertex(name = 'V_314',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_187_28,(0,1,0):C.UVGC_167_4,(0,2,0):C.UVGC_167_4})

V_315 = CTVertex(name = 'V_315',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_189_30,(0,0,1):C.UVGC_189_31,(0,0,3):C.UVGC_189_32,(0,0,4):C.UVGC_189_33,(0,0,5):C.UVGC_189_34,(0,0,6):C.UVGC_189_35,(0,0,2):C.UVGC_188_29,(0,1,2):C.UVGC_165_3,(0,2,2):C.UVGC_165_3})

V_316 = CTVertex(name = 'V_316',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_188_29,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_323_349,(0,2,0):C.UVGC_189_30,(0,2,1):C.UVGC_189_31,(0,2,2):C.UVGC_189_32,(0,2,3):C.UVGC_189_33,(0,2,5):C.UVGC_189_34,(0,2,6):C.UVGC_189_35,(0,2,4):C.UVGC_323_349})

V_317 = CTVertex(name = 'V_317',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_188_29,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_165_3,(0,2,0):C.UVGC_189_30,(0,2,1):C.UVGC_189_31,(0,2,2):C.UVGC_189_32,(0,2,3):C.UVGC_189_33,(0,2,5):C.UVGC_189_34,(0,2,6):C.UVGC_189_35,(0,2,4):C.UVGC_165_3})

V_318 = CTVertex(name = 'V_318',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,1):C.UVGC_188_29,(0,1,0):C.UVGC_189_30,(0,1,2):C.UVGC_189_31,(0,1,3):C.UVGC_189_32,(0,1,4):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,1):C.UVGC_293_270,(0,2,0):C.UVGC_189_30,(0,2,2):C.UVGC_189_31,(0,2,3):C.UVGC_189_32,(0,2,4):C.UVGC_189_33,(0,2,5):C.UVGC_189_34,(0,2,6):C.UVGC_189_35,(0,2,1):C.UVGC_293_270})

V_319 = CTVertex(name = 'V_319',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,2):C.UVGC_188_29,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,3):C.UVGC_189_32,(0,1,4):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,2):C.UVGC_165_3,(0,2,0):C.UVGC_189_30,(0,2,1):C.UVGC_189_31,(0,2,3):C.UVGC_189_32,(0,2,4):C.UVGC_189_33,(0,2,5):C.UVGC_189_34,(0,2,6):C.UVGC_189_35,(0,2,2):C.UVGC_165_3})

V_320 = CTVertex(name = 'V_320',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,0,4):C.UVGC_188_29,(0,1,0):C.UVGC_189_30,(0,1,1):C.UVGC_189_31,(0,1,2):C.UVGC_189_32,(0,1,3):C.UVGC_189_33,(0,1,5):C.UVGC_189_34,(0,1,6):C.UVGC_189_35,(0,1,4):C.UVGC_165_3,(0,2,0):C.UVGC_189_30,(0,2,1):C.UVGC_189_31,(0,2,2):C.UVGC_189_32,(0,2,3):C.UVGC_189_33,(0,2,5):C.UVGC_189_34,(0,2,6):C.UVGC_189_35,(0,2,4):C.UVGC_165_3})

V_321 = CTVertex(name = 'V_321',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_246_132,(0,0,1):C.UVGC_246_133})

V_322 = CTVertex(name = 'V_322',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_325_351,(0,0,2):C.UVGC_325_352,(0,0,1):C.UVGC_246_133})

V_323 = CTVertex(name = 'V_323',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_246_132,(0,0,1):C.UVGC_246_133})

V_324 = CTVertex(name = 'V_324',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_325_351,(0,0,2):C.UVGC_325_352,(0,0,1):C.UVGC_246_133})

V_325 = CTVertex(name = 'V_325',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_246_132,(0,0,1):C.UVGC_246_133})

V_326 = CTVertex(name = 'V_326',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_246_132,(0,0,1):C.UVGC_246_133})

V_327 = CTVertex(name = 'V_327',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_326_353,(0,1,0):C.UVGC_327_354})

V_328 = CTVertex(name = 'V_328',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_295_272,(0,1,0):C.UVGC_296_273})

V_329 = CTVertex(name = 'V_329',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_163_1})

V_330 = CTVertex(name = 'V_330',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_1})

V_331 = CTVertex(name = 'V_331',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_324_350,(0,1,0):C.UVGC_321_347})

V_332 = CTVertex(name = 'V_332',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_1})

V_333 = CTVertex(name = 'V_333',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_163_1})

V_334 = CTVertex(name = 'V_334',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_294_271,(0,1,0):C.UVGC_291_268})

V_335 = CTVertex(name = 'V_335',
                 type = 'UV',
                 particles = [ P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_307_296,(0,1,0):C.UVGC_194_38})

V_336 = CTVertex(name = 'V_336',
                 type = 'UV',
                 particles = [ P.S3m13__star__, P.S3m13 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3m13] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_305_294,(0,0,1):C.UVGC_305_295,(0,1,0):C.UVGC_194_38})

V_337 = CTVertex(name = 'V_337',
                 type = 'UV',
                 particles = [ P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.S3m43] ], [ [P.g, P.S3p23] ] ],
                 couplings = {(0,0,0):C.UVGC_305_294,(0,0,1):C.UVGC_305_295,(0,1,0):C.UVGC_194_38})

V_338 = CTVertex(name = 'V_338',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.S3m13], [P.S3m43], [P.S3p23] ], [ [P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_308_297,(0,1,3):C.UVGC_308_298,(0,1,4):C.UVGC_308_299,(0,0,1):C.UVGC_177_8,(0,0,2):C.UVGC_177_9})

V_339 = CTVertex(name = 'V_339',
                 type = 'UV',
                 particles = [ P.S3p23__star__, P.S3p23__star__, P.S3p23, P.S3p23 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3p23] ], [ [P.g, P.S3p23, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_280_208,(1,0,0):C.UVGC_282_218,(1,0,3):C.UVGC_280_210,(1,0,5):C.UVGC_282_219,(1,0,1):C.UVGC_282_220,(1,0,4):C.UVGC_282_221,(0,0,2):C.UVGC_280_208,(0,0,0):C.UVGC_282_218,(0,0,3):C.UVGC_280_210,(0,0,5):C.UVGC_282_219,(0,0,1):C.UVGC_282_220,(0,0,4):C.UVGC_282_221})

V_340 = CTVertex(name = 'V_340',
                 type = 'UV',
                 particles = [ P.S3m13__star__, P.S3m13, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13], [P.a, P.g, P.S3p23] ], [ [P.a, P.g, P.S3m13, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3m13], [P.g, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23] ], [ [P.g, P.S3m13, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.S3p23, P.Z] ], [ [P.g, P.S3m13, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.Z], [P.g, P.S3p23, P.Z] ], [ [P.g, P.W__plus__] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_286_240,(1,0,0):C.UVGC_288_254,(1,0,4):C.UVGC_286_242,(1,0,10):C.UVGC_283_224,(1,0,11):C.UVGC_288_255,(1,0,1):C.UVGC_288_256,(1,0,5):C.UVGC_286_245,(1,0,8):C.UVGC_286_246,(1,0,9):C.UVGC_288_257,(1,0,2):C.UVGC_288_258,(1,0,6):C.UVGC_284_228,(1,0,7):C.UVGC_288_259,(0,0,3):C.UVGC_285_229,(0,0,0):C.UVGC_280_209,(0,0,4):C.UVGC_285_231,(0,0,10):C.UVGC_285_232,(0,0,11):C.UVGC_287_250,(0,0,1):C.UVGC_280_212,(0,0,5):C.UVGC_285_235,(0,0,8):C.UVGC_285_236,(0,0,9):C.UVGC_287_251,(0,0,2):C.UVGC_287_252,(0,0,6):C.UVGC_284_226,(0,0,7):C.UVGC_287_253})

V_341 = CTVertex(name = 'V_341',
                 type = 'UV',
                 particles = [ P.S3m13__star__, P.S3m13__star__, P.S3m13, P.S3m13 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13] ], [ [P.g] ], [ [P.g, P.S3m13] ], [ [P.g, P.S3m13, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_280_208,(1,0,0):C.UVGC_280_209,(1,0,3):C.UVGC_280_210,(1,0,5):C.UVGC_280_211,(1,0,1):C.UVGC_280_212,(1,0,4):C.UVGC_280_213,(0,0,2):C.UVGC_280_208,(0,0,0):C.UVGC_280_209,(0,0,3):C.UVGC_280_210,(0,0,5):C.UVGC_280_211,(0,0,1):C.UVGC_280_212,(0,0,4):C.UVGC_280_213})

V_342 = CTVertex(name = 'V_342',
                 type = 'UV',
                 particles = [ P.S3m13__star__, P.S3m13__star__, P.S3m43, P.S3p23 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.W__plus__], [P.g, P.S3m13, P.S3p23, P.W__plus__], [P.g, P.S3m43, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.W__plus__] ], [ [P.g, P.S3m43, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.W__plus__] ] ],
                 couplings = {(1,0,3):C.UVGC_253_152,(1,0,1):C.UVGC_284_226,(1,0,2):C.UVGC_284_227,(1,0,0):C.UVGC_284_228,(0,0,3):C.UVGC_253_152,(0,0,1):C.UVGC_284_226,(0,0,2):C.UVGC_284_227,(0,0,0):C.UVGC_284_228})

V_343 = CTVertex(name = 'V_343',
                 type = 'UV',
                 particles = [ P.S3m13, P.S3m13, P.S3m43__star__, P.S3p23__star__ ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.S3m13, P.S3m43, P.W__plus__], [P.g, P.S3m13, P.S3p23, P.W__plus__], [P.g, P.S3m43, P.S3p23, P.W__plus__] ], [ [P.g, P.S3m13, P.W__plus__] ], [ [P.g, P.S3m43, P.W__plus__], [P.g, P.S3p23, P.W__plus__] ], [ [P.g, P.W__plus__] ] ],
                 couplings = {(1,0,3):C.UVGC_253_152,(1,0,1):C.UVGC_284_226,(1,0,2):C.UVGC_284_227,(1,0,0):C.UVGC_284_228,(0,0,3):C.UVGC_253_152,(0,0,1):C.UVGC_284_226,(0,0,2):C.UVGC_284_227,(0,0,0):C.UVGC_284_228})

V_344 = CTVertex(name = 'V_344',
                 type = 'UV',
                 particles = [ P.S3m43__star__, P.S3m43, P.S3p23__star__, P.S3p23 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m43], [P.a, P.g, P.S3p23] ], [ [P.a, P.g, P.S3m43, P.S3p23] ], [ [P.g] ], [ [P.g, P.S3m43], [P.g, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23] ], [ [P.g, P.S3m43, P.S3p23, P.Z] ], [ [P.g, P.S3m43, P.Z], [P.g, P.S3p23, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_286_240,(1,0,0):C.UVGC_290_263,(1,0,4):C.UVGC_286_242,(1,0,8):C.UVGC_290_264,(1,0,1):C.UVGC_290_265,(1,0,5):C.UVGC_286_245,(1,0,7):C.UVGC_290_266,(1,0,2):C.UVGC_288_254,(1,0,6):C.UVGC_290_267,(0,0,3):C.UVGC_285_229,(0,0,0):C.UVGC_282_218,(0,0,4):C.UVGC_285_231,(0,0,8):C.UVGC_289_260,(0,0,1):C.UVGC_282_220,(0,0,5):C.UVGC_285_235,(0,0,7):C.UVGC_289_261,(0,0,2):C.UVGC_280_209,(0,0,6):C.UVGC_289_262})

V_345 = CTVertex(name = 'V_345',
                 type = 'UV',
                 particles = [ P.S3m13__star__, P.S3m13, P.S3m43__star__, P.S3m43 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m13], [P.a, P.g, P.S3m43] ], [ [P.a, P.g, P.S3m13, P.S3m43] ], [ [P.g] ], [ [P.g, P.S3m13], [P.g, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43] ], [ [P.g, P.S3m13, P.S3m43, P.W__plus__] ], [ [P.g, P.S3m13, P.S3m43, P.Z] ], [ [P.g, P.S3m13, P.W__plus__], [P.g, P.S3m43, P.W__plus__] ], [ [P.g, P.S3m13, P.Z], [P.g, P.S3m43, P.Z] ], [ [P.g, P.W__plus__] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_286_240,(1,0,0):C.UVGC_286_241,(1,0,4):C.UVGC_286_242,(1,0,10):C.UVGC_283_224,(1,0,11):C.UVGC_286_243,(1,0,1):C.UVGC_286_244,(1,0,5):C.UVGC_286_245,(1,0,8):C.UVGC_286_246,(1,0,9):C.UVGC_286_247,(1,0,2):C.UVGC_286_248,(1,0,6):C.UVGC_284_228,(1,0,7):C.UVGC_286_249,(0,0,3):C.UVGC_285_229,(0,0,0):C.UVGC_285_230,(0,0,4):C.UVGC_285_231,(0,0,10):C.UVGC_285_232,(0,0,11):C.UVGC_285_233,(0,0,1):C.UVGC_285_234,(0,0,5):C.UVGC_285_235,(0,0,8):C.UVGC_285_236,(0,0,9):C.UVGC_285_237,(0,0,2):C.UVGC_285_238,(0,0,6):C.UVGC_284_226,(0,0,7):C.UVGC_285_239})

V_346 = CTVertex(name = 'V_346',
                 type = 'UV',
                 particles = [ P.S3m43__star__, P.S3m43__star__, P.S3m43, P.S3m43 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.S3m43] ], [ [P.g] ], [ [P.g, P.S3m43] ], [ [P.g, P.S3m43, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_280_208,(1,0,0):C.UVGC_281_214,(1,0,3):C.UVGC_280_210,(1,0,5):C.UVGC_281_215,(1,0,1):C.UVGC_281_216,(1,0,4):C.UVGC_281_217,(0,0,2):C.UVGC_280_208,(0,0,0):C.UVGC_281_214,(0,0,3):C.UVGC_280_210,(0,0,5):C.UVGC_281_215,(0,0,1):C.UVGC_281_216,(0,0,4):C.UVGC_281_217})

