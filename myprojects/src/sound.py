'''
Created on 23/11/2012

@author: Andreas M
'''
import winsound, sys

def beep(sound):
    winsound.PlaySound('%s.wav' % sound, winsound.SND_FILENAME)

if __name__ == '__main__':
    beep(sys.argv[1])