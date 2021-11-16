!
! It is possible to run this card manually with:
!    LD_LIBRARY_PATH=/home/nick/Desktop/LQ_Research/mg_root/HEPTools/lib:$LD_LIBRARY_PATH /home/nick/Desktop/LQ_Research/mg_root/HEPTools/MG5aMC_PY8_interface/MG5aMC_PY8_interface tag_1_pythia8.cmd
!
!
! Pythia8 cmd card automatically generated by MadGraph5_aMC@NLO
! For more information on the use of the MG5aMC / Pythia8 interface, visit
!    https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/LOPY8Merging
!
! ==================
! General parameters 
! ==================
!
Main:numberOfEvents      = -1
!
! -------------------------------------------------------------------
! Specify the HEPMC output of the Pythia8 shower. You can set it to:
!   auto      : MG5aMC will automatically place it the run_<i> directory
!   autoremove: MG5aMC will automatically remove the file at the end of the run.
!                (usefull when running with Delphes)
!   /dev/null : to turn off the HEPMC output.
!   <path>    : to select where the HEPMC file must written. It will 
!               therefore not be placed in the run_<i> directory. The
!               specified path, if not absolute, will be relative to 
!               the Event/run_<i> directory of the process output.
!   fifo      : to have MG5aMC setup the piping of the PY8 output to 
!               analysis tools such as MadAnalysis5.  
!   fifo@<fifo_path> :
!               Same as 'fifo', but selecting a custom path to create the
!               fifo pipe. (useful to select a mounted drive that supports 
!               fifo). Note that the fifo file extension *must* be '.hepmc.fifo'.
! -------------------------------------------------------------------
!
HEPMCoutput:file         = tag_1_pythia8_events.hepmc
!
! --------------------------------------------------------------------
! Parameters relevant only when performing MLM merging, which can be
! turned on by setting ickkw to '1' in the run_card and chosing a 
! positive value for the parameter xqcut.
! For details, see section 'Jet Matching' on the left-hand menu of 
!    http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html
! --------------------------------------------------------------------
! If equal to -1.0, MadGraph5_aMC@NLO will set it automatically based 
! on the parameter 'xqcut' of the run_card.dat 
JetMatching:qCut         = 4.5000000000e+01
! Use default kt-MLM to match parton level jets to those produced by the
! shower. But the other Shower-kt scheme is available too with this option.
JetMatching:doShowerKt   = off
! A value of -1 means that it is automatically guessed by MadGraph.
! It is however always safer to explicitly set it.
JetMatching:nJetMax      = 1
!
! --------------------------------------------------------------------
! Parameters relevant only when performing CKKW-L merging, which can
! be turned on by setting the parameter 'ptlund' *or* 'ktdurham' to
! a positive value. 
! For details, see section 'CKKW-L Merging' on the left-hand menu of 
!    http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html
! --------------------------------------------------------------------
! Central merging scale values you want to be used.
! If equal to -1.0, then MadGraph5_aMC@NLO will set this automatically
! based on the parameter 'ktdurham' of the run_card.dat
! The following parameter was forced to be commented out by MG5aMC.
! Merging:TMS              = -1.0
! This must be set manually, according to Pythia8 directives.
! An example of possible value is 'pp>LEPTONS,NEUTRINOS'
! Alternatively, from Pythia v8.223 onwards, the value 'guess' can be 
! used to instruct Pythia to guess the hard process. The guess would mean 
! that all particles apart from light partons will be considered as a part 
! of the hard process. This guess is prone to errors if the desired hard 
! process is complicated (i.e. contains light partons). The user should
! then be wary of suspicious error messages in the Pythia log file. 
! The following parameter was forced to be commented out by MG5aMC.
! Merging:Process          = <set_by_user>
! A value of -1 means that it is automatically guessed by MadGraph.
! It is however always safer to explicitly set it.
! The following parameter was forced to be commented out by MG5aMC.
! Merging:nJetMax  		 = -1
!
! For all merging schemes, decide whehter you want the merging scale
! variation computed for only the central weights or all other 
! PDF and scale variation weights as well
SysCalc:fullCutVariation = off
!
! ==========================
! User customized parameters 
! ==========================
!
! By default, Pythia8 generates multi-parton interaction events. This is
! often irrelevant for phenomenology and very slow. You can turn this 
! feature off by uncommenting the line below if so desired.
!partonlevel:mpi = off
!
! Additional technical parameters set by MG5_aMC.
!
! Tell Pythia8 that an LHEF input is used.
Beams:frameType=4
! This parameter is automatically set to True by MG5aMC when doing MLM merging with PY8.
Beams:setProductionScalesFromLHEF=on
! 1.0 corresponds to HEPMC weight given in [mb]. We choose here the [pb] normalization.
HEPMCoutput:scaling=1.0000000000e+09
! Be more forgiving with momentum mismatches.
Check:epTolErr=1.0000000000e-02
JetMatching:etaJetMax=1.0000000000e+03
! Specifiy if we are merging sample of different multiplicity.
JetMatching:merge=on
! Do veto externally (e.g. in SysCalc).
JetMatching:doVeto=off
JetMatching:scheme=1
! Specify one must read inputs from the MadGraph banner.
JetMatching:setMad=off
JetMatching:coneRadius=1.0000000000e+00
JetMatching:nQmatch=5
SysCalc:qCutList=67.500,90.000
! Value of the merging scale below which one does not even write the HepMC event.
SysCalc:qWeed=3.0000000000e+01
! 
!     ====================
!     Subrun definitions
!     ====================
!     
LHEFInputs:nSubruns=1
Main:subrun=0
!
!  Definition of subrun 0
!
Beams:LHEF=unweighted_events.lhe.gz
