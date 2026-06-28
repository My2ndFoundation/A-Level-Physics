---
type: application
subject: physics
tags:
  - aqa-7407-7408
  - a-level-physics
  - electronics
  - signal-processing
  - waves
level: a-level
difficulty: 3
status: draft
aliases:
  - AM
  - FM
  - Amplitude Modulation
  - Frequency Modulation
  - Time-Division Multiplexing
sources: []
---

# Communication Systems

## Problem Context

A signal we want to send (voice, video, data) often has a low frequency and cannot itself travel efficiently as a wave through space or down a cable. Communication systems solve this by **modulating** a high-frequency carrier with the information signal, transmitting the modulated carrier, and recovering the information at the receiver.

## Physical Ideas

- [[Analogue-and-Digital-Signals]]
- [[Signal-Processing]]
- [[Electromagnetic-Spectrum]]
- [[LC-Resonance-Filter]] — tunes the receiver to one carrier.

## Mathematical Tools

Every system has the same skeleton:

$$\text{source} \to \text{transmitter} \to \text{channel} \to \text{receiver} \to \text{user}$$

- **Source**: produces the information signal (microphone, camera, computer).
- **Transmitter**: modulates the carrier and feeds it into the channel (cable or aerial).
- **Channel**: the physical medium (free space, fibre, copper) — adds noise and attenuation.
- **Receiver**: selects the wanted carrier, demodulates it, amplifies the recovered signal.

**Amplitude modulation (AM).** The carrier amplitude is varied in step with the information signal. If the carrier is $v_{c}(t) = V_{c} \cos(2\pi f_{c} t)$ and the message has amplitude $V_{m}$ at frequency $f_{m}$, the AM signal is approximately

$$v_{AM}(t) = \left[V_{c} + V_{m}\cos(2\pi f_{m} t)\right]\cos(2\pi f_{c} t)$$

with symbols:

- $V_{c}$: carrier amplitude (V)
- $f_{c}$: carrier frequency (Hz)
- $V_{m}$: message amplitude (V)
- $f_{m}$: message frequency (Hz)

The bandwidth required is $\Delta f \approx 2 f_{m,\,\text{max}}$ (twice the highest message frequency).

**Frequency modulation (FM).** The carrier frequency is varied in step with the message; amplitude stays constant. Schematically, the instantaneous carrier frequency becomes

$$f(t) = f_{c} + k\, v_{m}(t)$$

with $k$ a constant (Hz / V) called the modulation sensitivity. FM uses more bandwidth than AM for the same message but is much less affected by amplitude noise, because receivers ignore amplitude changes.

**Bandwidth.** A channel of bandwidth $B$ (Hz) is the range of frequencies it can carry. Different services occupy different bands of the electromagnetic spectrum; bandwidth is a finite, regulated resource.

**Time-division multiplexing (TDM).** A single channel carries several signals by giving each one its own short time slot in a repeating cycle. If $N$ users share a channel and each gets slot length $\tau$, the cycle is $N\tau$ long. Provided the user signals are sampled fast enough (see [[Analogue-and-Digital-Signals]]) the receiver reassembles each stream from its allotted slots.

## Typical Questions

- For a given message bandwidth, calculate the bandwidth of the AM signal.
- Explain why FM radio sounds cleaner than AM radio in a noisy environment.
- Describe how a tuning circuit selects one station among many.
- For $N$ phone calls multiplexed onto one channel, find the slot rate needed.

## Method Outline

1. Identify the source, channel, and receiver.
2. Pick a modulation scheme: AM, FM, or digital (PSK / QAM at frontier).
3. Calculate the carrier frequency and required bandwidth.
4. Choose a selectivity filter ([[LC-Resonance-Filter]]) for the receiver.
5. Demodulate to recover the message and amplify for the user.

## Assumptions

- The channel is linear (does not distort).
- Carrier frequency is much higher than the highest message frequency.
- Noise is small enough that the receiver can lock onto the carrier.
- For TDM, signals are sampled above the Nyquist rate.

## Links to Other Subjects

- Mathematics: trigonometric identities, Fourier ideas.
- Computer Science: digital modulation, error-correcting codes, packet protocols.

## Frontier Links

- [[Semiconductor-Physics-Map]] — modern radios are largely digital signal processors on silicon.

## Common Mistakes

- Mixing up AM and FM: AM varies amplitude, FM varies frequency.
- Forgetting that bandwidth depends on message frequency, not on carrier frequency.
- Believing TDM needs a separate physical channel per user — it shares one channel in time.
- Confusing **carrier frequency** (where the channel lives in the spectrum) with **modulation frequency** (the highest message frequency).

## Visuals

### Generic communication chain

```mermaid
flowchart LR
    Src["Source: mic / camera"] --> Mod["Modulator (AM / FM)"]
    Mod --> Ch["Channel: free space / cable"]
    Ch --> Tuner["LC tuned filter"]
    Tuner --> Demod["Demodulator"]
    Demod --> Amp["Amplifier"]
    Amp --> User["User: speaker / screen"]
```

*Figure: every link in the chain has a clear role; modulation shifts the message onto a high-frequency carrier so it can travel.*
*Source: Authored for this vault (CC0). No external copyright.*

### From Wikimedia

<!-- wiki-images: yes -->

#### Amplitude modulation of a carrier
![[_attachments/10_Applications/Communication-Systems--wiki-amplitude-modulation.svg]]
*Figure: a low-frequency message signal varies the amplitude of a high-frequency carrier to produce the AM waveform.*
*Source: Wikimedia Commons — [Amplitude Modulated Wave-hm-64.svg](https://commons.wikimedia.org/wiki/File:Amplitude_Modulated_Wave-hm-64.svg) — CC0 — The.ever.kid. Retrieved 2026-06-27.*

## Source Trace

- Source: [[AQA-Physics-7407-7408-Specification]] §3.13
- Public source: HyperPhysics; All About Circuits
- Section/Page: Electronics — communication systems, modulation, multiplexing
