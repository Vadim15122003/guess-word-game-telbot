from .chat import Chat

def get_translation(key: str, chat: Chat):
	# last else is english
	if key == 'help':
		if chat.language == 'ro':
			return '/help ofera informatii despre bot\n/rules pentru regulile jocului\n/settings pentru a schimba limba\n/points pentru a vedea fiecare cate puncte are\n/reset_points pentru a reseta puntele la 0\n/start_game incepe un joc\n/end_game pentru a opri un joc inceput\n/play incepe jocul dupa ce s-au alaturat toti jucatorii, regulile jocului vor fi afisate in chat\n/report_word incearca sa ghicesti cuvantul\n/report_player incearca sa ghicesti persoana care nu stie cuvantul\n/verify_my_word verifica daca cuvantul pe care l-ai ghicit este corect\n'
		elif chat.language == 'ru':
			return '/help предоставляет информацию о боте\n/rules для правил игры\n/settings для смены языка\n/points для просмотра количества очков каждого\n/reset_points для сброса очков на 0\n/start_game начинает игру\n/end_game для остановки начатой игры\n/play начинает игру после того, как все игроки присоединились, правила игры будут отображены в чате\n/report_word попробуйте угадать слово\n/report_player попробуйте угадать человека, который не знает слово\n/verify_my_word проверьте, правильно ли вы угадали слово\n'
		else:
			return '/help provides information about the bot\n/rules for the rules of the game\n/settings to change the language\n/points to see how many points each has\n/reset_points to reset the points to 0\n/start_game starts a game\n/end_game to stop a started game\n/play starts the game after all players have joined, the rules of the game will be displayed in the chat\n/report_word try to guess the word\n/report_player try to guess the person who does not know the word\n/verify_my_word check if the word you guessed is correct\n'

	elif key == 'rules':
		if chat.language == 'ro':
			return str('Regulile jocului:\n'
					+ 'Toti primesc in privat un cuvant. Unele persoane nu a primit cuvantul\n'
					+ 'acele persoane vor trebui sal ghiceasca\n'
					+ 'Restu persoanelor vor trebui sa ghiceasca persoanele care nu stiu cuvantul\n'
					+ '\n'
					+ '- Pentru a ghici cuvantul scrie in privat /report_word apoi vei putea trimite cuvantul\n'
					+ '- Dacal ghicesti vei primi 3 puncte daca nu vei pierde 1 punct si jocul pentru tine se va incheia\n'
					+ '- Daca crezi ca ai ghicit cuvantul dar ai spus un sinonim poti scrie /verify_my_word si ceilanti jucatori vor vota daca ai spus cuvantul corect sau nu\n'
					+ '\n'
					+ '- Pentru a ghici persoana care nu stie cuvantul scrie in privat /report_player si dupa vei putea selecta dintro list persoana pe care o presupui\n'
					+ '- Daca nu ghicesti atat tu cat si acea persoana veti parasi jocul iar cel ce nu a ghicit va pierde 4 puncte\n'
					+ '- Daca vei ghici tu vei primi 2 puncte, iar daca nu mai sunt persoane care nu stiu cuvantul jocul se va termina\n'
					+ '\n'
					+ 'In continuare fiecare pe rand va adresa urmatorului jucator cate o intrebare iar acela va trebui sa raspunda\n'
					+ 'Jucatorul numarul 1 va adresa intrebarea jucatorului numarului 2, iar numarul 2 va raspunde dupa care numarul 2 va adresa intrebare numarului 3 si tot asa\n'
					+ 'In acest fel jucatorii care stiu cuvantul va trebui sasi dea seama cine nul stie, iar cei ce nu stiu cuvantul trebuie sasi dea seama care este acel cuvant')
		elif chat.language == 'ru':
			return str('Правила игры:\n'
					+ 'Все получают в личном чате слово. Некоторые люди не получили слово\n'
					+ 'эти люди должны его угадать\n'
					+ 'Остальные люди должны угадать людей, которые не знают слово\n'
					+ '\n'
					+ '- Чтобы угадать слово, введите в личном чате с ботом /report_word, после чего вы сможете отправить слово\n'
					+ '- Если вы угадаете, вы получите 3 очка, если нет, вы потеряете 1 очко и игра закончится для вас\n'
					+ '- Если вы думаете, что угадали слово, но сказали синоним, вы можете написать /verify_my_word, и другие игроки проголосуют, правильно ли вы сказали слово или нет\n'
					+ '\n'
					+ '- Чтобы угадать человека, который не знает слово, введите в личном чате с ботом /report_player, после чего вы сможете выбрать из списка человека, которого вы подозреваете\n'
					+ '- Если вы не угадаете, вы и та персона покинете игру, и тот, кто не угадал, потеряет 4 очка\n'
					+ '- Если вы угадаете, игра закончится, и вы получите 2 очка\n'
					+ '\n'
					+ 'Затем каждый по очереди задает следующему игроку вопрос, и тот должен ответить\n'
					+ 'Игрок номер 1 задает вопрос игроку номер 2, а номер 2 отвечает, после чего номер 2 задает вопрос номеру 3 и так далее\n'
					+ 'Таким образом, игроки, которые знают слово, должны понять, кто его не знает, а те, кто не знает слово, должны понять, какое это слово')
		else:
			return str('Rules of the game:\n'
					+ 'Everyone receives a word in private. Some people did not receive the word\n'
					+ 'those people will have to guess it\n'
					+ 'The rest of the people will have to guess the people who do not know the word\n'
					+ '\n'
					+ '- To guess the word write in private /report_word then you will be able to send the word\n'
					+ '- If you guess you will receive 3 points if not you will lose 1 point and the game will end for you\n'
					+ '- If you think you guessed the word but said a synonym you can write /verify_my_word and the other players will vote if you said the word correctly or not\n'
					+ '\n'
					+ '- To guess the person who does not know the word write in private /report_player and then you will be able to select from a list the person you suspect\n'
					+ '- If you do not guess both you and that person will leave the game and the one who did not guess will lose 4 points\n'
					+ '- If you guess the game will end and you will receive 2 points, and if there are no more people who do not know the word the game will end\n'
					+ '\n'
					+ 'Next, each in turn will ask the next player a question and that will have to answer\n'
					+ 'Player number 1 will ask player number 2 a question, and number 2 will answer after which number 2 will ask a question to number 3 and so on\n'
					+ 'In this way the players who know the word will have to figure out who does not know it, and those who do not know the word must figure out what that word is')

	if key == 'ch_lang':
		if chat.language == 'ro':
			return 'schimba limba'
		elif chat.language == 'ru':
			return 'сменить язык'
		else:
			return 'change language'

	elif key == 'select_edit':
		if chat.language == 'ro':
			return 'Alege ce vrei sa editezi'
		elif chat.language == 'ru':
			return 'Выберите, что вы хотите отредактировать'
		else:
			return 'Select what you want to edit'

	elif key == 'select_lang':
		if chat.language == 'ro':
			return 'Selecteaza limba'
		elif chat.language == 'ru':
			return 'Выберите язык'
		else:
			return 'Select language'

	elif key == 'cancel':
		if chat.language == 'ro':
			return 'Anuleaza'
		elif chat.language == 'ru':
			return 'Отмена'
		else:
			return 'cancel'

	elif key == 'op_cancel':
		if chat.language == 'ro':
			return 'Operatie anulata'
		elif chat.language == 'ru':
			return 'Операция отменена'
		else:
			return 'Operation canceled'

	elif key == 'op_lang_success':
		if chat.language == 'ro':
			return 'Limba schimbata cu succes la romana'
		elif chat.language == 'ru':
			return 'Язык успешно изменен на русский'
		else:
			return 'Language changed successfully to english'
		
	elif key == 'in_game':
		if chat.language == 'ro':
			return 'Jocul este in desfasurare nu puteti face aceasta operatie acum'
		elif chat.language == 'ru':
			return 'Игра идет, вы не можете сделать эту операцию сейчас'
		else:
			return 'The game is in progress you can not do this operation now'
		
	elif key == 'already_in_game':
		if chat.language == 'ro':
			return 'Jocul este deja in desfasurare'
		elif chat.language == 'ru':
			return 'Игра уже идет'
		else:
			return 'The game is already in progress'
		
	elif key == 'start_game':
		if chat.language == 'ro':
			return 'Jocul a inceput pentru a participa apasa pe butonul de mai jos'
		elif chat.language == 'ru':
			return 'Игра началась, чтобы присоединиться, нажмите кнопку ниже'
		else:
			return 'The game has started to participate press the button below'
		
	elif key == 'join':
		if chat.language == 'ro':
			return 'Participa'
		elif chat.language == 'ru':
			return 'Присоединиться'
		else:
			return 'Join'
		
	elif key == 'play':
		if chat.language == 'ro':
			return 'tapeaza /play pentru a incepe jocul (dupa nu vor putea intra alti participanti)'
		elif chat.language == 'ru':
			return 'напишите /play, чтобы начать игру (после этого другие участники не смогут присоединиться)'
		else:
			return 'type /play to start the game (after no other participants will be able to join)'
		
	elif key == 'joined':
		if chat.language == 'ro':
			return 's-a alaturat jocului'
		elif chat.language == 'ru':
			return 'присоединился к игре'
		else:
			return 'joined the game'
		
	elif key == 'private_msg':
		if chat.language == 'ro':
			return 'te rog initiaza o conversatie in privat cu mine pentru ati putea trimite mesaje apoi apasa din nou pentru a participa'
		elif chat.language == 'ru':
			return 'пожалуйста, начните приватный разговор со мной, чтобы я мог отправлять вам сообщения, а затем нажмите еще раз, чтобы присоединиться'
		else:
			return 'please start a private conversation with me so I can send you messages then press again to join'
		
	elif key == 'you_start':
		if chat.language == 'ro':
			return 'Ai inceput un joc nou asteapta ca jucatorii sa apese pe Participa apoi scrie in chat-ul grupuli /play pentru a incepe'
		elif chat.language == 'ru':
			return 'Вы начали новую игру, подождите, пока игроки нажмут Присоединиться, а затем введите /play в групповом чате, чтобы начать'
		else:
			return 'You have started a new game wait for the players to press Join then type /play in the group chat to start'
		
	elif key == 'you_join':
		if chat.language == 'ro':
			return 'Participi intrun joc'
		elif chat.language == 'ru':
			return 'Вы участвуете в игре'
		else:
			return 'You are participating in a game'
		
	elif key == 'not_in_game':
		if chat.language == 'ro':
			return 'Nu esti intrun joc, pentru a incepe un joc tapeaza mai intai /start_game'
		elif chat.language == 'ru':
			return 'Вы не в игре, чтобы начать игру сначала введите /start_game'
		else:
			return 'You are not in a game, to start a game first type /start_game'
	
	elif key == 'game_running':
		if chat.language == 'ro':
			return 'Jocul este deja in desfasurare'
		elif chat.language == 'ru':
			return 'Игра уже идет'
		else:
			return 'The game is already in progress'
		
	elif key == 'game_not_started_by_you':
		if chat.language == 'ro':
			return ' a creat jocul , doar el poate folosi comanda /play pentru a incepe jocul'
		elif chat.language == 'ru':
			return ' создал игру, только он может использовать команду /play для начала игры'
		else:
			return ' created the game, only he can use the /play command to start the game'
		
	elif key == 'not_enough_players':
		if chat.language == 'ro':
			return 'Nu sunt suficienti jucatori pentru a incepe jocul, este nevoie de minim 3 jucatori'
		elif chat.language == 'ru':
			return 'Недостаточно игроков для начала игры, нужно минимум 3 игрока'
		else:
			return 'There are not enough players to start the game, at least 3 players are needed'
		
	elif key == 'no_words':
		if chat.language == 'ro':
			return 'Nam gasit cuvinte in baza de date (sau nam putut accesa baza de date)'
		elif chat.language == 'ru':
			return 'Слова не найдены в базе данных (или я не смог получить доступ к базе данных)'
		else:
			return 'No words found in the database (or I could not access the database)'
		
	elif key == 'game_started':
		if chat.language == 'ro':
			return 'Jocul a inceput, iată lista participanților:'
		elif chat.language == 'ru':
			return 'Игра началась, вот список участников:'
		else:
			return 'The game has started, here is the list of participants:'
		
	elif key == 'rules1':
		if chat.language == 'ro':
			return 'Reguli:\nToti ati primit in privat un cuvant. '
		elif chat.language == 'ru':
			return 'Правила:\nВсе вы получили слово в личном чате. '
		else:
			return 'Rules:\nAll of you received a word in private. '
		
	elif key == 'rules2':
		if chat.language == 'ro':
			return 'O persoana nu a primit cuvantul\nacea persoana va trebui sal ghiceasca\nRestu persoanelor vor trebui sa ghiceasca persoana care nu stie cuvantul\n\n'
		elif chat.language == 'ru':
			return 'Один человек не получил слово\nэтот человек должен его угадать\nОстальные люди должны угадать человека, который не знает слово\n\n'
		else:
			return 'A person did not receive the word\nthat person will have to guess it\nThe rest of the people will have to guess the person who does not know the word\n\n'
		
	elif key == 'rules3':
		if chat.language == 'ro':
			return ' persoane nu au primit cuvantul, acele persoane vor trebui sal ghiceasca\nRestu persoanelor vor trebui sa ghiceasca persoanele care nu stiu cuvantul\n\n'
		elif chat.language == 'ru':
			return ' людей не получили слово, эти люди должны его угадать\nОстальные люди должны угадать людей, которые не знают слово\n\n'
		else:
			return ' people did not receive the word, those people will have to guess it\nThe rest of the people will have to guess the people who do not know the word\n\n'
		
	elif key == 'rules4':
		if chat.language == 'ro':
			return '- Pentru a ghici cuvantul scrie in privat /report_word apoi vei putea trimite cuvantul\n- Dacal ghicesti vei primi 3 puncte daca nu vei pierde 1 punct si jocul pentru tine se va incheia\n- Daca crezi ca ai ghicit cuvantul dar ai spus un sinonim poti scrie /verify_my_word si ceilanti jucatori vor vota daca ai spus cuvantul corect sau nu\n\n- Pentru a ghici persoana care nu stie cuvantul scrie in privat /report_player si dupa vei putea selecta dintro list persoana pe care o presupui\n- Daca nu ghicesti atat tu cat si acea persoana veti parasi jocul iar cel ce nu a ghicit va pierde 4 puncte\n- Daca vei ghici jocul se va termina si tu vei primi 2 puncte'
		elif chat.language == 'ru':
			return '- Чтобы угадать слово, введите в личном чате с ботом /report_word, после чего вы сможете отправить слово\n- Если вы угадаете, вы получите 3 очка, если нет, вы потеряете 1 очко и игра закончится для вас\n- Если вы думаете, что угадали слово, но сказали синоним, вы можете написать /verify_my_word, и другие игроки проголосуют, правильно ли вы сказали слово или нет\n\n- Чтобы угадать человека, который не знает слово, введите в личном чате с ботом /report_player, после чего вы сможете выбрать из списка человека, которого вы подозреваете\n- Если вы не угадаете, вы и та персона покинете игру, и тот, кто не угадал, потеряет 4 очка\n- Если вы угадаете, игра закончится, и вы получите 2 очка'
		else:
			return '- To guess the word write in private /report_word then you will be able to send the word\n- If you guess you will receive 3 points if not you will lose 1 point and the game will end for you\n- If you think you guessed the word but said a synonym you can write /verify_my_word and the other players will vote if you said the word correctly or not\n\n- To guess the person who does not know the word write in private /report_player and then you will be able to select from a list the person you suspect\n- If you do not guess both you and that person will leave the game and the one who did not guess will lose 4 points\n- If you guess the game will end and you will receive 2 points'
	
	elif key == 'rules5':
		if chat.language == 'ro':
			return 'In continuare fiecare pe rand va adresa urmatorului jucator cate o intrebare iar acela va trebui sa raspunda\nJucatorul numarul 1 va adresa intrebarea jucatorului numarului 2, iar numarul 2 va raspunde dupa care numarul 2 va adresa intrebare numarului 3 si tot asa\nIn acest fel jucatorii care stiu cuvantul va trebui sasi dea seama cine nul stie, iar cei ce nu stiu cuvantul trebuie sasi dea seama care este acel cuvant'
		elif chat.language == 'ru':
			return 'Затем каждый по очереди задает следующему игроку вопрос, и тот должен ответить\nИгрок номер 1 задает вопрос игроку номер 2, а номер 2 отвечает, после чего номер 2 задает вопрос номеру 3 и так далее\nТаким образом, игроки, которые знают слово, должны понять, кто его не знает, а те, кто не знает слово, должны понять, какое это слово'
		else:
			return 'Next, each in turn will ask the next player a question and that will have to answer\nPlayer number 1 will ask player number 2 a question, and number 2 will answer after which number 2 will ask a question to number 3 and so on\nIn this way the players who know the word will have to figure out who does not know it, and those who do not know the word must figure out what that word is'
	
	elif key == 'you_guess':
		if chat.language == 'ro':
			return 'Jocul a inceput, tu nu stii cuvantul si va trebui sal ghicesti care e\nPentru a incerca sal ghicesti tapeaza /report_word'
		elif chat.language == 'ru':
			return 'Игра началась, вы не знаете слово и должны угадать, что это\nЧтобы попытаться угадать, введите /report_word'
		else:
			return 'The game has started, you do not know the word and will have to guess what it is\nTo try to guess it type /report_word'
		
	elif key == "your_word":
		if chat.language == 'ro':
			return 'Jocul a inceput tu va trebui sa ghicesti persoana care nu stie cuvantul pentru a face aceasta tapeaza /report_player\nCuvantul este - '
		elif chat.language == 'ru':
			return 'Игра началась, вам нужно угадать человека, который не знает слово, чтобы сделать это, введите /report_player\nСлово - '
		else:
			return 'The game has started you will have to guess the person who does not know the word to do this type /report_player\nThe word is - '

	elif key == 'ask':
		if chat.language == 'ro':
			return ' scrie o intrebare iar '
		elif chat.language == 'ru':
			return ' напишите вопрос и '
		else:
			return ' write a question and '
		
	elif key == 'respond':
		if chat.language == 'ro':
			return ' va trebui sa raspunda '
		elif chat.language == 'ru':
			return ' должен ответить '
		else:
			return ' will have to answer '
		
	elif key == 'responder':
		if chat.language == 'ro':
			return ' raspunde la intrebarea adresata de '
		elif chat.language == 'ru':
			return ' отвечает на вопрос, заданный '
		else:
			return ' answer the question asked by '
		
	elif key == 'reminder':
		if chat.language == 'ro':
			return 'Reamintire:\nPentru a ghici cuvantul tastati in privat botului /report_word\nPentru a ghici persoana care nu stie cuvantul tastati in privat botului /report_player'
		elif chat.language == 'ru':
			return 'Напоминание:\nЧтобы угадать слово, введите в личном чате с ботом /report_word\nЧтобы угадать человека, который не знает слово, введите в личном чате с ботом /report_player'
		else:
			return 'Reminder:\nTo guess the word type in private to the bot /report_word\nTo guess the person who does not know the word type in private to the bot /report_player'

	elif key == 'private_conv':
		if chat.language == 'ro':
			return 'Aceasta comanda poate fi folosita doar in conversatie privata cu botul'
		elif chat.language == 'ru':
			return 'Эта команда может использоваться только в личном разговоре с ботом'
		else:
			return 'This command can only be used in private conversation with the bot'
		
	elif key == 'is_in_game':
		if chat.language == 'ro':
			return ' esti deja inrtun joc in alt chat, nu poti participa simultan la mai multe jocuri'
		elif chat.language == 'ru':
			return 'вы уже участвуете в игре в другом чате, вы не можете одновременно участвовать в нескольких играх'
		else:
			return ' you are already in a game in another chat, you can not participate in multiple games simultaneously'
		
	elif key == 'report_player':
		if chat.language == 'ro':
			return 'a presupus ca persoana care nu stie cuvantul este'
		elif chat.language == 'ru':
			return 'предположил, что человек, который не знает слово, -'
		else:
			return 'guessed that the person who does not know the word is'
		
	elif key == 'report_succes':
		if chat.language == 'ro':
			return ', si a avut dreptate, au mai ramas'
		elif chat.language == 'ru':
			return ', и он был прав, осталось'
		else:
			return ', and was right, there are'
		
	elif key == 'report_fail':
		if chat.language == 'ro':
			return ', dar a gresit, si i se vor scadea'
		elif chat.language == 'ru':
			return ', но он ошибся, и ему будут вычтены'
		else:
			return ', but was wrong, and will be deducted'
		
	elif key == 'points':
		if chat.language == 'ro':
			return 'puncte'
		elif chat.language == 'ru':
			return 'очков'
		else:
			return 'points'
		
	elif key == 'remained_to_guess':
		if chat.language == 'ro':
			return 'persoane care nu stiu cuvantul'
		elif chat.language == 'ru':
			return 'людей, которые не знают слово'
		else:
			return 'more people who do not know the word'
		
	elif key == 'report_eliminated':
		if chat.language == 'ro':
			return 'a fost eliminat din joc, iar'
		elif chat.language == 'ru':
			return 'был исключен из игры, и'
		else:
			return 'was eliminated from the game, and'
		
	elif key == 'report_get_points':
		if chat.language == 'ro':
			return 'a primit 2 puncte pentru ca l-a ghicit'
		elif chat.language == 'ru':
			return 'получил 2 очка за то, что угадал'
		else:
			return 'received 2 points for guessing it'
		
	elif key == 'game_ended':
		if chat.language == 'ro':
			return 'Jocul s-a terminat, pentru a incepe altul tastati /start_game'
		elif chat.language == 'ru':
			return 'Игра окончена, чтобы начать другую, введите /start_game'
		else:
			return 'The game has ended, to start another type /start_game'
		
	elif key == 'points_info':
		if chat.language == 'ro':
			return 'Punte:\n'
		elif chat.language == 'ru':
			return 'Очки:\n'
		else:
			return 'Points:\n'
		
	elif key == 'two_quit':
		if chat.language == 'ro':
			return 'Ambii au parasit jocul'
		elif chat.language == 'ru':
			return 'Оба покинули игру'
		else:
			return 'Both left the game'
		
	elif key == 'no_games':
		if chat.language == 'ro':
			return 'Nu ati jucat niciun joc inca in acest chat, deci toti au 0 puncte'
		elif chat.language == 'ru':
			return 'Вы еще не играли ни в одну игру в этом чате, поэтому у всех 0 очков'
		else:
			return 'You have not played any games yet in this chat, so everyone has 0 points'
		
	elif key == 'points_reset':
		if chat.language == 'ro':
			return 'Punctele la toti participantii din acest chat au fost resetate la 0'
		elif chat.language == 'ru':
			return 'Очки всех участников этого чата сброшены на 0'
		else:
			return 'Points for all participants in this chat have been reset to 0'
		
	elif key == 'admin':
		if chat.language == 'ro':
			return 'Aceasta comanda poate fi folosita doar de catre admini'
		elif chat.language == 'ru':
			return 'Эта команда может использоваться только администраторами'
		else:
			return 'This command can only be used by admins'
		
	elif key == 'word_guess_try':
		if chat.language == 'ro':
			return ' a incercat sa ghiceasca cuvantul si a presupus ca acesta este: '
		elif chat.language == 'ru':
			return 'попытался угадать слово и предположил, что это: '
		else:
			return ' tried to guess the word and guessed that it is: '
		
	elif key == 'word_wrong':
		if chat.language == 'ro':
			return 'Nu a avut dreptate de aceia i se va scadea un punct (daca persoana crede ca totusi a ghicit cuvantul poate folosi comanda /verify_my_word in privat si ceilalti jucatori vor vota daca a ghicit sau nu)'
		elif chat.language == 'ru':
			return 'Он ошибся, поэтому ему будет вычтено одно очко (если человек считает, что он угадал слово, он может использовать команду /verify_my_word в личном чате, и другие игроки проголосуют, угадал ли он или нет)'
		else:
			return 'He was wrong so he will be deducted one point (if the person thinks he guessed the word he can use the /verify_my_word command in private and the other players will vote if he guessed or not)'

	elif key == 'word_right':
		if chat.language == 'ro':
			return 'A avut dreptate si a primit 3 puncte'
		elif chat.language == 'ru':
			return 'Он был прав и получил 3 очка'
		else:
			return 'He was right and received 3 points'
		
	elif key == 'verify_word1':
		if chat.language == 'ro':
			return ' a cerut sa i se verifice cuvantul pe care el la presupus in ultimul joc, el a scris cuvantul: '
		elif chat.language == 'ru':
			return 'попросил проверить слово, которое он предположил в последней игре, он написал слово: '
		else:
			return ' asked to verify the word he guessed in the last game, he wrote the word: '
		
	elif key == 'verify_word2':
		if chat.language == 'ro':
			return 'cel corect era: '
		elif chat.language == 'ru':
			return 'правильное слово было: '
		else:
			return 'the correct word was: '
		
	elif key == 'verify_word3':
		if chat.language == 'ro':
			return '\nToti jucatorii care au participat la ultimul joc pot vota daca raspunsul sau a fost corect sau nu (daca nu ati participat votul nu vi se va lua in calcul)'
		elif chat.language == 'ru':
			return '\nВсе игроки, которые участвовали в последней игре, могут проголосовать, был ли его ответ правильным или нет (если вы не участвовали, голос не будет учтен)'
		else:
			return '\nAll players who participated in the last game can vote if his answer was correct or not (if you did not participate the vote will not be taken into account)'
		
	elif key == 'verify_word4':
		if chat.language == 'ro':
			return 'Este corect si cuvantul scris de '
		elif chat.language == 'ru':
			return 'Это правильно, и слово, написанное '
		else:
			return 'It is correct and the word written by '
		
	elif key == 'total_votes':
		if chat.language == 'ro':
			return 'Total voturi posibile: '
		elif chat.language == 'ru':
			return 'Всего возможных голосов: '
		else:
			return 'Total possible votes: '
		
	elif key == 'votes_yes':
		if chat.language == 'ro':
			return 'Voturi pentru DA: '
		elif chat.language == 'ru':
			return 'Голоса за ДА: '
		else:
			return 'Votes for YES: '
	
	elif key == 'votes_no':
		if chat.language == 'ro':
			return 'Voturi pentru NU: '
		elif chat.language == 'ru':
			return 'Голоса за НЕТ: '
		else:
			return 'Votes for NO: '
		
	elif key == 'verify_word_not_allowed':
		if chat.language == 'ro':
			return 'Nu mai poti vota acum'
		elif chat.language == 'ru':
			return 'Теперь вы не можете голосовать'
		else:
			return 'You can not vote now'
		
	elif key == 'cant vote':
		if chat.language == 'ro':
			return ' nu poti vota pentru ca nu ai participat la ultimul joc'
		elif chat.language == 'ru':
			return ' вы не можете голосовать, потому что не участвовали в последней игре'
		else:
			return ' you can not vote because you did not participate in the last game'
		
	elif key == 'word_verified':
		if chat.language == 'ro':
			return 'Cuvantul a fost votat ca fiind corect, persoana care a scris cuvantul a primit 3 puncte (in loc sa i se scada unul)'
		elif chat.language == 'ru':
			return 'Слово было проголосовано как правильное, человек, который написал слово, получил 3 очка (вместо вычета одного)'
		else:
			return 'The word was voted as correct, the person who wrote the word received 3 points (instead of being deducted one)'
		
	elif key == 'word_not_verified':
		if chat.language == 'ro':
			return 'Cuvantul a fost votat ca fiind gresit, persoana care a scris cuvantul nu mai poate vota din nou sa i se verifice'
		elif chat.language == 'ru':
			return 'Слово было проголосовано как неправильное, человек, который написал слово, больше не может проголосовать, чтобы его проверили'
		else:
			return 'The word was voted as wrong, the person who wrote the word can not vote again to be verified'
		
	elif key == 'game_ended':
		if chat.language == 'ro':
			return 'Jocul s-a încheiat'
		elif chat.language == 'ru':
			return 'Игра окончена'
		else:
			return 'The game has ended'
		
	elif key == 'no_game':
		if chat.language == 'ro':
			return 'Nu este niciun joc in desfasurare'
		elif chat.language == 'ru':
			return 'В процессе нет игры'
		else:
			return 'There is no game in progress'

	else:
		return 'undefined'
