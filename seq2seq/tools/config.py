UNK_TOKEN = '<unk>'
PAD_TOKEN = '<pad>'
BOS_TOKEN = '<s>'
EOS_TOKEN = '<\s>'

PAD, UNK, BOS, EOS = [0, 1, 2, 3]

LANGUAGE_TOKENS = {lang: '<%s>' % lang
                   for lang in sorted(['en', 'de', 'fr', 'he'])}
