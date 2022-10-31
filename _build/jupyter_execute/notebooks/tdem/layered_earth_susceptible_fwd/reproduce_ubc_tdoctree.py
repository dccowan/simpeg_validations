#!/usr/bin/env python
# coding: utf-8

# Reproduce: UBC-GIF OcTree
# =======================
# 
# ## Simulating Transient TEM Data over a Conductive and Susceptible Layered Earth
# 
# Transient TEM data are simulated over a conductive 1D layered Earth. The Earth consists of 3 layers all with electrical conductivities of $\sigma_1$ = $\sigma_2$ = $\sigma_3$ = 0.01 S/m. From the top layer down we define magnetic susceptibilities of $\chi_1$ = 0 SI, $\chi_2$ = 9 SI and $\chi_3$ = 0 SI for the layers. The thicknesses of the top two layers are both 64 m.
# 
# The transient response is simulated for x, y and z oriented magnetic dipoles at (0, 0, 5). The x, y and z components of H and dB/dt are simulated at (10, 0, 5). However, we only plot the data for horizontal coaxial, horizontal coplanar and vertical coplanar geometries.

# ## UBC-GIF Package Details
# 
# There are two packages capable of modeling TEM data on OcTree meshes. These are:
# 
# **UBC TD Octree v1:** [TD OcTree v1](https://tdoctree.readthedocs.io/en/tdoctree_v1/) is a voxel cell TDEM forward modeling and inversion package developed by the UBC Geophysical Inversion Facility. This software is proprietary and can ONLY be acquired through appropriate [academic](https://gif.eos.ubc.ca/software/licenses_academic) or [commerical](https://gif.eos.ubc.ca/software/licenses_commercial) licenses. The numerical approach of the forward simulation is described in the [online manual's theory section](https://tdoctree.readthedocs.io/en/tdoctree_v1/content/theory.html). If you have a valid license, there are instructions for reproducing the results (add link).
# 
# **UBC TD Octree v2:** [TD OcTree v2](https://tdoctree.readthedocs.io/en/tdoctree_v2/) is a voxel cell TDEM forward modeling and inversion package developed by the UBC Geophysical Inversion Facility. This software is proprietary and can ONLY be acquired through appropriate [academic](https://gif.eos.ubc.ca/software/licenses_academic) or [commerical](https://gif.eos.ubc.ca/software/licenses_commercial) licenses. The numerical approach of the forward simulation is described in the [online manual's theory section](https://tdoctree.readthedocs.io/en/tdoctree_v2/content/theory.html). If you have a valid license, there are instructions for reproducing the results (add link).

# ## Running the Forward Simulation

# ### Step 1: Acquiring a commercial or academic license.
# 
# - Explain and link to where you would get licenses. Make ABSOLUTELY CLEAR we don't just give out the licenses willy-nilly.

# ### Step 2: Downloading and extracting assets
# 
# - Link and instructions for download

# ### Step 3: Running the forward modeling executable
# 
# - Brief description of what files are needed
# - Link to the manual page where we run the forward simulation

# In[ ]:




