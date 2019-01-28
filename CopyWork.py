#! python3
# CopyWork.py - A script to automate copying for Castleberry Dental

import pyperclip
import sys
from pprint import pprint

COPYPASTE = {'1': 'Patient Information',
             '2': 'Informed Consent Endodontic',
             '3': 'Financial and Broken',
             '4': 'Consent for Oral Surgery Pg. 1 of 2',
             '5': 'Dental Implant Consent Form pg. 1 of 2',
             '6': 'Referral Sheet',
             '7': 'Medical History',
             '8': 'Patient Registration'}


while True:
    print('Input a number relating to the Copy and Paste Sheet value you want (9 to quit)')
    cmd = input()
    if cmd == '1':
        pyperclip.copy('Patient Information')
        pyperclip.paste()
    elif cmd == '2':
        pyperclip.copy('Informed Consent Endodontic')
        pyperclip.paste()
    elif cmd == '3':
        pyperclip.copy('Financial and Broken')
        pyperclip.paste()
    elif cmd == '4':
        pyperclip.copy('Consent for Oral Surgery Pg. 1 of 2')
        pyperclip.paste()
    elif cmd == '5':
        pyperclip.copy('Dental Implant Consent Form pg. 1 of 2')
        pyperclip.paste()
    elif cmd == '6':
        pyperclip.copy('Referral Sheet')
    elif cmd == '7':
        pyperclip.copy('Medical History')
    elif cmd == '8':
        pyperclip.copy('Patient Registration')
    elif cmd == '9':
        break
    else:
        print('please input a valid value')