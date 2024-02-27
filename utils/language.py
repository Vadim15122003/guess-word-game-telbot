from .chat import Chat

def get_translation(key: str, chat: Chat):
	# last else is english
	if key == 'help':
		if chat.language == 'ro':
			return 'Aceasta comanda va afisa informatii despre comenzile si utilizarea botului'
		else:
			return 'This command will show information about commands and bot usage'

	if key == 'ch_lang':
		if chat.language == 'ro':
			return 'schimba limba'
		else:
			return 'change language'

	elif key == 'select_edit':
		if chat.language == 'ro':
			return 'Alege ce vrei sa editezi'
		else:
			return 'Select what you want to edit'

	elif key == 'select_lang':
		if chat.language == 'ro':
			return 'Selecteaza limba'
		else:
			return 'Select language'

	elif key == 'cancel':
		if chat.language == 'ro':
			return 'Anuleaza'
		else:
			return 'cancel'

	elif key == 'op_cancel':
		if chat.language == 'ro':
			return 'Operatie anulata'
		else:
			return 'Operation canceled'

	elif key == 'op_lang_success':
		if chat.language == 'ro':
			return 'Limba schimbata cu succes la romana'
		else:
			return 'Language changed successfully to english'
		
	elif key == 'in_game':
		if chat.language == 'ro':
			return 'Jocul este in desfasurare nu puteti face aceasta operatie acum'
		else:
			return 'The game is in progress you can not do this operation now'
		
	elif key == 'already_in_game':
		if chat.language == 'ro':
			return 'Jocul este deja in desfasurare'
		else:
			return 'The game is already in progress'
		
	elif key == 'start_game':
		if chat.language == 'ro':
			return 'Jocul a inceput pentru a participa apasa pe butonul de mai jos'
		else:
			return 'The game has started to participate press the button below'
		
	elif key == 'join':
		if chat.language == 'ro':
			return 'Participa'
		else:
			return 'Join'
		
	elif key == 'play':
		if chat.language == 'ro':
			return 'tapeaza /play pentru a incepe jocul (dupa nu vor putea intra alti participanti)'
		else:
			return 'type /play to start the game (after no other participants will be able to join)'
		
	elif key == 'joined':
		if chat.language == 'ro':
			return 's-a alaturat jocului'
		else:
			return 'joined the game'
		
	elif key == 'private_msg':
		if chat.language == 'ro':
			return 'te rog initiaza o conversatie in privat cu mine pentru ati putea trimite mesaje apoi apasa din nou pentru a participa'
		else:
			return 'please start a private conversation with me so I can send you messages then press again to join'
		
	elif key == 'you_start':
		if chat.language == 'ro':
			return 'Ai inceput un joc nou asteapta ca jucatorii sa apese pe Participa apoi scrie in chat-ul grupuli /play pentru a incepe'
		else:
			return 'You have started a new game wait for the players to press Join then type /play in the group chat to start'
		
	elif key == 'you_join':
		if chat.language == 'ro':
			return 'Participi intrun joc'
		else:
			return 'You are participating in a game'
		
	elif key == 'not_in_game':
		if chat.language == 'ro':
			return 'Nu esti intrun joc, pentru a incepe un joc tapeaza mai intai /start_game'
		else:
			return 'You are not in a game, to start a game first type /start_game'
	
	elif key == 'game_running':
		if chat.language == 'ro':
			return 'Jocul este deja in desfasurare'
		else:
			return 'The game is already in progress'
		
	elif key == 'game_not_started_by_you':
		if chat.language == 'ro':
			return ' a creat jocul , doar el poate folosi comanda /play pentru a incepe jocul'
		else:
			return ' created the game, only he can use the /play command to start the game'
		
	elif key == 'not_enough_players':
		if chat.language == 'ro':
			return 'Nu sunt suficienti jucatori pentru a incepe jocul, este nevoie de minim 3 jucatori'
		else:
			return 'There are not enough players to start the game, at least 3 players are needed'
		
	elif key == 'no_words':
		if chat.language == 'ro':
			return 'Nam gasit cuvinte in baza de date (sau nam putut accesa baza de date)'
		else:
			return 'No words found in the database (or I could not access the database)'
		
	elif key == 'game_started':
		if chat.language == 'ro':
			return 'Jocul a inceput, iată lista participanților:'
		else:
			return 'The game has started, here is the list of participants:'
		
	elif key == 'rules1':
		if chat.language == 'ro':
			return 'Reguli:\nToti ati primit in privat un cuvant. '
		else:
			return 'Rules:\nAll of you received a word in private. '
		
	elif key == 'rules2':
		if chat.language == 'ro':
			return 'O persoana nu a primit cuvantul\nacea persoana va trebui sal ghiceasca\nRestu persoanelor vor trebui sa ghiceasca persoana care nu stie cuvantul\n\n'
		else:
			return 'A person did not receive the word\nthat person will have to guess it\nThe rest of the people will have to guess the person who does not know the word\n\n'
		
	elif key == 'rules3':
		if chat.language == 'ro':
			return ' persoane nu au primit cuvantul, acele persoane vor trebui sal ghiceasca\nRestu persoanelor vor trebui sa ghiceasca persoanele care nu stiu cuvantul\n\n'
		else:
			return ' people did not receive the word, those people will have to guess it\nThe rest of the people will have to guess the people who do not know the word\n\n'
		
	elif key == 'rules4':
		if chat.language == 'ro':
			return '- Pentru a ghici cuvantul scrie in privat /report_word apoi vei putea trimite cuvantul\n- Dacal ghicesti vei primi 3 puncte daca nu vei pierde 1 punct si jocul pentru tine se va incheia\n- Daca crezi ca ai ghicit cuvantul dar ai spus un sinonim poti scrie /verify_my_word si ceilanti jucatori vor vota daca ai spus cuvantul corect sau nu\n\n- Pentru a ghici persoana care nu stie cuvantul scrie in privat /report_player si dupa vei putea selecta dintro list persoana pe care o presupui\n- Daca nu ghicesti atat tu cat si acea persoana veti parasi jocul iar cel ce nu a ghicit va pierde 4 puncte\n- Daca vei ghici jocul se va termina si tu vei primi 2 puncte'
		else:
			return '- To guess the word write in private /report_word then you will be able to send the word\n- If you guess you will receive 3 points if not you will lose 1 point and the game will end for you\n- If you think you guessed the word but said a synonym you can write /verify_my_word and the other players will vote if you said the word correctly or not\n\n- To guess the person who does not know the word write in private /report_player and then you will be able to select from a list the person you suspect\n- If you do not guess both you and that person will leave the game and the one who did not guess will lose 4 points\n- If you guess the game will end and you will receive 2 points'
	
	elif key == 'rules5':
		if chat.language == 'ro':
			return 'In continuare fiecare pe rand va adresa urmatorului jucator cate o intrebare iar acela va trebui sa raspunda\nJucatorul numarul 1 va adresa intrebarea jucatorului numarului 2, iar numarul 2 va raspunde dupa care numarul 2 va adresa intrebare numarului 3 si tot asa\nIn acest fel jucatorii care stiu cuvantul va trebui sasi dea seama cine nul stie, iar cei ce nu stiu cuvantul trebuie sasi dea seama care este acel cuvant'
		else:
			return 'Next, each in turn will ask the next player a question and that will have to answer\nPlayer number 1 will ask player number 2 a question, and number 2 will answer after which number 2 will ask a question to number 3 and so on\nIn this way the players who know the word will have to figure out who does not know it, and those who do not know the word must figure out what that word is'
	
	elif key == 'you_guess':
		if chat.language == 'ro':
			return 'Jocul a inceput, tu nu stii cuvantul si va trebui sal ghicesti care e\nPentru a incerca sal ghicesti tapeaza /report_word'
		else:
			return 'The game has started, you do not know the word and will have to guess what it is\nTo try to guess it type /report_word'
		
	elif key == "your_word":
		if chat.language == 'ro':
			return 'Jocul a inceput tu va trebui sa ghicesti persoana care nu stie cuvantul pentru a face aceasta tapeaza /report_player\nCuvantul este - '
		else:
			return 'The game has started you will have to guess the person who does not know the word to do this type /report_player\nThe word is - '

	elif key == 'ask':
		if chat.language == 'ro':
			return ' scrie o intrebare iar '
		else:
			return ' write a question and '
		
	elif key == 'respond':
		if chat.language == 'ro':
			return ' va trebui sa raspunda '
		else:
			return ' will have to answer '
		
	elif key == 'responder':
		if chat.language == 'ro':
			return ' raspunde la intrebarea adresata de '
		else:
			return ' answer the question asked by '
		
	elif key == 'reminder':
		if chat.language == 'ro':
			return 'Reamintire:\nPentru a ghici cuvantul tastati in privat botului /report_word\nPentru a ghici persoana care nu stie cuvantul tastati in privat botului /report_player'
		else:
			return 'Reminder:\nTo guess the word type in private to the bot /report_word\nTo guess the person who does not know the word type in private to the bot /report_player'

	elif key == 'private_conv':
		if chat.language == 'ro':
			return 'Aceasta comanda poate fi folosita doar in conversatie privata cu botul'
		else:
			return 'This command can only be used in private conversation with the bot'
		
	elif key == 'is_in_game':
		if chat.language == 'ro':
			return ' esti deja inrtun joc in alt chat, nu poti participa simultan la mai multe jocuri'
		else:
			return ' you are already in a game in another chat, you can not participate in multiple games simultaneously'
		
	elif key == 'report_player':
		if chat.language == 'ro':
			return 'a presupus ca persoana care nu stie cuvantul este'
		else:
			return 'guessed that the person who does not know the word is'
		
	elif key == 'report_succes':
		if chat.language == 'ro':
			return ', si a avut dreptate, au mai ramas'
		else:
			return ', and was right, there are'
		
	elif key == 'report_fail':
		if chat.language == 'ro':
			return ', dar a gresit, si i se vor scadea'
		else:
			return ', but was wrong, and will be deducted'
		
	elif key == 'points':
		if chat.language == 'ro':
			return 'puncte'
		else:
			return 'points'
		
	elif key == 'remained_to_guess':
		if chat.language == 'ro':
			return 'persoane care nu stiu cuvantul'
		else:
			return 'more people who do not know the word'
		
	elif key == 'report_eliminated':
		if chat.language == 'ro':
			return 'a fost eliminat din joc, iar'
		else:
			return 'was eliminated from the game, and'
		
	elif key == 'report_get_points':
		if chat.language == 'ro':
			return 'a primit 2 puncte pentru ca l-a ghicit'
		else:
			return 'received 2 points for guessing it'
		
	elif key == 'game_ended':
		if chat.language == 'ro':
			return 'Jocul s-a terminat, pentru a incepe altul tastati /start_game'
		else:
			return 'The game has ended, to start another type /start_game'
		
	elif key == 'points_info':
		if chat.language == 'ro':
			return 'Punte:\n'
		else:
			return 'Points:\n'
		
	elif key == 'two_quit':
		if chat.language == 'ro':
			return 'Ambii au parasit jocul'
		else:
			return 'Both left the game'
		
	elif key == 'no_games':
		if chat.language == 'ro':
			return 'Nu ati jucat niciun joc inca in acest chat, deci toti au 0 puncte'
		else:
			return 'You have not played any games yet in this chat, so everyone has 0 points'

	else:
		return 'undefined'
