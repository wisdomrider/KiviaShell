import random

happyEmojis = "😀 😁 😂 😃 😄 😅 😆 😉 😊 😋 😎 😍 🥰 ☺️ 😛 😜 😝 😺 😸 😹 👍 ✊ ✌ ⭐️ ✨ ⚡️ ☄️ 🖖 👨 🦖 🦇 🦚 💥 🍭  🎸 🎮 ❤️ 🧡 💛 💚 💙 💜 ".split(
    " ")
sadEmojis = "😥 😮 😯 😪 😫".split(" ")
animalsEmojis = "🐶;🐱;🐭;🐹;🐰;🦊;🦝;🐻;🐼;🦘;🦡;🐨;🐯;🦁;🐮;🐷;🐽;🐸;🐵;🙈;🙉;🙊;🐒;🐔;🐧;🐦;🐤;🐣;🐥;🦆;🦢;🦅;🦉;🦚;🦜;🦇;🐺;🐗;🐴;🦄;🐝;🐛;🦋;🐌;🐚;🐞;🐜;🦗;🕷;🕸;🦂;🦟;🦠;🐢;🐍;🦎;🦖;🦕;🐙;🦑;🦐;🦀;🐡;🐠;🐟;🐬;🐳;🐋;🦈;🐊;🐅;🐆;🦓;🦍;🐘;🦏;🦛;🐪;🐫;🦙;🦒;🐃;🐂;🐄;🐎;🐖;🐏;🐑;🐐;🦌;🐕;🐩;🐈;🐓;🦃;🕊;🐇;🐁;🐀;🐿;🦔;🐾;🐉;🐲;".split(
    ";")
natureEmojis = "🌵;🎄;🌲;🌳;🌴;🌱;🌿;☘️;🍀;🎍;🎋;🍃;🍂;🍁;🍄;🌾;💐;🌷;🌹;🥀;🌺;🌸;🌼;🌻;🌞;🌝;🌛;🌜;🌚;🌕;🌖;🌗;🌘;🌑;🌒;🌓;🌔;🌙;🌎;🌍;🌏;💫;⭐️;🌟;✨;⚡️;☄️;💥;🔥;🌪;🌈;☀️;🌤;⛅️;🌥;☁️;🌦;🌧;⛈;🌩;🌨;❄️;☃️;⛄️;🌬;💨;💧;💦;☔️;☂️;🌊;🌫;".split(
    ";")

travelEmojis = "🚗;🚕;🚙;🚌;🚎;🏎;🚓;🚑;🚒;🚐;🚚;🚛;🚜;🛴;🚲;🛵;🏍;🚨;🚔;🚍;🚘;🚖;🚡;🚠;🚟;🚃;🚋;🚞;🚝;🚄;🚅;🚈;🚂;🚆;🚇;🚊;🚉;✈️;🛫;🛬;🛩;💺;🛰;🚀;🛸;🚁;🛶;⛵️;🚤;🛥;🛳;⛴;🚢;⚓️;⛽️;🚧;🚦;🚥;🚏;🗺;🗿;🗽;🗼;🏰;🏯;🏟;🎡;🎢;🎠;⛲️;⛱;🏖;🏝;🏜;🌋;⛰;🏔;🗻;🏕;⛺️;🏠;🏡;🏘;🏚;🏗;🏭;🏢;🏬;🏣;🏤;🏥;🏦;🏨;🏪;🏫;🏩;💒;🏛;⛪️;🕌;🕍;🕋;⛩;🛤;🛣;🗾;🎑;🏞;🌅;🌄;🌠;🎇;🎆;🌇;🌆;🏙;🌃;🌌;🌉;🌁".split(
    ";")


def getHappyEmoji():
    return happyEmojis[random.randrange(len(happyEmojis))]


def getTravelEmoji():
    return travelEmojis[random.randrange(len(travelEmojis))]


def getNatureEmoji():
    return natureEmojis[random.randrange(len(natureEmojis))]


def getAnimalEmoji():
    return animalsEmojis[random.randrange(len(animalsEmojis))]


def getSadEmoji():
    return sadEmojis[random.randrange(len(sadEmojis))]


def getBlank():
    return ""
