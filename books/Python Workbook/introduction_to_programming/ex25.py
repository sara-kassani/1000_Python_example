# exercise 25: Units of Time (Again)

tot_sec = int(input('insert number of seconds: '))
# dividing the seconds in total by the seconds in a day (86400), getting the number of days (with decimals)
dd_floating = tot_sec / 86400
# to get the number of days as integer, I use int
dd = int(dd_floating)

# multiplying the difference between "decimal day" and "integer day" by 24, namely the hours
# in this way I get the hours (with decimals)
hh_floating = (dd_floating - dd) * 24
# same logic to get the actual hours (no decimals), using int
hh = int(hh_floating)

# this time I multiply the difference between "decimal hours" and "integer hours" by 60, to find minutes
mm_floating = (hh_floating - hh) * 60
mm = int(mm_floating)

ss_floating = (mm_floating - mm) * 60
ss = int(ss_floating)

# note that writing %02d means that the number will have anyway two elements (e.g. 01, 02, etc.)
print("%d:%02d:%02d:%02d" % (dd, hh, mm, ss))
