# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:25:14 2026

@author: Denis Micere
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D

# ==========================================
# PART I: Plot the RFI Signals
# ==========================================

# 1. READ CSV FILES (Numbered 1 through 16 to match filenames)
df1 = pd.read_csv("GB-RFI-N-H001.csv")
df2 = pd.read_csv("GB-RFI-N-V002.csv")
df3 = pd.read_csv("GB-RFI-NE-H003.csv")
df4 = pd.read_csv("GB-RFI-NE-V004.csv")
df5 = pd.read_csv("GB-RFI-E-H005.csv")
df6 = pd.read_csv("GB-RFI-E-V006.csv")
df7 = pd.read_csv("GB-RFI-SE-H007.csv")
df8 = pd.read_csv("GB-RFI-SE-V008.csv")
df9 = pd.read_csv("GB-RFI-S-H009.csv")
df10 = pd.read_csv("GB-RFI-S-V010.csv")
df11 = pd.read_csv("GB-RFI-SW-H011.csv")
df12 = pd.read_csv("GB-RFI-SW-V012.csv")
df13 = pd.read_csv("GB-RFI-W-H013.csv")
df14 = pd.read_csv("GB-RFI-W-V014.csv")
df15 = pd.read_csv("GB-RFI-NW-H015.csv")
df16 = pd.read_csv("GB-RFI-NW-V016.csv")

# 2. EXTRACT FREQUENCY
dffreq = df1.iloc[44:677, 0].rename("Frequency")

# 3. EXTRACT AND REORDER AMPLITUDES
cols_in_order = [
    dffreq,
    df1.iloc[44:677,1].rename("N-H"),
    df2.iloc[44:677,1].rename("N-V"),
    df3.iloc[44:677,1].rename("NE-H"),
    df4.iloc[44:677,1].rename("NE-V"),
    df5.iloc[44:677,1].rename("E-H"),
    df6.iloc[44:677,1].rename("E-V"),
    df7.iloc[44:677,1].rename("SE-H"),
    df8.iloc[44:677,1].rename("SE-V"),
    df9.iloc[44:677,1].rename("S-H"),
    df10.iloc[44:677,1].rename("S-V"),
    df11.iloc[44:677,1].rename("SW-H"),
    df12.iloc[44:677,1].rename("SW-V"),
    df13.iloc[44:677,1].rename("W-H"),
    df14.iloc[44:677,1].rename("W-V"),
    df15.iloc[44:677,1].rename("NW-H"),
    df16.iloc[44:677,1].rename("NW-V")
]

# 4. COMBINE INTO FINAL DATAFRAME
df = pd.concat(cols_in_order, axis=1)
df = df.apply(pd.to_numeric, errors="coerce")
df = df.drop(df[df['Frequency'] <= 4e7].index)

clrs = ['lightcoral','red','darkorange','goldenrod','olive','gold','darkolivegreen','lawngreen',
        'mediumturquoise','dodgerblue','navy','slateblue','blueviolet','plum','purple','deeppink']

df.plot(x="Frequency", y=["N-H","N-V","NE-H","NE-V","E-H","E-V","SE-H","SE-V","S-H","S-V","SW-H","SW-V","W-H","W-V","NW-H","NW-V"], linewidth=0.5, color=clrs)
plt.ylabel('Amplitude dB', fontsize=12, fontweight="bold")
plt.xlabel('Frequency Hz', fontsize=12, fontweight="bold")
plt.ylim(-110, 10)
plt.title("RFI SIGNALS",fontsize=12, fontweight="bold", pad=20)
plt.gca().legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=10)
plt.grid(True, which="both", linestyle="--", alpha=0.5)  
plt.savefig("RFISIGNALS.png", dpi=1080, bbox_inches="tight")
plt.show()



# ==========================================
# PART II: Updated Polar Plot
# ==========================================

# 1. LABELS AND EXACT ANGLES
labels = ["N-H","N-V","NE-H","NE-V","E-H","E-V","SE-H","SE-V","S-H","S-V","SW-H","SW-V","W-H","W-V","NW-H","NW-V"]
theta_degrees = [0,0,45,45,90,90,135,135,180,180,225,225,270,270,315,315]
label_to_theta = {lbl: np.radians(deg) for lbl, deg in zip(labels, theta_degrees)}

# Color polarization: Blue = H, Orange = V
polarization_colors = ['blue' if '-H' in label else 'orange' for label in labels]

real_maxamp = df[labels].max()
maxamp = real_maxamp + 80  # Shift values to be positive for the polar plot

max_idx = np.argmax(maxamp)
max_label = labels[max_idx]
max_theta = label_to_theta[max_label]
max_r = maxamp.iloc[max_idx]
max_r_real = real_maxamp.iloc[max_idx]

fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(projection='polar')

# Transparent figure background
fig.patch.set_alpha(0.0)
ax.set_facecolor('none')

# Annotate strongest signal
label_angle = max_theta
label_radius = max_r + 2.5

ax.text(label_angle, label_radius,
        f"{max_label}\n({max_r_real:.1f} dB)",
        ha='center', va='bottom',
        fontsize=12, fontweight="bold",
        color='blue' if '-H' in max_label else 'green')

# Polar styling
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rlabel_position(135)
ax.set_title("Maximum RFI Amplitude by Direction", fontsize=12, fontweight="bold", pad=20)
ax.grid(color='gray', linestyle="--", linewidth=0.5)

