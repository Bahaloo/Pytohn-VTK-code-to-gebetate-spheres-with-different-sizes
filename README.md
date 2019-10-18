# Pytohn-VTK-code-to-gebetate-spheres-with-different-sizes
Uses VTK in Python to plot a glyph 3D of spheres with input coordinates and different radii (sizes)
This code used the ability of VTK to visualize multiple spheres with different sizes. The location and the
radii of spheres were given as a vtkPoints and vtkFloatArrays respectively. Then these two are imported into 
a vtkPolyData and a Glyph was constructed accordingly. Note that to be able to scale the spheres to read the
radii from the provided vtkFloatArray, we needed to include:

g.ScalingOn()
g.SetScaleModeToScaleByScalar()
g.SetVectorModeToUseVector()
g.ClampingOn()


which "g." stands for "glyph.". Also note that we used m.SetInputData(poly) instead of 
using mapper.SetInputConnection(g.GetOutputPort()). 
