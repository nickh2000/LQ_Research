# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (October 5, 2011)
# Date: Sun 3 Dec 2017 09:36:59


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.S3m13,P.ve__tilde__):'((MB**2 - MS3**2)*(3*MB**2*yLL3x1**2 - 3*MS3**2*yLL3x1**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3m13,P.vm__tilde__):'((MB**2 - MS3**2)*(3*MB**2*yLL3x2**2 - 3*MS3**2*yLL3x2**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3m13,P.vt__tilde__):'((MB**2 - MS3**2)*(3*MB**2*yLL3x3**2 - 3*MS3**2*yLL3x3**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3m43,P.e__plus__):'((MB**2 - MS3**2)*(6*MB**2*yLL3x1**2 - 6*MS3**2*yLL3x1**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3m43,P.mu__plus__):'((MB**2 - MS3**2)*(6*MB**2*yLL3x2**2 - 6*MS3**2*yLL3x2**2))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.S3m43,P.ta__plus__):'((6*MB**2*yLL3x3**2 - 6*MS3**2*yLL3x3**2 + 6*MTA**2*yLL3x3**2)*cmath.sqrt(MB**4 - 2*MB**2*MS3**2 + MS3**4 - 2*MB**2*MTA**2 - 2*MS3**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_S3m13 = Decay(name = 'Decay_S3m13',
                    particle = P.S3m13,
                    partial_widths = {(P.b,P.ve):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x1**2 + 3*MS3**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.vm):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x2**2 + 3*MS3**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.vt):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x3**2 + 3*MS3**2*yLL3x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.e__minus__):'(MS3**4*yLL2x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.mu__minus__):'(MS3**4*yLL2x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.ta__minus__):'((MS3**2 - MTA**2)*(3*MS3**2*yLL2x3**2 - 3*MTA**2*yLL2x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.ve):'(MS3**4*yLL1x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.vm):'(MS3**4*yLL1x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.vt):'(MS3**4*yLL1x3**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.t):'((MS3**2 - MT**2)*(3*MS3**2*yLL3x1**2 - 3*MT**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.u):'(MS3**4*yLL1x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.t):'((MS3**2 - MT**2)*(3*MS3**2*yLL3x2**2 - 3*MT**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.u):'(MS3**4*yLL1x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.ve):'(MS3**4*yLL2x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.vm):'(MS3**4*yLL2x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.vt):'(MS3**4*yLL2x3**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.ta__minus__):'((3*MS3**2*yLL3x3**2 - 3*MT**2*yLL3x3**2 - 3*MTA**2*yLL3x3**2)*cmath.sqrt(MS3**4 - 2*MS3**2*MT**2 + MT**4 - 2*MS3**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.ta__minus__,P.u):'((MS3**2 - MTA**2)*(3*MS3**2*yLL1x3**2 - 3*MTA**2*yLL1x3**2))/(48.*cmath.pi*abs(MS3)**3)'})

Decay_S3m43 = Decay(name = 'Decay_S3m43',
                    particle = P.S3m43,
                    partial_widths = {(P.b,P.e__minus__):'((-MB**2 + MS3**2)*(-6*MB**2*yLL3x1**2 + 6*MS3**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.mu__minus__):'((-MB**2 + MS3**2)*(-6*MB**2*yLL3x2**2 + 6*MS3**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.ta__minus__):'((-6*MB**2*yLL3x3**2 + 6*MS3**2*yLL3x3**2 - 6*MTA**2*yLL3x3**2)*cmath.sqrt(MB**4 - 2*MB**2*MS3**2 + MS3**4 - 2*MB**2*MTA**2 - 2*MS3**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.e__minus__):'(MS3**4*yLL1x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.mu__minus__):'(MS3**4*yLL1x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.ta__minus__):'((MS3**2 - MTA**2)*(6*MS3**2*yLL1x3**2 - 6*MTA**2*yLL1x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.s):'(MS3**4*yLL2x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.s):'(MS3**4*yLL2x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.ta__minus__):'((MS3**2 - MTA**2)*(6*MS3**2*yLL2x3**2 - 6*MTA**2*yLL2x3**2))/(48.*cmath.pi*abs(MS3)**3)'})

Decay_S3p23 = Decay(name = 'Decay_S3p23',
                    particle = P.S3p23,
                    partial_widths = {(P.c,P.ve):'(MS3**4*yLL2x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.vm):'(MS3**4*yLL2x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.vt):'(MS3**4*yLL2x3**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.ve):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x1**2 - 6*MT**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.vm):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x2**2 - 6*MT**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.vt):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x3**2 - 6*MT**2*yLL3x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.ve):'(MS3**4*yLL1x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.vm):'(MS3**4*yLL1x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.vt):'(MS3**4*yLL1x3**2)/(8.*cmath.pi*abs(MS3)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.S3m13,P.e__plus__):'((-MS3**2 + MT**2)*(-3*MS3**2*yLL3x1**2 + 3*MT**2*yLL3x1**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3m13,P.mu__plus__):'((-MS3**2 + MT**2)*(-3*MS3**2*yLL3x2**2 + 3*MT**2*yLL3x2**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3m13,P.ta__plus__):'((-3*MS3**2*yLL3x3**2 + 3*MT**2*yLL3x3**2 + 3*MTA**2*yLL3x3**2)*cmath.sqrt(MS3**4 - 2*MS3**2*MT**2 + MT**4 - 2*MS3**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3p23,P.ve__tilde__):'((-MS3**2 + MT**2)*(-6*MS3**2*yLL3x1**2 + 6*MT**2*yLL3x1**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3p23,P.vm__tilde__):'((-MS3**2 + MT**2)*(-6*MS3**2*yLL3x2**2 + 6*MT**2*yLL3x2**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.S3p23,P.vt__tilde__):'((-MS3**2 + MT**2)*(-6*MS3**2*yLL3x3**2 + 6*MT**2*yLL3x3**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.S3m13,P.c__tilde__):'((-MS3**2 + MTA**2)*(-3*MS3**2*yLL2x3**2 + 3*MTA**2*yLL2x3**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S3m13,P.t__tilde__):'((-3*MS3**2*yLL3x3**2 + 3*MT**2*yLL3x3**2 + 3*MTA**2*yLL3x3**2)*cmath.sqrt(MS3**4 - 2*MS3**2*MT**2 + MT**4 - 2*MS3**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S3m13,P.u__tilde__):'((-MS3**2 + MTA**2)*(-3*MS3**2*yLL1x3**2 + 3*MTA**2*yLL1x3**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S3m43,P.b__tilde__):'((6*MB**2*yLL3x3**2 - 6*MS3**2*yLL3x3**2 + 6*MTA**2*yLL3x3**2)*cmath.sqrt(MB**4 - 2*MB**2*MS3**2 + MS3**4 - 2*MB**2*MTA**2 - 2*MS3**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S3m43,P.d__tilde__):'((-MS3**2 + MTA**2)*(-6*MS3**2*yLL1x3**2 + 6*MTA**2*yLL1x3**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.S3m43,P.s__tilde__):'((-MS3**2 + MTA**2)*(-6*MS3**2*yLL2x3**2 + 6*MTA**2*yLL2x3**2))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.S3m13,P.S3m43__star__):'(((-12*ee**2*MS3**2)/sw**2 + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(-4*MS3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.S3m13__star__,P.S3p23):'(((-12*ee**2*MS3**2)/sw**2 + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(-4*MS3**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3m13__star__,P.S3m13):'(((-4*ee**2*MS3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MS3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3m43__star__,P.S3m43):'((8*ee**2*MS3**2 - 2*ee**2*MZ**2 - (12*cw**2*ee**2*MS3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 - (4*ee**2*MS3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MS3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.S3p23__star__,P.S3p23):'((-8*ee**2*MS3**2 + 2*ee**2*MZ**2 - (12*cw**2*ee**2*MS3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 - (4*ee**2*MS3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MS3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

