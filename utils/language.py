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

	else:
		return 'undefined'
