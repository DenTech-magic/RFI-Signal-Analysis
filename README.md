# 📡 Directional RFI Signal Analysis & Classification

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

📂 Project Structure
Plaintext

├── GB-RFI-N-H001.csv          # Example input data (Repeat for N through NW, H & V)
├── rfi_analysis.py            # Main processing and visualization script
├── RFISIGNALS.png             # Output: Spectral line plot
├── RFIPOLARPOINTS.png         # Output: Polar max-amplitude map
├── RFISOURCES.png             # Output: Identified sources bar chart
└── README.md                  # Project documentation

📊 Outputs Generated

    RFISIGNALS.png — Overlaid frequency response curves for all 16 directional channels.

    RFIPOLARPOINTS.png — A 360-degree radar view indicating spatial orientation and peak intensity of interference.

    RFISOURCES.png — A categorized horizontal bar chart mapping specific frequency spikes to common RF services.

👤 Author

Denis Micere
