# Qualcomm OA

## 2026-10-13 · IIT Delhi · Intern

### Q1. Glucose solution dilution

A 40% glucose (C6H12O6) solution is first diluted with water to make a 32% solution (assume volumes add). This 32% solution is then mixed with a 20% glucose solution to obtain 50 L of a 26% glucose solution. How many litres of the original 40% solution were used? Options: 16 L, 20 L, 18 L, 24 L. (Compiled answer: 20 L)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q2. Array vs stack difference

Which option correctly states the difference between an array and a stack? Options: Array is an ordered collection of items and stack is not; Array may contain different data types and stack contains the same data type; Array obeys the FIFO rule and stack uses LIFO; Array is a static object whereas stack is a dynamic object. (Compiled answer: the last option)

Topics: Stack/Queue, Arrays  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q3. Queue via a single stack: time complexity

Consider a queue implemented using a single stack. Enqueue(x): push x onto the stack. Dequeue: 1) if the stack is empty, error; 2) if the stack has only one element, return it; 3) otherwise recursively pop everything from the stack, store the popped item in a variable var, push var back onto the stack and return var. What is the time complexity of deleting an element from a stack of size n, followed by x insertions? Options: O(x*n), O(x), O(n), O(1). (Compiled answer: O(n))

Topics: Stack/Queue, Recursion/Backtracking  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q4. In-order predecessor of the root

What is the in-order predecessor of the root node in a complete binary tree with 7 nodes? Options: left child of the root; left child of the root's left subtree; right child of the root's left subtree; right child of the root. (Compiled answer: right child of the root's left subtree)

Topics: Trees  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q5. Bucket sort statements

Which statement(s) about bucket sort are true? I) It is a sorting technique that generalizes counting sort by partitioning an array into a finite number of buckets. II) It is best suited to data sets of a limited range. III) It uses the divide-and-conquer technique. Options: all of (I), (II) and (III); only (I) and (III); only (II); only (I). (Compiled answer: all three)

Topics: Sorting  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q6. Priority scheduling statements

Which statement(s) about the priority scheduling algorithm are correct? I) The algorithm provides a good mechanism to schedule processes properly as defined. II) Static priority keeps changing until the process completes its execution. III) Internal priority depends on system limits and memory requirements. Options: only (II) and (III); only (I) and (III); only (II); only (III). (Compiled answer: only (III))

Topics: OS/DBMS/CN MCQ  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q7. Smallest-hole allocation technique

Which allocation technique allocates the smallest hole among the free partitions in main memory? Options: Best Fit, Next Fit, Worst Fit, First Fit. (Compiled answer: Best Fit)

Topics: OS/DBMS/CN MCQ  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q8. I/O controller OS function

Which operating system function does an I/O controller belong to? Options: Process Management, Device Management, Memory Management, File Management. (Compiled answer: Device Management)

Topics: OS/DBMS/CN MCQ  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q9. C output: bitwise shift/mask

What is the output? int main(){ static int m = 4, n = 2; m <<= n | 3 & m; n = n >> 2 | m + 1 << n - 1; printf("%d  %d", m, n); return 0; } Options: 16 34, 0 13, 16 12. (Compiled answer: 16 34)

Topics: Bit Manipulation, Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q10. C output: printf format mismatch

What is the output? int main(void){ int a = 1.00; int b = -2.22; printf("%.2f  %d ", --b, --b); printf("%.2f  %d", -a, -a<<1); return 0; } Options: 0.00 -4 0.00 -4; -3.22 -4 -2.00 -3; -3.22 -4 0.00 -4; compile-time error. (Compiled answer: 0.00 -4 0.00 -4)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q11. C error finding: array pointer

Which line(s) generate errors? int main(){ int array[] = {2, 4, 6, 8, 5, 7}; int *ar = array + 3; ++*ar += 1; printf("%d ", --(array[1 + 3])); /* Line 1 */ printf("%d", (array[!1]) + 2); /* Line 2 */ return 0; /* Line 3 */ } Options: Line 1, Line 2 and Line 3; no error in the program; Line 2 and Line 3; Line 1. (Compiled answer: no error)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q12. Shopkeeper markup and discount

