import pygame
import os

class CreatorsScreen:
    def __init__(self, screen):
        self.screen = screen

        # 🔹 Ścieżka do katalogu z obrazkami
        self.image_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")

        # 🔹 Wczytanie tła
        self.background_image = self.load_image("main_screen.jpg", (1280, 720))

        # 🔹 Lista plików z autorami
        self.creators = ["creators.png", "ck.png", "kk.png", "ws.png", "kw.png"]

        # 🔹 Wczytanie obrazków autorów
        self.creator_images = [self.load_image(name, (400, 80)) for name in self.creators]

        # 🔹 Obliczenie pozycji dla obrazków (wyśrodkowane)
        self.creator_positions = [(640, 180 + i * 100) for i in range(len(self.creators))]

        # 🔹 Wczytanie przycisku "Powrót"
        self.back_button = (self.load_image("back.png"), self.load_image("back_hover.png"))
        self.back_button_pos = (150, 650)  

    def load_image(self, filename, size=None):
        """Ładuje obrazek z katalogu assets/images/"""
        path = os.path.join(self.image_dir, filename)
        if not os.path.exists(path):
            print(f"⚠ Błąd: Nie znaleziono pliku {path}")
            return None
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size) if size else image

    def draw(self):
        """Rysuje ekran autorów"""
        self.screen.blit(self.background_image, (0, 0))  

        # Rysowanie obrazków autorów
        for i, img in enumerate(self.creator_images):
            if img:
                rect = img.get_rect(center=self.creator_positions[i])
                self.screen.blit(img, rect)

        # Rysowanie przycisku "Powrót"
        self.draw_button(self.back_button, self.back_button_pos)

    def draw_button(self, button_images, position):
        """Rysuje przycisk z odpowiednim obrazkiem (hover lub normalny)"""
        normal_img, hover_img = button_images
        x, y = position
        img = hover_img if self.is_hovered(position) else normal_img
        if img:
            rect = img.get_rect(center=(x, y))
            self.screen.blit(img, rect)

    def is_hovered(self, position):
        """Sprawdza, czy kursor myszki najechał na dany obszar"""
        x, y = position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return x - 50 < mouse_x < x + 50 and y - 25 < mouse_y < y + 25

    def check_mouse_click(self, pos):
        """Sprawdza, czy kliknięto na przycisk Powrót"""
        if self.is_hovered(self.back_button_pos):
            return "BACK"
        return None


class MapSelection:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width  

        # 🔹 Ścieżka do katalogu z obrazkami
        self.image_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")

        # 🔹 Wczytanie tła
        self.background_image = self.load_image("map_selection_bg.jpg", (1280, 720))

        # 🔹 Lista dostępnych map
        self.maps = ["map1.png", "map2.png", "map3.png"]

        # 🔹 Wczytanie obrazków dla map
        self.map_images = [self.load_image(map_name, (200, 200)) for map_name in self.maps]
        self.map_hover_images = [self.load_image(map_name.replace(".png", "_hover.png"), (200, 200)) for map_name in self.maps]

        # 🔹 Pozycje map (wyśrodkowane)
        total_maps = len(self.maps)
        total_width = total_maps * 200 + (total_maps - 1) * 30
        start_x = (self.width - total_width) // 2  

        self.map_positions = [(start_x + i * (315 + 30), 300) for i in range(total_maps)]

        self.selected = None  
        self.hovered = -1  

        # 🔹 Wczytanie przycisków "Cofnij" i "Dalej"
        self.back_button = (self.load_image("back.png"), self.load_image("back_hover.png"))
        self.next_button = (self.load_image("next.png"), self.load_image("next_hover.png"))

        # 🔹 Pozycje przycisków
        self.back_button_pos = (150, 650)  
        self.next_button_pos = (1130, 650)  

    def load_image(self, filename, size=None):
        """Ładuje obrazek z katalogu assets/images/"""
        path = os.path.join(self.image_dir, filename)
        if not os.path.exists(path):
            print(f"⚠ Błąd: Nie znaleziono pliku {path}")
            return None
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size) if size else image

    def draw(self):
        """Rysuje ekran wyboru mapy"""
        self.screen.blit(self.background_image, (0, 0))  

        # Rysowanie map
        for i, map_img in enumerate(self.map_images):
            x, y = self.map_positions[i]
            if i == self.selected:  
                img = self.map_hover_images[i]
            elif i == self.hovered:  
                img = self.map_hover_images[i]
            else:
                img = map_img  
            if img:
                rect = img.get_rect(center=(x, y))
                self.screen.blit(img, rect)

        # Rysowanie przycisków
        self.draw_button(self.back_button, self.back_button_pos)
        self.draw_button(self.next_button, self.next_button_pos)

    def draw_button(self, button_images, position):
        """Rysuje przycisk z odpowiednim obrazkiem (hover lub normalny)"""
        normal_img, hover_img = button_images
        x, y = position
        img = hover_img if self.is_hovered(position) else normal_img
        if img:
            rect = img.get_rect(center=(x, y))
            self.screen.blit(img, rect)

    def is_hovered(self, position):
        """Sprawdza, czy kursor myszki najechał na dany obszar"""
        x, y = position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return x - 50 < mouse_x < x + 50 and y - 25 < mouse_y < y + 25

    def move_left(self):
        """Przesuwa zaznaczenie mapy w lewo"""
        self.selected = (self.selected - 1) % len(self.maps)

    def move_right(self):
        """Przesuwa zaznaczenie mapy w prawo"""
        self.selected = (self.selected + 1) % len(self.maps)

    def get_selected_map(self):
        """Zwraca wybraną mapę"""
        return self.maps[self.selected] if self.selected is not None else None

    def check_mouse_hover(self, pos):
        """Zmienia zaznaczoną mapę, jeśli myszka najeżdża na obrazek"""
        self.hovered = -1  
        for i, map_img in enumerate(self.map_images):
            if map_img:
                x, y = self.map_positions[i]
                rect = map_img.get_rect(center=(x, y))  
                if rect.collidepoint(pos):
                    self.hovered = i
                    break

    def check_mouse_click(self, pos):
        """Sprawdza, czy kliknięto na mapę"""
        for i, map_img in enumerate(self.map_images):
            if map_img:
                x, y = self.map_positions[i]
                rect = map_img.get_rect(center=(x, y))  
                if rect.collidepoint(pos):
                    if self.selected == i:  
                        return None
                    self.selected = i  
                    break

        if self.is_hovered(self.back_button_pos):
            return "BACK"
        elif self.is_hovered(self.next_button_pos):
            return "NEXT"
        
        return None


