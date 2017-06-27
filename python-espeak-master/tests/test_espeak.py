import tempfile
import unittest

import espeak


class ESpeakTestCase(unittest.TestCase):
    def setUp(self):
        self.e = espeak.ESpeak()

    def test_init_arg(self):
        self.e = espeak.ESpeak(amplitude=10)
        self.assertEqual(self.e.args['amplitude'][1], 10)

    def test_init_ordered(self):
        args = ['amplitude', 'word_gap', 'capitals', 'line_length', 'pitch',
                'speed', 'voice', 'spell_punctuation', 'split']
        self.assertEqual(list(self.e.args.keys()), args)

    def test_getter(self):
        """ Getters/Setters are copy-pasted so we only test one """

        self.assertEqual(self.e.args['voice'], self.e.voice)

    def test_setter(self):
        self.e.voice = 'pt'
        self.assertEqual(self.e.args['voice'][1], 'pt')

    def test_validate_args(self):
        self.e.voice = 5
        self.assertRaises(TypeError, self.e._validate_args)

    def test_espeak_args_say(self):
        text = 'test'
        expected = ['espeak', '-a100', '-g10', '-k1', '-l1', '-p50', '-s175',
                    '-ven', '--punct=', '--split=', '-x', 'test']
        self.assertEqual(self.e._espeak_args(text), expected)

    def test_espeak_args_save(self):
        text = 'test'
        filename = 'test.wav'
        expected = ['espeak', '-a100', '-g10', '-k1', '-l1', '-p50', '-s175',
                    '-ven', '--punct=', '--split=', '-x', '--split=',
                    '-wtest.wav', 'test']
        self.assertEqual(self.e._espeak_args(text, filename), expected)

    def test_command_say(self):
        text = 'test'
        expected = 'espeak -a100 -g10 -k1 -l1 -p50 -s175 ' +\
                   '-ven --punct= --split= -x test'
        self.assertEqual(self.e.command(text), expected)

    def test_command_save(self):
        text = filename = 'test'
        expected = 'espeak -a100 -g10 -k1 -l1 -p50 -s175 ' +\
                   '-ven --punct= --split= -x --split= -wtest test'
        self.assertEqual(self.e.command(text, filename), expected)

    def test_execute(self):
        self.assertEqual(self.e._execute(['espeak', '']), '')

    def test_say(self):
        expected = " _#X1t'Est_\n"
        self.assertEqual(self.e.say('Test'), expected)

    def test_save(self):
        temp = tempfile.NamedTemporaryFile()
        self.e.save('Test', temp.name)
        with open("{}".format(temp.name), 'rb') as f:
            self.assertEqual(str(f.read())[2:6], 'RIFF')

    def test_extract_entry(self):
        entry = ' 5  af             M  afrikaans            other/af     '
        expected = {'age_gender': 'M', 'voice_name': 'afrikaans',
                    'other_languages': '     ',
                    'language': 'af', 'file': 'other/af', 'pty': '5'}
        self.assertEqual(self.e._extract_entry(entry), expected)
