import pip
ip = pip.get_installed_distributions()
ipl = sorted(["%s==%s" % (i.key, i.version)
	for i in ip])
print(ipl)