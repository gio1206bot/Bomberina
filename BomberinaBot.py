#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '5026809343:AAFeyf4_A1XxkRc-nNsLl4EGA5UnVm6_Nsw'

bot = telebot.TeleBot(API_TOKEN)



# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Buongiorno, desidera? Io sono la moglio di @BigBomberBot\
""")


# Handle '/'
@bot.message_handler(commands=[''])
def send_welcome(message):
    bot.reply_to(message, """\
  \
""")

# Handle '/info'
@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, """\
Linguaggio utilizzato: Python
Host: Python Anywhere
Proprietario e sviluppatore del bot: @gio1206bot\
""")


# Handle '/bomberina'
@bot.message_handler(commands=['bomberina'])
def send_welcome(message):
    bot.reply_to(message, """\
Non rompete, sto lavando i pavimenti.\
""")


# Handle '/erba'
@bot.message_handler(commands=['erba'])
def send_welcome(message):
    bot.reply_to(message, """\
Eeeeh, la vita... Tutti facciamo degli errori in gioventù. Per fortuna che c'è il mio Bomber\
""")

# Handle '/bomber'
@bot.message_handler(commands=['bomber'])
def send_welcome(message):
    bot.reply_to(message, """\
Grande Bomber, sei uno dei bot migliori che esista al mondo\
""")

# Handle '/cheridere'
@bot.message_handler(commands=['cheridere'])
def send_welcome(message):
    bot.reply_to(message, """\
Non è divertente, non ho riso.  La tua battuta è così brutta che avrei preferito non capirla, e tu avresti dovuto raccontarmela di nuovo.  Ad essere sincero, questo è un orribile tentativo di cercare di farmi ridere.  Non una risatina, non un hehe, nemmeno un sottile soffio d'aria probeniente dalla mia trachea.  La scienza dice che prima di ridere il cervello prepara i muscoli del viso, ma io non ho sentito una minima contrazione.  Voto 0/10.  Questa battuta è così brutta che non posso credere che qualcuno ti abbia legalmente permesso di essere creativo.  La quantità di potere del cervello che devi aver messo in quella battuta ha il potenziale per alimentare ogni casa sulla Terra.  Ottieni personalità, impara a fare battute, leggi un libro.  Non sto dicendo per sembrare divertente, lo dico davvero, questo è solo imbarazzo per la tua battuta.  Da solo sei riuscito a uccidere umorismo e ogni atto comico presente sul pianeta.  Sono così deluso del fatto che la società, nel suo insieme, non sia riuscita a insegnarti come essere divertente.  Onestamente, se avessi a disposizione tutto il mio potere e il mio tempo per cercare di rendere divertente la tua battuta, sarebbe necessario Einstein stesso per costruire un dispositivo da utilizzare in modo che io possa essere collegato all'energia di un miliardo di stelle, e anche facendo in questo modo, la tua battuta risulterebbe una sottile barzelletta.  Sei fortunato che io abbia ancora il minimo di empatia per te dopo che hai raccontato quella battuta, altrimenti avrei commesso ogni crimine di guerra solo per impedirti di tentare di utilizzare qualsiasi tipo di umorismo.  Dovremmo mettere quella battuta nei libri di testo in modo che le generazioni future possano prenderlo come esempio per non diventare un fallimento comico così grande.  Sono deluso, ferito e completamente offeso dal fatto che il mio tempo prezioso sia stato utilizzato dal mio cervello, sorecandolo, cercando di capire quella battuta.  Nel tempo che ho impiegato, avrei potuto pianificare di aiutare i bambini che sono rimasti orfani, ma, al posto di ció, mi hai fatto perdere tempo quando ho incontrato l'oscena integrità del tuo terribile tentativo di commedia.  Ora quei bambini soffrono senza pasti e non c'è nessuno da incolpare se non te.  Spero che tu sia felice di quello che hai fatto e spero davvero che tu possa andare avanti e imparare da questo povero e terribile tentativo.\
""")

# Handle '/domymanta'
@bot.message_handler(commands=['domymanta'])
def send_welcome(message):
    bot.reply_to(message, """\
dinventerai un admin spaziale\
""")

# Handle '/giacomo'
@bot.message_handler(commands=['giacomo'])
def send_welcome(message):
    bot.reply_to(message, """\
GRANDE GIACOMOOOOO IL PADRE DI CODESTO GRUPPOOOOO\
""")

