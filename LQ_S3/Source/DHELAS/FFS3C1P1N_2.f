C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     (ProjM(2,1)) * C(51,2) * C(52,1)
C     
      SUBROUTINE FFS3C1P1N_2(F2, S3, COUP,F1)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(6)
      COMPLEX*16 F2(*)
      COMPLEX*16 S3(*)
      F1(3)= COUP*(-CI )* F2(3)*S3(3)
      F1(4)= COUP*(-CI )* F2(4)*S3(3)
      F1(5)= COUP*0D0
      F1(6)= COUP*0D0
      END


