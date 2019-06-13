#!/usr/bin/env python


class LineIO(object):
	def __iter__(self):
		return self

	def __next__(self):
		raise StopIteration


def main():
	# Do nothing but raise an error
	raise 'This script should not be the launcher'

if __name__ == '__main__':
	main()
