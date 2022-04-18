from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView

class Container(BoxLayout):

    result_label = ObjectProperty()
    add_player = ObjectProperty()
    start_d = ObjectProperty()
    #show_players = ObjectProperty()
    scroll_players = ObjectProperty()
    scroll_draw = ObjectProperty()
    team = ObjectProperty()
    rate = ObjectProperty()
    country = ObjectProperty()
    tournament = ObjectProperty()
    players = ObjectProperty()
    draw = ObjectProperty()
    results = ObjectProperty()
    empty = ObjectProperty()
    box_tournament = ObjectProperty()
    box_players = ObjectProperty()
    box_draw = ObjectProperty()
    box_results = ObjectProperty()
    beacon = 0
    pl = []

    def change_box(self, x):
        if Container.beacon == 1:
            if x == 2:
                self.remove_widget(self.box_tournament)
                self.add_widget(self.box_players)
            if x == 3:
                self.remove_widget(self.box_tournament)
                self.add_widget(self.box_draw)
            if x == 4:
                self.remove_widget(self.box_tournament)
                self.add_widget(self.box_results)
        elif Container.beacon == 2:
            if x == 1:
                self.remove_widget(self.box_players)
                self.add_widget(self.box_tournament)
            if x == 3:
                self.remove_widget(self.box_players)
                self.add_widget(self.box_draw)
            if x == 4:
                self.remove_widget(self.box_players)
                self.add_widget(self.box_results)
        elif Container.beacon == 3:
            if x == 1:
                self.remove_widget(self.box_draw)
                self.add_widget(self.box_tournament)
            if x == 2:
                self.remove_widget(self.box_draw)
                self.add_widget(self.box_players)
            if x == 4:
                self.remove_widget(self.box_draw)
                self.add_widget(self.box_results)
        elif Container.beacon == 4:
            if x == 1:
                self.remove_widget(self.box_results)
                self.add_widget(self.box_tournament)
            if x == 2:
                self.remove_widget(self.box_results)
                self.add_widget(self.box_players)
            if x == 3:
                self.remove_widget(self.box_results)
                self.add_widget(self.box_draw)
        elif Container.beacon == 0:
            if x == 1:
                self.remove_widget(self.empty)
                self.add_widget(self.box_tournament)
            if x == 2:
                self.remove_widget(self.empty)
                self.add_widget(self.box_players)
            if x == 3:
                self.remove_widget(self.empty)
                self.add_widget(self.box_draw)
            if x == 4:
                self.remove_widget(self.empty)
                self.add_widget(self.box_results)
        Container.beacon = x

    def add_player_scroll(self):
        player = GridLayout(cols=3)
        player.add_widget(Label(text=self.team.text))
        player.add_widget(Label(text=self.rate.text))
        player.add_widget(Label(text=self.country.text))
        self.scroll_players.add_widget(player)
        Container.pl.append(self.team.text)
        Container.pl.append(self.rate.text)
        Container.pl.append(self.country.text)

    def add_player_draw(self):
        i = 0
        player = GridLayout(cols=3)
        while i != len(Container.pl):
            player.add_widget(Label(text=Container.pl[i]))
            i += 1
        self.scroll_draw.add_widget(player)

    def continue_draw(self):
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
        #top = GridLayout(cols=1, size_hint_y=10, row_force_default=True, row_default_height=35)
        mid = GridLayout(cols=3, size_hint_y=10, row_force_default=True, row_default_height=35)
        mid.add_widget(Label(text='Место в турнире'))
        mid.add_widget(Label(text='Название команды'))
        mid.add_widget(Label(text='Страна'))
        mid.add_widget(Label(text='1 место'))
        mid.add_widget(Label(text=Container.pl[0]))
        mid.add_widget(Label(text=Container.pl[2]))
        mid.add_widget(Label(text='2 место'))
        mid.add_widget(Label(text=Container.pl[3]))
        mid.add_widget(Label(text=Container.pl[5]))
        mid.add_widget(Label(text='3 место'))
        mid.add_widget(Label(text=Container.pl[6]))
        mid.add_widget(Label(text=Container.pl[8]))
        mid.add_widget(Label(text='4 место'))
        mid.add_widget(Label(text=Container.pl[9]))
        mid.add_widget(Label(text=Container.pl[11]))
        #top.add_widget(mid)
        scroll.add_widget(mid)
        self.box_results.remove_widget(self.result_label)
        self.box_results.add_widget(scroll)

    def start_draw(self):
        #self.scroll_draw.remove_widget(self.show_players)
        self.scroll_players.remove_widget(self.add_player)
        self.scroll_draw.remove_widget(self.start_d)
        continue_d = Button(text = 'Продолжить жеребьёвку', on_press = lambda x:Container.continue_draw(self))
        self.scroll_draw.add_widget(continue_d)
        draw = BoxLayout(orientation='vertical')
        #draw.add_widget(Button(text='Начать жеребьёвку'))
        draw.add_widget(Label(text='Пары(0/2)'))
        tournament_box = GridLayout(cols=5, row_force_default=True, row_default_height=35)
        tournament_box.add_widget(Label(text=str(Container.pl[0])))
        tournament_box.add_widget(TextInput())
        tournament_box.add_widget(Label(text='1:1'))
        tournament_box.add_widget(TextInput())
        tournament_box.add_widget(Label(text=str(Container.pl[3])))
        tournament_box.add_widget(Label(text=str(Container.pl[6])))
        tournament_box.add_widget(TextInput())
        tournament_box.add_widget(Label(text='1:1'))
        tournament_box.add_widget(TextInput())
        tournament_box.add_widget(Label(text=str(Container.pl[9])))
        draw.add_widget(tournament_box)
        #self.remove_widget(self.box_draw)
        self.scroll_draw.add_widget(draw)



class TournamentApp(App):

    def build(self):
        c = Container()
        c.remove_widget(c.box_tournament)
        c.remove_widget(c.box_players)
        c.remove_widget(c.box_draw)
        c.remove_widget(c.box_results)
        return c


if __name__ == '__main__':
    TournamentApp().run()