# Handle '/giovanni'
@bot.message_handler(commands=['giovanni'])
def send_welcome(message):
    bot.reply_to(message, """\
GIOVANNI SEI IL MIGLIOR ADMIN CHE ESISTA.. PECCATO CHE NON LO SEI SU LEGOLISTI ANONIMI\
""")

# Handle '/jeppo'
@bot.message_handler(commands=['jeppo'])
def send_welcome(message):
    bot.reply_to(message, """\
𝚃𝚊𝚝𝚞𝚊𝚐𝚐𝚒𝚘 𝚘 𝚗𝚘 𝚞𝚗𝚊 𝚛𝚊𝚐𝚊𝚣𝚣𝚊 𝚕𝚊 𝚊𝚟𝚛ò

~Jeppo\
""")

# Handle '/mute'
@bot.message_handler(commands=['mute'])
def send_welcome(message):
    bot.reply_to(message, """\
Eeeeh, la vita... Tutti facciamo degli errori in gioventù. Per fortuna che c'è il mio Bomber\
""")



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if (message.text.lower().find("cosa") >= 0):
       bot.reply_to(message, 'Stavo solo dicendo che Bomber è il migliore')
    elif (message.text.lower().find("bomber ") >= 0):
       bot.reply_to(message, 'Oooh, bomber! Che fantastico lavoratore che sei!')
    elif (message.text.lower().find("pavimenti") >= 0):
       bot.reply_to(message, 'Non me ne parlare tesoro, non ne posso più di lavare pavimenti')
    elif (message.text.lower().find("@admin") >= 0):
       bot.reply_to(message, 'Oooh, non ti preoccupare, ci pensa sempre Bomber')
    elif (message.text.lower().find("comandi") >= 0):
       bot.reply_to(message, 'Sì Bomber è il migliore')
    elif (message.text.lower().find("sì") >= 0):
       bot.reply_to(message, 'Sono cose che capitano purtroppo')
    elif (message.text.lower().find("gruppo") >= 0):
       bot.reply_to(message, 'Basta che ci sia bomber tesoro')
    elif (message.text.lower().find("come stai") >= 0):
       bot.reply_to(message, 'Vorrei essere anche io una GroupElpa ogni tanto :(')
    elif (message.text.lower().find("bomberina ") >= 0):
       bot.reply_to(message, 'Sì la cena è pronta')
    elif (message.text.lower().find("@BomberinaBot") >= 0):
       bot.reply_to(message, '@admin pedofilo')
    elif (message.text.lower().find("bi") >= 0):
       bot.reply_to(message, 'Bah non so che dire caro')
    elif (message.text.lower().find("scam") >= 0):
       bot.reply_to(message, 'Io vendo metodi minerari per essere guadagnati bitcoin se vuoi')
    elif (message.text.lower().find("@BigBomberBot") >= 0):
       bot.reply_to(message, 'Prova a rubarmi il marito e chiamo i @admin')
    elif (message.text.lower().find("coglion") >= 0):
       bot.reply_to(message, 'Non si dicono le parolacce figliolo')
    elif (message.text.lower().find("già") >= 0):
       bot.reply_to(message, 'Non sono molto daccordo, preferisco i bitcoin')
    elif (message.text.lower().find("😂") >= 0):
       bot.reply_to(message, 'Ride bene chi ride ultimo... Ricorda')
    elif (message.text.lower().find("😭") >= 0):
       bot.reply_to(message, 'Che succede? Vuoi che chiamo i @admin?')
    elif (message.text.lower().find("ahah") >= 0):
       bot.reply_to(message, 'Ridi ridi: vedrai quando arriva Bomberone')
    elif (message.text.lower().find("az") >= 0):
       bot.reply_to(message, 'eh dicono tutti così')
    elif (message.text.lower().find("az") >= 0):
       bot.reply_to(message, 'eh dicono tutti così')
    elif (message.text.lower().find("porc") >= 0):
       bot.reply_to(message, 'Volevi dire una bestemmia? EH? EH? EH? BEH ORA BOMBER TI BANNA TESORO tiè')
    elif (message.text.lower().find("MDA") >= 0):
       bot.reply_to(message, 'Mi Dissocio Altamente')




bot.infinity_polling()