A shopkeeper marks an item 40% above the cost price. He allows a 10% discount on the marked price and still earns a profit of ₹126. What is the cost price of the item? Options: ₹484.62, ₹472.68, ₹512.26, ₹562.88. (Compiled answer: ₹484.62)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q13. C error finding: pointer to pointer

Point out the error, if any: int main(){ int a = 4; int *m, **n; m = &a; n = &m; /* Line 1 */ /* Line 2 */ printf("%d", **n++); /* Line 3 */ return 0; } Options: no error; Line 1 and Line 2; Line 3; Line 2. (Compiled answer: no error)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q14. C: NULL pointer assignment

What is the likely cause of the error? int main(){ int x = 4; int b = 5; b = x; printf("Result: %d", x); return 0; }. Related pointer variant asked in the exam: int *A = NULL; int b = 5; A = &b; printf("%d ", (*A)++); What is the output? Options: 6, 5, compile-time error, garbage value. (Compiled answer: 5)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q15. 4-bit R-2R ladder DAC

The reference voltage of a 4-bit R-2R ladder digital-to-analog converter is 5 V. Find the magnitude of the analog output voltage for input 1010. Options: 3.125 V, 2.675 V, 4.115 V, 1.565 V. (Compiled answer: 3.125 V)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q16. Weighted-resistor DAC

A weighted-resistor 4-bit DAC has VR = -5 V, R = 8 kΩ and Rf = R/2 (resistors 8R for b0, 4R for b1, 2R for b2 and R for b3/MSB, feeding an inverting op-amp). Find Vout for binary input 0101. (Compiled answer: 1.5625 V)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q17. 4x1 MUX realized function

A 4x1 MUX has select lines S0 = y and S1 = x and data inputs I0 = z, I1 = z', I2 = 0, I3 = 1. What function F(x,y,z) does it realize? Options: Σ(1,2,6,7), Σ(2,4,6,7), Σ(1,3,6,7), Σ(1,2,5,7). (Compiled answer: Σ(1,2,6,7))

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q18. T flip-flop input frequency

If the output frequency of a T flip-flop is 100 Hz, what is its input frequency? Options: 400 Hz, 200 Hz, 50 Hz, 100 Hz. (Compiled answer: 200 Hz)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q19. Excess-3 code use case

Excess-3 code can be used to perform the addition and subtraction of which numbers effectively? Options: Binary, Octal, Hexadecimal, BCD. (Compiled answer: BCD, since Excess-3 is self-complementing)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q20. Testability definition

Under which condition is the circuit 'low' when any particular node X is set to logic 1 or 0 through input vector combinations so as to propagate the error from X to the output? Options: all of the given options, Observability, Controllability, Testability. (Compiled answer: Testability)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q21. PMOS triode region condition

A PMOS with threshold voltage -1 V and source at 3 V (gate VG, drain VD) operates in the triode region if: Options: VD >= VG + 1, VD = VG - 1, VD < VG + 1, VD = VG. (Compiled answer: VD >= VG + 1)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q22. Logic families matching

Match each logic family in List A (1. MOS, 2. TTL, 3. ECL, 4. CMOS, 5. BiCMOS) with its most significant characteristic in List B (1. high fan-out, 2. saturated bipolar logic, 3. low power consumption, 4. higher packing density, 5. low propagation delay, 6. low output resistance). (Compiled answer: MOS-4, TTL-2, ECL-5, CMOS-3, BiCMOS-6)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q23. Factory production rate

A factory produces 400 units in 10 hours. How many units will it produce in 18 hours? Options: 900, 800, 720, 600. (Compiled answer: 720)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q24. 5-variable Boolean simplification

Simplify: A'B'C'D'E' + A'B'CD'E' + A'BCD'E' + A'BC'D'E' + A'B'C'D'E + A'BCD'E + A'BCDE + AB'C'D'E' + AB'C'D'E + ABCD'E + ABCDE + AB'CDE. Options: A'DE' + B'C'D' + BCE + ACDE; A'D'E' + B'C'D + BCE' + ACDE; A'D'E' + B'C'D' + BCE + ACDE; A'D'E' + B'C'D' + BCE + ACDE'. (Compiled answer: A'D'E' + B'C'D' + BCE + ACDE)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q25. JK flip-flop counter: J1 and K1

