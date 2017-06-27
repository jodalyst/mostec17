# python-espeak - Python interface to the espeak text-to-speech CLI program

python-espeak is a simple Python 3 wrapper for the espeak speech
synthesizer, which is a fancy way to say that it can make your computer talk.

It's synchronous and meant to be used for scripting, as it's very
simple to use but does not involve ctypes and libespeak.so,
which would have allowed a greater degree of control at the expense of
complexity (something outside the scope of this little project).

I developed this in parallel with a Ruby version as an experiment: with the
same goal and a similar (but idiomatic) design, write a (simple) library in two
different languages in a single day.
I completed the Ruby version in half the time I took for the Python version,
even though I have been a Python programmer for longer. This experiment has
really given me a clear perspective on the two languages, and will inevitably
influence my future projects.

## Usage

To install the python-espeak package, make sure you have Python 3 and the
espeak programs installed - both of which can be commonly found on distro
repositories on GNU/Linux, then type

`make install`

You can run the test suite by typing `make test`. Type `make` for a detailed
list of actions.

Using python-espeak is very easy. After importing the package with

```python
import espeak
```

you can initialize an ESpeak object with

```python
es = espeak.ESpeak(options)
```

The options argument is not required; python-espeak comes with a lot of
defaults ideal for your average English-reading experience.

You can make your computer talk by using

```python
es.say(text)
```

And you can save the output to a .wav file by using

```python
es.save(text, filename)
```

Additionally, you can generate an espeak command by using

```python
es.command(text, filename)
```

The filename is optional and matters only if you want a command to generate a
wav file.

espeak is not limited to reading English and has a lot of options. You can see
a list of them by typing `espeak --help` in your terminal and set a lot of
them directly from a ESpeak instance, for example

```python
es.voice = 'de'
es.speed = 1
```

will make your PC sound like an angry German.

You can see a list of the available voices by typing

```python
print(es.voices)
```

## License

All files in this distribution are released under version 3 of the
GNU General Public License or any later version, unless otherwise stated.