class Menu:
    def __init__(self, screen):
        self.screen = screen

        # 🔹 Ścieżka do katalogu z obrazkami
        self.image_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "images")

        # 🔹 Wczytanie tła
        self.background_image = self.load_image("main_screen.jpg", (1280, 720))

        # 🔹 Wczytanie logo
        self.logo = self.load_image("logo.png", (400, 240))  # Dopasowany rozmiar logo
        self.logo_pos = (640, 100)  # Pozycja na środku, u góry

        # 🔹 Opcje menu
        self.options = [
            ("single.png", "single_hover.png"),
            ("split.png", "split_hover.png"),
            ("shop.png", "shop_hover.png"),
            ("creators.png", "creators_hover.png"),
            ("exit.png", "exit_hover.png")
        ]

        self.buttons = [(self.load_image(normal), self.load_image(hover)) for normal, hover in self.options]
        self.option_positions = [(640, 250 + i * 100) for i in range(len(self.options))]

        self.selected = 0  

    def load_image(self, filename, size=None):
        """Ładuje obrazek z katalogu assets/images/"""
        path = os.path.join(self.image_dir, filename)
        if not os.path.exists(path):
            print(f"⚠ Błąd: Nie znaleziono pliku {path}")
            return None
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size) if size else image

    def draw(self):
        """Rysuje menu na ekranie"""
        self.screen.blit(self.background_image, (0, 0))  

        # 🔹 Rysowanie logo
        if self.logo:
            rect = self.logo.get_rect(center=self.logo_pos)
            self.screen.blit(self.logo, rect)

        for i, (normal_img, hover_img) in enumerate(self.buttons):
            x, y = self.option_positions[i]
            img = hover_img if i == self.selected else normal_img  
            if img:
                rect = img.get_rect(center=(x, y))
                self.screen.blit(img, rect)

    def move_up(self):
        """Przesuwa zaznaczenie w górę"""
        self.selected = (self.selected - 1) % len(self.options)

    def move_down(self):
        """Przesuwa zaznaczenie w dół"""
        self.selected = (self.selected + 1) % len(self.options)

    def get_selected(self):
        return ["Jeden gracz", "Podzielony ekran", "Sklep", "Autorzy", "Wyjdź z gry"][self.selected]

    def check_mouse_hover(self, pos):
        """Zmienia zaznaczoną opcję, jeśli myszka najeżdża na obrazek"""
        for i, (normal_img, _) in enumerate(self.buttons):
            if normal_img:
                x, y = self.option_positions[i]
                rect = normal_img.get_rect(center=(x, y))

                # 🔹 Zmniejszamy hitbox o 20% szerokości i wysokości
                smaller_rect = rect.inflate(-rect.width * 0.2, -rect.height * 0.2)

                if smaller_rect.collidepoint(pos):
                    self.selected = i
                    break

    def check_mouse_click(self, pos):
        """Sprawdza, czy kliknięto na opcję"""
        for i, (normal_img, _) in enumerate(self.buttons):
            if normal_img:
                x, y = self.option_positions[i]
                rect = normal_img.get_rect(center=(x, y))

                # 🔹 Zmniejszony hitbox o 20%
                smaller_rect = rect.inflate(-rect.width * 0.2, -rect.height * 0.2)

                if smaller_rect.collidepoint(pos):
                    return self.get_selected()
        return None
