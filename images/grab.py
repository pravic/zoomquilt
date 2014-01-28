D = "FUjD9hf gbHhxTR 8YyzJdR xP3aNkR 2Qi4fQr E6pW5Ky zmtWIBF Af7LtYp TuXy30d 3nKGLr2 hNoWscB mSBvv3K f4wJ70e mIt9XmM M4TkAyh P4L4qhd hNM6bTv VoT8JXM jqcGH0B DYVoN8n bOPQkOI NeaTfJ1 18ppMNr FZ3d8Jv HsoX2RP mjv4kzI 6rpJbef pySKauq WjNQYRV Ffooo8y Xei5XfD T5A415r LiV0VNB nGcwiO4 b1Gdjjy GE828iy eSQ7SLe 1mPyGgL GNtwJIr KxBlU7E aKXhms5 9Quu2wu Y07quDf r0yC5Qa 273fCkD 2wMyCUw FUjD9hf".split(" ");
print("@rem %d images" % len(D))
for a in range(len(D)):
	print("wget -q -O %02d.jpg http://imgur.com/%s.jpg" % (a, D[(20 + a) % 46]))
