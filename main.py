import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
# from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
# from kivy.base import EventLoop
from random import shuffle


class Container(BoxLayout):

    continue_d = ObjectProperty()
    id_title = ObjectProperty()
    id_date = ObjectProperty()
    id_place = ObjectProperty()
    id_sport = ObjectProperty()
    id_format = ObjectProperty()
    # id_count = ObjectProperty()
    start_t = ObjectProperty()
    result_label = ObjectProperty()
    add_player = ObjectProperty()
    start_d = ObjectProperty()
    # show_players = ObjectProperty()
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
    is_tournament_start = False
    tournament_list = []
    players_info = []
    players = []
    players_l = []
    all_tours = None
    now_tour = None
    child = None

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

    def start_tournament(self):
        if self.id_title.text != "" and self.id_date.text != "" and self.id_place.text != "":
            self.box_tournament.remove_widget(self.start_t)
            Container.tournament_list.append(self.id_title.text)
            Container.tournament_list.append(self.id_date.text)
            Container.tournament_list.append(self.id_place.text)
            tournament_box = GridLayout(cols=3, row_force_default=True, row_default_height=35)
            tournament_box.add_widget(Label(text=Container.tournament_list[0]))
            tournament_box.add_widget(Label(text=Container.tournament_list[1]))
            tournament_box.add_widget(Label(text=Container.tournament_list[2]))
            self.scroll_draw.remove_widget(self.start_d)
            self.scroll_draw.add_widget(tournament_box)
            self.scroll_draw.add_widget(self.start_d)
            Container.is_tournament_start = True
        elif self.id_title.text == "":
            self.id_title.text = "Введите значение!"
        elif self.id_date.text == "":
            self.id_date.text = "Введите значение!"
        elif self.id_place.text == "":
            self.id_place.text = "Введите значение!"

    def add_player_scroll(self):
        if self.team.text != "" and self.rate.text != "" and self.country.text and self.team.text != "Введите значение!" and self.rate.text != "Введите значение!" and self.country.text != "Введите значение!":
            player = GridLayout(cols=3)
            player.add_widget(Label(text=self.team.text))
            player.add_widget(Label(text=self.rate.text))
            player.add_widget(Label(text=self.country.text))
            self.scroll_players.add_widget(player)
            Container.players_info.append(self.team.text)
            Container.players_info.append(self.rate.text)
            Container.players_info.append(self.country.text)
            self.team.text = ""
            self.rate.text = ""
            self.country.text = ""
        elif self.team.text == "":
            self.team.text = "Введите значение!"
        elif self.rate.text == "":
            self.rate.text = "Введите значение!"
        elif self.country.text == "":
            self.country.text = "Введите значение!"



    """def add_player_draw(self):
        i = 0
        player = GridLayout(cols=3)
        while i != len(Container.pl):
            player.add_widget(Label(text=Container.pl[i]))
            i += 1
        self.scroll_draw.add_widget(player)"""

    def start_draw(self):
        # Пока реализую только Single elimination (турнир на выбывание без сетки лузеров)
        if len(Container.players_info)/3 <= 128 and len(Container.players_info)/3 >= 2 and len(Container.players) == 0:
            self.scroll_players.remove_widget(self.add_player) # убирает кнопку добавления игроков
            i = 0
            while len(Container.players) != len(Container.players_info)/3:
                Container.players.append(Container.players_info[i])
                i += 3
            random.shuffle(Container.players)
            j = len(Container.players) // 2
            i = 1
            while j != 1:
                j = j // 2
                i += 1
            raznica = len(Container.players) - 2 ** i
            if raznica == 0:
                Container.all_tours = i
            else:
                Container.all_tours = i + 1
            Container.now_tour = 1
            draw = BoxLayout(orientation='vertical')
            draw.add_widget(Label(text='Тур(' + str(Container.now_tour) + '/' + str(Container.all_tours) + ')'))
            tournament_box = GridLayout(cols=4, row_force_default=True, row_default_height=35)
            j = 0
            if raznica == 0:
                while j != len(Container.players):
                    tournament_box.add_widget(Label(text=str(Container.players[j])))
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(Label(text=str(Container.players[j+1])))
                    j+=2
            else:
                while j != raznica*2:
                    tournament_box.add_widget(Label(text=str(Container.players[j])))
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(Label(text=str(Container.players[j + 1])))
                    j += 2
            draw.add_widget(tournament_box)
            self.scroll_draw.add_widget(draw)
            Container.child = self.scroll_draw.children
            Container.child = Container.child[0].children
            Container.child = Container.child[0].children
            # print(len(children))
            print(len(Container.child))
        elif len(Container.players) != 0:
            j = 0
            while j != len(Container.child):
                if int(Container.child[j+1].text) >= int(Container.child[j+2].text):
                    Container.players_l.append(Container.child[j+3].text)
                    Container.players.remove(Container.child[j+3].text)
                elif int(Container.child[j+1].text) <= int(Container.child[j+2].text):
                    Container.players_l.append(Container.child[j].text)
                    Container.players.remove(Container.child[j].text)
                j += 4
            print(Container.players_l)
            print(Container.players)
            self.scroll_draw.clear_widgets(children = None)
            Container.now_tour += 1
            if Container.now_tour <= Container.all_tours:
                self.scroll_draw.add_widget(self.start_d)

                draw = BoxLayout(orientation='vertical')
                draw.add_widget(Label(text='Тур(' + str(Container.now_tour) + '/' + str(Container.all_tours) + ')'))
                tournament_box = GridLayout(cols=4, row_force_default=True, row_default_height=35)
                j = 0
                while j != len(Container.players):
                    tournament_box.add_widget(Label(text=str(Container.players[j])))
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(Label(text=str(Container.players[j + 1])))
                    j += 2
                draw.add_widget(tournament_box)
                self.scroll_draw.add_widget(draw)
                Container.child = self.scroll_draw.children
                Container.child = Container.child[0].children
                Container.child = Container.child[0].children
                # print(len(children))
                print(Container.child)
            else:

                # self.scroll_draw.remove_widget(Button)
                scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
                # top = GridLayout(cols=1, size_hint_y=10, row_force_default=True, row_default_height=35)
                mid = GridLayout(cols=3, size_hint_y=10, row_force_default=True, row_default_height=35)
                mid.add_widget(Label(text=Container.tournament_list[0]))
                mid.add_widget(Label(text=Container.tournament_list[1]))
                mid.add_widget(Label(text=Container.tournament_list[2]))
                mid.add_widget(Label(text='Место в турнире'))
                mid.add_widget(Label(text='Название команды'))
                mid.add_widget(Label(text='Страна'))
                mid.add_widget(Label(text='1 место'))
                mid.add_widget(Label(text=Container.players[0]))
                mid.add_widget(Label(text=Container.players_info[2]))
                j = 0
                while j !=  len(Container.players_l):
                    mid.add_widget(Label(text=str(j+2) + ' место'))
                    mid.add_widget(Label(text=Container.players_l[-j]))
                    mid.add_widget(Label(text=Container.players_info[2]))
                    j += 1
                # top.add_widget(mid)
                scroll.add_widget(mid)
                self.box_results.remove_widget(self.result_label)
                self.box_results.add_widget(scroll)


    def continue_draw(self):
        # self.scroll_draw.remove_widget(Button)
        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
        # top = GridLayout(cols=1, size_hint_y=10, row_force_default=True, row_default_height=35)
        mid = GridLayout(cols=3, size_hint_y=10, row_force_default=True, row_default_height=35)
        mid.add_widget(Label(text=Container.tournament_list[0]))
        mid.add_widget(Label(text=Container.tournament_list[1]))
        mid.add_widget(Label(text=Container.tournament_list[2]))
        mid.add_widget(Label(text='Место в турнире'))
        mid.add_widget(Label(text='Название команды'))
        mid.add_widget(Label(text='Страна'))
        mid.add_widget(Label(text='1 место'))
        mid.add_widget(Label(text=Container.players_info[0]))
        mid.add_widget(Label(text=Container.players_info[2]))
        mid.add_widget(Label(text='2 место'))
        mid.add_widget(Label(text=Container.players_info[3]))
        mid.add_widget(Label(text=Container.players_info[5]))
        mid.add_widget(Label(text='3 место'))
        mid.add_widget(Label(text=Container.players_info[6]))
        mid.add_widget(Label(text=Container.players_info[8]))
        mid.add_widget(Label(text='4 место'))
        mid.add_widget(Label(text=Container.players_info[9]))
        mid.add_widget(Label(text=Container.players_info[11]))
        # top.add_widget(mid)
        scroll.add_widget(mid)
        self.box_results.remove_widget(self.result_label)
        self.box_results.add_widget(scroll)


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
