
C     PY ((21, 13), (-1, 1, 13)) : (21, 13, 13, 1, -1) # M0_ 1
C     PY ((21, 13), (-1, 3, 13)) : (21, 13, 13, 3, -1) # M1_ 1
C     PY ((21, 13), (-3, 1, 13)) : (21, 13, 13, 1, -3) # M2_ 1
C     PY ((21, 13), (-3, 3, 13)) : (21, 13, 13, 3, -3) # M3_ 1
C     PY ((1, 13), (1, 13, 21)) : (1, 13, 13, 1, 21) # M4_ 1
C     PY ((1, 13), (3, 13, 21)) : (1, 13, 13, 3, 21) # M5_ 1
C     PY ((3, 13), (1, 13, 21)) : (3, 13, 13, 1, 21) # M6_ 1
C     PY ((3, 13), (3, 13, 21)) : (3, 13, 13, 3, 21) # M7_ 1
      SUBROUTINE SMATRIXHEL(PDGS, PROCID, NPDG, P, ALPHAS, SCALE2,
     $  NHEL, ANS)
      IMPLICIT NONE
C     ALPHAS is given at scale2 (SHOULD be different of 0 for loop
C      induced, ignore for LO)  

CF2PY double precision, intent(in), dimension(0:3,npdg) :: p
CF2PY integer, intent(in), dimension(npdg) :: pdgs
CF2PY integer, intent(in):: procid
CF2PY integer, intent(in) :: npdg
CF2PY double precision, intent(out) :: ANS
CF2PY double precision, intent(in) :: ALPHAS
CF2PY double precision, intent(in) :: SCALE2
      INTEGER PDGS(*)
      INTEGER NPDG, NHEL, PROCID
      DOUBLE PRECISION P(*)
      DOUBLE PRECISION ANS, ALPHAS, PI,SCALE2
      INCLUDE 'coupl.inc'

      PI = 3.141592653589793D0
      G = 2* DSQRT(ALPHAS*PI)
      CALL UPDATE_AS_PARAM()
