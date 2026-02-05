# Log files for modest_from-jani_to-aut_default on model [firewire.false-36-800](../../models/firewire.false-36-800)

Parsed values: `[20500183.0, 20500183.0, 20500183.0, 20500183.0, 20500183.0]`



### Log file: modest_from-jani_to-aut_default_firewire.false-36-800_rep1.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model.aut AUT  -D --exhaustive
Wallclock time: 6.922 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/firewire.false-36-800/model.aut".

Peak memory usage: 133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               246823 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 19.55 MB

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.5 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.5 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/firewire.false-36-800/model.aut:	Size of output file is 20500183 bytes
```



### Log file: modest_from-jani_to-aut_default_firewire.false-36-800_rep2.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep2.aut AUT  -D --exhaustive
Wallclock time: 6.537 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep2.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep2.aut".

Peak memory usage: 135 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               257920 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 19.55 MB

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.2 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.2 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep2.aut:	Size of output file is 20500183 bytes
Removing output file to save space for repetition #2
```



### Log file: modest_from-jani_to-aut_default_firewire.false-36-800_rep3.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep3.aut AUT  -D --exhaustive
Wallclock time: 7.328 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep3.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep3.aut".

Peak memory usage: 136 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               240667 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 19.55 MB

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.9 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.9 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep3.aut:	Size of output file is 20500183 bytes
Removing output file to save space for repetition #3
```



### Log file: modest_from-jani_to-aut_default_firewire.false-36-800_rep4.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep4.aut AUT  -D --exhaustive
Wallclock time: 7.355 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep4.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep4.aut".

Peak memory usage: 135 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               248267 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 19.55 MB

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.9 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.9 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep4.aut:	Size of output file is 20500183 bytes
Removing output file to save space for repetition #4
```



### Log file: modest_from-jani_to-aut_default_firewire.false-36-800_rep5.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep5.aut AUT  -D --exhaustive
Wallclock time: 7.475 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani --statespace out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep5.aut AUT -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.
model.jani: info: Exported state space to file "/rwthfs/rz/cluster/hpcwork/rwth1632/umb-benchmarking/experiments-final/out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep5.aut".

Peak memory usage: 134 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               238236 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Export to AUT
  Time:      0.2 s
  File size: 19.55 MB

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        6.0 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        6.0 s


############################## Output files ##############################
out/modest_from-jani_to-aut_default/firewire.false-36-800/model_rep5.aut:	Size of output file is 20500183 bytes
Removing output file to save space for repetition #5
```

