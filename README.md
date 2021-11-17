# GAN Gallery

This project was created for an intro course I took my first semester in RIT's Software Engineering program. It's an exploration of Deep Learning aimed at training a Generative Adversarial Network (GAN) capable of generating original art. This project was created over the course of one semester by a two person team: John McCarroll and Troy Potter.


desc abt GANs


### Setup

Clone the repo to your local machine:
```buildoutcfg
$ git clone https://github.com/JohnMcCarroll/GAN_Gallery.git
```
Set up a virtual environment:
```buildoutcfg
$ python -m venv .
```

Activate your new virtual environment. This command is platform dependent, but for Linux it reads:
```buildoutcfg
$ source bin/activate 
```

Install dependencies:
```buildoutcfg
$ pip install -r requirements.txt
```

Collect gallery of paintings from wikiArt:
```buildoutcfg
$ python src/wikiArt.py
```

Run the training loop:
```buildoutcfg
$ python src/TrainingLoop.py
```



