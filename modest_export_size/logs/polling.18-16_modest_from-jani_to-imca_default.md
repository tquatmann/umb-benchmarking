# Log files for modest_from-jani_to-imca_default on model [polling.18-16](../../models/polling.18-16)

Parsed values: `[2008492573.0, 2008492573.0, 2008492573.0, 2008492573.0, 2008492573.0]`



### Log file: modest_from-jani_to-imca_default_polling.18-16_rep1.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model.mrm IMCA  -D --exhaustive
Wallclock time: 149.033 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[3]: info: Expanding variable "a" into 2 locations in automaton "server".
model.jani:automata[1].variables[0]: info: Expanding variable "s1" into 2 locations in automaton "station1".
model.jani:automata[2].variables[0]: info: Expanding variable "s2" into 2 locations in automaton "station2".
model.jani:automata[3].variables[0]: info: Expanding variable "s3" into 2 locations in automaton "station3".
model.jani:automata[4].variables[0]: info: Expanding variable "s4" into 2 locations in automaton "station4".
model.jani:automata[5].variables[0]: info: Expanding variable "s5" into 2 locations in automaton "station5".
model.jani:automata[6].variables[0]: info: Expanding variable "s6" into 2 locations in automaton "station6".
model.jani:automata[7].variables[0]: info: Expanding variable "s7" into 2 locations in automaton "station7".
model.jani:automata[8].variables[0]: info: Expanding variable "s8" into 2 locations in automaton "station8".
model.jani:automata[9].variables[0]: info: Expanding variable "s9" into 2 locations in automaton "station9".
model.jani:automata[10].variables[0]: info: Expanding variable "s10" into 2 locations in automaton "station10".
model.jani:automata[11].variables[0]: info: Expanding variable "s11" into 2 locations in automaton "station11".
model.jani:automata[12].variables[0]: info: Expanding variable "s12" into 2 locations in automaton "station12".
model.jani:automata[13].variables[0]: info: Expanding variable "s13" into 2 locations in automaton "station13".
model.jani:automata[14].variables[0]: info: Expanding variable "s14" into 2 locations in automaton "station14".
model.jani:automata[15].variables[0]: info: Expanding variable "s15" into 2 locations in automaton "station15".
model.jani:automata[16].variables[0]: info: Expanding variable "s16" into 2 locations in automaton "station16".
model.jani:automata[17].variables[0]: info: Expanding variable "s17" into 2 locations in automaton "station17".
model.jani:automata[18].variables[0]: info: Expanding variable "s18" into 2 locations in automaton "station18".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 7077888 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/polling.18-16/model.mrm".
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1707 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               109015 states/s
  Peak memory:        363.90 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 64.9 s
  Time (merging):     4.3 s

