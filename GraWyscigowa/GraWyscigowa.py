import pygame
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "core"))
from core.ui import Menu, MapSelection, CreatorsScreen

pygame.init()

WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra Wyścigowa")

menu = Menu(SCREEN)
map_selection = MapSelection(SCREEN, WIDTH)  # Przekazujemy WIDTH
creators_screen = CreatorsScreen(SCREEN)

# Stany gry
current_screen = "MENU"
running = True

while running:
    SCREEN.fill((0, 0, 0))

    if current_screen == "MENU":
        menu.draw()
    elif current_screen == "MAP_SELECTION":
        map_selection.draw()
    elif current_screen == "CREATORS":
        creators_screen.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if current_screen == "MENU":
                if event.key == pygame.K_UP:
                    menu.move_up()
                elif event.key == pygame.K_DOWN:
                    menu.move_down()
                elif event.key == pygame.K_RETURN:
                    selected_option = menu.get_selected()

                    if selected_option == "Jeden gracz":
                        current_screen = "MAP_SELECTION"
                    elif selected_option == "Podzielony ekran":
                        print("Tryb podzielonego ekranu")
                    elif selected_option == "Sklep":
                        print("Przejście do sklepu")
                    elif selected_option == "Autorzy":
                        current_screen = "CREATORS"
                    elif selected_option == "Wyjdź z gry":
                        running = False

            elif current_screen == "MAP_SELECTION":
                if event.key == pygame.K_LEFT:
                    map_selection.move_left()
                elif event.key == pygame.K_RIGHT:
                    map_selection.move_right()
                elif event.key == pygame.K_RETURN:
                    print(f"Załadowano mapę: {map_selection.get_selected_map()}")
                    current_screen = "MENU"

            elif current_screen == "CREATORS":
                if event.key == pygame.K_ESCAPE:
                    current_screen = "MENU"

        elif event.type == pygame.MOUSEMOTION:
            if current_screen == "MENU":
                menu.check_mouse_hover(event.pos)
            elif current_screen == "MAP_SELECTION":
                map_selection.check_mouse_hover(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_screen == "MENU":
                selected_option = menu.check_mouse_click(event.pos)
                if selected_option == "Jeden gracz":
                    current_screen = "MAP_SELECTION"
                elif selected_option == "Autorzy":
                    current_screen = "CREATORS"
                elif selected_option == "Wyjdź z gry":
                    running = False

            elif current_screen == "MAP_SELECTION":
                selected_map = map_selection.check_mouse_click(event.pos)
                if selected_map == "BACK":
                    current_screen = "MENU"
                elif selected_map == "NEXT":
                    print(f"Załadowano mapę: {map_selection.get_selected_map()}")
                    current_screen = "MENU"

            elif current_screen == "CREATORS":
                selected_action = creators_screen.check_mouse_click(event.pos)
                if selected_action == "BACK":
                    current_screen = "MENU"

pygame.quit()
sys.exit()
