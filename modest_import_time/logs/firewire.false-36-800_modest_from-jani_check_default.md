# Log files

Tool configuration: modest_from-jani_check_default
Benchmark: [firewire.false-36-800](../../models/firewire.false-36-800)
Parsed values: [0.9, 0.7999999999999999, 1.0, 0.8, 1.0]



### Log file: modest_from-jani_check_default_firewire.false-36-800_rep1.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani  -D --exhaustive
Wallclock time: 6.077 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.

Peak memory usage: 133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               264015 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.8 s
  Time (merging):     0.1 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.0 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.0 s

```



### Log file: modest_from-jani_check_default_firewire.false-36-800_rep2.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani  -D --exhaustive
Wallclock time: 6.798 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.

Peak memory usage: 134 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               312619 states/s
  Peak memory:        81.92 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.7 s
  Time (merging):     0.1 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.6 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.5 s

```



### Log file: modest_from-jani_check_default_firewire.false-36-800_rep3.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani  -D --exhaustive
Wallclock time: 7.665 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.

Peak memory usage: 135 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               256362 states/s
  Peak memory:        81.92 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        6.2 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        6.2 s

```



### Log file: modest_from-jani_check_default_firewire.false-36-800_rep4.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani  -D --exhaustive
Wallclock time: 6.043 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.

Peak memory usage: 133 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               286462 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.8 s
  Time (merging):     0.0 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        5.0 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        5.0 s

```



### Log file: modest_from-jani_check_default_firewire.false-36-800_rep5.log

```
Command(s):
../bin/modest mcsta models/firewire.false-36-800/model.jani  -D --exhaustive
Wallclock time: 7.417 seconds
Return code: 0
##############################
The Modest Toolset (www.modestchecker.net), version v3.1.309-gc50f44578+35483c89e7bc88e02bb68bd8068d28d0682448b1.
Command: modest mcsta models/firewire.false-36-800/model.jani -D --exhaustive




model.jani:model: info: model is an MDP model.
model.jani:automata[0].variables[0]: info: Expanding variable "w12" into 10 locations in automaton "wire12".
model.jani:variables[2]: info: Expanding variable "s1" into 9 locations in automaton "node1".
model.jani:automata[2].variables[0]: info: Expanding variable "w21" into 10 locations in automaton "wire21".
model.jani:variables[3]: info: Expanding variable "s2" into 9 locations in automaton "node2".
model.jani: info: Need 16 bytes per state.
model.jani: info: Explored 212268 states.

Peak memory usage: 134 MB
Analysis results for model.jani

+ State space exploration
  State size:         16 bytes
  States:             212268
  Choices:            478756
  Branches:           481792
  Rate:               244267 states/s
  Peak memory:        81.96 MB
  Final size:         14.68 MB
  Size on disk:       1.68 MB
  Time (exploration): 0.9 s
  Time (merging):     0.1 s

+ Property deadline
  Probability: 0.939453125
  Bounds:      [0.939453125, 1]
  CDF:         { (0, 0), ..., (202, 0), (203, 0.5), ..., (323, 0.5), (324, 0.625), ..., (405, 0.625), (406, 0.75), ..., (444, 0.75), (445, 0.78125), ..., (526, 0.78125), (527, 0.84375), ..., (565, 0.84375), (566, 0.8515625), ..., (608, 0.8515625), (609, 0.8828125), ..., (647, 0.8828125), (648, 0.90625), ..., (686, 0.90625), (687, 0.908203125), ..., (729, 0.908203125), (730, 0.931640625), ..., (768, 0.931640625), (769, 0.939453125), ..., (800, 0.939453125) }
  Time:        6.2 s

  + Value iteration
    Final error: 0
    Iterations:  2374
    Time:        6.2 s

```

