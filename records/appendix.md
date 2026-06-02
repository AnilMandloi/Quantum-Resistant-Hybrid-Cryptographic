# Appendix: QR-HybridFin Simulation Summary

This appendix condenses the transaction-level simulator into paper-style tables and captions.
It is derived from the layered model implemented in `poc/qr_hybridfin_methodology_sim.py`.

## Table A1. Core simulation outcomes

| Metric | Value |
|---|---:|
| Adaptive trace mean latency | 106.258 ms |
| Adaptive trace p95 latency | 285.982 ms |
| Adaptive classical selections | 1 |
| Adaptive static-hybrid selections | 5587 |
| Adaptive ML-optimized selections | 4412 |
| Best throughput at 50 nodes | 1012.64 TPS |
| Worst cross-border mean settlement | 242.30 ms |
| Classical ablation mean latency | 105.506 ms |
| Static-hybrid ablation mean latency | 111.582 ms |
| ML-optimized ablation mean latency | 108.157 ms |

## Table A2. Derived interpretation

| Observation | Interpretation |
|---|---|
| Classical fallback remains available | Low-risk domestic transactions can stay on the legacy path during migration. |
| Static hybrid dominates mid-load traffic | The agility manager shifts to the hybrid mode as load rises. |
| ML-optimized covers cross-border/high-threat flows | The policy layer pushes the stronger profile where risk or WAN friction is highest. |
| Throughput remains in the paper's target range | The batch service model preserves the 1180 / 965 / 1015 TPS calibration envelope. |

## Figure Captions

Figure A1. QR-HybridFin architecture diagram showing the cryptographic, blockchain, ML agility, and network layers connected by the transaction flow.
Figure A2. Cryptographic latency comparison anchored to the paper's Table I values and ML-optimized overhead reduction.
Figure A3. Wholesale throughput comparison showing the calibrated classical, static-hybrid, and ML-optimized TPS points.
Figure A4. Throughput scaling across 50-500 nodes under the paper's CBDC deployment scenario.
Figure A5. Latency versus payload size generated from the layered transaction cost model.
Figure A6. Cross-border settlement latency under Mininet + tc WAN emulation with 100-300 ms links.
Figure A7. Quantum resistance comparison for classical and hybrid schemes under the paper's Shor/Grover discussion.

## Methodological Notes

- The per-transaction breakdown records cryptographic, blockchain, routing, queueing, and ML-agility terms separately.
- The adaptive selector uses transaction threat level, current load, and cross-border status to choose the cryptographic profile.
- Cross-border and ablation summaries use the same cost model, so the comparison is generated from one simulation pipeline rather than a replot of static values.
