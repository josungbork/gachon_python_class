f = open("yesterday.song", 'r') 
yesterday_lyric = ""
while 1: 
	line = f.readline()
	if not line: break 
	yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

n_of_yesterday = yesterday_lyric.count("Yesterday")
n2_of_yesterday = yesterday_lyric.count("yesterday")
print "Number of A Word 'Yesterday'" , n_of_yesterday
print "Number of A Word 'yesterday'" , n2_of_yesterday
