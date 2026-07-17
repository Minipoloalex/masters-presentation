import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

input_file = "figures/example_svm_selection.png"
output_file = "figures/example_svm_selection_with_legend.png"

img = plt.imread(input_file)
height, width = img.shape[:2]

dpi = 100
fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])

ax.imshow(img)
ax.axis("off")

# Replace these labels with the correct terminology.
legend_items = [
    Line2D(
        [], [],
        marker="o",
        linestyle="none",
        markerfacecolor="#0877D1",
        markeredgecolor="none",
        markersize=18,
        label="CLK",
    ),
    Line2D(
        [], [],
        marker="o",
        linestyle="none",
        markerfacecolor="#EA8AF4",
        markeredgecolor="none",
        markersize=18,
        label="LKCC",
    ),
    # Line2D(
    #     [], [],
    #     color="red",
    #     linewidth=2,
    #     linestyle="-",
    #     label="Selection boundary",
    # ),
    # Line2D(
    #     [], [],
    #     color="red",
    #     linewidth=2,
    #     linestyle="--",
    #     label="Boundary limits",
    # ),
]

ax.legend(
    handles=legend_items,
    loc="upper right",
    bbox_to_anchor=(0.98, 0.98),
    frameon=True,
    facecolor="white",
    edgecolor="0.7",
    framealpha=0.95,
    fontsize=25,
    borderpad=0.7,
    labelspacing=0.6,
    handletextpad=0.6,
)

# Avoid bbox_inches="tight", which can change the image dimensions.
fig.savefig(output_file, dpi=dpi)
plt.close(fig)
