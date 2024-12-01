import re
import hashlib


SALT = 'qzyelonm'
SALT_sample = 'abc'
KEY_STRETCH = 2016


def stretch_key(s, stretch_val):
    md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
    while stretch_val > 0:
        md5 = hashlib.md5(md5.encode('utf-8')).hexdigest()
        stretch_val -= 1
    return md5


def day14(salt):
   triple = re.compile(r'(\w)\1{2}')
   quintuple = re.compile(r'(\w)\1{4}')
  
   keys = set()
   i = 0

   # Pulls extra keys to be on the safe side.
   while len(keys) < 75:
       a = stretch_key(salt + str(i), KEY_STRETCH)
       a_m = quintuple.findall(a)
       for q in set(a_m):
           for j in range(max(i-1000, 0), i):
               b = stretch_key(salt + str(j), KEY_STRETCH)
               b_m = triple.search(b)
               if b_m and q == b_m.group(1):
                   keys.add(j)
                

       i += 1
   print(sorted(keys))
   return sorted(keys)[63]

#print('Sample: %d' % day14(SALT_sample))
print('Challenge: %d' % day14(SALT))