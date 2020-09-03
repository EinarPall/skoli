d_str = input( 'Number of days after 9/25/09: ')
d = int(d_str)

vega = 16637000000 #Mílur í heildina
hradi = 917784 # Mílur á dag
km=1.609344
AU=92955887.6

færsla=hradi*d #Dagar * hraði á dag
vegalengd=færsla+vega # færsla + fyrri vegalengd

vegalengdkm=(vegalengd*km) #Vegalengd í km
vegkm=round(vegalengdkm) #Vegalengd í km námundað

vegalengdau=(vegalengd/AU) #Vegalengd í AU
vegau=round(vegalengdau) #Vegalengd í AU námundað

print("Miles from the sun: ", vegalengd) 
print("Kilometers from the sun: ", vegkm)
print("AU from the sun: ", vegau)
