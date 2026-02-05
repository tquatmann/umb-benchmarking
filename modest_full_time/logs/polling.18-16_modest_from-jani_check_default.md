# Log files

Tool configuration: modest_from-jani_check_default
Benchmark: [polling.18-16](../../models/polling.18-16)
Parsed values: [121.016, 145.15, 147.871, 128.374, 121.352]



### Log file: modest_from-jani_check_default_polling.18-16_rep1.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani  -D --exhaustive
Wallclock time: 121.016 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani -D --exhaustive




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
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1709 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               116524 states/s
  Peak memory:        363.74 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 60.8 s
  Time (merging):     3.8 s

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        56.1 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        56.1 s

```



### Log file: modest_from-jani_check_default_polling.18-16_rep2.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani  -D --exhaustive
Wallclock time: 145.150 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani -D --exhaustive




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
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1708 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               108254 states/s
  Peak memory:        363.91 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 65.4 s
  Time (merging):     3.9 s

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        75.6 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        75.5 s

```



### Log file: modest_from-jani_check_default_polling.18-16_rep3.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani  -D --exhaustive
Wallclock time: 147.871 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani -D --exhaustive




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
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1707 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               97611 states/s
  Peak memory:        364.06 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 72.5 s
  Time (merging):     4.7 s

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        70.3 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        70.3 s

```



### Log file: modest_from-jani_check_default_polling.18-16_rep4.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani  -D --exhaustive
Wallclock time: 128.374 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani -D --exhaustive




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
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1708 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               110923 states/s
  Peak memory:        363.85 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 63.8 s
  Time (merging):     4.1 s

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        60.2 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        60.1 s

```



### Log file: modest_from-jani_check_default_polling.18-16_rep5.log

```
Command(s):
../bin/modest mcsta models/polling.18-16/model.jani  -D --exhaustive
Wallclock time: 121.352 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/polling.18-16/model.jani -D --exhaustive




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
model.jani: warning: Encountered a value greater than 1 during value iteration. The final result for property "s1_before_s2" is likely affected by floating-point errors.

Peak memory usage: 1707 MB
Analysis results for model.jani

+ State space exploration
  State size:         24 bytes
  States:             7077888
  Choices:            7077888
  Branches:           69599232
  Rate:               117429 states/s
  Peak memory:        363.73 MB
  Final size:         1116.00 MB
  Size on disk:       223.88 MB
  Time (exploration): 60.3 s
  Time (merging):     3.7 s

+ Property s1_before_s2
  Probability: 0.5389863190184031
  Bounds:      [0.5389863190184031, 1]
  Time:        56.7 s

  + Value iteration
    Final error: 9.911481067918133E-07
    Iterations:  417
    Time:        56.7 s

```

