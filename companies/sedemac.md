# Sedemac

**39 questions** from 2 OA drives · seen at IIT Roorkee, NIT Surathkal · latest 2026-10-11

**Topics:** [Mechanical](../topics/mechanical.md) (17) · [Circuits](../topics/circuits.md) (14) · [Math](../topics/math.md) (10) · [Control Systems](../topics/control-systems.md) (5) · [Signals & Systems](../topics/signals-systems.md) (4) · [Analog Electronics](../topics/analog-electronics.md) (4) · [Code Output (C/C++/Java/Python)](../topics/code-output-c-c-java-python.md) (3) · [Aptitude](../topics/aptitude.md) (3) · [OA Format](../topics/oa-format.md) (1) · [Guesstimates & Cases](../topics/guesstimates-cases.md) (1)

**Drives:**

- [2026-10-11 · IIT Roorkee · FTE · Electronics Engineer](#2026-10-11--iit-roorkee--fte--electronics-engineer) · 38 questions
- [2026-10-06 · NIT Surathkal · FTE · Embedded Software](#2026-10-06--nit-surathkal--fte--embedded-software) · 1 question

[← all companies](../README.md#companies)

---

## 2026-10-11 · IIT Roorkee · FTE · Electronics Engineer

### Q1. Steady-state voltage at node A in RC network

Consider the circuit (Vbat in series with R and C, then 4R and 3C to ground, node A between C and 4R). Suppose Vbat is 20V, R is 5 ohm and C is 10 mF. What will be the steady-state voltage at node A?

A. 0V
B. 4V
C. 5V
D. 15V
E. 16V
F. 20V

<sub>Topics: Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q2. Isometric view from top and front views

Choose the correct isometric view of the part whose top and front views are shown (an engineering drawing with dimensions such as 110, 40, 25, R25, 30R, 50, 10). Options are isometric images of the part.

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q3. Steady-state pressure drop across relief valve with piping

A hydraulic device, a Relief valve, has a pressure P vs flow Q characteristic as shown in a graph. This is typical of pressure relief valves, which do not allow the pressure drop to exceed a certain limit. The relief valve is connected in a hydraulic circuit where a pump delivers fluid at a constant pressure of 10 bar above atmospheric pressure. The piping system is assumed to have a pressure-flow relationship given by Q = P/2. Assume the relief valve discharges the fluid into a tank at atmospheric pressure (1 bar). What value will the steady-state pressure drop across the relief valve have?

A. 2
B. 4
C. 6
D. 9

(The P-Q graph is not transcribed.)

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q4. Pressure drop across relief valve with orifice

Same relief valve and circuit as the previous question. Now suppose the piping section is replaced by an orifice whose pressure-flow relationship is given by Q = √(P/8). What will be the new value for the steady-state pressure drop across the relief valve?

A. 2
B. 4
C. 6
D. 9

(The P-Q graph is not transcribed.)

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q5. ABS braking: where to brake harder on road 1 (curve C1)

The graphs C1 and C2 show the amount of braking (retarding force F) as a function of wheel slip for a vehicle on two different roads. Slip is defined as (v_vehicle − v_wheel_speed)/v_vehicle, expressed as a percentage. v_vehicle is the true speed of the vehicle, while v_wheel_speed is the speed computed from the rotational speed of the wheels. Increased braking by the driver (braking harder) increases slip.

On road 1 where graph C1 is applicable (C1 rises to a peak near S1 and then falls), the driver finds him/herself in two situations. In one case the vehicle slip is S1 and in the other case the slip is S2. The driver wants to stop the vehicle in as short a distance as possible. In both cases, the initial braking applied by the driver is about 25% of the maximum braking possible. In which situation should s/he brake harder?

A. S1 and S2
B. S1 but not S2
C. S2 but not S1
D. Neither S1 nor S2

<sub>Topics: Mechanical, Control Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q6. ABS braking: where to brake harder on road 2 (curve C2)

Same setup as the previous question (curves C1 and C2 of braking force F vs slip, slip points S1 and S2, initial braking about 25% of maximum). Now suppose the tire and road materials are such that graph C2 (monotonically increasing, flattening out) is applicable. Once again, in which situation should s/he brake harder?

A. S1 and S2
B. S1 but not S2
C. S2 but not S1
D. Neither S1 nor S2

<sub>Topics: Mechanical, Control Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q7. Expected output of random() product program

A function random() generates a random number with a uniform probability distribution between −1 and +1 (density 0.5). Consider the pseudo-language program with C-like syntax (all variables are floating-point numbers):
```
Y = 0
for (a = 0; a < 1000000; a++)
{
    X1 = random()
    X2 = random()
    Y = Y + X1*X2
}
Y = Y/1000000
print(Y)
```
What is the (approximate) output expected from the program?

A. 0
B. 1/4
C. 1/3
D. 1/2

<sub>Topics: Math, Code Output (C/C++/Java/Python) · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q8. Expected output of random() squared program

A function random() generates a random number with a uniform distribution between −1 and +1. Consider another program:
```
Y = 0
for (a = 0; a < 1000000; a++)
{
    X = random()
    Y = Y + X*X
}
Y = Y/1000000
print(Y)
```
What is the (approximate) output expected from this program?

A. 0
B. 1/4
C. 1/3
D. 1/2

<sub>Topics: Math, Code Output (C/C++/Java/Python) · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q9. Expected output of random() with abs() program

A function random() generates a random number with a uniform distribution between −1 and +1. Consider another program that defines:
```
function abs(x) {
    If x > 0
        return x
    else
        return -x
}
```
followed by a loop of 1000000 iterations accumulating into Y and then dividing by 1000000 (the rest of the program is cut off in the screenshot). What is the (approximate) output expected from this program?

A. 0
B. 1/4
C. 1/3
D. 1/2

<sub>Topics: Math, Code Output (C/C++/Java/Python) · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q10. Thermistor divider: where is confidence in readings higher

Thermistors are typically used as temperature sensors by leveraging their temperature-dependent resistance. The figure shows the qualitative change in resistance Rt of a thermistor as a function of temperature (decreasing, convex curve). One interfacing method is a resistor divider between 5V: Rt on top and Ro (fixed) below, with the midpoint going to an ADC. Suppose we use an ADC with infinitely good resolution. In which temperature range will you prefer operating the thermistor to have greater confidence in the sensor measurement readings (purely because of temperature vs resistance characteristics of the thermistor)?

A. At high temperatures
B. At low temperatures
C. No such preference.
D. Confidence on temperature sensor readings should be similar at all temperature ranges

<sub>Topics: Analog Electronics, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q11. Estimate temperature from ADC counts for thermistor divider

Thermistor divider as above (5V, Rt on top, Ro to ground, midpoint to ADC). Assuming Ro = 1 kohm and Rt = 4 kohm at 25 degC and Rt = 2 kohm at 50 degC with a fairly linear characteristic between 25 degC and 50 degC, what is the estimated temperature if ADC counts is measured as 256 with 10 bit resolution between 0 - 5V?

A. 30 degC
B. 32.5 degC
C. 35 degC
D. 37.5 degC
E. 40 degC

<sub>Topics: Analog Electronics, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q12. Charge through 10 ohm resistor in infinite capacitor ladder

Consider the hypothetical circuit formed by an infinite ladder of 1 mF and 2 mF capacitors (series 2 mF capacitors, shunt 1 mF capacitors), a 12V source, a switch and a 10 Ohm resistor. Suppose all capacitors are initially discharged and at time t = 0 the switch is turned ON. What is (roughly) the amount of charge that will pass through the 10 ohm resistor in a duration of 1 second?

A. 0 mC
B. 3 mC
C. 4 mC
D. 8 mC
E. 12 mC
F. Infinite

<sub>Topics: Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q13. Thermistor in place of Ro: change in resolution

In reference to the previous question, if Ro in the circuit is replaced with Rt, such that the two thermistors are effectively in series, with both thermistors reading the temperature of the same object, how would the equivalent temperature measurement resolution change with respect to the previous configuration?

A. Resolution increases
B. Resolution remains same
C. Resolution reduces
D. Not enough information
E. ADC counts no longer have any correlation with temperature

<sub>Topics: Analog Electronics, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q14. Transformer with triangular current input: output voltage

A transformer with 1:1 turns ratio is shown. The primary side is powered by a current signal generator, while the secondary side voltage is monitored by an oscilloscope. Assume an ideal transformer with no leakage flux and no core saturation. The current source pumps in a triangular-wave current as shown in the adjacent figure. How will the voltage measured at output look like?

A. Square waveform with zero average voltage
B. Square waveform with positive average voltage
C. Square waveform with negative average voltage
D. Triangular waveform with zero average voltage
E. Triangular waveform with positive average voltage

<sub>Topics: Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q15. Heat dissipation in resistor with anti-parallel diodes

In the circuit shown, ideal diodes with forward drop of 0.7V and 100V breakdown voltage in reverse direction are used, in anti-parallel as shown, in series with a 10 ohm resistor R31 (unit IC5, 0.7V drop in either direction). The waveform of the voltage source with peak-to-peak voltage of 12V (Vpp = 12V, Freq = 10Hz) is a ±6V square wave as shown in the adjacent graph. What would be the heat dissipation in the unit IC5 in the circuit shown?

A. 371 mW
B. 840 mW
C. 565 mW
D. 791 mW

<sub>Topics: Circuits, Analog Electronics · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q16. Maximum Vout of voltage divider with resistor tolerances

Consider a voltage divider circuitry as shown. A 5V battery feeds R20 (1K, ±1.0%), R22 (1K, ±5.0%) and R24 (1K, ±0.1%) in series, then R25 (3.6K, ±0.1%) to ground; Vout is across R25. The tolerance of each resistor is mentioned in the circuit schematic. What would be the maximum value of Vout in this circuitry?

A. 2727 mV
B. 2743 mV
C. 2701 mV
D. 2754 mV
E. 2783 mV

<sub>Topics: Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q17. Voltage induced across an inductor from I-t graph

Consider an inductor L = 30 mH through which current flows as per the shown graph (I in Amp vs t in sec, a straight line through roughly (2,3), (4,6), (6,9), (10,15)). What is the value of voltage induced across the inductor?

A. 15 mV
B. 2 mV
C. 20 mV
D. 45 mV

<sub>Topics: Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q18. Steady-state temperature of resistor in oil tub

A resistor powered by a battery is immersed in a metallic oil tub. The ambient temperature around the system is maintained at a steady 25 degC. Thermal radiation of the resistor and oil tub combination has been empirically approximated using the formula Power dissipated = 4(T − Ta)², where Ta is the ambient temperature (25 degC). The system radiates heat from all sides (from oil surface as well as from the metallic oil tub). With a battery voltage of 10V and resistor value of 1 ohm, estimate the steady state temperature of the oil tub.

A. 26 degC
B. 28 degC
C. 30 degC
D. 32 degC
E. 34 degC

<sub>Topics: Circuits, Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q19. Thermal coefficient of resistance of the resistor in oil tub

Continuing the oil tub problem above (power dissipated = 4(T − Ta)², Ta = 25 degC, 10V battery): experimental results suggested that the estimated temperature does not match the observed value as the thermal coefficient of resistance was not accounted for. The experimental steady state temperature was observed as 29 degC. Assuming the resistor value was 1 ohm at 25 degC, what is the likely "average" value of the thermal coefficient of the resistor between 25 degC and 29 degC? Resistor variation with temperature can be assumed as R = 1Ω × (1 + θ ΔT_degC), where θ is the thermal coefficient of the resistor and ΔT_degC is the extra temperature on top of 25 degC.

A. 0.14 ohm/degC
B. 0.16 ohm/degC
C. 0.18 ohm/degC
D. 0.20 ohm/degC
E. 0.24 ohm/degC

<sub>Topics: Circuits, Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q20. Unique doubles badminton matches with 7 players

Every badminton doubles match has participation of 4 players, with 2 players in one team and the other 2 players in the other team. Consider a group of 7 players who regularly play badminton. How many unique combinations of doubles matches can happen with 7 players? For example, when players P, Q, R, S play a doubles match, the configuration "P, Q vs R, S" is the same as "Q, P vs R, S" but different than "P, R vs S, Q".

A. 21
B. 105
C. 126
D. 42

<sub>Topics: Math, Aptitude · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q21. Average matches played per player in one hour of court

Every badminton doubles match has 4 players, 2 in each team. Consider a group of 7 players who regularly play badminton. Suppose each doubles match lasts 10 mins, and the total duration for which the players have booked a badminton court is 1 hour. What is the expected value of average matches played by each player?

A. 4.00
B. 1.71
C. 3.43
D. 3.82
E. 2.86

<sub>Topics: Math, Aptitude · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q22. Waveform with highest RMS value

Which of the below waveforms has the highest RMS (root mean square) value? Only one period of the waveform is shown, but for the purpose of the analysis, consider periodic waveforms running from −infinity to +infinity.

Options include: a sine wave of amplitude √2·x, a square wave of amplitude x (positive and negative halves), a sine wave of amplitude 1.5x, and more (cut off in the screenshot).

<sub>Topics: Signals & Systems, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q23. Steady-state voltage with proportional regulator on RC

In the circuit (supply U in series with R and capacitor C), the supply voltage U is updated with the intention of maintaining the value across the capacitor as y0. A Proportional regulator (only the P regulator of the PID regulator) is used with the control law `U = K × (y0 − y)`, where y is the instantaneous voltage across the capacitor. What will be the steady-state voltage value at node y?

A. y0
B. y0 × k/(k+1)
C. y0 × 2k/(2k+1)
D. 0V
E. Depends on values of R and C

(An option may be cut off in the screenshot.)

<sub>Topics: Control Systems, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q24. Estimate total functional two-wheelers in India

Suppose 2 Cr scooters are sold in India annually. Let us make a simplistic assumption that life of each two-wheeler is 10 years. Suppose the number of two-wheelers sold per year has stabilized to 2 Cr and the market is not growing. What is a good estimate for total number of functional two-wheelers in India?

A. 2 Cr
B. 10 Cr
C. 20 Cr
D. 24 Cr
E. Insufficient information to make any reasonable guess

<sub>Topics: Guesstimates & Cases, Aptitude · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q25. Motor lifetime when speed ramps linearly

An electric motor's life has been characterized at different speeds. The analytical expression for life in hours as a function of speed is roughly Life = 8,000,000/Speed. For example, if the motor is operated continuously at 8000 RPM, the motor breaks down after about 1000 hours. Suppose the motor is operated such that its speed is linearly increased from 0 RPM to indefinitely high speeds at a rate of 100 RPM per hour (i.e., after 1 hour the motor's speed will be 100 RPM, after 2 hours 200 RPM, ...). The rest of the question (likely asking at what speed the motor will fail) is cut off in the screenshot.

A. 20,000 RPM
B. 40,000 RPM
C. 60,000 RPM
D. 80,000 RPM

<sub>Topics: Mechanical, Math · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q26. Expected motor lifetime under a drive cycle

An electric motor's life is roughly Life = 8,000,000/Speed (hours, with speed in RPM); e.g. at 8000 RPM it breaks down after about 1000 hours. Suppose the motor is subjected to the drive cycle shown in a graph (not visible in the screenshot). What is the expected lifetime of the motor?

A. 1600 hours
B. 2048 hours
C. 3200 hours
D. 4096 hours

<sub>Topics: Mechanical, Math · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q27. Planetary gear tooth relation between sun, planet and ring

Consider a cylindrical volume in space defined by diameter D = 120 mm and axial length L = 12 mm. It is required to design a planetary gear system which can be housed in the defined volume. The input power is provided at the sun gear and output is taken from the ring while the centers of the three planets are held fixed. Some external design constraints dictate that the shaft rotating the sun must have a minimum diameter of 20 mm. If the sun, planet and ring have m, n and k teeth respectively, which of the following relations hold true?

A. m + n = k
B. m + 2n = k
C. 2m + n = k
D. 2m = k + n

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q28. Planetary gear combination for maximum speed reduction

Same planetary gear setup (D = 120 mm, L = 12 mm, input at sun, output at ring, three planets with fixed centers, sun shaft minimum diameter 20 mm). Which amongst the following gear teeth combinations for sun, planet and ring respectively provide the maximum speed reduction ratio, while respecting the constraints mentioned?

A. 23, 59, 141
B. 25, 58, 141
C. 23, 46, 115
D. 21, 50, 122

<sub>Topics: Mechanical, Math · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q29. Vibration level felt by motorbike rider

The seat of a motor bike, with the rider, weighs M = 100 Kg and is found to have a static deflection of 250/169 mm under the self-weight. The vibration of the engine is transmitted to the base of the seat as harmonic motion with frequency 12 Hz and amplitude 1 mm. Assume g = 10 m/s² and π = sqrt(10). Feel free to assume the lump model as shown (mass M on a spring). What is the level of vibration felt by the rider?

A. 6.76 mm at 12 Hz
B. 8.45 mm at 13 Hz
C. 6.76 mm at 13 Hz
D. 8.45 mm at 12 Hz

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q30. Which change guarantees reduced vibration of the seat

Same motorbike seat setup (M = 100 Kg, static deflection 250/169 mm, base vibration 12 Hz and 1 mm amplitude, g = 10 m/s², π = sqrt(10)). Which of the following will guarantee reducing the effect of vibration?

1. Increase stiffness of the seat
2. Reduce weight of the seat
3. Decrease stiffness of the seat
4. Increase weight of the seat

A. Both 1 and 4
B. Both 2 and 3
C. Both 1 and 2
D. None of statements

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q31. Periscope mirror angle with tolerances

Consider a periscope-like system consisting of two plane mirrors M1 and M2. The base length of the mirrors along with the tolerance in them is √2h ± ΔL. The points P1 and P2 where the two mirrors are mounted on the vertical walls are also shown with tolerance (h ± Δh). Assume that both the vertical walls are parallel, and all other features of the system are exact. An illuminated object is kept at infinity in front of the periscope. Choose the correct description of the angle (in rad) made by the mirrors with the horizontal wall? [For calculation assume that the tolerance values are very small in comparison to the base dimensions.]

A. π/4 ± (1/(√2 h))(√2 Δh + ΔL)
B. π/4 ± (1/(√2 h))(√2 Δh − ΔL)
C. π/4 ± (1/(√2 h))(Δh + ΔL)
D. π/4 ± (1/h)(√2 Δh + ΔL)

<sub>Topics: Mechanical, Math · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q32. Periscope system: which statements hold (cut off)

Same periscope-like system of two plane mirrors M1 and M2 with tolerances (base length √2h ± ΔL, mounting points h ± Δh, parallel vertical walls, object at infinity). The question asks which of a numbered list of statements (1 to 6) are true. The statements are not visible in the screenshot.

A. 2 & 4
B. Only 3
C. 1 & 3
D. 5 & 6
E. Only 6

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q33. Qualitative capacitor waveform under P control

Same circuit and control law as above (`U = K × (y0 − y)`, P regulator, supply U driving R and C). What will be the qualitative nature of the waveform across the capacitor?

Options are waveform graphs: (1) smooth exponential rise to a steady value, (2) rise with small sustained ripples, (3) rise with overshoot and decaying oscillation, (4) exponential decay.

<sub>Topics: Control Systems, Circuits · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q34. Steady-state speed of motor driving a fan

A motor is driving a fan. The motor's torque-vs-speed characteristic is a straight line from torque τ0 at zero speed to zero torque at speed ω0. The fan's load torque has a quadratic relationship with speed, τ = k × ω², reaching 2 × τ0 at speed ω0. What will be the steady-state operating speed of the motor?

A. ω0/4
B. ω0/3
C. ω0/2
D. 2ω0/3
E. 3ω0/4
F. (one more option cut off in the screenshot)

<sub>Topics: Mechanical, Control Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q35. Steady-state output of first-order digital filter with step input

A micro-controller based system is sensing an input signal on its analog-to-digital converter and implementing a filter `y_k = α·x_k + β·y_{k-1}` with y_0 = 0 as the initial condition. The input samples are of constant value 1 (k = 1, 2, 3, ...). Suppose α = 1 and β = 0.5. What will be the steady-state value of y for large values of k?

A. 0.5
B. 1
C. 1.5
D. 2

<sub>Topics: Signals & Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q36. Digital filter response to impulse input at k=10

A micro-controller based system implements the filter `y_k = α·x_k + β·y_{k-1}` with y_0 = 0 as the initial condition. The input is an "impulse": x = 1 at k = 5 and 0 at all other samples. Suppose α = 0.5 and β = 2. What will be the value of y for k = 10?

A. 16
B. 12
C. 8
D. 4

<sub>Topics: Signals & Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q37. Pick the graph of the integral F(x) of f(x)

Consider the plot of f(x) versus x: a piecewise-linear curve between x = −5 and x = +5, going down to −2 around x = −2.5 to 0, rising through 0 to +2 and then falling back to 0 at x = +5. Suppose F(x) = ∫ from −5 to x of f(y) dy. Which one of the following is a graph of F(x)?

Options are four graphs of F(x) (curves with various dips and humps). The graphs are not transcribed.

<sub>Topics: Math, Signals & Systems · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

### Q38. Velocity vs time graph of body thrown upward

A body is thrown vertically upwards. Which one of the following graphs correctly represents the velocity vs time?

Options are graphs of v vs t. The graphs are not transcribed.

<sub>Topics: Mechanical · Source: [SEDMAC_IITR_New.pdf](../archive/files/5089-SEDMAC_IITR_New.pdf)</sub>

## 2026-10-06 · NIT Surathkal · FTE · Embedded Software

### Q1. Sedemac OA pattern (Embedded software)

Round 1 is Aptitude + reasoning. Round 2 contains 2 coding questions in C and the rest 13-15 MCQs based on Embedded C and core ECE. This was for the Embedded software role.

<sub>Topics: OA Format · Source: [chat, 6 Oct](../archive/silicon-labs-oa/2026-10.jsonl#L3), [chat, 6 Oct](../archive/silicon-labs-oa/2026-10.jsonl#L4), [chat, 6 Oct](../archive/silicon-labs-oa/2026-10.jsonl#L5)</sub>
