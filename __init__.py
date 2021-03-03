from mycroft import MycroftSkill, intent_file_handler


class SinaisDeAlerta(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alerta.de.sinais.intent')
    def handle_alerta_de_sinais(self, message):
        self.speak_dialog('alerta.de.sinais')


def create_skill():
    return SinaisDeAlerta()

