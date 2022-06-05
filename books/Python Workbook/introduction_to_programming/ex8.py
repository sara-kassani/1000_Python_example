# exercise 8: Widget and Gizmos

widget_weight_gr = 75
gizmo_weight_gr = 112
widgets = int(input('number of widgets in the order: '))
gizmos = int(input('number of gizmos in the order: '))
tot_weight_kg = float((widgets*widget_weight_gr + gizmos*gizmo_weight_gr) / 1000)
print("the order's weight is %.3f kg" % tot_weight_kg)
