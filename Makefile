# download datasets
.PHONY: all
all: mystringdb.txt myensembldb.txt degree_boxplot.png

mystringdb.txt:
	curl https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz | gunzip > mystringdb.txt

myensembldb.txt:
	curl -L https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex > myensembldb.txt 
 
degree_boxplot.png: degree_boxplot.py
	python degree_boxplot.py
