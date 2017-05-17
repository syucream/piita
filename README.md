# piita

Poem detector for Qiita :innocent:

## Quickstart

1. Store prefered training data as JSON.

2. (If you need it) crawl items from Qiita API.

```
$ cat labels.json | python crawler.py > items.json
```

3. Learn Doc2Vec mode from these items.

```
$ cat items.json | python learn.py
# Model file, piita.model will be saved.
```

4. Prepare target data and judge it.

```
$ cat sample01.md | python judge.py
Its maybe poem!
$ cat sample02.md | python judge.py
Its NOT poem.
```
