#!/usr/bin/env python

import sys
from LineIO import LineIO

class FileLineIO(LineIO):
	ST_OPEN = 1
	ST_CLOSED = 0
	def __init__(self, path, showProcess=True, singleLine=True):
		self.path = path
		self.fin = open(path, 'ro')
		self.showProcess = showProcess
		self.singleLine = singleLine
		if not self.fin:	raise IOError('Cannot open file for reading: %s' % path)
		if showProcess:
			sys.stdout.write('Reading file %s:%s' % (path, singleLine and '\n' or ''))
			sys.stdout.flush()

		self.status = FileLineIO.ST_OPEN
		self.linenum = 0

	def next(self):
		if self.status == FileLineIO.ST_CLOSED:
			raise StopIteration('Could not read lines from a closed file.')

		assert(self.fin)
		
		line = self.fin.readline()
		if not line:
			if self.showProcess:
				sys.stdout.write('\nDone.\n')
				sys.stdout.flush()
			self.status = FileLineIO.ST_CLOSED
			self.fin.close()
			raise StopIteration

		line = line[:-1]
		self.linenum += 1
		if self.showProcess:
			sys.stdout.write('%sLine %d: ' % (self.singleLine and '\r' or '\n', self.linenum))
			sys.stdout.flush()
		return line

	def __str__(self):
		status = self.status == FileLineIO.ST_OPEN and 'Open at position %d' % self.linenum or 'Closed'
		return '[FileLineIO <File %s>: %s]' % (self.path, status)


def main():
	#stream = FileLineIO('FileLineIO.py')
	#total = 0
	#for line in stream:
		#total += len(line)
		#print '\t%s' % line
		#print stream
	#print total
	#print stream
	#pass
	raise IOError('%s: Should not run from this script' % sys.argv[0])

if __name__ == '__main__':
	main()
