#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Note: This is a modification on: https://public.kitware.com/pipermail/vtkusers/2002-December/014959.html
from vtk import *

p = vtkPoints()
p.SetNumberOfPoints(5)
p.SetPoint(0, [0., 0., 0.])
p.SetPoint(1, [.5, 0., 0.])
p.SetPoint(2, [0., 1., 0.])
p.SetPoint(3, [0., 0., 1.])
p.SetPoint(4, [1., 1., 1.])

l = vtkCellArray()
l.Allocate(6, 6)

l.InsertNextCell(2)
l.InsertCellPoint(0)
l.InsertCellPoint(1)

l.InsertNextCell(2)
l.InsertCellPoint(0)
l.InsertCellPoint(2)

l.InsertNextCell(2)
l.InsertCellPoint(0)
l.InsertCellPoint(3)

l.InsertNextCell(2)
l.InsertCellPoint(1)
l.InsertCellPoint(4)

l.InsertNextCell(2)
l.InsertCellPoint(2)
l.InsertCellPoint(4)

l.InsertNextCell(2)
l.InsertCellPoint(3)
l.InsertCellPoint(4)

col = vtkIntArray()
col.SetNumberOfComponents(1)
col.InsertNextTuple1(0)
col.InsertNextTuple1(1)
col.InsertNextTuple1(2)
col.InsertNextTuple1(3)
col.InsertNextTuple1(4)
col.SetName('col')

sizes = vtkFloatArray()
sizes.SetNumberOfComponents(1)
sizes.InsertNextTuple1(.1)
sizes.InsertNextTuple1(.2)
sizes.InsertNextTuple1(.12)
sizes.InsertNextTuple1(.6)
sizes.InsertNextTuple1(.5)
sizes.SetName('sizes')

poly = vtkPolyData()
poly.SetPoints(p)
poly.SetLines(l)
#poly.GetPointData().AddArray(col)
poly.GetPointData().AddArray(sizes)

# If I use this, I can scale the glyphs
poly.GetPointData().SetScalars(sizes)

# look table (red/green/blue/gray/yellow)
t = vtkLookupTable()
t.SetNumberOfColors(5)
t.Build()
t.SetTableValue(0, 1, 0, 0, 1)
t.SetTableValue(1, 0, 1, 0, 1)
t.SetTableValue(2, 0, 0, 1, 1)
t.SetTableValue(3, .5, 0.5, 0.5, 1)
t.SetTableValue(4, 1, 1, 0, 1)

m = vtkPolyDataMapper()
m.SetInputData(poly)
m.SetScalarRange(0.0, 4.0)
m.SetLookupTable(t)
# this seems to work
m.SetScalarModeToUsePointFieldData()
m.ColorByArrayComponent('col', 0)

#
# Add sphere glyphs
#
s = vtkSphereSource()
s.SetThetaResolution(36)
s.SetPhiResolution(36)
s.Update()
g = vtkGlyph3D()
g.SetInputData(poly)
g.SetSourceConnection(s.GetOutputPort())

g.SetColorModeToColorByScalar()

g.ScalingOn()
g.SetScaleModeToScaleByScalar()
g.SetVectorModeToUseVector()
g.ClampingOn()

m = vtkPolyDataMapper()
m.SetInputConnection(g.GetOutputPort())
m.SetScalarRange(0.0, 4.0)

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(g.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)

ren = vtkRenderer()
ren.SetBackground(0.2, 0.5, 0.3)
ren.AddActor(actor)

renwin = vtk.vtkRenderWindow()
renwin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
iren.SetRenderWindow(renwin)

renwin.Render()
iren.Initialize()
renwin.Render()
iren.Start()