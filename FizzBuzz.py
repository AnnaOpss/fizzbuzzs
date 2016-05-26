import base64

result = [x for x in range(1, 20+1)]
for n in result:
	if n%3 == 0 and n%5 == 0: result[n-1] = 'FizzBuzz'
	elif n%3 == 0: result[n-1] = 'Fizz'
	elif n%5 == 0: result[n-1] = 'Buzz'
print result


for n in range(1, 20+1):
	if n%3 == 0 and n%5 == 0: print 'FizzBuzz'
	elif n%3 == 0: print 'Fizz'
	elif n%5 == 0: print 'Buzz'
	else: print n

# TODO replace CracklePop to FizzBuzz
print "\\n".join('CracklePop' if y%3 == 0 and y%5 == 0 else ('Crackle' if y%3 == 0 else ('Pop' if y%5 == 0 else str(y))) for y in range(1, 100+1)) #  \xe8\x0c\xb8skd

s1 = "IlxuIi5qb2luKCdDcmFja2xlUG9wJyBpZiB5JTMgPT0gMCBhbmQgeSU1ID09IDAgZWxzZSAoJ0NyYWNrbGUnIGlmIHklMyA9PSAwIGVsc2UgKCdQb3AnIGlmIHklNSA9PSAwIGVsc2Ugc3RyKHkpKSkgZm9yIHkgaW4gcmFuZ2UoMSwgMTAwKzEpKSAjICAg6Ay4c2tk"
x = (8, 20, 103, 52, 192, 162, 8, 192, 162, 14, 52, 16, 71, 14, 52)
print eval(getattr(__import__(''.join(s1[n] for n in x[:6])), ''.join(s1[n] for n in x[6:]))(s1))

s = (73, 108, 120, 117, 73, 105, 53, 113, 98, 50, 108, 117, 75, 67, 100, 68, 99, 109, 70, 106, 97, 50, 120, 108, 85, 71, 57, 119, 74, 121, 66, 112, 90, 105, 66, 53, 74, 84, 77, 103, 80, 84, 48, 103, 77, 67, 66, 104, 98, 109, 81, 103, 101, 83, 85, 49, 73, 68, 48, 57, 73, 68, 65, 103, 90, 87, 120, 122, 90, 83, 65, 111, 74, 48, 78, 121, 89, 87, 78, 114, 98, 71, 85, 110, 73, 71, 108, 109, 73, 72, 107, 108, 77, 121, 65, 57, 80, 83, 65, 119, 73, 71, 86, 115, 99, 50, 85, 103, 75, 67, 100, 81, 98, 51, 65, 110, 73, 71, 108, 109, 73, 72, 107, 108, 78, 83, 65, 57, 80, 83, 65, 119, 73, 71, 86, 115, 99, 50, 85, 103, 99, 51, 82, 121, 75, 72, 107, 112, 75, 83, 107, 103, 90, 109, 57, 121, 73, 72, 107, 103, 97, 87, 52, 103, 99, 109, 70, 117, 90, 50, 85, 111, 77, 83, 119, 103, 77, 84, 65, 119, 75, 122, 69, 112, 75, 83, 65, 106, 73, 67, 65, 103, 54, 65, 121, 52, 99, 50, 116, 107, 8, 20, 103, 52, 192, 162, 8, 192, 162, 14, 52, 16, 71, 14, 52)
print eval(getattr(__import__(''.join(''.join(map(chr, s[:200]))[n] for n in s[200:206])), ''.join(''.join(map(chr, s[:200]))[n] for n in s[206:]))(''.join(map(chr, s[:200]))))


print eval(base64.b64decode(s1))
