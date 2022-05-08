from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from random import shuffle
from datetime import date


class Container(BoxLayout):
    empty = ObjectProperty()

    box_tournament = ObjectProperty()
    id_title = ObjectProperty()
    id_date = ObjectProperty()
    id_place = ObjectProperty()
    id_sport = ObjectProperty()
    id_format = ObjectProperty()
    start_t = ObjectProperty()

    box_players = ObjectProperty()
    scroll_players = ObjectProperty()
    id_team = ObjectProperty()
    id_rate = ObjectProperty()
    id_country = ObjectProperty()
    add_p = ObjectProperty()

    box_draw = ObjectProperty()
    scroll_draw = ObjectProperty()
    start_d = ObjectProperty()

    box_results = ObjectProperty()
    results_label = ObjectProperty()

    beacon = 0
    is_correct = True
    is_tournament_start = False
    tournament_list = []
    players_info = []
    players_w = []
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
        d = self.id_date.text
        d = d.split('.', 2)
        try:
            d = date(int(d[2]), int(d[1]), int(d[0]))
            if self.id_title.text.isalnum() and self.id_place.text.isalpha() and d >= date.today():
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
            elif self.id_title.text.isalnum() is False:
                self.id_title.text = "Некорректно"
            elif self.id_place.text.isalpha() is False:
                self.id_place.text = "Некорректно"
        except ValueError:
            self.id_date.text = "Некорректно"
        except IndexError:
            self.id_date.text = "Некорректно"
        except OverflowError:
            self.id_date.text = "Некорректно"

    def add_player(self):
        if self.id_team.text.isalnum() and self.id_rate.text.isdigit() and self.id_country.text.isalpha():
            player = GridLayout(cols=3)
            player.add_widget(Label(text=self.id_team.text))
            player.add_widget(Label(text=self.id_rate.text))
            player.add_widget(Label(text=self.id_country.text))
            self.scroll_players.add_widget(player)
            Container.players_info.append(self.id_team.text)
            Container.players_info.append(self.id_rate.text)
            Container.players_info.append(self.id_country.text)
            self.id_team.text = ""
            self.id_rate.text = ""
            self.id_country.text = ""
        elif self.id_team.text.isalnum() is False:
            self.id_team.text = "Некорректно"
        elif self.id_rate.text.isdigit() is False:
            self.id_rate.text = "Некорректно"
        elif self.id_country.text.isalpha() is False:
            self.id_country.text = "Некорректно"

    def start_draw(self):
        # Пока реализую только Single elimination (турнир на выбывание без сетки лузеров)
        if 128 >= len(Container.players_info) / 3 >= 2 and len(Container.players_w) == 0:
            self.scroll_players.remove_widget(self.add_p)
            i = 0
            while len(Container.players_w) != len(Container.players_info) / 3:
                Container.players_w.append(Container.players_info[i])
                i += 3
            shuffle(Container.players_w)
            j = len(Container.players_w) // 2
            i = 1
            while j != 1:
                j = j // 2
                i += 1
            difference = len(Container.players_w) - 2 ** i
            if difference == 0:
                Container.all_tours = i
            else:
                Container.all_tours = i + 1
            Container.now_tour = 1
            draw = BoxLayout(orientation='vertical')
            draw.add_widget(Label(text='Тур(' + str(Container.now_tour) + '/' + str(Container.all_tours) + ')'))
            tournament_box = GridLayout(cols=4, row_force_default=True, row_default_height=35)
            j = 0
            if difference == 0:
                while j != len(Container.players_w):
                    tournament_box.add_widget(Label(text=str(Container.players_w[j])))
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(Label(text=str(Container.players_w[j + 1])))
                    j += 2
            else:
                while j != difference * 2:
                    tournament_box.add_widget(Label(text=str(Container.players_w[j])))
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(TextInput())
                    tournament_box.add_widget(Label(text=str(Container.players_w[j + 1])))
                    j += 2
            draw.add_widget(tournament_box)
            self.scroll_draw.add_widget(draw)
            Container.child = self.scroll_draw.children
            Container.child = Container.child[0].children
            Container.child = Container.child[0].children
            # print(len(children))
            # print(len(Container.child))
        elif len(Container.players_w) != 0:
            j = 0
            a = 0
            b = 0
            while j != len(Container.child):
                if Container.child[j + 1].text.isdigit() and Container.child[j + 2].text.isdigit():
                    if int(Container.child[j + 1].text) == int(Container.child[j + 2].text):
                        Container.child[j + 1].text = 'Некорректно'
                        Container.child[j + 2].text = 'Некорректно'
                    else:
                        a += 1
                elif Container.child[j + 1].text.isdigit() is False or Container.child[j + 2].text.isdigit() is False:
                    Container.child[j + 1].text = 'Некорректно'
                    Container.child[j + 2].text = 'Некорректно'
                b += 1
                j += 4
            # print(Container.players_l)
            # print(Container.players)
            if a == b:
                j = 0
                while j != len(Container.child):
                    if int(Container.child[j + 1].text) > int(Container.child[j + 2].text):
                        Container.players_l.append(Container.child[j + 3].text)
                        Container.players_w.remove(Container.child[j + 3].text)
                    elif int(Container.child[j + 1].text) < int(Container.child[j + 2].text):
                        Container.players_l.append(Container.child[j].text)
                        Container.players_w.remove(Container.child[j].text)
                    j += 4
                self.scroll_draw.clear_widgets(children=None)
                Container.now_tour += 1
                if Container.now_tour <= Container.all_tours:
                    self.scroll_draw.add_widget(self.start_d)

                    draw = BoxLayout(orientation='vertical')
                    draw.add_widget(Label(text='Тур(' + str(Container.now_tour) + '/' + str(Container.all_tours) + ')'))
                    tournament_box = GridLayout(cols=4, row_force_default=True, row_default_height=35)
                    j = 0
                    while j != len(Container.players_w):
                        tournament_box.add_widget(Label(text=str(Container.players_w[j])))
                        tournament_box.add_widget(TextInput())
                        tournament_box.add_widget(TextInput())
                        tournament_box.add_widget(Label(text=str(Container.players_w[j + 1])))
                        j += 2
                    draw.add_widget(tournament_box)
                    self.scroll_draw.add_widget(draw)
                    Container.child = self.scroll_draw.children
                    Container.child = Container.child[0].children
                    Container.child = Container.child[0].children
                    # print(len(children))
                    # print(Container.child)
                else:
                    scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
                    mid = GridLayout(cols=3, size_hint_y=10, row_force_default=True, row_default_height=35)
                    mid.add_widget(Label(text=Container.tournament_list[0]))
                    mid.add_widget(Label(text=Container.tournament_list[1]))
                    mid.add_widget(Label(text=Container.tournament_list[2]))
                    mid.add_widget(Label(text='Место в турнире'))
                    mid.add_widget(Label(text='Название команды'))
                    mid.add_widget(Label(text='Страна'))
                    mid.add_widget(Label(text='1 место'))
                    mid.add_widget(Label(text=Container.players_w[0]))
                    mid.add_widget(
                        Label(text=Container.players_info[Container.players_info.index(Container.players_w[0]) + 2]))
                    j = 0
                    while j != len(Container.players_l):
                        mid.add_widget(Label(text=str(j + 2) + ' место'))
                        mid.add_widget(Label(text=Container.players_l[-(j + 1)]))
                        mid.add_widget(Label(
                            text=Container.players_info[Container.players_info.index(Container.players_l[-(j + 1)]) + 2]))
                        j += 1
                    scroll.add_widget(mid)
                    self.box_results.remove_widget(self.results_label)
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
