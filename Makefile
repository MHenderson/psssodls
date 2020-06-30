doc:
	pdoc --html psssodls --html-dir public
	mv public/psssodls/index.html public/index.html
	rm -rf public/psssodls
