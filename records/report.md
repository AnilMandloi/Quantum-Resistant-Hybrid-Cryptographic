# QR-HybridFin Methodology Simulation

This run simulates the paper's layered architecture rather than only replotting the table.

## Key outputs

- transaction trace rows: 10000
- mean latency: 106.258 ms
- p95 latency: 285.982 ms
- adaptive selection mix: classical=1, static=5587, ml=4412
- selected classical count: 1
- selected static hybrid count: 5587
- selected ml optimized count: 4412
- throughput rows: 10
- cross-border scenarios: 3

## Paper anchors

- Table I values are reproduced in `performance_table.csv`.
- The throughput model is calibrated to the paper's 1180 / 965 / 1015 TPS figures.
- Cross-border latency is generated from the paper's 100-300 ms network envelope.
- Security comparison is aligned with the paper's Qiskit/Shor discussion.

## Files

- `records/data/performance_table.csv`
- `records/data/transaction_trace_sample.csv`
- `records/data/transaction_breakdown_sample.csv`
- `records/data/transaction_summary.csv`
- `records/data/throughput_scaling.csv`
- `records/data/cross_border_summary.csv`
- `records/data/ablation_summary.csv`
- `records/data/quantum_risk.csv`
- `records/figures/architecture_diagram.svg`
- `records/figures/latency_comparison.svg`
- `records/figures/throughput_comparison.svg`
- `records/figures/throughput_scaling.svg`
- `records/figures/latency_vs_payload.svg`
- `records/figures/cross_border_latency.svg`
- `records/figures/quantum_risk.svg`