+ Export to IMCA
  Time:      16.3 s
  File size: 1915.45 MB

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        62.7 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        62.7 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/polling.18-16/model.mrm:	Size of output file is 2008492573 bytes
```



### Log file: modest_from-jani_to-imca_default_polling.18-16_rep2.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep2.mrm IMCA  -D --exhaustive
Wallclock time: 152.099 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep2.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[3]: info: Expanding variable "a" into 2 locations in automaton "server".
model.jani:automata[1].variables[0]: info: Expanding variable "s1" into 2 locations in automaton "station1".
model.jani:automata[2].variables[0]: info: Expanding variable "s2" into 2 locations in automaton "station2".
model.jani:automata[3].variables[0]: info: Expanding variable "s3" into 2 locations in automaton "station3".
model.jani:automata[4].variables[0]: info: Expanding variable "s4" into 2 locations in automaton "station4".
model.jani:automata[5].variables[0]: info: Expanding variable "s5" into 2 locations in automaton "station5".
model.jani:automata[6].variables[0]: info: Expanding variable "s6" into 2 locations in automaton "station6".
model.jani:automata[7].variables[0]: info: Expanding variable "s7" into 2 locations in automaton "station7".
model.jani:automata[8].variables[0]: info: Expanding variable "s8" into 2 locations in automaton "station8".
model.jani:automata[9].variables[0]: info: Expanding variable "s9" into 2 locations in automaton "station9".
model.jani:automata[10].variables[0]: info: Expanding variable "s10" into 2 locations in automaton "station10".
model.jani:automata[11].variables[0]: info: Expanding variable "s11" into 2 locations in automaton "station11".
model.jani:automata[12].variables[0]: info: Expanding variable "s12" into 2 locations in automaton "station12".
model.jani:automata[13].variables[0]: info: Expanding variable "s13" into 2 locations in automaton "station13".
model.jani:automata[14].variables[0]: info: Expanding variable "s14" into 2 locations in automaton "station14".
model.jani:automata[15].variables[0]: info: Expanding variable "s15" into 2 locations in automaton "station15".
model.jani:automata[16].variables[0]: info: Expanding variable "s16" into 2 locations in automaton "station16".
model.jani:automata[17].variables[0]: info: Expanding variable "s17" into 2 locations in automaton "station17".
model.jani:automata[18].variables[0]: info: Expanding variable "s18" into 2 locations in automaton "station18".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 7077888 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/polling.18-16/model_rep2.mrm".
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1707 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               104090 states/s
  Peak memory:        364.00 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 68.0 s
  Time (merging):     4.5 s

+ Export to IMCA
  Time:      16.0 s
  File size: 1915.45 MB

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        63.1 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        63.1 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/polling.18-16/model_rep2.mrm:	Size of output file is 2008492573 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-imca_default_polling.18-16_rep3.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep3.mrm IMCA  -D --exhaustive
Wallclock time: 136.833 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep3.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[3]: info: Expanding variable "a" into 2 locations in automaton "server".
model.jani:automata[1].variables[0]: info: Expanding variable "s1" into 2 locations in automaton "station1".
model.jani:automata[2].variables[0]: info: Expanding variable "s2" into 2 locations in automaton "station2".
model.jani:automata[3].variables[0]: info: Expanding variable "s3" into 2 locations in automaton "station3".
model.jani:automata[4].variables[0]: info: Expanding variable "s4" into 2 locations in automaton "station4".
model.jani:automata[5].variables[0]: info: Expanding variable "s5" into 2 locations in automaton "station5".
model.jani:automata[6].variables[0]: info: Expanding variable "s6" into 2 locations in automaton "station6".
model.jani:automata[7].variables[0]: info: Expanding variable "s7" into 2 locations in automaton "station7".
model.jani:automata[8].variables[0]: info: Expanding variable "s8" into 2 locations in automaton "station8".
model.jani:automata[9].variables[0]: info: Expanding variable "s9" into 2 locations in automaton "station9".
model.jani:automata[10].variables[0]: info: Expanding variable "s10" into 2 locations in automaton "station10".
model.jani:automata[11].variables[0]: info: Expanding variable "s11" into 2 locations in automaton "station11".
model.jani:automata[12].variables[0]: info: Expanding variable "s12" into 2 locations in automaton "station12".
model.jani:automata[13].variables[0]: info: Expanding variable "s13" into 2 locations in automaton "station13".
model.jani:automata[14].variables[0]: info: Expanding variable "s14" into 2 locations in automaton "station14".
model.jani:automata[15].variables[0]: info: Expanding variable "s15" into 2 locations in automaton "station15".
model.jani:automata[16].variables[0]: info: Expanding variable "s16" into 2 locations in automaton "station16".
model.jani:automata[17].variables[0]: info: Expanding variable "s17" into 2 locations in automaton "station17".
model.jani:automata[18].variables[0]: info: Expanding variable "s18" into 2 locations in automaton "station18".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 7077888 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/polling.18-16/model_rep3.mrm".
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1710 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               115612 states/s
  Peak memory:        363.77 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 61.2 s
  Time (merging):     3.8 s

+ Export to IMCA
  Time:      14.4 s
  File size: 1915.45 MB

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        57.1 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        57.0 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/polling.18-16/model_rep3.mrm:	Size of output file is 2008492573 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-imca_default_polling.18-16_rep4.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep4.mrm IMCA  -D --exhaustive
Wallclock time: 172.918 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep4.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[3]: info: Expanding variable "a" into 2 locations in automaton "server".
model.jani:automata[1].variables[0]: info: Expanding variable "s1" into 2 locations in automaton "station1".
model.jani:automata[2].variables[0]: info: Expanding variable "s2" into 2 locations in automaton "station2".
model.jani:automata[3].variables[0]: info: Expanding variable "s3" into 2 locations in automaton "station3".
model.jani:automata[4].variables[0]: info: Expanding variable "s4" into 2 locations in automaton "station4".
model.jani:automata[5].variables[0]: info: Expanding variable "s5" into 2 locations in automaton "station5".
model.jani:automata[6].variables[0]: info: Expanding variable "s6" into 2 locations in automaton "station6".
model.jani:automata[7].variables[0]: info: Expanding variable "s7" into 2 locations in automaton "station7".
model.jani:automata[8].variables[0]: info: Expanding variable "s8" into 2 locations in automaton "station8".
model.jani:automata[9].variables[0]: info: Expanding variable "s9" into 2 locations in automaton "station9".
model.jani:automata[10].variables[0]: info: Expanding variable "s10" into 2 locations in automaton "station10".
model.jani:automata[11].variables[0]: info: Expanding variable "s11" into 2 locations in automaton "station11".
model.jani:automata[12].variables[0]: info: Expanding variable "s12" into 2 locations in automaton "station12".
model.jani:automata[13].variables[0]: info: Expanding variable "s13" into 2 locations in automaton "station13".
model.jani:automata[14].variables[0]: info: Expanding variable "s14" into 2 locations in automaton "station14".
model.jani:automata[15].variables[0]: info: Expanding variable "s15" into 2 locations in automaton "station15".
model.jani:automata[16].variables[0]: info: Expanding variable "s16" into 2 locations in automaton "station16".
model.jani:automata[17].variables[0]: info: Expanding variable "s17" into 2 locations in automaton "station17".
model.jani:automata[18].variables[0]: info: Expanding variable "s18" into 2 locations in automaton "station18".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 7077888 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/polling.18-16/model_rep4.mrm".
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1708 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               97424 states/s
  Peak memory:        364.07 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 72.7 s
  Time (merging):     4.6 s

+ Export to IMCA
  Time:      16.7 s
  File size: 1915.45 MB

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        78.6 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        78.6 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/polling.18-16/model_rep4.mrm:	Size of output file is 2008492573 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-imca_default_polling.18-16_rep5.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep5.mrm IMCA  -D --exhaustive
Wallclock time: 134.745 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani --statespace out/modest_from-jani_to-imca_default/polling.18-16/model_rep5.mrm IMCA -D --exhaustive




model.jani:model: info: model is a CTMC model.
model.jani:variables[3]: info: Expanding variable "a" into 2 locations in automaton "server".
model.jani:automata[1].variables[0]: info: Expanding variable "s1" into 2 locations in automaton "station1".
model.jani:automata[2].variables[0]: info: Expanding variable "s2" into 2 locations in automaton "station2".
model.jani:automata[3].variables[0]: info: Expanding variable "s3" into 2 locations in automaton "station3".
model.jani:automata[4].variables[0]: info: Expanding variable "s4" into 2 locations in automaton "station4".
model.jani:automata[5].variables[0]: info: Expanding variable "s5" into 2 locations in automaton "station5".
model.jani:automata[6].variables[0]: info: Expanding variable "s6" into 2 locations in automaton "station6".
model.jani:automata[7].variables[0]: info: Expanding variable "s7" into 2 locations in automaton "station7".
model.jani:automata[8].variables[0]: info: Expanding variable "s8" into 2 locations in automaton "station8".
model.jani:automata[9].variables[0]: info: Expanding variable "s9" into 2 locations in automaton "station9".
model.jani:automata[10].variables[0]: info: Expanding variable "s10" into 2 locations in automaton "station10".
model.jani:automata[11].variables[0]: info: Expanding variable "s11" into 2 locations in automaton "station11".
model.jani:automata[12].variables[0]: info: Expanding variable "s12" into 2 locations in automaton "station12".
model.jani:automata[13].variables[0]: info: Expanding variable "s13" into 2 locations in automaton "station13".
model.jani:automata[14].variables[0]: info: Expanding variable "s14" into 2 locations in automaton "station14".
model.jani:automata[15].variables[0]: info: Expanding variable "s15" into 2 locations in automaton "station15".
model.jani:automata[16].variables[0]: info: Expanding variable "s16" into 2 locations in automaton "station16".
model.jani:automata[17].variables[0]: info: Expanding variable "s17" into 2 locations in automaton "station17".
model.jani:automata[18].variables[0]: info: Expanding variable "s18" into 2 locations in automaton "station18".
model.jani: info: Need 24 bytes per state.
model.jani: info: Explored 7077888 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-imca_default/polling.18-16/model_rep5.mrm".
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1710 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               117007 states/s
  Peak memory:        363.74 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 60.5 s
  Time (merging):     3.8 s

+ Export to IMCA
  Time:      13.3 s
  File size: 1915.45 MB

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        56.8 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        56.8 s


############################## Output files ##############################
out/modest_from-jani_to-imca_default/polling.18-16/model_rep5.mrm:	Size of output file is 2008492573 bytes
Removing output file to save space for repetition #5
```

