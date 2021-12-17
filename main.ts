scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardWater, function (sprite5, location4) {
    game.over(false, effects.dissolve)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (direccion == 0 && nivel == 2) {
        projectile = sprites.createProjectileFromSprite(assets.image`pro_dcha`, bueno, 200, 0)
    }
    if (direccion == 1 && nivel == 2) {
        projectile = sprites.createProjectileFromSprite(assets.image`pro_izqda`, bueno, -200, 0)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite6, otherSprite2) {
    if (bueno.overlapsWith(tesoro)) {
        info.changeScoreBy(1)
        music.baDing.play()
        tesoro.destroy()
    }
    if (bueno.overlapsWith(tesoro1)) {
        info.changeScoreBy(1)
        music.baDing.play()
        tesoro1.destroy()
    }
    if (bueno.overlapsWith(tesoro2)) {
        info.changeScoreBy(1)
        music.baDing.play()
        tesoro2.destroy()
    }
    if (bueno.overlapsWith(tesoro3)) {
        info.changeScoreBy(1)
        music.baDing.play()
        tesoro3.destroy()
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    game.over(false, effects.melt)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava1, function (sprite3, location3) {
    game.over(false, effects.melt)
})
function nivel_2 () {
    tesoro.destroy()
    tesoro1.destroy()
    tesoro2.destroy()
    tesoro3.destroy()
    tiles.setTilemap(tilemap`nivel_2`)
    color_fondo(randint(0, 15))
    bueno.ay = 200
    malo.setPosition(1024, 8)
    nivel = 2
    contador = 0
    info.startCountdown(10)
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite2, location2) {
    tiles.setTileAt(location2, img`
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
        `)
    info.changeScoreBy(1)
    music.baDing.play()
})
info.onCountdownEnd(function () {
    color_fondo(randint(0, 15))
    info.startCountdown(10)
})
function color_fondo (codigo_color: number) {
    if (codigo_color == 0) {
        scene.setBackgroundColor(0)
    }
    if (codigo_color == 1) {
        scene.setBackgroundColor(1)
    }
    if (codigo_color == 2) {
        scene.setBackgroundColor(2)
    }
    if (codigo_color == 3) {
        scene.setBackgroundColor(3)
    }
    if (codigo_color == 4) {
        scene.setBackgroundColor(4)
    }
    if (codigo_color == 5) {
        scene.setBackgroundColor(5)
    }
    if (codigo_color == 6) {
        scene.setBackgroundColor(6)
    }
    if (codigo_color == 7) {
        scene.setBackgroundColor(7)
    }
    if (codigo_color == 8) {
        scene.setBackgroundColor(8)
    }
    if (codigo_color == 9) {
        scene.setBackgroundColor(9)
    }
    if (codigo_color == 10) {
        scene.setBackgroundColor(10)
    }
    if (codigo_color == 11) {
        scene.setBackgroundColor(11)
    }
    if (codigo_color == 12) {
        scene.setBackgroundColor(12)
    }
    if (codigo_color == 13) {
        scene.setBackgroundColor(13)
    }
    if (codigo_color == 14) {
        scene.setBackgroundColor(14)
    }
    if (codigo_color == 15) {
        scene.setBackgroundColor(15)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite7, otherSprite3) {
    malo.destroy()
    malo = sprites.create(img`
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
        `, SpriteKind.Enemy)
    malo.setPosition(1024, 8)
    malo.follow(bueno, 25)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite4, otherSprite) {
    game.over(false, effects.dissolve)
})
let contador = 0
let projectile: Sprite = null
let direccion = 0
let nivel = 0
let malo: Sprite = null
let bueno: Sprite = null
let tesoro3: Sprite = null
let tesoro2: Sprite = null
let tesoro1: Sprite = null
let tesoro: Sprite = null
game.splash("come - come", "Autor: Claudio Orts")
game.setDialogTextColor(9)
game.setDialogFrame(img`
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
    `)
game.setDialogCursor(img`
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
    `)
game.showLongText("Tienes que recoger los 4 tesoros e impedir que el malo te detenga.", DialogLayout.Center)
info.setScore(0)
tiles.setTilemap(tilemap`nivel_1`)
tesoro = sprites.create(img`
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
    `, SpriteKind.Food)
tesoro.setPosition(120, 56)
tesoro1 = sprites.create(img`
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
    `, SpriteKind.Food)
tesoro1.setPosition(24, 120)
tesoro2 = sprites.create(img`
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
    `, SpriteKind.Food)
tesoro2.setPosition(168, 184)
tesoro3 = sprites.create(img`
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
    `, SpriteKind.Food)
tesoro3.setPosition(232, 72)
let nivel1 = sprites.create(img`
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
    `, SpriteKind.Food)
nivel1.setPosition(88, 200)
bueno = sprites.create(img`
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
    `, SpriteKind.Player)
bueno.setPosition(8, 88)
malo = sprites.create(img`
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
    `, SpriteKind.Enemy)
malo.setPosition(150, 110)
malo.follow(bueno, 25)
controller.moveSprite(bueno, 100, 100)
scene.cameraFollowSprite(bueno)
nivel = 1
direccion = 0
forever(function () {
    if (info.score() == 4 && bueno.overlapsWith(nivel1)) {
        info.changeScoreBy(10)
        music.magicWand.play()
        nivel1.destroy()
        nivel_2()
    }
    if (info.score() == 31) {
        game.over(true, effects.confetti)
    }
    if (controller.right.isPressed() && nivel == 2) {
        direccion = 0
    }
    if (controller.left.isPressed() && nivel == 2) {
        direccion = 1
    }
})
