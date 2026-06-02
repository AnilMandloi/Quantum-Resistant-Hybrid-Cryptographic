# QR-HybridFin Proof of Concept

This directory contains a local simulation derived from the paper's methodology and results sections.

## Paper-anchored performance table

| Operation | Classical | Hybrid PQC | Static Overhead | ML-Optimized | Derived Optimized | Paper Prediction |
|---|---:|---:|---:|---:|---:|---:|
| Key Generation | 0.8200 | 1.1900 | 45.12% | 34.20% | 1.1004 | 1.1600 |
| Encapsulation | 0.4100 | 0.6800 | 65.85% | 43.90% | 0.5900 | 0.6700 |
| Signing | 1.4800 | 2.7600 | 86.49% | 61.80% | 2.3946 | 2.7100 |
| End-to-End Wholesale TPS | 1180.0000 | 965.0000 | 18.22% | 11.80% | 1040.7600 | 1015.0000 |

## What was simulated

- A performance table anchored to the paper's reported latency/TPS values.
- A 50-500 node scaling run matching the paper's CBDC/cross-border deployment scenario.
- A cross-border latency model using the paper's 100-300 ms network range.
- A qualitative quantum-risk model aligned with the Qiskit/Shor discussion.
- An architecture diagram that mirrors the paper's four-layer QR-HybridFin stack.

## Generated artifacts

- `performance_table.csv`
- `scalability.csv`
- `latency_payload.csv`
- `cross_border.csv`
- `quantum_risk.csv`
- `architecture_diagram.svg`
- `performance_latency.svg`
- `throughput_comparison.svg`
- `latency_vs_payload.svg`
- `scalability.svg`
- `cross_border_latency.svg`
- `quantum_risk.svg`

## Notes

The simulation is intentionally self-contained. It does not require liboqs, Hyperledger Fabric, Mininet, tc, or Qiskit to run in this workspace.
It is meant to give a reproducible proof-of-concept that reflects the paper's stated methodology and observed trade-offs.
