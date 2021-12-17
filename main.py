def on_b_pressed():
    global projectile
    if direccion == 0 and nivel == 2:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            pro_dcha
        """), bueno, 200, 0)
    if direccion == 1 and nivel == 2:
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            pro_izqda
        """), bueno, -200, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile(sprite, location):
    game.over(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def nivel_2():
    global nivel, contador
    tesoro.destroy()
    tesoro1.destroy()
    tesoro2.destroy()
    tesoro3.destroy()
    tiles.set_tilemap(tilemap("""
        nivel_2
    """))
    color_fondo(randint(0, 15))
    bueno.ay = 200
    malo.set_position(1024, 8)
    nivel = 2
    contador = 0
    info.start_countdown(10)

def on_countdown_end():
    color_fondo(randint(0, 15))
    info.start_countdown(10)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2,
        img("""
            . b b b b b b b b b b b b b b . 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                    b b b b b b b d d b b b b b b b 
                    . b b b b b b c c b b b b b b . 
                    b c c c c c b c c b c c c c c b 
                    b c c c c c c b b c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b b b b b b b b b b b b b b b b 
                    b e e e e e e e e e e e e e e b 
                    b e e e e e e e e e e e e e e b 
                    b c e e e e e e e e e e e e c b 
                    b b b b b b b b b b b b b b b b 
                    . b b . . . . . . . . . . b b .
        """))
    info.change_score_by(1)
    music.ba_ding.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.over(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile3)

def on_on_overlap(sprite4, otherSprite):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_overlap_tile4(sprite5, location4):
    game.over(False, effects.dissolve)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile4)

def on_on_overlap2(sprite6, otherSprite2):
    if bueno.overlaps_with(tesoro):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro.destroy()
    if bueno.overlaps_with(tesoro1):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro1.destroy()
    if bueno.overlaps_with(tesoro2):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro2.destroy()
    if bueno.overlaps_with(tesoro3):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro3.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def color_fondo(codigo_color: number):
    if codigo_color == 0:
        scene.set_background_color(0)
    if codigo_color == 1:
        scene.set_background_color(1)
    if codigo_color == 2:
        scene.set_background_color(2)
    if codigo_color == 3:
        scene.set_background_color(3)
    if codigo_color == 4:
        scene.set_background_color(4)
    if codigo_color == 5:
        scene.set_background_color(5)
    if codigo_color == 6:
        scene.set_background_color(6)
    if codigo_color == 7:
        scene.set_background_color(7)
    if codigo_color == 8:
        scene.set_background_color(8)
    if codigo_color == 9:
        scene.set_background_color(9)
    if codigo_color == 10:
        scene.set_background_color(10)
    if codigo_color == 11:
        scene.set_background_color(11)
    if codigo_color == 12:
        scene.set_background_color(12)
    if codigo_color == 13:
        scene.set_background_color(13)
    if codigo_color == 14:
        scene.set_background_color(14)
    if codigo_color == 15:
        scene.set_background_color(15)

def on_on_overlap3(sprite7, otherSprite3):
    global malo
    malo.destroy()
    malo = sprites.create(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 5 5 5 5 5 2 2 2 2 5 5 5 5 5 2 
                    2 5 f f f 5 2 2 2 2 5 f f f 5 2 
                    2 5 f f f 5 2 2 2 2 5 f f f 5 2 
                    2 5 f f f 5 2 2 2 2 5 f f f 5 2 
                    2 5 5 5 5 5 2 2 2 2 5 5 5 5 5 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 a 5 a 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 a 5 a 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        SpriteKind.enemy)
    malo.set_position(1024, 8)
    malo.follow(bueno, 25)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

contador = 0
projectile: Sprite = None
direccion = 0
nivel = 0
malo: Sprite = None
bueno: Sprite = None
tesoro3: Sprite = None
tesoro2: Sprite = None
tesoro1: Sprite = None
tesoro: Sprite = None
game.splash("come - come", "Autor: Claudio Orts")
game.set_dialog_text_color(9)
game.set_dialog_frame(img("""
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
"""))
game.set_dialog_cursor(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . 6 6 6 5 5 6 6 6 . . . . 
        . . . 7 7 7 7 6 6 6 6 6 6 . . . 
        . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
        . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
        . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
        . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
        . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
        . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
        . . . 6 8 8 8 8 8 8 8 8 6 . . . 
        . . . . 6 6 8 8 8 8 6 6 . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . . . . . . . . . . . . .
"""))
game.show_long_text("Tienes que recoger los 4 tesoros e impedir que el malo te detenga.",
    DialogLayout.CENTER)
info.set_score(0)
tiles.set_tilemap(tilemap("""
    nivel_1
"""))
tesoro = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . 6 6 6 5 5 6 6 6 . . . . 
            . . . 7 7 7 7 6 6 6 6 6 6 . . . 
            . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
            . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
            . . . . 6 6 8 8 8 8 6 6 . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro.set_position(120, 56)
tesoro1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . 6 6 6 5 5 6 6 6 . . . . 
            . . . 7 7 7 7 6 6 6 6 6 6 . . . 
            . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
            . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
            . . . . 6 6 8 8 8 8 6 6 . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro1.set_position(24, 120)
tesoro2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro2.set_position(168, 184)
tesoro3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro3.set_position(232, 72)
nivel1 = sprites.create(img("""
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
            6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
            6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
            6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
            6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
            6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
            6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
            6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
            6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
            6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    """),
    SpriteKind.food)
nivel1.set_position(88, 200)
bueno = sprites.create(img("""
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 5 5 5 5 5 8 8 5 5 5 5 5 8 8 
            8 8 5 5 5 5 5 8 8 5 5 5 5 5 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """),
    SpriteKind.player)
bueno.set_position(8, 88)
malo = sprites.create(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 5 5 5 5 5 2 2 2 2 5 5 5 5 5 2 
            2 5 f f f 5 2 2 2 2 5 f f f 5 2 
            2 5 f f f 5 2 2 2 2 5 f f f 5 2 
            2 5 f f f 5 2 2 2 2 5 f f f 5 2 
            2 5 5 5 5 5 2 2 2 2 5 5 5 5 5 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 a 5 a 2 2 2 2 2 2 2 2 
            2 2 2 2 2 a 5 a 2 2 2 2 2 2 2 2 
            2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    """),
    SpriteKind.enemy)
malo.set_position(150, 110)
malo.follow(bueno, 25)
controller.move_sprite(bueno, 100, 100)
scene.camera_follow_sprite(bueno)
nivel = 1
direccion = 0

def on_forever():
    global direccion
    if info.score() == 4 and bueno.overlaps_with(nivel1):
        info.change_score_by(10)
        music.magic_wand.play()
        nivel1.destroy()
        nivel_2()
    if info.score() == 31:
        game.over(True, effects.confetti)
    if controller.right.is_pressed() and nivel == 2:
        direccion = 0
    if controller.left.is_pressed() and nivel == 2:
        direccion = 1
forever(on_forever)
