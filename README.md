# US Cyber Games 2022 Open 

## About

The US Cyber Games 2022 Open CTF was a collaborative effort to test competitors in pwn, crypto, reverse engineering, forensics, and web categories. The challenge authors included experts from academics, industry, and the inaugural US Cyber Games team members. We are thankful for the support from [Florida Tech](https://www.fit.edu/), [Dakota State](https://dsu.edu), [The US Naval Academy](https://usna.edu), the [University of North Georgia](https://ung.edu), [Research Innovations Inc](https://www.researchinnovations.com), [Battelle](https://www.battelle.org), and [MetaCTF](https://metactf.com).

## Challenges

| Name | Category| Author  |  Solutions |  
|------|-----|-----|---------|
| [twist](pwn/twist)                     | pwn  	| [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/twist/pwn-twist.py)                |
| [push](pwn/push)                       | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/push/pwn-push.py)                  | 
| [warmup](pwn/w_arm_up)                 | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/w_arm_up/pwn-wARMup.py)            |
| [ctf editor](pwn/ctf-editor)           | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/ctf-editor/pwn-ctf.py)             |
| [lyrics](pwn/lyrics)			         | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/lyrics/pwn-lyrics.py)              | 
| [99 problems](pwn/problems)		     | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/problems/pwn-problems.py)          | 
| [medal](pwn/medal)			         | pwn      | [TJ](https://github.com/tj-oconnor/)         |  [our solution](pwn/medal/pwn-medal.py)                | 
| [gibson](pwn/gibson)			         | pwn      | [Research Innovations Inc (RII)](https://www.researchinnovations.com)   |  [our solution](pwn/gibson/solution.py)| 
| [16bit](pwn/16bit)			         | pwn      | lms                                          |                                                        | 
| [too many houses](pwn/house)			 | pwn      | lms                                          |  [our solution](pwn/house/Solution.pdf)                | 
| [time](crypto/time)                    | crypto   | [TJ](https://github.com/tj-oconnor/)         |  [our solution](crypto/time/solve-time.py)                |  
| [whos that pokemon](crypto/pokemon)    | crypto   | Benderbot                                    |  [our solution](crypto/pokemon/solve.ipynb)            |  
| [major malfunction](crypto/malfunction)| crypto   | Eric                                         |                                                        |  
| [greys anatomy](crypto/greys)          | crypto   | Benderbot                                    |  [our solution](crypto/greys/solver.py)                |  
| [beacon](crypto/beacon)                | crypto   | [tsuto](https://github.com/jselliott)     |  [our solution](crypto/beacon)                       |
| [radiation leak](crypto/radiation-leak) | crypto | [MetaCTF](https://metactf.com)             |                                                           | 
| [archival](re/archival)                | RE       | Rajat                                        |  [our solution](re/archival/sol.py)                    |   
| [directionless](re/directionless)      | RE       | Rajat                                        |  [our solution](re/directionless/sol.bash)             |   
| [dynamo](re/dynamo)                    | RE       | Rajat                                        |  [our solution](re/dynamo)                             |   
| [river](re/river)                      | RE       | Rajat                                        |  [our solution](re/river)                              |   
| [trust](re/trust)                      | RE       | Rajat                                        |  [our solution](re/trust)                              |   
| [well ordered](re/well-ordered)        | RE       | Rajat                                        |  [our solution](re/well-ordered)                       |   
| [decaf pcap](forensics/decaf)          | forensics  | [MetaCTF](https://metactf.com)             |  [our solution](forensics/decaf)                       |
| [hidden wisdom](forensics/hiddenwisdom)| forensics  | [Batelle](https://www.battelle.org)        |  [our solution](forensics/hiddenwisdom/solve-hidden.py)|
| [ZeroZero2Hero](forensics/zerozero2Hero)     | forensics  | [TJ](https://github.com/tj-oconnor/) |  [our solution](forensics/zerozero2Hero/crc-checker.py)|
| [stomped](forensics/stomped)           | forensics  | [TJ](https://github.com/tj-oconnor/)       |  [our solution](forensics/stomped/stomped.py)         |
| [from Nand to Tetris to the big screen](forensics/bigscreen) | forensics | [DrB Hacking](https://github.com/jamrootz) | [our solution](forensics/bigscreen/files/solve.py)   |
| [fun facts](web/fun-facts)            | web      | [tsuto](https://github.com/jselliott)      |  [our solution](web/fun-facts/fun-facts.mp4)          |
| [grillmaster](web/grillmaster)        | web      | [tsuto](https://github.com/jselliott)      |  [our solution](web/grillmaster/grillmaster.mp4)      |
| [layers](web/layers)                  | web      | [tsuto](https://github.com/jselliott)      |  [our solution](web/layers/layers.mp4)                |
| [single use](web/single-use)          | web      | [tsuto](https://github.com/jselliott)      |  [our solution](web/single-use/single-use.mp4)        |
| [sweeper](web/sweeper)                | web      | [tsuto](https://github.com/jselliott)      |                                                       |
| [wordy](web/wordy)                | web      | [tsuto](https://github.com/jselliott)      |  [our solution](web/wordy/wordy.mp4)                  |
| [black friday](web/black-friday)      | web      | [MetaCTF](https://metactf.com)                |                                                       |

## References

0. [Twist](pwn/twist) is insipired by a problem of the same name from the [International Cyber Competition](https://www.enisa.europa.eu/topics/cybersecurity-education/international-cybersecurity-challenge-icc), where the remote environment was different than the local environment. It is still unsure if this was on purpose on not. 

1. The [Angr CTF](https://github.com/jakespringer/angr_ctf) served as motivation for the [99 problems](pwn/problems) constraint challenge. Further, our solution is modeled after the *scaffolding files* from the [Angr CTF](https://github.com/jakespringer/angr_ctf). 

2. The solution for [greys](crypto/greys) includes code from a [Stack Overflow post](https://stackoverflow.com/questions/38738835/generating-gray-codes) on generating gray codes.

3. The solution for [002hero](forensics/zerozero2Hero) slightly modifies code from the [PRCT Toolkit](https://github.com/sherlly/PCRT/blob/master/PCRT.py) to calculate the PNG header values for width and heigh.

4. [ZeroZero2Hero](forensics/zerozero2Hero) is inspired by the [Shes a Killed queen](https://ctftime.org/writeup/31187) challenge from the [Killer Queen CTF 2021](https://ctftime.org/event/1482).

5. [TJ](https://github.com/tj-oconnor) builds his docker containers off the template published by the [Order of the Overflow](https://github.com/o-o-overflow) for their [DEFCON 2019 Speed Run Challenges](https://github.com/o-o-overflow/dc2019q-speedrun-001). He uses ``kali-rolling`` when necessary because it makes the libc-database sad.


