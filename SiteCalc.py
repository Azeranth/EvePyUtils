from time import strftime
from time import gmtime

gasSiteMap = {
	"Barren" : [["50", 6000], ["60", 3000]],
	"Token" : [["60", 6000], ["70", 3000]],
	"Minor" : [["70", 6000], ["72", 6000]],
	"Ordinary" : [["72", 12000], ["84", 6000]],
	"Sizable" : [["84", 12000], ["50", 3000]],
	"Bountiful" : [["28", 20000], ["32", 4000]],
	"Vast" : [["32", 50000], ["28", 10000]],
	"Instrumental" : [["320", 60000], ["540", 10000]],
	"Vital" : [["540", 120000], ["320", 5000]]}
	
priceMap = {
	"50" : 5551,
	"60" : 2107,
	"70" : 3250,
	"72" : 4701,
	"84" : 2473,
	"28" : 4601,
	"32" : 3488,
	"320" : 7982,
	"540" : 5342}

harvestVol = 40
cycleTime = 22.5
harvestRate = harvestVol/cycleTime
cargoVol = 10000

print(str(harvestVol) + " m3/cycle\t@ " + str(cycleTime) +" cycle/sec\t = " + "{:,.2f}".format(harvestRate) + " m3/sec")
print(str(cargoVol) + " m3\t@ " + "{:,.2f}".format(harvestRate) + " m3/sec\t= " + strftime("%H Hours, %M Minutes, %S Seconds", gmtime(cargoVol/harvestRate))  + " ({:,.2f} seconds)".format(cargoVol/harvestRate))
for site in gasSiteMap:
	print(site + " Perimeter Resevoir:")
	for gas in gasSiteMap[site]:
		print("\tFullerite-C"  + gas[0] + "\t" + str(gas[1]) + " m3\t@ " + str(priceMap[gas[0]]) + " ISK/m3\t= " + str(priceMap[gas[0]] * gas[1]) + " ISK")
		print("\t\t" + strftime("%H Hours, %M Minutes, %S Seconds", gmtime(gas[1]/harvestRate)) + "\t@ " + "{:,.2f}".format(priceMap[gas[0]]*harvestRate*3600) + " ISK/hour")
		print("\t\t" + "{:,.2f}".format(gas[1]/cargoVol) + " Loads\t@ " + "{:,.2f}".format(priceMap[gas[0]]*cargoVol) + " ISK/Load")