A counter built from JK flip-flops (Q2 Q1 Q0) follows the sequence 2 -> 5 -> 4 -> 7 -> 6 -> 1 -> 0 -> 3 -> 2 (repeat). What are the equations for J1 and K1? Options: J1 = Q0' and K1 = Q0; J1 = Q0 and K1 = Q0'; J1 = Q1' and K1 = Q0'; J1 = Q0' and K1 = Q0'. (Compiled answer: J1 = K1 = Q0')

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q26. VLSI design methodology choice

Ethan leads a project to develop a high-performance processor for enterprise clients. It must deliver top-tier performance and launch within a year. The budget allows some flexibility but not unlimited spending. Which design methodology should Ethan choose? Options: full custom design for maximum performance; semi-custom design for a balance of performance; FPGA design for rapid prototyping but higher unit costs; standard cell design for faster development. (Compiled answer: semi-custom)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q27. Transfer function causality and stability

For the transfer function H(s) = 1 / (s^2 + 5s + 6) with ROC σ > -2, the system is: Options: causal & unstable, non-causal & stable, causal & stable, non-causal & unstable. (Compiled answer: causal & stable)

Topics: Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q28. 8085 program: register C and carry flag

An 8085 program runs with the carry flag initially clear (CY = 0): MVI B, 3CH; MVI A, A5H; ANA B; RLC; MOV C, A. What is the content of register C and the status of the carry flag after execution? Options: 48H with carry 1; 68H with carry 1; 48H with carry 0. (Compiled answer: 48H, carry 0)

Topics: Bit Manipulation, Other  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q29. Two students on a circular track

Two students start together from the same point on a circular jogging track of length 900 m and run in the same direction at 6 m/s and 10 m/s. After how many seconds will both be together again at the starting point for the first time? Options: 600 s, 300 s, 450 s. (Compiled answer: 450 s)

Topics: Aptitude, Math  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q30. Letter coding: HOUSE -> JQWUG

In a certain code language, HOUSE is written as JQWUG. How will PICTURE be written? Options: RKEVWTG, RKEVUTG, RKEVWVG, RKEUWTG. (Compiled answer: RKEVWTG, each letter shifted by +2)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q31. Analogy: POCKET : PTOECK :: SILVER : ?

The 2nd term relates to the 1st in the same way the 4th term relates to the 3rd. POCKET : PTOECK :: SILVER : ? Options: SRIELV, SIRELV, SRIEVL, SREILV. (Compiled answer: SRIELV, letter positions rearranged as [1,6,2,5,3,4])

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q32. Star-operation word coding

The following words are coded like this after going through the 'star operation': 'Words make sentences meaningful' => 8$A, 2!R, 6#C, 14$F; 'Rain stops every week' => 2^E, 2#O, 8+A, 8!E; 'Eagerly receives __(a)__' => 12%R, 4^R, 12+V; 'Rarely prepares tasty food' => 12%R, 2~S, __(b)__, 8@O. What goes in blank (a)? Options: food, rarely, prepares, tasty. (Compiled answer: food)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q33. Symbol coding: GIFT / MUST / TRUE

If GIFT is coded as "#!$@" and MUST is coded as "&$*^", how can TRUE be coded? Options: ^$+!, &$@%, &$%~, ~$+%. (Compiled answer: ^$+!; the compiler notes that the cipher is internally inconsistent)

Topics: Aptitude  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)

### Q34. Word rearrangement with a priority queue

Consider the text: "The Ram Mandir is a Hindu temple that is under construction in Ayodhya, Uttar Pradesh, India." Rearrangement algorithm: priority is assigned by word length (longer word = higher priority; ties go to the earlier occurrence). Insert only the words with even priority into a queue, from high to low priority, to get the modified text. Options: (a) construction Ayodhya Pradesh mandir temple hindu under utter india that The Ram is is in a, (b) a in is is Ram The that india utter under hindu temple mandir Ayodhya construction, (c) in is is that temple mandir construction, (d) construction mandir temple that is is in. (Compiled answer: d)

Topics: Aptitude, Stack/Queue, Strings  
📎 source: [msg 5859](../archive/inter-nit/2026-10.jsonl), [Qualcomm_Questions_Compiled.pdf](../archive/files/5860-Qualcomm_Questions_Compiled.pdf)
