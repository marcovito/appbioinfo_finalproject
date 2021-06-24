string_link = https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
ensembl_link = https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex

# download datasets
.PHONY: all
all: mystringdb.txt myensembldb.txt degree_barplot.png

mystringdb.txt:
	curl https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz | gunzip >> mystringdb.txt

myensembldb.txt:
	curl -L https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex >> myensembldb.txt 
 
degree_barplot.png: degree_barplot.py
	python degree_barplot.py
