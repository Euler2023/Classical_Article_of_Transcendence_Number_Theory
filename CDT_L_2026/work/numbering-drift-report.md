# Continuous Numbering Drift Audit — `CDT_L_2026`

Generated: 2026-06-16 10:22
Main TeX: `CDT_L_2026_Chn.tex`
Total Audited Counter Steps: 584
Total Drift Mismatches: 11

## ⚠️ Detected Numbering Drifts

The following entities compiled counter does not match their label-defined numbers. This usually indicates an unnumbered display formula or misplaced sectioning heading.

| # | File | Line | Type | Label | Simulated | Expected | Context |
|---|---|---|---|---|---|---|---|
| 1 | `tex/sec1.tex` | 312 | `figure` | `fig:1.3.0` | **1.3.1** | **1.3.0** | `\begin{figure}[!htbp]` |
| 2 | `tex/sec2.tex` | 792 | `equation` | `eq:2.12.0` | **2.12.1** | **2.12.0** | `\begin{equation}\label{eq:2.12.0}` |
| 3 | `tex/sec2.tex` | 798 | `equation` | `eq:2.12.1` | **2.12.2** | **2.12.1** | `\begin{equation}\label{eq:2.12.1}` |
| 4 | `tex/sec2.tex` | 805 | `equation` | `eq:2.12.2` | **2.12.3** | **2.12.2** | `\begin{equation}\label{eq:2.12.2}` |
| 5 | `tex/sec2.tex` | 809 | `equation` | `eq:2.12.3` | **2.12.4** | **2.12.3** | `\begin{equation}\label{eq:2.12.3}\tag{2.12.3}` |
| 6 | `tex/sec8.tex` | 884 | `remark` | `rem:8.2.41` | **8.2.42** | **8.2.41** | `\begin{remark}\label{rem:8.2.41}` |
| 7 | `tex/sec8.tex` | 891 | `remark` | `rem:8.2.42` | **8.2.43** | **8.2.42** | `\begin{remark}\label{rem:8.2.42}` |
| 8 | `tex/sec11.tex` | 9 | `mylemma` | `eq:11.1.2` | **11.1.1** | **11.1.2** | `\begin{mylemma}{}{lem:11.1.1}` |
| 9 | `tex/sec14.tex` | 601 | `equation` | `eq:14.5.3` | **14.5.2** | **14.5.3** | `\begin{equation}\label{eq:14.5.3}` |
| 10 | `tex/sec14.tex` | 606 | `equation` | `eq:14.5.4` | **14.5.3** | **14.5.4** | `\begin{equation}\label{eq:14.5.4}` |
| 11 | `tex/sec14.tex` | 615 | `equation` | `eq:14.5.5` | **14.5.4** | **14.5.5** | `\begin{equation}\label{eq:14.5.5}` |
