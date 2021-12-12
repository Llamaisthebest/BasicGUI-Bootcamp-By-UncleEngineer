# WriteFile

from datetime import datetime

def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543)
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'Date&Time: {} Food: {} kg. Pay {:,.2f} Bath'.format(stamp,quantity,total))


# writetext(90,9000)
# writetext(91,9100)
# writetext(92,9200)
# writetext(93,9300)