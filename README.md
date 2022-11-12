# IKEA Tags project

## Running

Place a file of choice called `in.csv`, which should have the following columns

```csv
top_text,title,sub_title,item_1,item_2,item_3,item_4,item_5,designer,price,valuta
```

```bash
python main.py
```

to compile

```bash
pdflatex  -synctex=1 -interaction=nonstopmode -file-line-error -recorder  out.tex
```
