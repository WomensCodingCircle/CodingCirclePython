count = 0
sum = 0
with open('theyellowwallpaper.txt') as fh:
    for line in fh:
        if line[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count += 1
            words = line.split()
            first_word = words[0]
            sum += len(first_word)
ave_len = sum/float(count)
with open('ave_first_word_length.txt', 'w') as fh:
    fh.write( "The Yellow Wallpaper\n")
    fh.write(str(ave_len))