from datetime import datetime
date_format="%d.%m.%Y"
upphafs_dagsetning=datetime.strptime('25.9.2009', date_format)
mfs=16637000000
mph=38241
mpd=mph*24
dagsetning=datetime.strptime(input('Skrifaðu niður dagsetningu dagsins í dag á forminu D/M/Y: '), date_format)
delta_dagsetning=dagsetning-upphafs_dagsetning
miles=mfs+mpd*delta_dagsetning.days
round_miles=round(miles)
print("Fjarlægð frá sól er:", round_miles, "mílur")
kilometers=miles*1.609344
round_kilometers=round(kilometers)
print("Fjarlægð frá sól er:", round_kilometers, "kílómetrar")
AU=miles/92955887.6
round_AU=round(AU)
print("Fjarlægð frá sól er:", round_AU, "stjarnfræðilegar einingar")
