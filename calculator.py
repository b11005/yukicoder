#!/usr/bin/env python3
# -*- coding; UTF-8 -*-

import time

@profile #to use memory_profile 
def main():
    #N = map(int, input().split())
    print (sum([int(i) for i in input().split()]))




if __name__ == '__main__':
	#start = time.time()
    main()
    #print('{} [ms]'.format(1000 * time.time() - start))