# Add compass labels perfectly on the outer edge
compass_labels = ["N","NE","E","SE","S","SW","W","NW"]
ax.set_xticks(np.linspace(0, 2*np.pi, 8, endpoint=False))
ax.set_xticklabels(compass_labels, color="red", fontweight="bold", fontsize=18)
ax.tick_params(axis='x', pad=10)  # Adds a little padding between the radar edge and the letters

# Build peak info
peak_info = []
for label in labels:
    series = df[label]
    amp = series.max()
    freq = df.loc[series.idxmax(), 'Frequency']
    peak_info.append((label, amp, freq))

# Sort from highest to lowest amplitude
peak_info_sorted = sorted(peak_info, key=lambda x: x[1], reverse=True)

# Identify RFI sources
def identify_rfi_source(freq_hz):
    freq_mhz = freq_hz / 1e6
    
    if 87 <= freq_mhz <= 108:
        return "FM Radio"
    elif 108 < freq_mhz <= 137:
        return "Aviation / Airband"
    elif 137 < freq_mhz < 174:
        return "VHF / Land Mobile / Amateur"
    elif 174 <= freq_mhz <= 230:
        return "VHF TV"
    elif 470 <= freq_mhz <= 862:
        return "UHF TV"
    elif 862 < freq_mhz <= 960:
        return "Cellular (2G / Low-Band LTE)"
    elif 1500 <= freq_mhz <= 1610:
        return "GPS / Sat Comms"
    elif 1700 <= freq_mhz <= 2200:
        return "Cellular (3G / 4G LTE / PCS)"
    elif 2300 <= freq_mhz < 2400:
        return "Cellular (LTE) / Amateur"
    elif 2400 <= freq_mhz <= 2500:
        return "Wi-Fi / Bluetooth"
    elif 2500 <= freq_mhz <= 2690:
        return "Cellular (4G LTE / 5G)"
    elif 5100 <= freq_mhz <= 5900:
        return "5 GHz Wi-Fi / Radar"
    elif freq_mhz > 6000:
        return "High-band Radar / Sat"
    else:
        return "Unknown / Local Device"

print("\n📡 RFI Source Summary by Direction:")
for label, amp, freq in peak_info_sorted:
    source = identify_rfi_source(freq)
    print(f"{label:<6}: {amp:>6.1f} dB at {freq/1e6:>7.2f} MHz → {source}")

ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

# --- THE NEW DRAWING METHOD ---
# We loop through `peak_info_sorted` (Highest Amplitude to Lowest).
# This guarantees that the longest stems are drawn underneath, 
# and the shorter dots are layered beautifully on top of them!
for label, amp, freq in peak_info_sorted:
    line_color = 'blue' if label.endswith('-H') else 'orange'
    current_theta = label_to_theta[label]
    
    ax.plot([current_theta, current_theta], [0, maxamp[label]],
            color=line_color,
            linewidth=4.5,
            marker='o',
            markersize=3,   # Slightly larger dot to ensure it covers the line beneath
            alpha=0.9,
            solid_capstyle='round',
            zorder=3)

# Adds a 5-unit visual buffer beyond your longest line
ax.set_ylim(0, max_r + 5)
#ax.set_ylim(0, 80) 

plt.tight_layout()
plt.savefig("RFIPOLARPOINTS.png", dpi=1080, bbox_inches="tight", transparent=True)
plt.show()


# ==========================================
# PART III: RFI Sources Bar Chart
# ==========================================

peak_df = pd.DataFrame(peak_info_sorted, columns=["Direction", "Amplitude", "Frequency"])
peak_df["Frequency_MHz"] = peak_df["Frequency"] / 1e6
peak_df["Source"] = peak_df["Frequency"].apply(identify_rfi_source)
peak_df = peak_df.sort_values(by="Amplitude", ascending=False)

source_list = peak_df["Source"].unique()

# Define the exact vibrant colors from the Set3 palette (Teal, Yellow, Red/Salmon, etc.)
vibrant_colors = ['#8dd3c7', '#ffffb3', '#fb8072', '#bebada', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']

# Map these specific colors directly to your sources
source_color_map = {src: vibrant_colors[i % len(vibrant_colors)] for i, src in enumerate(source_list)}
peak_df["Color"] = peak_df["Source"].map(source_color_map)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars with a darkgray edge for better definition
bars = ax.barh(peak_df["Direction"], peak_df["Amplitude"], color=peak_df["Color"], edgecolor='darkgray')

# Place text inside the bars perfectly aligned
for _, row in peak_df.iterrows():
    ax.text(row["Amplitude"] + 1, row["Direction"], 
            f'{row["Frequency_MHz"]:.1f} MHz\n{row["Source"]}', 
            va='center', ha='left', fontsize=8, color='black')

ax.invert_yaxis()
ax.set_xlabel("Max Amplitude (dB)", fontsize=12)
ax.set_title("Identified RFI Sources by Direction", fontsize=12, fontweight=0.5)
ax.grid(True, which="both", linestyle="--", alpha=0.5)

# Create the custom legend using the mapped colors
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label=src, 
           markerfacecolor=clr, markeredgecolor='darkgray', markersize=10)
    for src, clr in source_color_map.items()]

ax.legend(handles=legend_elements, title="RFI Source", loc='lower right', frameon=True, fontsize=12)

plt.tight_layout()
plt.savefig("RFISOURCES.png", dpi=1080, bbox_inches="tight")
plt.show()

