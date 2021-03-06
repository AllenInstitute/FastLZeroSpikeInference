from FastLZeroSpikeInference import fast
import numpy as np

gam = 0.98
y = np.power(gam, np.concatenate([np.arange(100), np.arange(100)]))

# Basic fit, no calcium concentration estimated
fit = fast.estimate_spikes(y, gam, 1, False)

# Determine calcium concentration from fit
fit = fast.estimate_calcium(fit)

# Estimate both spikes and calcium concentration
fit = fast.estimate_spikes(y, gam, 1, False, True)
