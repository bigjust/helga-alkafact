from helga.plugins import command

@command('alkafact', help='like chuck norris facts, but for alkapwn')
def alkafact(client, channel, nick, message, cmd, args):
    return 'Success!'
