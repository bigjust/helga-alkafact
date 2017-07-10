import smokesignal

from helga import settings
from helga.db import db
from helga.plugins import command

def add_fact(fact):
    db.alkafact.insert({
        'text': fact
    })

def retrieve_fact(key):

    pipeline = [
        {'$match': {
            'text': {'$regex': key}
        }},
        {'$sample': {'size': 1}}
    ]

    result = db.alkafact.aggregate(pipeline)

    try:
        return result.next()['text']
    except StopIteration:
        return 'no results :('

@command('rem', help='like chuck norris facts, but for alkapwn')
def alkafact(client, channel, nick, message, cmd, args):

    if args[0] == 'add':
        add_fact(' '.join(args[1:]))
        return 'Added.'

    return retrieve_fact(args[0])
