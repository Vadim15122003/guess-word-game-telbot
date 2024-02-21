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

	else:
		return 'undefined'
