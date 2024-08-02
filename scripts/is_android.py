# By OrangeDog Team, MG30
# classes/is_android.py содержит функцию которая возвращяет 1 если системой является андроид.

import sys

def is_android():
	return int(hasattr(sys, 'getandroidapilevel'))