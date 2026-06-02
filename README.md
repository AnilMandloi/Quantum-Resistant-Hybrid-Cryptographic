# Quantum-Resistant Hybrid Cryptographic Frameworks for CBDC and Cross-Border Payment Systems

This repository now includes a self-contained proof-of-concept simulation aligned with the paper's methodology and results sections.

## Proof of Concept

Run the methodology simulator from the repo root:

```bash
python3 poc/qr_hybridfin_methodology_sim.py
```

It writes reproducible artifacts to `records/data/` and `records/figures/`, including:

- `performance_table.csv`
- `transaction_trace_sample.csv`
- `transaction_breakdown_sample.csv`
- `transaction_summary.csv`
- `throughput_scaling.csv`
- `cross_border_summary.csv`
- `ablation_summary.csv`
- `quantum_risk.csv`
- `architecture_diagram.svg`
- `latency_comparison.svg`
- `throughput_comparison.svg`
- `throughput_scaling.svg`
- `latency_vs_payload.svg`
- `cross_border_latency.svg`
- `quantum_risk.svg`
- `report.md`
- `appendix.md`
- `appendix.tex`
- `appendix_body.tex`
- `report.tex`

To compile the manuscript wrapper, run `pdflatex report.tex` from the `records/` directory.

## Alignment Notes

- The performance table is anchored to the paper's reported classical, hybrid, and ML-optimized values.
- The scaling, payload, and cross-border runs are generated from the paper's architecture, network assumptions, and batch throughput model.
- The architecture diagram mirrors the paper's four-layer QR-HybridFin design.
- The trace output reflects transaction-level simulation with adaptive strategy selection and explicit per-layer breakdowns.
