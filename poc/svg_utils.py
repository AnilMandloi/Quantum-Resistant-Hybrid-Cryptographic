from __future__ import annotations

from typing import Sequence


def svg_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def write_text(path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_svg(path, width: int, height: int, body: str) -> None:
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
        '<rect width="100%" height="100%" fill="#f7f5ef"/>\n'
        f"{body}\n"
        "</svg>\n"
    )
    write_text(path, svg)


def text(x: float, y: float, value: str, size: int = 12, anchor: str = "middle", fill: str = "#1e1b18", weight: str = "normal") -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" '
        f'font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}">{svg_escape(value)}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "#4e463e", rx: int = 4) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = "#4e463e", width: float = 1.5, dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{dash_attr}/>'


def chart_title(width: int, title: str, subtitle: str | None = None) -> str:
    body = [text(width / 2, 34, title, size=20, weight="bold")]
    if subtitle:
        body.append(text(width / 2, 56, subtitle, size=11, fill="#5c544c"))
    return "\n".join(body)


def draw_axes(width: int, height: int, margin: int) -> str:
    x0 = margin
    y0 = height - margin
    x1 = width - margin
    y1 = margin
    grid = []
    grid.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="#2f2a24" stroke-width="2"/>')
    grid.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="#2f2a24" stroke-width="2"/>')
    return "\n".join(grid)


def render_grouped_bar_chart(
    title: str,
    subtitle: str,
    categories: Sequence[str],
    series: Sequence[tuple[str, Sequence[float], str]],
    y_label: str,
    outpath,
    width: int = 1100,
    height: int = 620,
) -> None:
    margin = 80
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin
    all_values = [value for _, values, _ in series for value in values]
    max_value = max(all_values) * 1.15 if all_values else 1.0
    min_value = 0.0
    ticks = 5

    def y_for(value: float) -> float:
        return margin + plot_h - ((value - min_value) / (max_value - min_value)) * plot_h

    def x_for(index: int) -> float:
        return margin + (index + 0.5) * plot_w / len(categories)

    parts = [chart_title(width, title, subtitle), draw_axes(width, height, margin)]
    for i in range(ticks + 1):
        v = max_value * i / ticks
        y = y_for(v)
        parts.append(line(margin, y, width - margin, y, stroke="#d9d0c3", width=1))
        parts.append(text(margin - 12, y + 4, f"{v:.0f}", size=11, anchor="end", fill="#5c544c"))
    parts.append(text(22, height / 2, y_label, size=12, fill="#5c544c"))

    group_w = plot_w / len(categories)
    bar_w = group_w * 0.22
    bar_gap = bar_w * 0.22
    series_count = len(series)
    start_offset = -(series_count - 1) * (bar_w + bar_gap) / 2
    legend_x = width - margin - 250
    legend_y = margin - 36
    for s_idx, (label, values, color) in enumerate(series):
        parts.append(rect(legend_x + s_idx * 130, legend_y, 16, 16, color, stroke=color))
        parts.append(text(legend_x + 22 + s_idx * 130, legend_y + 13, label, size=11, anchor="start", fill="#3c362f"))
        for idx, value in enumerate(values):
            x_center = x_for(idx)
            x = x_center + start_offset + s_idx * (bar_w + bar_gap) - bar_w / 2
            y = y_for(value)
            h = margin + plot_h - y
            parts.append(rect(x, y, bar_w, h, color, stroke=color, rx=2))

    for idx, category in enumerate(categories):
        x_center = x_for(idx)
        parts.append(text(x_center, height - 52, category, size=11))
        parts.append(line(x_center, height - margin, x_center, height - margin + 6, stroke="#2f2a24", width=1))

    write_svg(outpath, width, height, "\n".join(parts))


