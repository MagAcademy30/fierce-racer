# By OrangeDog Team, MG30.
# config.py содержит настройки игры, которые изменяются только
# через исходный код

screensize = (165, 100)
fps = 60
debug = 0
disable_collision = 0
mixer_channels = 4
version = "0.6"
font_path = "assets/font.ttf"
button_colors = [(255, 255, 255), (150, 150, 150), (0, 0, 0)] # Неактивная, активная, цвет шрифта
player_pos = (63.3, 78)

paths_to_sound = {
	"gfx": {
		"car_crash": "assets/gfx/car_crash.ogg",
		"car_move": "assets/gfx/car_move.ogg",
		"game_pause": "assets/gfx/game_pause.ogg",
		"car_engine": "assets/gfx/car_engine.ogg"
	}
}

paths_to_texture = {
	"car": {
		"car_aqua":"assets/texture/car/car_aqua.png",
		"car_lime":"assets/texture/car/car_lime.png",
		"car_taxi":"assets/texture/car/car_taxi.png",
		"car_white":"assets/texture/car/car_white.png"
	},
	"bus": {
		"bus_aqua": "assets/texture/bus/bus_aqua.png",
		"bus_grey": "assets/texture/bus/bus_grey.png",
		"bus_lime": "assets/texture/bus/bus_lime.png"
	},
	"gazzel": {
		"gazzel_aqua": "assets/texture/gazzel/gazzel_aqua.png",
		"gazzel_lime": "assets/texture/gazzel/gazzel_lime.png",
		"gazzel_red": "assets/texture/gazzel/gazzel_red.png",
		"gazzel_white": "assets/texture/gazzel/gazzel_white.png"
	},
	"skin": {
		"skin_2young": "assets/texture/skin/skin_2young.png",
		"skin_3young": "assets/texture/skin/skin_3young.png",
		"skin_4young": "assets/texture/skin/skin_4young.png",
		"skin_police": "assets/texture/skin/skin_police.png",
		"skin_sportblue": "assets/texture/skin/skin_sportblue.png",
		"skin_sportlime": "assets/texture/skin/skin_sportlime.png",
		"skin_sportyellow": "assets/texture/skin/skin_sportyellow.png",
		"skin_xp14": "assets/texture/skin/skin_xp14.png",
		"skin_young": "assets/texture/skin/skin_young.png",
	},
	"bg": {
		"bg_default": "assets/texture/bg/bg_default.png",
	},
	"gui": {
		"gameover_screen": "assets/texture/gui/gameover_screen.png",
		"logo": "assets/texture/gui/logo.png",
		"button": "assets/texture/gui/button.png"
	},
	"intro": {
		"orangedogteam_logo": "assets/texture/intro/orangedogteam_logo.png",
		"pygame_powered_logo": "assets/texture/intro/pygame_powered_logo.png"
	}
}