Markdown# 📡 Directional RFI Signal Analysis & Classification

A Python pipeline designed to ingest, process, analyze, and visualize Radio Frequency Interference (RFI) data captured across 8 cardinal/intercardinal directions with dual-polarization (Horizontal `-H` and Vertical `-V`) measurements.

---

## 🚀 Features

* **Spectral Line Plotting:** Cleans and plots RFI amplitude (dB) against Frequency (Hz) across 16 distinct directional datasets, utilizing custom color palettes for readability.
* **Polar/Radar Distribution Maps:** Computes peak amplitudes per direction, shifts and maps them onto a custom polar coordinate system, and automatically highlights the strongest RFI source.
* **Automated Source Identification:** Categorizes peak frequencies into known real-world emitters (e.g., FM Radio, Aviation/Airband, Cellular LTE/5G, Wi-Fi, and Radar).
* **Summary Bar Charts:** Generates horizontal bar charts sorted by maximum amplitude, complete with a color-coded legend mapped to categorized emitter types.

---

## 🛠️ Prerequisites & Dependencies

Make sure you have Python installed along with the following required libraries:

```bash
pip install pandas matplotlib numpy
📂 Project StructurePlaintext.
├── GB-RFI-N-H001.csv          # Example input data (Repeat for N through NW, H & V)
├── rfi_analysis.py            # Main processing and visualization script
├── RFISIGNALS.png             # Output: Spectral line plot
├── RFIPOLARPOINTS.png         # Output: Polar max-amplitude map
├── RFISOURCES.png             # Output: Identified sources bar chart
└── README.md                  # Project documentation
📊 Analysis & Visual Results1. Spectral Line PlotShows frequency response curves across all 16 directional channels ($0^\circ$ to $315^\circ$, H & V).2. Spatial Directional DistributionA 360-degree polar radar plot highlighting spatial orientation, directional power distribution, and peak intensity.3. Identified Signal SourcesCategorized horizontal bar chart mapping specific frequency spikes to known signal allocations (e.g., FM Radio, Cellular, Radar).
👤 AuthorDenis Micere
