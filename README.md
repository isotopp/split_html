# split_html

```
$ split_html --help
Split a HTML file into chapters
Usage: split_html [OPTIONS] INFILE

Options:
  -c, --chapterstart INTEGER
  -t, --filetype TEXT
  --help                      Show this message and exit.
```

# Sample Usage

```
$ cat sample.html 
<!DOCTYPE html>
<html>
<head>
    <title>Some title</title>
</head>
<body>
<h1>The #^@! Beginning</h1>
<p>I am a paragraph</p>
<p>I am paragraph 2</p>
<h1>IN THE MIDDLE</h1>
<p>Just another random paragraph.</p>
<h1>Oh, No! It's the end!</h1>
<div>The closing paragraph.</div>
</body>
</html>
```

Call it like this:

```
$ cat sample.html 
<!DOCTYPE html>
<html>
<head>
    <title>Some title</title>
</head>
<body>
<h1>The #^@! Beginning</h1>
<p>I am a paragraph</p>
<p>I am paragraph 2</p>
<h1>IN THE MIDDLE</h1>
<p>Just another random paragraph.</p>
<h1>Oh, No! It's the end!</h1>
<div>The closing paragraph.</div>
</body>
</html>
```

Get this:

```
$ ls -1 0*
01-the-beginning.html
02-in-the-middle.html
03-oh-no-it-s-the-end-.html
```
