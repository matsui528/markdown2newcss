# Markdown To new.css

Convert a plain markdown to an HTML with [new.css](https://github.com/xz/new.css).

## [Demo](https://matsui528.github.io/markdown2newcss/)

## Getting started
```bash
git clone https://github.com/matsui528/markdown2newcss.git
cd markdown2newcss
pip install -r requirements.txt
# Read sample/index.md and create index.html
python markdown2newcss.py --body sample/index.md --header sample/header.md --out index.html --title index
# Read sample/usage.md and create usage.html
python markdown2newcss.py --body sample/usage.md --header sample/header.md --out usage.html --title usage
# Now you can open index.html and usage.html
```

## How to use
1. Write a markdown file for a header. Let's say `my_header.md`. See [sample/header.md](sample/header.md) for details.
1. Write a markdown file for a body.  Let's say `my_website.md`. See [sample/index.md](sample/index.md) for details.
1. Run the following and generate `my_website.html`.
    ```bash
    python markdown2newcss.py --body my_website.md --header my_header.md --out my_website.html --title my_website
    ```

## Contribute
Feel free to open a pull request :smile:

## Author
[@matsui528](https://github.com/matsui528)

