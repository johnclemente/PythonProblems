import re
Consonant = '[bcdfghjklmnpqrstvwrxyz]'
Vowel = '[aeiou]'
String =  'if you take my hand ill march in the band'
print String
String = re.sub(Consonant , '0' , String)
print String
String = re.sub(Vowel , '1' , String)
print String


