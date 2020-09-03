## voyager1 
dagar_str=input("Number of days after 9/25/09: ")
dagar_int=int(dagar_str)
v_mile=38241 #miles/hour
l_mile=16637000000  # upphafvegalengd
length_mile=v_mile*dagar_int*24
length_mile_all=length_mile+l_mile

l_km=l_mile*1,609344 # upphafsvegalengd breytt í km
l_AU=l_mile*92955887,6 # upphafsvegalengd breytt í AU
length_km=length_mile*1,609344
length_AU=length_mile*92955887,6
length_km_all=length_km+l_km
length_AU_all=length_AU+l_AU
#
km=round(length_km_all)
AU=round(length_AU_all)
print("Miles from the sun:",length_mile_all)
print("Kilometers from the sun:",km)
print("AU from the sun:",AU)
