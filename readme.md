Разработка приостановлена.

install

```
git clone
hugo new site website

#install hugo theme
mkdir themes && cd themes
git clone https://github.com/chipsenkbeil/grid-side
cd ..

```

copy flickr_keys.example.py to flickr_keys.py.
Open flickr_keys.py and fill in keys, obtained from https://www.flickr.com/services/apps/by/username

At frist run a browser window with authorization will appeared



```
python main.py
hugo server --buildDrafts
```
