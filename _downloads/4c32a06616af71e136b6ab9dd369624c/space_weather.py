"""
Space Weather
=============

Plotting the :math:`K_p`, :math:`A_p`, and F10.7 space weather indices
"""

import os
import pyspaceaware as ps
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# %%
# Loading the space weather file and extracting the dates and indices
sw_file_path = os.path.join(os.environ["DATADIR"], "SW-Last5Years.csv")
sw_df = pd.read_csv(sw_file_path, header=0)
dates = [datetime.datetime.strptime(x, "%Y-%m-%d") for x in sw_df["DATE"]]
f107 = sw_df["F10.7_ADJ"]
ap = sw_df["AP_AVG"]
kp = sw_df["KP_SUM"]

# %%
# Plotting F10.7 radio flux
plt.scatter(dates, f107, s=1)
ps.texit("F10.7 Radio Flux at 1 AU", "Date", "F10.7")
plt.show()

# %%
# Plotting the geomagnetic index :math:`K_p`
plt.scatter(dates, ap, s=1)
ps.texit("Equivalent Amplitude $A_p$", "Date", "$A_p$")
plt.show()

# %%
# Plotting the geomagnetic index :math:`K_p`
plt.scatter(dates, kp, s=1)
ps.texit("Range Index $K_p$", "Date", "$K_p$")
plt.show()

# %%
# Reference for the CSV format found `at CelesTrak <https://celestrak.org/SpaceData/SpaceWx-format.php>`_