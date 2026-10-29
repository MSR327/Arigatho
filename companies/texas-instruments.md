# Texas Instruments

**148 questions** from 6 OA drives · seen at BITS Pilani, IIIT Hyderabad, IIT BHU, IIT Bombay, IIT Hyderabad, Unknown · latest 2026-10-28

**Topics:** [Aptitude](../topics/aptitude.md) (60) · [Digital Electronics](../topics/digital-electronics.md) (30) · [Circuits](../topics/circuits.md) (27) · [Puzzles](../topics/puzzles.md) (24) · [Analog Electronics](../topics/analog-electronics.md) (23) · [Math](../topics/math.md) (16) · [Code Output (C/C++/Java/Python)](../topics/code-output-c-c-java-python.md) (9) · [Signals & Systems](../topics/signals-systems.md) (8) · [OA Format](../topics/oa-format.md) (4) · [OS/DBMS/CN MCQ](../topics/os-dbms-cn-mcq.md) (2) · [Linked List](../topics/linked-list.md) (1) · [Bit Manipulation](../topics/bit-manipulation.md) (1)

**Drives:**

- [2026-10-28 · IIT BHU · Unknown · Embedded SW · Other round](#2026-10-28--iit-bhu--unknown--embedded-sw--other-round) · 5 questions
- [2026-10-25 · IIT BHU · FTE](#2026-10-25--iit-bhu--fte) · 1 question
- [2026-10-18 · IIIT Hyderabad · FTE · Analog / Digital](#2026-10-18--iiit-hyderabad--fte--analog--digital) · 1 question
- [2026-10-08 · Unknown · FTE](#2026-10-08--unknown--fte) · 60 questions
- [2026-10-08 · IIT Hyderabad · FTE](#2026-10-08--iit-hyderabad--fte) · 60 questions
- [2026-10-08 · IIT Bombay · FTE](#2026-10-08--iit-bombay--fte) · 21 questions

[← all companies](../README.md#companies)

---

## 2026-10-28 · IIT BHU · Unknown · Embedded SW · Other round

### Q1. Slowest and fastest implementation by memory section

For a deeply embedded processor such that it:
- does not have any cache
- has three memories such that in terms of speed: L1 RAM > L2 RAM > FLASH
- on startup zero-initializes its .bss section (where all un-initialized variables are placed)

Identify which implementations would be the slowest and fastest.

Section to memory mapping: .data - L2 RAM, .bss - L1 RAM, .stack - L1 RAM, .heap - L2 RAM, .code - FLASH, .rodata - FLASH

Implementation 1:
```c
int global_sum = 0;
compute_sum(range)
{
   for value in range {
      global_sum = global_sum + value
   }
}
```
Implementation 2:
```c
int global_sum = 0;
compute_sum(range)
{
   int local_sum = 0;
   for value in range {
      local_sum = local_sum + value
   }
   global_sum = local_sum;
}
```
Implementation 3:
```c
int global_sum = 0;
compute_sum(range)
{
   static int local_sum = 0;
   for value in range {
      local_sum = local_sum + value
   }
   global_sum = local_sum;
}
```

<sub>Topics: Code Output (C/C++/Java/Python), OS/DBMS/CN MCQ · Source: [Prep for TI - Embedded SW.pdf](../archive/files/15288-Prep_for_TI_-_Embedded_SW.pdf)</sub>

### Q2. Identify the error in digit-reversal function

Identify the error in the implementation:
```c
int length;
void foo(int sg)
{
   int reverse_sg;
   while(sg>0)
   {
    length = length + 1;
    reverse_sg = reverse_sg * 10 + (sg%10);
    sg = sg / 10;
   }
}
```

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Prep for TI - Embedded SW.pdf](../archive/files/15288-Prep_for_TI_-_Embedded_SW.pdf)</sub>

### Q3. Cortex-A72 performance: data structure, matrix order, list cycle

Consider a high performance application running on Cortex-A72. It has many different functions.
1. It has a function that loops over every element of a linear data-structure from beginning to end. To reduce the run time of this function, which linear data structure should it loop onto?
2. It has a function that does computation of a 2D matrix. Should that matrix be computed in column-major fashion or row-major fashion in order to reduce run-time? Why?
3. In a linked-list, how would you detect a loop?

<sub>Topics: OS/DBMS/CN MCQ, Linked List · Source: [Prep for TI - Embedded SW.pdf](../archive/files/15288-Prep_for_TI_-_Embedded_SW.pdf)</sub>

### Q4. Read 4 bytes with garbage LSB at elevated temperature

An industrial memory access controller accesses a memory bank which is 16K-bytes in size and is organized as 16K x 8. During testing, it was found that:
1. At normal temperature, it works as per its design, i.e. it reads and writes 4 bytes at a time.
2. At elevated temperature of 105 deg C, it writes 4 bytes correctly but reads 4 bytes with Least-Significant-Byte as garbage.

Write functions in C that read 4 bytes of data at a time at elevated temperature.

<sub>Topics: Bit Manipulation · Source: [Prep for TI - Embedded SW.pdf](../archive/files/15288-Prep_for_TI_-_Embedded_SW.pdf)</sub>

### Q5. TI Embedded SW syllabus for written test and interview

Topics for both written test and interview: basic C programming (pointers, algorithms, stacks/queues; data structures up to basics of graphs, BST, hash, LL for NCG, up to LL for interns); Embedded C (struct size calculation, bit manipulation, memory layout of C program, static and volatile keywords, compilation stages); Operating systems (scheduling algorithms, multi-process synchronization, virtual and physical memory for NCG; synchronization for interns); Computer Architecture for NCG (caches, DMA, organization, pipeline); Microcontroller (8051 assembly, interrupts and their processing, DMA, timers, memories, ADC, DAC, GPIO and SPI).

<sub>Topics: OA Format · Source: [Prep for TI - Embedded SW.pdf](../archive/files/15288-Prep_for_TI_-_Embedded_SW.pdf)</sub>

## 2026-10-25 · IIT BHU · FTE

### Q1. OA pattern (Digital/Analog role): op-amp MCQs + aptitude

Texas Instruments OA for the digital/analog role: MCQs on op-amps, aptitude questions, and questions from every core electronics topic.

<sub>Topics: OA Format, Analog Electronics · Source: [chat, 25 Oct](../archive/inter-iit/2026-10.jsonl#L993)</sub>

## 2026-10-18 · IIIT Hyderabad · FTE · Analog / Digital

### Q1. TI OA format

Simple OA. CS MCQs on C programming, microprocessors and COA. One very easy coding question, only in C language.

<sub>Topics: OA Format · Source: [chat, 18 Oct](../archive/campus-iiit-hyderabad-placements/2026-10.jsonl#L25)</sub>

## 2026-10-08 · Unknown · FTE

### Q1. Pens on a shelf ordering

There are four pens: a red pen, a black pen, a green pen and a blue pen. The pens need to be kept in a shelf from left to right. The red pen should be on the left. The black pen should be kept just after the red pen and the blue pen should be on the right. The green pen should be on the left of the blue pen but on the right of the black pen. Which of the following pen is kept on the left of the black pen?

A. Red
B. Green
C. Blue
D. Cannot be determined

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q2. Minimum time to build wall with pairs

Three men P, Q and R working individually take 12 days, 15 days and 20 days respectively to construct a wall. Find the minimum time required to construct a wall if not more than 2 men are working together on a day and no same pair of men work on two consecutive days.

A. 6.5 days
B. 7 days
C. 7.5 days
D. 8 days

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q3. Event schedule with slot restriction

A management club has 5 distinct technical activities and 4 distinct strategy activities. For a short event, exactly 2 technical activities and exactly 1 strategy activity must be selected. The selected 3 activities will be conducted in three distinct slots: Slot 1, Slot 2, and Slot 3. The strategy activity must not be conducted in Slot 1.
In how many ways can the event schedule be prepared?

A. 120
B. 140
C. 160
D. 180

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q4. Count triangles in grid with diagonal

Use the figure given below to answer the question. The figure is a 5×5 square grid with one main diagonal drawn from the top-left corner to the bottom-right corner.

What is the number of triangles in the figure?

A. 30
B. 27
C. 20
D. 15

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q5. Probability three books together

15 books are placed on a table. The probability that three of the books will always be together is x/y. The value of x is 1 and the value of y is __________ .

<sub>Topics: Math, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q6. Doctors in a queue

In a queue of more than 10 doctors, Dr. A is 9th from the left end and Dr. B is 3th from the right end, there are three doctors between Dr. A and Dr. B. A total of __________ doctors are there in the queue.

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q7. Football players team selection

Seven football players namely Gaurav, Harsh, Kunal, Lalit, Manish, Naman and Ojha are to be selected for one of the college teams, the Phoenix and the Devils.

- If Gaurav is selected for the Phoenix, then Harsh will be selected for the Devils
- If Kunal is selected for the Phoenix, then Lalit and Manish will be selected for the Devils.
- Naman is selected on a different team than Ojha.
- Manish is selected on a different team than Gaurav.
- If Ojha is selected for the Phoenix, then Harsh will also play for the Phoenix.

Which of these could be a complete and accurate list of players in the Phoenix team?

A. Gaurav, Kunal, Ojha
B. Harsh, Manish, Naman, Ojha
C. Kunal, Harsh, Lalit, Ojha
D. Lalit, Manish, Naman

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q8. Painter average daily earnings

A painter is paid x rupees for painting every 10 metres of a wall and y rupees for painting every extra metre. During one week, he painted 10 metres on Monday, 13 metres on Tuesday, 12 metres on Wednesday, 11 metres on Thursday, and 12 metres on Friday. What is his average daily earnings in rupees for the five - day week?

A. x + (8/5)y
B. (5x + 9y)/5
C. 10x + (8/5)y
D. 5x + 8y

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q9. Speeds of A, B, C, D

The difference between A's speed and B's Speed is 3km/hr. C's speed is twice as that of A and B's speed is twice as that of D. the difference between C and D speed is 30km/hr. The speed of B is:

A. 18 km/hr
B. 19 km/hr
C. 21 km/hr
D. 24 km/hr

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q10. Two dice sum is 5

Two dice are thrown simultaneously, What is the probability that the sum of the numbers shown on the two dice is 5?

A. 1/6
B. 1/9
C. 2/27
D. 1/12

<sub>Topics: Math, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q11. Alphanumeric sequence completion

Which of the following will come in place of the question mark (?) in the following sequence so that it completes the sequence?

L₁₂QK, MS₁₀I, NUG₈, O₆WE, (?)

A. P₄YC
B. PY₄C
C. PYC₄
D. PW₄C

(The subscript numbers are 12, 10, 8, 6 in the given terms; the position of the subscript 4 differs between options.)

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q12. Blood relation from photograph

Pointing to a photograph Rita, said "he is the son-in-law of the grand mother of my father's father's only son". How is Rita's father related to the wife of the man in photograph?

A. Son-in-law
B. Brother-in-law
C. Nephew
D. Brother

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q13. Six people sitting in a row

Arpita, Purna, Rina, Xola, Sofia and Zain are sitting in a row. Sofia and Zain are in the center. Arpita and Purna are at the ends. Rina is sitting just to the left of Arpita. __________ is to the immediate right of Purna.

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q14. Convolution of exponentials at t=1

Let the input signal be

x(t) = e^(−2t) u(t)

where u(t) is the unit step function. The system has an impulse response:

h(t) = e^(−t) u(t)

What is the value of the output y(t) at t=1, where y(t) = x(t) * h(t)?

A. 0.367
B. 0.232
C. 0.632
D. 0.500

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q15. Finite-gain op-amp as high-pass filter

The op-amp shown below (fig. 1) is an ideal op-amp having a finite gain of A₀ is modeled as a HPF (High Pass Filter) shown in fig. 2. The condition of C_X & R_X for which the poles of fig. 1 & fig. 2 will concide will be given as _________

Fig. 1: inverting op-amp with input capacitor C in series from Vin to the inverting node A, feedback resistor R from output to node A, non-inverting input grounded. Fig. 2: series capacitor C_X from Vin to Vout, with resistor R_X from Vout to ground.

A. C_X = A₀C₁ & R_X = R₁/A₀
B. C_X = (1 + A₀)C₁ & R_X = R₁/A₀
C. C_X = C₁/(1 + A₀) & R_X = R₁
D. C_X = C₁/A₀ & R_X = (1 + A₀)R₁

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q16. Two NMOS stacked, find Vx

The N-channel MOS transitor has u_nC_ox = 100uA/V² & threshold voltage 1V, for the circuit shown below the value of Vx when Vdd & Vin are set to 6V & 2V respectively will be __________ V

Circuit: upper NMOS (W/L = 4) with drain at Vdd, gate at Vin, source at node Vx; lower NMOS (W/L = 1) diode-connected (gate tied to drain at Vx), source at ground.

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q17. Fourier transform of piecewise signal, find A

If the Fourier transform of signal x(t) shown below is given by

X(jω) = (1/jω) [ A + e^(−jω) − 3e^(−j2ω) ]

then the value of A will be:

Signal x(t): equals 2 for 0 ≤ t < 1, equals 3 for 1 ≤ t < 2, and 0 elsewhere.

A. 2
B. 3
C. 5
D. 8

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q18. RL series circuit current

In the circuit shown below, if V(t) = 50 cos 200t V then the value of current 'i' will be:

Circuit: voltage source v_s in series with a 20 Ω resistor and a 20 mH inductor.

A. 2.451 cos(200t + 11.31°) A
B. 2.451 cos(200t - 11.31°) A
C. 20.4 cos(200t - 11.31°) A
D. 20.4 cos(200t + 11.31°) A

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q19. PN diode and Schottky diode states

In the diode circuit shown assume that the forward voltage drops of the PN diode D1 and Schottky diode D2 are 0.7 V and 0.3 V, respectively, if ON denotes conducting state of the diode and OFF denotes non conducting state of the diode, then in the circuit the condition will be:

Circuit: 10 V source, 1 kΩ series resistor, D1 from the node to ground, then a 20 Ω resistor in series with D2 (Schottky) to ground, D2 in parallel with D1.

A. D1 is OFF D2 is ON
B. D1 is ON D2 is OFF
C. Both D1 & D2 ON
D. Both D1 & D2 OFF

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q20. RC filter time constant

In an industrial motor control panel, a voltage monitoring circuit uses an RC filter to suppress high-frequency transients caused by switching operations. The schematic of the filter section is shown below. The capacitor is rated at 3 μF, and the resistors connected represent the equivalent resistances from different signal paths inside the control logic.

What is the time constant of this RC network that determines how quickly the system responds to a change in input voltage?

Circuit: source 10u(t), 2 Ω series resistor, then 2 Ω to ground; 3 μF capacitor in series leading to 6 Ω and 3 Ω resistors in parallel to ground.

A. 3μ sec
B. 9μ sec
C. 15μ sec
D. 25μ sec

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q21. Maximum average power in variable resistor

The circuit shown below consists of a variable resistor 'R' which is tuned till it absorbs the maximum average power then the maximum average power absorbed will be ______________

Circuit: j1 Ω inductor, 3 Ω resistor, 4∠0° A current source, 6 Ω resistor, −j2 Ω capacitor in series with variable resistor R.

A. 1.235W
B. 2.451W
C. 3.798W
D. 7.285W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q22. Emitter current of self-bias NPN

In NPN amplifier circuit using self bias circuit, Base current I_B = 300 μA and α = 0.98. Find emitter current I_E.

Answer __________ mA

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q23. Marathon runners finishing order

For runners (R1, R2, R3, and R4) completed a marathon. R1 finished before R4 but after R2. R2 finished after R3. Who finished the marathon first?

A. R1
B. R2
C. R3
D. R4

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q24. Resistance seen at MOS source terminal

For the MOS circuit shown below, the value of R_x seen through the source terminal will be: ___________________ (assume λ = 0)

Circuit: common-source NMOS M1 with load Z_L to VDD, Vin at gate, Vout at drain, body connected to ground, R_x looking into the source.

A. R_x = 1 / g_mb
B. R_x = 1 / g_m
C. R_x = 1 / (g_m + g_mb)
D. R_x = g_m / (g_m + g_mb)

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q25. Average power absorbed by 5 ohm resistor

For the circuit shown below, the average power absorbed by the 5 ohm resistor will be ____________

Circuit: current source 2∠0° A in parallel with a 5 Ω resistor and a branch of −j4 Ω capacitor in series with j1 Ω inductor.

A. 1.21W
B. 5W
C. 3.21W
D. 2.64W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q26. Equivalent impedance of passive network

The equivalent impedance of a linear passive circuit shown below will be _______________

Circuit (as drawn): 2 Ω, 4 Ω, 8 Ω, j6 Ω, 5 Ω, −j5 Ω, j2 Ω, 3 Ω, −j4 Ω and −j4 Ω elements in a network between the two terminals (diagram not reproducible as text).

A. (16/5 + j 14/15) Ω
B. (14/15 + j 16/5) Ω
C. (14/15 − j 16/5) Ω
D. (16/5 − j 14/15) Ω

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q27. RC charging wait time

A heart rate monitoring device uses an RC circuit to shape the input signal from a skin-contact sensor. The circuit has a resistor of 100 kΩ and a capacitor of 1 μF. When a step input of 5V is applied, the sensor processing unit must wait until the capacitor charges to at least 3.15V before triggering the next stage.

How long must the system wait after the step input is applied to safely trigger the next stage?

A. 23 ms
B. 69 ms
C. 100 ms
D. 50 ms

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q28. BJT base drive current

BJT is connected to common emitter mode and operated in active region with collector current Ic =1.01 mA for this when common base current gain is 0.98 and reverse bias saturation current is 0.5 μA then what is the base drive current?

A. 0.2mA
B. 0.2 μA
C. 0.22μA
D. 0.3μA

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q29. IC 555 astable charging vs discharging time

An IC 555 in an astable multivibrator mode is shown below where RA=RB=20KΩ & C=1pF. The pin description is as 1 and 8-supply; 2-trigger; 4-reset; 6-threshold 7-discharge. The relation between charging & discharging time will be :

Circuit: RA from +Vcc to pin 7, RB from pin 7 to pins 2/6, capacitor C from pins 2/6 to ground, and a diode connected across RB (between pin 7 and pins 2/6).

A. T_Charging < T_Discharging
B. T_Charging > T_Discharging
C. T_Charging = T_Discharging
D. T_Charging = 1/T_Discharging

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q30. Switched-capacitor effective resistance

A switched-capacitor circuit uses a 1 pF capacitor switched between input and virtual ground at a rate of 250 kHz. What is the effective resistance seen at the input?

A. 4 MΩ
B. 400 kΩ
C. 2 MΩ
D. 4 kΩ

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q31. Power dissipated in 12 ohm resistor

For the resistive network shown below, the power dissipated by 12Ω resistor will be:

Circuit: 6 A current source in parallel with 2 Ω; 1 Ω (voltage Vx across it) in series, then 4 Ω to a node with 3 Ω and 6 Ω in parallel; 1.2 Ω in series leading to 8 Ω and 12 Ω in parallel.

A. 1W
B. 1.5W
C. 1.92W
D. 3.84W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q32. Op-amp capacitor voltage decay

The op-amp shown below has initial voltage across capacitor v(0) = 5 V, then for t > 0 the voltage across capacitor v(t) will be _______________________ (assume R = 10kΩ and C = 1μF)

Circuit: op-amp in a unity-gain buffer configuration with the capacitor C (voltage v) at the non-inverting input and three equal resistors R in the network.

A. e^(-100t/3) u(t) V
B. 2e^(-100t/3) u(t) V
C. 5e^(-100t/3) u(t) V
D. 10e^(-100t/3) u(t) V

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q33. Diode clipper peak output

For the diode circuit shown below, if V₁ is 1KHz, 5V peak sin wave then the value of V_o,peak will be

Circuit: 10 V supply feeding a 1 mA current source, output Vo taken at the node above a 1 kΩ resistor which connects to the parallel anodes of D1 (cathode at V₁) and D2 (cathode to ground).

A. 1 V
B. -1 V
C. 4 V
D. -4 V

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q34. Five teachers in four schools

Five teachers I, J, K, L and M teach in four different schools. M and K do not teach in DPS, L teaches in St. Paul's and I teaches in St. Xavier's. If two teachers out of the five teach in Model school, which school does M teach in?

A. St. Paul's
B. St. Xavier's
C. Model School
D. Cannot be determined

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q35. Ripple factor of inductor filter

The output voltage across the load resistance of an inductor filter connected to a bridge rectifier shows a DC value of 25 V and a peak-to-peak ripple voltage of 1.5 V. Calculate the ripple factor.

A. 0.03
B. 0.0173
C. 0.0208
D. 0.0375

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q36. 4:1 MUX output function

Find output (f) of the following 4:1 MUX.

MUX inputs: I3, I2, I1 tied to logic 1, I0 tied to ground; select lines S1 = X, S0 = Y.

A. XY
B. X'Y'
C. X+Y
D. X'+Y'

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q37. Verilog/VHDL toggle flop final value

Consider the following RTL module (code given in Verilog and VHDL):

Verilog
```verilog
module seq (
input clk,
input reset,
input sel,
input d,
output reg q
);

always @(posedge clk or posedge reset) begin
if (reset)
q <= 1'b0;
else if (sel)
q <= ~q;
else
q <= d;
end

endmodule
```

VHDL
```vhdl
architecture Behavioral of seq is
signal q_reg : STD_LOGIC := '0';
begin
process(clk, reset)
begin
if reset = '1' then
q_reg <= '0';
elsif rising_edge(clk) then
if sel = '1' then
q_reg <= not q_reg;
else
q_reg <= d;
end if;
end if;
end process;

q <= q_reg;
end Behavioral;
```

Starting from the reset state, the following inputs are applied at four consecutive rising edges:

| Edge | sel | d |
|---|---|---|
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |
| 4 | 0 | 0 |

What is the final value of q?

A. 0
B. 1
C. X
D. Z

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q38. PROM size for dual 4-to-1 multiplexers

You are designing a digital control system for a smart irrigation unit using dual 4-to-1 multiplexers. The system has:

4 soil moisture sensors (8-bit output each)
4 temperature sensors (8-bit output each)
2 control lines to select which sensor pair to read
Both multiplexers share the same control lines

If you implement the selection logic using a PROM that stores the control logic only, what is the minimum PROM size required?

A. 64 bits
B. 128 bits
C. 256 bits
D. 512 bits

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q39. Setup slack of two flip-flops

For the circuit shown below the set up slack time will be ________________ (assume T_clk = 10ns)

Timing data: FF1 clock path wire tmin 1 ns / tmax 2 ns; FF1 t_clk-q,min 9 ns / t_clk-q,max 11 ns; wire FF1→inverter tmin 1 / tmax 2 ns; inverter tmin 6 / tmax 9 ns; wire inverter→FF2 tmin 1 / tmax 2 ns. Clock path to FF2: wire tmin 2 / tmax 3 ns, buffer tmin 5 / tmax 9 ns, wire tmin 2 / tmax 3 ns. FF2 t_hold 2 ns, t_setup 4 ns.

A. 26ns
B. 21ns
C. 5ns
D. -5ns

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q40. C output with $ and _ macros

What will be the output of the program given below?

```c
#include <stdio.h>

#define $ a

#define _ b

static int $, _;

int main()
{

$ = _ = 2;

printf("%d ", (fun(fun($, _), fun($, _))));

return 0;

}

fun(int $, int _)

{

$ = $ >>= _ <<= 2;

return _;

return $;

}
```

A. 32
B. 0
C. 8
D. Compile time error

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q41. BCD counter after 7 clock pulses

A BCD (Binary Coded Decimal) counter counts from 0000 to 1001 and then resets. If the counter is initially at 0110 (BCD) and receives 7 clock pulses, the final count will be __________ (BCD).

Express your answer as a 4-digit binary number.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q42. C program digit weighting output

What will be the output of the program given below?

```c
#include <stdio.h>
int main()
{
int N = 1111101;
int a = 2;
int res = 0;
while (N != 0) {
res = res + (N % 10) * a;
N = N / 10;
a = a * 2;
}

printf("%d", res);

}
```

A. 250
B. 227
C. 251
D. Compile time error

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q43. Discrete system y[n]=3x[n]-2x[n-1] properties

A discrete-time system satisfies

y[n]=3x[n]−2x[n−1]

Which property is true?

A. Non-linear and time varying
B. Linear and time invariant
C. Non-linear but time invariant
D. Linear but unstable

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q44. 3-input NAND count of HIGH outputs

A 3-input NAND gate has the following input combinations applied sequentially: ABC = 000, 001, 010, 011, 100, 101, 110, 111. Count the number of times the output is HIGH (logic 1).
The answer is __________

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q45. Letter pairs in PRECISE

How many such pairs of letters are there in the word 'PRECISE' which has as many letter between them (from both the sides) as in the alphabets from A to Z?

A. 0
B. 1
C. 2
D. 3

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q46. Fix WNS after place-and-route

An ASIC targeting 1 GHz has completed place-and-route. The timing report shows a worst negative slack (WNS) of -0.18 ns, while all other paths have positive slack. RTL simulation, synthesis, and logical equivalence checking have already passed. The RTL architecture is frozen, and functional changes are not permitted.

Which action is most appropriate to improve timing with the least impact on functionality?

A. Re-optimize placement and routing around the failing path while preserving logic functionality.
B. Relax the clock uncertainty so that setup analysis becomes less pessimistic.
C. Increase the drive strength uniformly across every standard cell in the design.
D. Replace all flip-flops on the failing path with lower setup-time library cells.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q47. Identify flip-flop type from circuit

The type of flip flop realized by the circuit shown below will be _______________

Circuit: an SR flip-flop whose S and R inputs are driven through AND gates (with clock) from an OR of two AND gates; input X and the flip-flop's Q/Q' feedback feed those AND gates through inverters.

A. D Flip Flop
B. T Flip Flop
C. JK Flip Flop where J = K = X
D. None of these options

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q48. Synchronous counter for sequence 0→3→1→2→0

The correct implementation of a synchronous counter for the count sequence 0 → 3 → 1 → 2 → 0 will be ________________

Options are circuit diagrams:
A. Two D flip-flops; D1 fed from Q0-side feedback, D0 = XOR of Q1 and Q0 (as drawn).
B. Two D flip-flops; D1 fed from feedback, D0 = XNOR-type gate of Q1 and Q0 (as drawn, with output bubble).
C. Two T flip-flops with T1 = 0 and T0 connected to Q1', common CLK.
D. Two T flip-flops with T1 = 1 and T0 connected to Q1, common CLK.

(Diagrams not reproducible in text.)

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q49. PROM size for traffic light controller

A traffic light controller system uses a PROM to store the next state logic. The system design requires:

Inputs: 3 state bits + 2 sensor inputs + 1 timer input (total 6 inputs)
Outputs: 3 next state bits + 6 traffic light control bits (total 9 outputs)

Calculate the minimum PROM storage capacity required to implement this sequential logic circuit.

A. 288 bits
B. 576 bits
C. 864 bits
D. 1152 bits

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q50. Microcontroller loop final count

Consider the following pseudocode executed by a microcontroller:

```
count = 0

while (count < 5)
{
if (INPUT == HIGH)
count = count + 2;
else
count = count + 1;
}
```

If INPUT remains HIGH throughout the execution, what will be the final value of count?

A. 4
B. 5
C. 6
D. 7

<sub>Topics: Digital Electronics, Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q51. 8086 assembly final CX value

Consider the following 8086 assembly program:

```
MOV AX, 0005H
MOV BX, 0003H
MOV CX, 0000H

L1: ADD CX, AX
DEC BX
JNZ L1

SUB CX, 0004H
```

What will be the final value of the CX register after the program executes?

A. 000BH
B. 000FH
C. 0011H
D. 0015H

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q52. Thevenin equivalent from Norton values

If the Norton current and resistance for the circuit shown are respectively are 6A and 4 Ohm, what is the value of V_Thevenin (V_Th) and R_Thevenin (R_Th)?

Circuit: current source I_sc in parallel with resistor r, with load R across terminals A–B.

A. V_Th = 2 V, R_Th = 1.5 Ω
B. V_Th = 24 V, R_Th = 1.5 Ω
C. V_Th = 1.5 V, R_Th = 1.5 Ω
D. V_Th = 24 V, R_Th = 4 Ω

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q53. CMOS 3-input NAND delay

A 3- input NAND gate (NMOS & PMOS based) is showing in figure parasitic elements.

Figure: pull-up P1, P2, P3 in parallel to out; pull-down stack N3 (input in_c), N2 (in_b), N1 (in_a) in series to ground, with parasitic capacitors C_c, C_b, C_a at internal nodes and C_p+load at the output.

Determine the total time difference of CMOS based NAND gate when the value of Resistance Ra = .5K, Rb = 2K, Rc = 1K, capacitance Ca = 1μF, Cb = 1.5μF, Cc = 0.3μF, and Cpload = .2μF.

A. 6.5msec
B. 10.5msec
C. 16.5msec
D. 9.1msec

<sub>Topics: Digital Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q54. Minterm function equivalent expression

Consider a four variable based function expressed in terms of its min terms.

F (w, x, y, z) = Σ(0,3, 5, 6, 7,9,10,11,12,14,15)

F (w, x, y, z) can be expressed as ( no need to simplify)

A. ∏ (1,2,4,8,13) + (w'x'y'z + w'x'yz' + w'xy'z' + wx'y'z' + wxy'z)
B. Σ(1,2,4,8,13) - ∏ (0,3, 5, 6, 7,9,10,11,12,14,15 )
C. Σ(0-15) - ∏ (1,2,4,8,13)
D. ∏ (0-7) + Σ (0-7) - Σ (1,2,4,8,13)

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q55. Aliasing when sampling at 30 kHz

A sensor signal contains frequency components up to 18 kHz. An engineer samples the signal at 30 kHz without using an anti-aliasing filter.

Which statement is correct

A. All frequency components are reconstructed correctly.
B. Frequencies above 15 kHz will alias into the sampled spectrum.
C. Aliasing occurs only if the sampling frequency is below 18 kHz.
D. Increasing the ADC resolution eliminates aliasing.

<sub>Topics: Signals & Systems, Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q56. Five friends piggy bank savings

Five friends - Rohan, Sia, Tanu, Varun, and Zoya - save money in their piggy banks.

- Together, they save ₹1,150.
- Rohan saves ₹150 more than Sia.
- Tanu saves twice as much as Sia.
- Varun saves the same amount as Rohan.
- Zoya saves ₹50 less than Sia.

How much does Tanu save?

A. ₹250
B. ₹280
C. ₹300
D. ₹320

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q57. 4-bit ripple counter settling time

A 4-bit ripple counter using JK flip-flops has a propagation delay of 12ns per flip-flop. When the counter transitions from 1111 to 0000, the maximum settling time is __________ ns.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q58. Day of week after 15 days

If today is Wednesday, __________ will be the day of the week after 15 days.

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q59. Number arrangement machine

A number arrangement machine, when given an input line of numbers, rearranges them following a particular rule in each step. Illustration:

| | | | | | |
|---|---|---|---|---|---|
| Input | 531842 | 764125 | 902317 | 648531 | 287964 | 413256 |
| Step I | 8 | 12 | 3 | 15 | 21 | 9 |
| Step II | 15 | 13 | 19 | 12 | 15 | 12 |
| Step III | 289 | 313 | 370 | 369 | 666 | 225 |
| Step IV | 64 (first two) | 353 (middle two) | 1 (last two) | | | |
| Step V | 10 (first two) | 11 (middle two) | 1 (last two) | | | |

Step V is the last step of the rearrangement. As per the rules followed in the above steps, find out the output for the below input:

```
825431  370962  641528  954210  718346  260871
```

Step V of the above input is __________ .

(Table layout of Steps IV and V is approximate: the values span pairs of columns.)

<sub>Topics: Puzzles, Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q60. Streaming plans subscribers

A U.S. streaming service offers three plans: Basic at $15, Standard at $25, and Pro at $45 per month. There are 600 subscribers in total, and the average monthly revenue per subscriber is $26. Also, the number of Pro subscribers is 60 less than the number of Basic subscribers. How many Standard subscribers are there?

A. 280
B. 340
C. 320
D. 300

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10881-Texas_Instruments_All_60_Questions.pdf)</sub>

## 2026-10-08 · IIT Hyderabad · FTE

### Q1. Pen arrangement on shelf

There are four pens: a red pen, a black pen, a green pen and a blue pen. The pens need to be kept in a shelf from left to right. The red pen should be on the left. The black pen should be kept just after the red pen and the blue pen should be on the right. The green pen should be on the left of the blue pen but on the right of the black pen. Which of the following pen is kept on the left of the black pen?

- **A.** Red  
- **B.** Green  
- **C.** Blue  
- **D.** Cannot be determined

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q2. Wall construction with pairs of men

Three men P, Q and R working individually take 12 days, 15 days and 20 days respectively to construct a wall. Find the minimum time required to construct a wall if not more than 2 men are working together on a day and no same pair of men work on two consecutive days.

- **A.** 6.5 days  
- **B.** 7 days  
- **C.** 7.5 days  
- **D.** 8 days

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q3. Scheduling club activities in slots

A management club has 5 distinct technical activities and 4 distinct strategy activities. For a short event, exactly 2 technical activities and exactly 1 strategy activity must be selected. The selected 3 activities will be conducted in three distinct slots: Slot 1, Slot 2 and Slot 3. The strategy activity must not be conducted in Slot 1. In how many ways can the event schedule be prepared?

- **A.** 120  
- **B.** 140  
- **C.** 160  
- **D.** 180

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q4. Count triangles in grid with diagonal

Figure: a 5x5 square grid with one diagonal drawn from the top-left corner to the bottom-right corner. What is the number of triangles in the figure?

- **A.** 30  
- **B.** 27  
- **C.** 20  
- **D.** 15

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q5. Probability 3 books together

15 books are placed on a table. The probability that three of the books will always be together is x/y. The value of x is 1 and the value of y is ________.

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q6. Doctors in a queue

In a queue of more than 10 doctors, Dr. A is 9th from the left end and Dr. B is 3rd from the right end; there are three doctors between Dr. A and Dr. B. A total of ________ doctors are there in the queue.

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q7. Football team selection (Phoenix/Devils)

Seven football players namely Gaurav, Harsh, Kunal, Lalit, Manish, Naman and Ojha are to be selected for one of the college teams, the Phoenix and the Devils. If Gaurav is selected for the Phoenix, then Harsh will be selected for the Devils. If Kunal is selected for the Phoenix, then Lalit and Manish will be selected for the Devils. Naman is selected on a different team than Ojha. Manish is selected on a different team than Gaurav. If Ojha is selected for the Phoenix, then Harsh will also play for the Phoenix. Which of these could be a complete and accurate list of players in the Phoenix team?

- **A.** Gaurav, Kunal, Ojha  
- **B.** Harsh, Manish, Naman, Ojha  
- **C.** Kunal, Harsh, Lalit, Ojha  
- **D.** Lalit, Manish, Naman

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q8. Painter average daily earnings

A painter is paid x rupees for painting every 10 metres of a wall and y rupees for painting every extra metre. During one week, he painted 10 metres on Monday, 13 metres on Tuesday, 12 metres on Wednesday, 11 metres on Thursday and 12 metres on Friday. What is his average daily earnings in rupees for the five-day week?

- **A.** x + (8/5)y  
- **B.** (5x + 9y)/5  
- **C.** 10x + (8/5)y  
- **D.** 5x + 8y

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q9. Speeds of A, B, C, D

The difference between A's speed and B's speed is 3 km/hr. C's speed is twice that of A and B's speed is twice that of D. The difference between C and D speed is 30 km/hr. The speed of B is:

- **A.** 18 km/hr  
- **B.** 19 km/hr  
- **C.** 21 km/hr  
- **D.** 24 km/hr

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q10. Two dice sum 5

Two dice are thrown simultaneously. What is the probability that the sum of the numbers shown on the two dice is 5?

- **A.** 1/6  
- **B.** 1/9  
- **C.** 2/27  
- **D.** 1/12

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q11. Alphanumeric sequence

Which of the following will come in place of the question mark (?) in the sequence: L12QK, MS10I, NUG8, O6WE, (?) (numbers are subscripts).

- **A.** P4YC  
- **B.** PY4C  
- **C.** PYC4  
- **D.** PW4C

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q12. Blood relation - photograph (Rita)

Pointing to a photograph Rita said, "he is the son-in-law of the grand mother of my father's father's only son". How is Rita's father related to the wife of the man in photograph?

- **A.** Son-in-law  
- **B.** Brother-in-law  
- **C.** Nephew  
- **D.** Brother

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q13. Seating in a row

Arpita, Purna, Rina, Xola, Sofia and Zain are sitting in a row. Sofia and Zain are in the center. Arpita and Purna are at the ends. Rina is sitting just to the left of Arpita. ________ is to the immediate right of Purna.

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q14. Convolution output y(1)

Let the input signal be x(t) = e^(-2t) u(t), where u(t) is the unit step function. The system has an impulse response h(t) = e^(-t) u(t). What is the value of the output y(t) at t = 1, where y(t) = x(t) * h(t) (convolution)?

- **A.** 0.367  
- **B.** 0.232  
- **C.** 0.632  
- **D.** 0.500

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q15. Op-amp differentiator modeled as HPF

The op-amp shown in fig. 1 (Vin -> capacitor C -> inverting node A, feedback resistor R from A to Vout, non-inverting input grounded) is an ideal op-amp having a finite gain of A0 and is modeled as a HPF (High Pass Filter) shown in fig. 2 (Vin -> series Cx -> Vout, Rx from Vout to ground). The condition on Cx and Rx for which the poles of fig. 1 and fig. 2 will coincide is:

- **A.** Cx = A0*C1 & Rx = R1/A0  
- **B.** Cx = (1+A0)C1 & Rx = R1/A0  
- **C.** Cx = C1/(1+A0) & Rx = R1  
- **D.** Cx = C1/A0 & Rx = (1+A0)R1

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q16. NMOS source follower with diode-connected load

The N-channel MOS transistor has unCox = 100 uA/V^2 and threshold voltage 1 V. Circuit: upper NMOS (W/L = 4) with drain at Vdd, gate at Vin, source at node Vx; lower NMOS (W/L = 1) diode-connected (gate tied to drain at Vx), source to ground. The value of Vx when Vdd and Vin are set to 6 V and 2 V respectively will be ________ V.

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q17. Fourier transform of staircase pulse

x(t) = 2 for 0 &lt; t &lt; 1, 3 for 1 &lt; t &lt; 2, 0 otherwise. If the Fourier transform of x(t) is X(jw) = (1/jw)[A + e^(-jw) - 3e^(-j2w)], then the value of A will be:

- **A.** 2  
- **B.** 3  
- **C.** 5  
- **D.** 8

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q18. Current in series RL circuit

In the circuit with source vs, a 20 ohm resistor in series with a 20 mH inductor, if V(t) = 50 cos 200t V then the current i will be:

- **A.** 2.451 cos(200t + 11.31 deg) A  
- **B.** 2.451 cos(200t - 11.31 deg) A  
- **C.** 20.4 cos(200t - 11.31 deg) A  
- **D.** 20.4 cos(200t + 11.31 deg) A

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q19. PN diode vs Schottky diode states

A 10 V source feeds a node through a 1 kohm resistor; PN diode D1 is connected from that node to ground, and a 20 ohm resistor in series with Schottky diode D2 is also connected from that node to ground. The forward voltage drops of D1 and D2 are 0.7 V and 0.3 V respectively. If ON denotes conducting and OFF denotes non-conducting, the condition will be:

- **A.** D1 OFF, D2 ON  
- **B.** D1 ON, D2 OFF  
- **C.** Both D1 and D2 ON  
- **D.** Both D1 and D2 OFF

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q20. RC network time constant

In an industrial motor control panel, a voltage monitoring circuit uses an RC filter to suppress high-frequency transients. Circuit: source 10u(t) in series with 2 ohm to node 1; 2 ohm from node 1 to ground; a 3 uF capacitor from node 1 to node 2; 6 ohm and 3 ohm from node 2 to ground. What is the time constant of this RC network?

- **A.** 3 us  
- **B.** 9 us  
- **C.** 15 us  
- **D.** 25 us

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q21. Maximum average power transfer to R

Circuit: j1 ohm inductor on the left branch, 3 ohm resistor connecting to a node with a 4∠0° A current source and a 6 ohm shunt resistor, then -j2 ohm in series to a variable resistor R. R is tuned till it absorbs the maximum average power. The maximum average power absorbed will be:

- **A.** 1.235 W  
- **B.** 2.451 W  
- **C.** 3.798 W  
- **D.** 7.285 W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q22. BJT self-bias emitter current

In an NPN amplifier circuit using self bias (voltage-divider R1, R2 at base, RC at collector, RE at emitter), base current IB = 300 uA and alpha = 0.98. Find emitter current IE. Answer ____ mA.

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q23. Marathon finishing order

Four runners (R1, R2, R3 and R4) completed a marathon. R1 finished before R4 but after R2. R2 finished after R3. Who finished the marathon first?

- **A.** R1  
- **B.** R2  
- **C.** R3  
- **D.** R4

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q24. Resistance seen at MOS source

For the MOS circuit (M1 with gate at Vin, drain to load ZL to VDD with Vout at drain, body grounded), the value of Rx seen looking into the source terminal will be (assume lambda = 0):

- **A.** 1/gmb  
- **B.** 1/gm  
- **C.** 1/(gm + gmb)  
- **D.** gm/(gm + gmb)

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q25. Average power in 5 ohm resistor

Circuit: -j4 ohm capacitor branch, j1 ohm inductor in series, 2∠0° A current source and a 5 ohm resistor in parallel. The average power absorbed by the 5 ohm resistor will be:

- **A.** 1.21 W  
- **B.** 5 W  
- **C.** 3.21 W  
- **D.** 2.64 W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q26. Equivalent impedance of AC network

Find the equivalent impedance Zeq of the linear passive network shown (elements: 2 ohm, 4 ohm, 8 ohm, j6 ohm, 5 ohm in series with -j5 ohm as a bridge, j2 ohm, -j4 ohm, 3 ohm, -j4 ohm).

- **A.** (16/5 + j14/15) ohm  
- **B.** (14/15 + j16/5) ohm  
- **C.** (14/15 - j16/5) ohm  
- **D.** (16/5 - j14/15) ohm

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q27. RC charging wait time

A heart rate monitoring device uses an RC circuit with R = 100 kohm and C = 1 uF. When a step input of 5 V is applied, the processing unit must wait until the capacitor charges to at least 3.15 V before triggering the next stage. How long must the system wait?

- **A.** 23 ms  
- **B.** 69 ms  
- **C.** 100 ms  
- **D.** 50 ms

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q28. BJT base drive current

A BJT is connected in common emitter mode and operated in the active region with collector current Ic = 1.01 mA. Common base current gain is 0.98 and reverse bias saturation current is 0.5 uA. What is the base drive current?

- **A.** 0.2 mA  
- **B.** 0.2 uA  
- **C.** 0.22 uA  
- **D.** 0.3 uA

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q29. IC 555 astable charging vs discharging time

An IC 555 in astable multivibrator mode with RA = RB = 20 kohm and C = 1 pF, with a diode connected across RB. Pins: 1 and 8 supply, 2 trigger, 4 reset, 6 threshold, 7 discharge. The relation between charging and discharging time will be:

- **A.** Tcharging &lt; Tdischarging  
- **B.** Tcharging > Tdischarging  
- **C.** Tcharging = Tdischarging  
- **D.** Tcharging = 1/Tdischarging

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q30. Switched-capacitor effective resistance

A switched-capacitor circuit uses a 1 pF capacitor switched between input and virtual ground at a rate of 250 kHz. What is the effective resistance seen at the input?

- **A.** 4 Mohm  
- **B.** 400 kohm  
- **C.** 2 Mohm  
- **D.** 4 kohm

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q31. Power in 12 ohm resistor

Resistive network: 6 A current source with 2 ohm shunt, 1 ohm series (voltage Vx), 4 ohm to a node with 3 ohm || 6 ohm to ground, 1.2 ohm series, then 8 ohm and 12 ohm shunts. The power dissipated by the 12 ohm resistor will be:

- **A.** 1 W  
- **B.** 1.5 W  
- **C.** 1.92 W  
- **D.** 3.84 W

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q32. Op-amp RC capacitor voltage

An op-amp circuit with three resistors R and a capacitor C (capacitor at the non-inverting input, output fed back to the inverting input) has initial capacitor voltage v(0) = 5 V. For t > 0, the voltage across the capacitor v(t) will be (R = 10 kohm, C = 1 uF):

- **A.** e^(-100t/3) u(t) V  
- **B.** 2e^(-100t/3) u(t) V  
- **C.** 5e^(-100t/3) u(t) V  
- **D.** 10e^(-100t/3) u(t) V

<sub>Topics: Analog Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q33. Diode circuit output peak

A 1 mA current source from 10 V feeds output node Vo, then a 1 kohm resistor to a node connecting the anodes of D1 and D2; D1's cathode goes to V1 and D2's cathode goes to ground. If V1 is a 1 kHz, 5 V peak sine wave, the value of Vo,peak will be:

- **A.** 1 V  
- **B.** -1 V  
- **C.** 4 V  
- **D.** -4 V

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q34. Teachers in schools

Five teachers I, J, K, L and M teach in four different schools. M and K do not teach in DPS, L teaches in St. Paul's and I teaches in St. Xavier's. If two teachers out of the five teach in Model school, which school does M teach in?

- **A.** St. Paul's  
- **B.** St. Xavier's  
- **C.** Model School  
- **D.** Cannot be determined

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q35. Ripple factor of inductor filter

The output voltage across the load resistance of an inductor filter connected to a bridge rectifier shows a DC value of 25 V and a peak-to-peak ripple voltage of 1.5 V. Calculate the ripple factor.

- **A.** 0.03  
- **B.** 0.0173  
- **C.** 0.0208  
- **D.** 0.0375

<sub>Topics: Analog Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q36. 4:1 MUX output

A 4:1 MUX has input I0 = 0 (grounded) and I1 = I2 = I3 = 1, with select lines S1 = X and S0 = Y. Find the output f.

- **A.** XY  
- **B.** X'Y'  
- **C.** X+Y  
- **D.** X'+Y'

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q37. RTL toggle/load flip-flop final value

Verilog: module seq(input clk, reset, sel, d, output reg q); always @(posedge clk or posedge reset) if (reset) q &lt;= 1'b0; else if (sel) q &lt;= ~q; else q &lt;= d; endmodule (an equivalent VHDL version was also given). Starting from the reset state, inputs at four consecutive rising edges: edge 1: sel=0, d=1; edge 2: sel=1, d=0; edge 3: sel=1, d=1; edge 4: sel=0, d=0. What is the final value of q?

- **A.** 0  
- **B.** 1  
- **C.** X  
- **D.** Z

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q38. PROM size for dual mux selection logic

A digital control system for a smart irrigation unit uses dual 4-to-1 multiplexers: 4 soil moisture sensors (8-bit output each), 4 temperature sensors (8-bit output each), 2 control lines to select which sensor pair to read, and both multiplexers share the same control lines. If you implement the selection logic using a PROM that stores the control logic only, what is the minimum PROM size required?

- **A.** 64 bits  
- **B.** 128 bits  
- **C.** 256 bits  
- **D.** 512 bits

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q39. Setup slack (static timing analysis)

Tclk = 10 ns. CLK -> FF1 clock wire: tmin 1 ns, tmax 2 ns. FF1 tclk-q min 9 ns, max 11 ns. FF1 Q -> wire (1/2 ns) -> inverter (tmin 6 ns, tmax 9 ns) -> wire (1/2 ns) -> FF2 D. CLK -> FF2 clock path: wire (tmin 2, tmax 3 ns) -> buffer (tmin 5, tmax 9 ns) -> wire (tmin 2, tmax 3 ns). FF2 thold = 2 ns, tsetup = 4 ns. The setup slack will be:

- **A.** 26 ns  
- **B.** 21 ns  
- **C.** 5 ns  
- **D.** -5 ns

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q40. C macro/shift operator output

What will be the output? #include &lt;stdio.h> #define $ a #define _ b static int $, _; int main() { $ = _ = 2; printf("%d ", (fun(fun($, _), fun($, _)))); return 0; } fun(int $, int _) { $ = $ >>= _ &lt;&lt;= 2; return _; return $; }

- **A.** 32  
- **B.** 0  
- **C.** 8  
- **D.** Compile time error

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q41. BCD counter after 7 pulses

A BCD counter counts from 0000 to 1001 and then resets. If the counter is initially at 0110 (BCD) and receives 7 clock pulses, the final count will be ________ (BCD). Express your answer as a 4-digit binary number.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q42. C program output (digit-weighted sum)

What will be the output? int main() { int N = 1111101; int a = 2; int res = 0; while (N != 0) { res = res + (N % 10) * a; N = N / 10; a = a * 2; } printf("%d", res); }

- **A.** 250  
- **B.** 227  
- **C.** 251  
- **D.** Compile time error

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q43. Discrete-time system properties

A discrete-time system satisfies y[n] = 3x[n] - 2x[n-1]. Which property is true?

- **A.** Non-linear and time varying  
- **B.** Linear and time invariant  
- **C.** Non-linear but time invariant  
- **D.** Linear but unstable

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q44. 3-input NAND HIGH output count

A 3-input NAND gate has the input combinations ABC = 000, 001, 010, 011, 100, 101, 110, 111 applied sequentially. Count the number of times the output is HIGH (logic 1).

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q45. Letter pairs in PRECISE

How many such pairs of letters are there in the word 'PRECISE' which has as many letters between them (from both the sides) as in the alphabets from A to Z?

- **A.** 0  
- **B.** 1  
- **C.** 2  
- **D.** 3

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q46. Fixing WNS after place-and-route

An ASIC targeting 1 GHz has completed place-and-route. The timing report shows a worst negative slack (WNS) of -0.18 ns, while all other paths have positive slack. RTL simulation, synthesis and logical equivalence checking have passed. The RTL architecture is frozen and functional changes are not permitted. Which action is most appropriate to improve timing with the least impact on functionality?

- **A.** Re-optimize placement and routing around the failing path while preserving logic functionality.  
- **B.** Relax the clock uncertainty so that setup analysis becomes less pessimistic.  
- **C.** Increase the drive strength uniformly across every standard cell in the design.  
- **D.** Replace all flip-flops on the failing path with lower setup-time library cells.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q47. Flip-flop type realized by SR circuit

A circuit with input X and feedback from Q/Q' through two inverters and two AND gates into an OR gate, whose output drives AND gates (gated with Q and Q') feeding the S and R inputs of a clocked SR flip-flop. The type of flip-flop realized will be:

- **A.** D Flip Flop  
- **B.** T Flip Flop  
- **C.** JK Flip Flop where J = K = X  
- **D.** None of these options

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q48. Synchronous counter 0-3-1-2

The correct implementation of a synchronous counter for the count sequence 0 -> 3 -> 1 -> 2 -> 0 will be:

- **A.** two D flip-flops with D1 fed back from Q1-related wiring and D0 driven by an XOR gate  
- **B.** same as A but with an XNOR gate driving D0  
- **C.** two T flip-flops with T1 = 0 and T0 = Q1'  
- **D.** two T flip-flops with T1 = 1 and T0 = Q1 (options were circuit diagrams)

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q49. PROM size for traffic light FSM

A traffic light controller uses a PROM to store the next state logic. Inputs: 3 state bits + 2 sensor inputs + 1 timer input (6 inputs). Outputs: 3 next state bits + 6 traffic light control bits (9 outputs). Calculate the minimum PROM storage capacity required.

- **A.** 288 bits  
- **B.** 576 bits  
- **C.** 864 bits  
- **D.** 1152 bits

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q50. Microcontroller loop count

Pseudocode: count = 0; while (count &lt; 5) { if (INPUT == HIGH) count = count + 2; else count = count + 1; } If INPUT remains HIGH throughout the execution, what will be the final value of count?

- **A.** 4  
- **B.** 5  
- **C.** 6  
- **D.** 7

<sub>Topics: Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q51. 8086 assembly CX value

MOV AX, 0005H; MOV BX, 0003H; MOV CX, 0000H; L1: ADD CX, AX; DEC BX; JNZ L1; SUB CX, 0004H. What will be the final value of the CX register?

- **A.** 000BH  
- **B.** 000FH  
- **C.** 0011H  
- **D.** 0015H

<sub>Topics: Digital Electronics, Code Output (C/C++/Java/Python) · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q52. Norton to Thevenin conversion

Circuit: current source Isc in parallel with r, load R across terminals A-B. If the Norton current and resistance are 6 A and 4 ohm respectively, what are VTh and RTh?

- **A.** VTh = 2 V, RTh = 1.5 ohm  
- **B.** VTh = 24 V, RTh = 1.5 ohm  
- **C.** VTh = 1.5 V, RTh = 1.5 ohm  
- **D.** VTh = 24 V, RTh = 4 ohm

<sub>Topics: Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q53. CMOS 3-input NAND delay with parasitics

A 3-input CMOS NAND gate (PMOS P1-P3 in parallel, NMOS N1-N3 in series) is shown with parasitic capacitances Ca, Cb, Cc at internal nodes and Cp+load at the output. Determine the total time difference (delay) of the NAND gate when Ra = 0.5K, Rb = 2K, Rc = 1K, Ca = 1 uF, Cb = 1.5 uF, Cc = 0.3 uF and Cpload = 0.2 uF.

- **A.** 6.5 msec  
- **B.** 10.5 msec  
- **C.** 16.5 msec  
- **D.** 9.1 msec

<sub>Topics: Digital Electronics, Circuits · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q54. Minterm expression equivalence

Consider F(w, x, y, z) = Σ(0, 3, 5, 6, 7, 9, 10, 11, 12, 14, 15). F can be expressed as (no need to simplify):

- **A.** Π(1,2,4,8,13) + (w'x'y'z + w'x'yz' + w'xy'z' + wx'y'z' + wxy'z)  
- **B.** Σ(1,2,4,8,13) - Π(0,3,5,6,7,9,10,11,12,14,15)  
- **C.** Σ(0-15) - Π(1,2,4,8,13)  
- **D.** Π(0-7) + Σ(0-7) - Σ(1,2,4,8,13)

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q55. Aliasing when sampling at 30 kHz

A sensor signal contains frequency components up to 18 kHz. An engineer samples the signal at 30 kHz without using an anti-aliasing filter. Which statement is correct?

- **A.** All frequency components are reconstructed correctly.  
- **B.** Frequencies above 15 kHz will alias into the sampled spectrum.  
- **C.** Aliasing occurs only if the sampling frequency is below 18 kHz.  
- **D.** Increasing the ADC resolution eliminates aliasing.

<sub>Topics: Signals & Systems · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q56. Piggy bank savings of five friends

Five friends - Rohan, Sia, Tanu, Varun and Zoya - save money in their piggy banks. Together they save Rs 1,150. Rohan saves Rs 150 more than Sia. Tanu saves twice as much as Sia. Varun saves the same amount as Rohan. Zoya saves Rs 50 less than Sia. How much does Tanu save?

- **A.** Rs 250  
- **B.** Rs 280  
- **C.** Rs 300  
- **D.** Rs 320

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q57. Ripple counter settling time

A 4-bit ripple counter using JK flip-flops has a propagation delay of 12 ns per flip-flop. When the counter transitions from 1111 to 0000, the maximum settling time is ________ ns.

<sub>Topics: Digital Electronics · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q58. Day of week after 15 days

If today is Wednesday, ________ will be the day of the week after 15 days. (fill in the blank)

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q59. Number arrangement machine

A number arrangement machine, when given an input line of numbers, rearranges them following a particular rule in each step. Illustration: Input: 531842, 764125, 902317, 648531, 287964, 413256. Step I: 8, 12, 3, 15, 21, 9. Step II: 15, 13, 19, 12, 15, 12. Step III: 289, 313, 370, 369, 666, 225. Step IV: 64, 353, 1. Step V: 10, 11, 1. Step V is the last step. As per the rules followed in the above steps, find the output for the input: 825431, 370962, 641528, 954210, 718346, 260871. Step V of the above input is ________.

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

### Q60. Streaming plan subscribers

A U.S. streaming service offers three plans: Basic at $15, Standard at $25 and Pro at $45 per month. There are 600 subscribers in total, and the average monthly revenue per subscriber is $26. Also, the number of Pro subscribers is 60 less than the number of Basic subscribers. How many Standard subscribers are there?

- **A.** 280  
- **B.** 340  
- **C.** 320  
- **D.** 300

<sub>Topics: Aptitude · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/10827-Texas_Instruments_All_60_Questions.pdf) · Also asked at: BITS Pilani ×2 (last 2026-10-08)</sub>

## 2026-10-08 · IIT Bombay · FTE

### Q1. Pens on a shelf ordering

There are four pens: a red pen, a black pen, a green pen and a blue pen. The pens need to be kept in a shelf from left to right. The red pen should be on the left. The black pen should be kept just after the red pen and the blue pen should be on the right. The green pen should be on the left of the blue pen but on the right of the black pen. Which of the following pen is kept on the left of the black pen?

A. Red
B. Green
C. Blue
D. Cannot be determined

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q2. Three men building a wall

Three men P, Q and R working individually take 12 days, 15 days and 20 days respectively to construct a wall. Find the minimum time required to construct a wall if not more than 2 men are working together on a day and no same pair of men work on two consecutive days.

A. 6.5 days
B. 7 days
C. 7.5 days
D. 8 days

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q3. Event schedule with slots

A management club has 5 distinct technical activities and 4 distinct strategy activities. For a short event, exactly 2 technical activities and exactly 1 strategy activity must be selected. The selected 3 activities will be conducted in three distinct slots: Slot 1, Slot 2, and Slot 3. The strategy activity must not be conducted in Slot 1. In how many ways can the event schedule be prepared?

A. 120
B. 140
C. 160
D. 180

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q4. Number of triangles in grid figure

A 5x5 square grid figure with its main diagonal drawn (top-left to bottom-right) is shown. What is the number of triangles in the figure?

A. 30
B. 27
C. 20
D. 15

(Figure not reproduced.)

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q5. Probability three books together

15 books are placed on a table. The probability that three of the books will always be together is x/y. The value of x is 1 and the value of y is __________ .

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q6. Queue of doctors

In a queue of more than 10 doctors, Dr. A is 9th from the left end and Dr. B is 3th from the right end, there are three doctors between Dr. A and Dr. B. A total of __________ doctors are there in the queue.

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q7. Football players team selection

Seven football players namely Gaurav, Harsh, Kunal, Lalit, Manish, Naman and Ojha are to be selected for one of the college teams, the Phoenix and the Devils.

- If Gaurav is selected for the Phoenix, then Harsh will be selected for the Devils
- If Kunal is selected for the Phoenix, then Lalit and Manish will be selected for the Devils.
- Naman is selected on a different team than Ojha.
- Manish is selected on a different team than Gaurav.
- If Ojha is selected for the Phoenix, then Harsh will also play for the Phoenix.

Which of these could be a complete and accurate list of players in the Phoenix team?

A. Gaurav, Kunal, Ojha
B. Harsh, Manish, Naman, Ojha
C. Kunal, Harsh, Lalit, Ojha
D. Lalit, Manish, Naman

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q8. Painter average daily earnings

A painter is paid x rupees for painting every 10 metres of a wall and y rupees for painting every extra metre. During one week, he painted 10 metres on Monday, 13 metres on Tuesday, 12 metres on Wednesday, 11 metres on Thursday, and 12 metres on Friday. What is his average daily earnings in rupees for the five - day week?

A. x + (8/5)y
B. (5x + 9y)/5
C. 10x + (8/5)y
D. 5x + 8y

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q9. Speeds of A, B, C, D

The difference between A's speed and B's Speed is 3km/hr. C's speed is twice as that of A and B's speed is twice as that of D. the difference between C and D speed is 30km/hr. The speed of B is:

A. 18 km/hr
B. 19 km/hr
C. 21 km/hr
D. 24 km/hr

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q10. Two dice sum is 5

Two dice are thrown simultaneously, What is the probability that the sum of the numbers shown on the two dice is 5?

A. 1/6
B. 1/9
C. 2/27
D. 1/12

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q11. Alphanumeric sequence completion

Which of the following will come in place of the question mark (?) in the following sequence so that it completes the sequence?

L12QK, MS10I, NUG8, O6WE, (?)

A. P4YC
B. PY4C
C. PYC4
D. PW4C

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q12. Photograph blood relation

Pointing to a photograph Rita, said "he is the son-in-law of the grand mother of my father's father's only son". How is Rita's father related to the wife of the man in photograph?

A. Son-in-law
B. Brother-in-law
C. Nephew
D. Brother

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q13. Seating arrangement in a row

Arpita, Purna, Rina, Xola, Sofia and Zain are sitting in a row. Sofia and Zain are in the center. Arpita and Purna are at the ends. Rina is sitting just to the left of Arpita. __________ is to the immediate right of Purna.

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q14. Rest of the 60-question paper

The shared PDF contains 60 questions in total (aptitude and technical); only the first 20 are transcribed here.

<sub>Topics: OA Format · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q15. Marathon runners finishing order

For runners (R1, R2, R3, and R4) completed a marathon. R1 finished before R4 but after R2. R2 finished after R3. Who finished the marathon first?

A. R1
B. R2
C. R3
D. R4

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q16. Teachers in schools

Five teachers I, J, K, L and M teach in four different schools. M and K do not teach in DPS, L teaches in St. Paul's and I teaches in St. Xavier's. If two teachers out of the five teach in Model school, which school does M teach in?

A. St. Paul's
B. St. Xavier's
C. Model School
D. Cannot be determined

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q17. Letter pairs in PRECISE

How many such pairs of letters are there in the word 'PRECISE' which has as many letter between them (from both the sides) as in the alphabets from A to Z?

A. 0
B. 1
C. 2
D. 3

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q18. Five friends piggy bank savings

Five friends - Rohan, Sia, Tanu, Varun, and Zoya - save money in their piggy banks.

- Together, they save ₹1,150.
- Rohan saves ₹150 more than Sia.
- Tanu saves twice as much as Sia.
- Varun saves the same amount as Rohan.
- Zoya saves ₹50 less than Sia.

How much does Tanu save?

A. ₹250
B. ₹280
C. ₹300
D. ₹320

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q19. Day of week after 15 days

If today is Wednesday, __________ will be the day of the week after 15 days.

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q20. Number arrangement machine

A number arrangement machine, when given an input line of numbers, rearranges them following a particular rule in each step. Illustration:

```
Input:    531842 764125 902317 648531 287964 413256
Step I:   8 12 3 15 21 9
Step II:  15 13 19 12 15 12
Step III: 289 313 370 369 666 225
Step IV:  64 353 1
Step V:   10 11 1
```

Step V is the last step. As per the rules followed above, find the output for the input below.

```
Input: 825431 370962 641528 954210 718346 260871
```

Step V of the above input is __________ .

<sub>Topics: Aptitude, Puzzles · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>

### Q21. Streaming plans subscribers

A U.S. streaming service offers three plans: Basic at $15, Standard at $25, and Pro at $45 per month. There are 600 subscribers in total, and the average monthly revenue per subscriber is $26. Also, the number of Pro subscribers is 60 less than the number of Basic subscribers. How many Standard subscribers are there?

A. 280
B. 340
C. 320
D. 300

<sub>Topics: Aptitude, Math · Source: [Texas_Instruments_All_60_Questions.pdf](../archive/files/8232-Texas_Instruments_All_60_Questions.pdf)</sub>
