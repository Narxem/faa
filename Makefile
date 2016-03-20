
rapport.pdf : README.md
	pandoc -o $@ $< -f markdown_github

clean : 
	rm -f rapport.pdf