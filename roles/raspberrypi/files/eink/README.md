```

$ /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --clear
$ fortune -s -n 300 | /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --write --border --font-size 28 --font-padding 5 --font DejaVuSerif --rotate
$ /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --weather
$ /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --draw --filename /opt/eink/resources/promenade_des_anglais.jpg
$ /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --draw --filename /opt/eink/resources/matisse.png
$ python3 sensors/sense.py 24 | /opt/eink/venv/bin/python3 /opt/eink/eink/main.py --write --border --font-size 36 --font-padding 5

```