C     if (scale2.ne.0d0) stop 1

      IF(21.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.1.EQ.PDGS(4).AND.-1.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 0
        CALL M0_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(21.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.3.EQ.PDGS(4).AND.-1.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 1
        CALL M1_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(21.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.1.EQ.PDGS(4).AND.-3.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 2
        CALL M2_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(21.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.3.EQ.PDGS(4).AND.-3.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 3
        CALL M3_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(1.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.1.EQ.PDGS(4).AND.21.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 4
        CALL M4_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(1.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.3.EQ.PDGS(4).AND.21.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 5
        CALL M5_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(3.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.1.EQ.PDGS(4).AND.21.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 6
        CALL M6_SMATRIXHEL(P, NHEL, ANS)
      ELSE IF(3.EQ.PDGS(1).AND.13.EQ.PDGS(2).AND.13.EQ.PDGS(3)
     $ .AND.3.EQ.PDGS(4).AND.21.EQ.PDGS(5)
     $ .AND.(PROCID.LE.0.OR.PROCID.EQ.1)) THEN  ! 7
        CALL M7_SMATRIXHEL(P, NHEL, ANS)
      ENDIF

      RETURN
      END

      SUBROUTINE INITIALISE(PATH)
C     ROUTINE FOR F2PY to read the benchmark point.
      IMPLICIT NONE
      CHARACTER*512 PATH
CF2PY INTENT(IN) :: PATH
      CALL SETPARA(PATH)  !first call to setup the paramaters
      RETURN
      END


      SUBROUTINE CHANGE_PARA(NAME, VALUE)
      IMPLICIT NONE
CF2PY intent(in) :: name
CF2PY intent(in) :: value

      CHARACTER*512 NAME
      DOUBLE PRECISION VALUE

      LOGICAL M0_HELRESET
      COMMON /M0_HELRESET/ M0_HELRESET
      LOGICAL M7_HELRESET
      COMMON /M7_HELRESET/ M7_HELRESET
      LOGICAL M6_HELRESET
      COMMON /M6_HELRESET/ M6_HELRESET
      LOGICAL M2_HELRESET
      COMMON /M2_HELRESET/ M2_HELRESET
      LOGICAL M4_HELRESET
      COMMON /M4_HELRESET/ M4_HELRESET
      LOGICAL M5_HELRESET
      COMMON /M5_HELRESET/ M5_HELRESET
      LOGICAL M3_HELRESET
      COMMON /M3_HELRESET/ M3_HELRESET
      LOGICAL M1_HELRESET
      COMMON /M1_HELRESET/ M1_HELRESET

      INCLUDE '../Source/MODEL/input.inc'
      INCLUDE '../Source/MODEL/coupl.inc'

      M0_HELRESET = .TRUE.
      M7_HELRESET = .TRUE.
      M6_HELRESET = .TRUE.
      M2_HELRESET = .TRUE.
      M4_HELRESET = .TRUE.
      M5_HELRESET = .TRUE.
      M3_HELRESET = .TRUE.
      M1_HELRESET = .TRUE.

      SELECT CASE (NAME)
      CASE ('MU_R')
      MU_R = VALUE
      CASE ('LOOP_1')
      MU_R = VALUE
      CASE ('MB')
      MDL_MB = VALUE
      CASE ('MASS_5')
      MDL_MB = VALUE
      CASE ('MT')
      MDL_MT = VALUE
      CASE ('MASS_6')
      MDL_MT = VALUE
      CASE ('MTA')
      MDL_MTA = VALUE
      CASE ('MASS_15')
      MDL_MTA = VALUE
      CASE ('MZ')
      MDL_MZ = VALUE
      CASE ('MASS_23')
      MDL_MZ = VALUE
      CASE ('MH')
      MDL_MH = VALUE
      CASE ('MASS_25')
      MDL_MH = VALUE
      CASE ('MS1t')
      MDL_MS1T = VALUE
      CASE ('MASS_9000005')
      MDL_MS1T = VALUE
      CASE ('aEWM1')
      AEWM1 = VALUE
      CASE ('SMINPUTS_1')
      AEWM1 = VALUE
      CASE ('Gf')
      MDL_GF = VALUE
      CASE ('SMINPUTS_2')
      MDL_GF = VALUE
      CASE ('aS')
      AS = VALUE
      CASE ('SMINPUTS_3')
      AS = VALUE
      CASE ('ymb')
      MDL_YMB = VALUE
      CASE ('YUKAWA_5')
      MDL_YMB = VALUE
      CASE ('ymt')
      MDL_YMT = VALUE
      CASE ('YUKAWA_6')
      MDL_YMT = VALUE
      CASE ('ymtau')
      MDL_YMTAU = VALUE
      CASE ('YUKAWA_15')
      MDL_YMTAU = VALUE
      CASE ('yRR1x1')
      MDL_YRR1X1 = VALUE
      CASE ('YUKS1TRR_1_1')
      MDL_YRR1X1 = VALUE
      CASE ('yRR1x2')
      MDL_YRR1X2 = VALUE
      CASE ('YUKS1TRR_1_2')
      MDL_YRR1X2 = VALUE
      CASE ('yRR1x3')
      MDL_YRR1X3 = VALUE
      CASE ('YUKS1TRR_1_3')
      MDL_YRR1X3 = VALUE
      CASE ('yRR2x1')
      MDL_YRR2X1 = VALUE
      CASE ('YUKS1TRR_2_1')
      MDL_YRR2X1 = VALUE
      CASE ('yRR2x2')
      MDL_YRR2X2 = VALUE
      CASE ('YUKS1TRR_2_2')
      MDL_YRR2X2 = VALUE
      CASE ('yRR2x3')
      MDL_YRR2X3 = VALUE
      CASE ('YUKS1TRR_2_3')
      MDL_YRR2X3 = VALUE
      CASE ('yRR3x1')
      MDL_YRR3X1 = VALUE
      CASE ('YUKS1TRR_3_1')
      MDL_YRR3X1 = VALUE
      CASE ('yRR3x2')
      MDL_YRR3X2 = VALUE
      CASE ('YUKS1TRR_3_2')
      MDL_YRR3X2 = VALUE
      CASE ('yRR3x3')
      MDL_YRR3X3 = VALUE
      CASE ('YUKS1TRR_3_3')
      MDL_YRR3X3 = VALUE
      CASE ('WT')
      MDL_WT = VALUE
      CASE ('DECAY_6')
      MDL_WT = VALUE
      CASE ('WZ')
      MDL_WZ = VALUE
      CASE ('DECAY_23')
      MDL_WZ = VALUE
      CASE ('WW')
      MDL_WW = VALUE
      CASE ('DECAY_24')
      MDL_WW = VALUE
      CASE ('WH')
      MDL_WH = VALUE
      CASE ('DECAY_25')
      MDL_WH = VALUE
      CASE ('WS1t')
      MDL_WS1T = VALUE
      CASE ('DECAY_9000005')
      MDL_WS1T = VALUE
      CASE DEFAULT
      WRITE(*,*) 'no parameter matching', NAME, VALUE
      END SELECT

      RETURN
      END

      SUBROUTINE UPDATE_ALL_COUP()
      IMPLICIT NONE
      CALL COUP()
      RETURN
      END


      SUBROUTINE GET_PDG_ORDER(PDG, ALLPROC)
      IMPLICIT NONE
CF2PY INTEGER, intent(out) :: PDG(8,5)
CF2PY INTEGER, intent(out) :: ALLPROC(8)
      INTEGER PDG(8,5), PDGS(8,5)
      INTEGER ALLPROC(8),PIDS(8)
      DATA PDGS/ 21,21,21,21,1,1,3,3,13,13,13,13,13,13,13,13,13,13,13
     $ ,13,13,13,13,13,1,3,1,3,1,3,1,3,-1,-1,-3,-3,21,21,21,21 /
      DATA PIDS/ 1,1,1,1,1,1,1,1 /
      PDG = PDGS
      ALLPROC = PIDS
      RETURN
      END

      SUBROUTINE GET_PREFIX(PREFIX)
      IMPLICIT NONE
CF2PY CHARACTER*20, intent(out) :: PREFIX(8)
      CHARACTER*20 PREFIX(8),PREF(8)
      DATA PREF / 'M0_','M1_','M2_','M3_','M4_','M5_','M6_','M7_'/
      PREFIX = PREF
      RETURN
      END



