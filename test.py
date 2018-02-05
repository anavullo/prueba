import pandas as pd
import numpy as np

from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

dem = pd.read_table('DemCorr.txt', header=None, skiprows=6, delim_whitespace=True, na_values=-9999)

plt.figure('dem')
plt.grid(False)
plt.imshow(dem)
plt.show()

	