def render_line_chart(
    title: str,
    subtitle: str,
    x_values: Sequence[float],
    series: Sequence[tuple[str, Sequence[float], str]],
    x_label: str,
    y_label: str,
    outpath,
    width: int = 1100,
    height: int = 620,
) -> None:
    margin = 80
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin
    all_values = [value for _, values, _ in series for value in values]
    max_value = max(all_values) * 1.15 if all_values else 1.0
    min_value = min(0.0, min(all_values) * 0.9) if all_values else 0.0
    x_min = min(x_values)
    x_max = max(x_values)

    def x_for(value: float) -> float:
        if x_max == x_min:
            return margin + plot_w / 2
        return margin + ((value - x_min) / (x_max - x_min)) * plot_w

    def y_for(value: float) -> float:
        return margin + plot_h - ((value - min_value) / (max_value - min_value)) * plot_h

    parts = [chart_title(width, title, subtitle), draw_axes(width, height, margin)]
    for i in range(6):
        v = min_value + (max_value - min_value) * i / 5.0
        y = y_for(v)
        parts.append(line(margin, y, width - margin, y, stroke="#d9d0c3", width=1))
        parts.append(text(margin - 12, y + 4, f"{v:.0f}", size=11, anchor="end", fill="#5c544c"))

    parts.append(text(width / 2, height - 18, x_label, size=12, fill="#5c544c"))
    parts.append(text(22, height / 2, y_label, size=12, fill="#5c544c"))

    legend_x = width - margin - 250
    legend_y = margin - 36
    for s_idx, (label, values, color) in enumerate(series):
        parts.append(rect(legend_x + s_idx * 150, legend_y, 16, 16, color, stroke=color))
        parts.append(text(legend_x + 22 + s_idx * 150, legend_y + 13, label, size=11, anchor="start", fill="#3c362f"))
        points = []
        for xv, yv in zip(x_values, values):
            x = x_for(xv)
            y = y_for(yv)
            points.append(f"{x},{y}")
            parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{color}" stroke="#fff" stroke-width="1"/>')
        parts.append(f'<polyline fill="none" stroke="{color}" stroke-width="2.5" points="{" ".join(points)}"/>')

    for xv in x_values:
        x = x_for(xv)
        parts.append(text(x, height - 52, str(int(xv)), size=11))
        parts.append(line(x, height - margin, x, height - margin + 6, stroke="#2f2a24", width=1))

    write_svg(outpath, width, height, "\n".join(parts))


def render_quantum_risk_chart(outpath, rows: Sequence[dict[str, float | str]]) -> None:
    width = 1100
    height = 620
    margin = 90
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin
    max_value = 100
    parts = [chart_title(width, "Quantum Resistance vs Classical Breakability", "A paper-aligned qualitative model for the Qiskit/Shor discussion"), draw_axes(width, height, margin)]

    for i in range(6):
        v = max_value * i / 5
        y = margin + plot_h - (v / max_value) * plot_h
        parts.append(line(margin, y, width - margin, y, stroke="#d9d0c3", width=1))
        parts.append(text(margin - 12, y + 4, f"{v:.0f}", size=11, anchor="end", fill="#5c544c"))

    categories = [str(r["scheme"]) for r in rows]
    bar_w = plot_w / (len(categories) * 2.2)
    for idx, row in enumerate(rows):
        x_center = margin + (idx + 0.5) * plot_w / len(rows)
        risk = float(row["risk_score"])
        resist = float(row["resistance_score"])
        parts.append(rect(x_center - bar_w - 6, margin + plot_h - (risk / max_value) * plot_h, bar_w, (risk / max_value) * plot_h, "#c85a4d", stroke="#c85a4d"))
        parts.append(rect(x_center + 6, margin + plot_h - (resist / max_value) * plot_h, bar_w, (resist / max_value) * plot_h, "#558b6e", stroke="#558b6e"))
        parts.append(text(x_center, height - 44, categories[idx], size=10))
    parts.append(rect(width - margin - 240, margin - 40, 18, 18, "#c85a4d", stroke="#c85a4d"))
    parts.append(text(width - margin - 216, margin - 26, "Breakability risk", size=11, anchor="start"))
    parts.append(rect(width - margin - 120, margin - 40, 18, 18, "#558b6e", stroke="#558b6e"))
    parts.append(text(width - margin - 96, margin - 26, "Resistance score", size=11, anchor="start"))
    write_svg(outpath, width, height, "\n".join(parts))
