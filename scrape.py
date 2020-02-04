from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('podcast')

fg.id('http://lernfunk.de/media/654321')
fg.title('Hackmods hosts a radio show')
fg.author( {'name':'Ryan Morris','email':'ryan@ryanmorris.ca'} )
fg.link( href='http://ryanmorris.ca', rel='alternate' )
fg.logo('http://ex.com/logo.jpg')
fg.subtitle('This is a cool feed!')
fg.link( href='http://ryanmorris.ca/show.rss', rel='self' )
#fg.link( href='http://ryanmorris.ca/show.atom', rel='self' )
fg.language('en')

#fg.contributor({'name':'Ryan Morris','email':'ryan@ryanmorris.ca'})

#http://dl.ahangfa.ir/Khareji/T/The%20Witcher%20soundtrack/The%20Witcher%20soundtrack/
fe = fg.add_entry()
fe.id('http://dl.ahangfa.ir/Khareji/T/The%20Witcher%20soundtrack/The%20Witcher%20soundtrack/The%20End%27s%20Beginning.mp3')
fe.title('The First Episode')
fe = fg.add_entry()
fe.id('http://dl.ahangfa.ir/Khareji/T/The%20Witcher%20soundtrack/The%20Witcher%20soundtrack/The%20Last%20Rose%20Of%20Cintra.mp3')
fe.title('The Second Episode')
fe = fg.add_entry()
fe.id('http://dl.ahangfa.ir/Khareji/T/The%20Witcher%20soundtrack/The%20Witcher%20soundtrack/Calm%20Before%20The%20Storm.mp3')
fe.title('The Third Episode')

fg.podcast.itunes_category('Music', 'Podcasting')
fg.rss_str(pretty=True)
fg.rss_file('zxcvPodcast.xml')

print (fg.rss())
#>>> atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
#>>> fg.atom_file('atom.xml') # Write the ATOM feed to a file