import urllib.request

for i in range(1,10000):
	print("getting "+str(i))
	urllib.request.urlretrieve("https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq="+str(i), str(i)+".png")