#!/usr/bin/python

import en
import sys

went = 'went'
going = 'going'
gone = 'gone'
goes = 'goes'

print "Content-Type: text/html"
print
print "<html><head><title>Stack Overflow answer</title></head><body>"
print ' The present tense of <b>',going, '</b> is <i>',en.verb.present(going),'</i><br>'
print ' The present tense of <b>',goes, '</b> is <i>',en.verb.present(goes),'</i><br>'
print ' The present tense of <b>',gone, '</b> is <i>',en.verb.present(gone),'</i><br>'
print ' The present tense of <b>',went, '</b> is <i>',en.verb.present(went),'</i><br>'
print "</body></html>"