import emoji

print('------------------------   EMOJI CHAT IN PYTHON   ------------------------')
print('¡Hello everyone! ¡Welcome to the Emoji Chat in Python!')
print('Here are the emoji options')
print('In this program you can type any text and emoji command ¡We will show them!')
print('------------------------  EMOJI OPTIONS  ------------------------')
print(':) = Happy face'
      '\n :( = Sad face'
      '\n (y) = Good hand'
      '\n :p or :P = Face with tongue'
      '\n If you write "COL" You you see a Colombian flag')
print('------------------------------------------------------------')
text = input('Now, TYPE YOUR TEXT :D')

text = text.replace(':p' or ':P', emoji.emojize(':face_with_tongue:'))
text = text.replace(':(', emoji.emojize(':slightly_frowning_face:'))
text = text.replace(':)', emoji.emojize(':slightly_smiling_face:'))
text = text.replace('(y)', emoji.emojize(':thumbs_up:'))
text = text.replace('COL', emoji.emojize(':Colombia:'))

print(text)



