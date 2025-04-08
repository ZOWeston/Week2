import matplotlib.pyplot as plot
# set up your lists
numlist = [2, 4, 10, 8]
namelist = ['RED', 'GREEN', 'PINKERTON', 'BLUE']
colorlist = ['red', 'green', 'black', 'yellow' ]
explodelist = [0.0, 0.0, 0.1, 0.1]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.4f%%', colors=colorlist,
    	explode = explodelist, startangle = 180)
plot.axis('equal')
plot.savefig('piechart.png')

