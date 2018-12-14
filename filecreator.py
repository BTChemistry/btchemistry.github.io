numbers_of_topics = []
month = "10"
day = 3
for x in range(15):
    day_output = day + x
    day_output = str(day_output)
    f = open("2018-" + month + "-" + day_output + "-.md","w+")
