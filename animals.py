# cowsay模比我预期所想象的要糟糕得多，我决定做一个比它更好的
import pprint as pp
import unicodedata

def get_all_animals():
    print("The following animals are included in this module:")
    # 生词中英互译 rhino = 犀牛 hippo = 河马 sloth = 树懒 otter = 水獭 hamster = 仓鼠 squirrel = 松鼠 peacock = 孔雀 
    all_ani = [
        'cat','dog','fish','goldfish',
        'cow','horse','sheep','pig','buffalo',
        'tiger','lion','bear','panda','fox',
        'rabbit','mouse','bat','hamster','squirrel',
        'monkey','ox','donkey','camel','wolf','leopard',
        'elephant','rhino','hippo','giraffe','zebra',
        'kangaroo','koala','sloth','otter','seal',
        'whale','dolphin','shark','penguin','parrot',
        'eagle','owl','peacock','chicken','duck']
    pp.pprint(all_ani)
    print(f"Total number of animals: {len(all_ani)}")
    print("Different animals have different actions and behaviors, which can be simulated in this module.")

def get_ani_act(ani_item,output=False):
    """获取动物的动作列表，ani_item必须是一个实例"""
    try:
        actions = getattr(ani_item, "act_list", None)
        if not isinstance(actions, list):
            raise TypeError
        if output:
             pp.pprint(actions)
        else:
            return actions
    except TypeError:
         print("ani_item 必须是带有 act_list 列表属性的动物对象")

def spk(outlook,words):
    """打印对话框，并在下方显示动物外观。"""
    lines = []
    current_line = ""
    current_width = 0
    def char_width(character):
        return 2 if unicodedata.east_asian_width(character) in ("W", "F") else 1
    for word in words.split():
        word_width = sum(char_width(character) for character in word)
        if current_line and current_width + 1 + word_width <= 20:
            current_line += " " + word
            current_width += 1 + word_width
            continue
        if current_line:
            lines.append(current_line)
            current_line = ""
            current_width = 0
        for character in word:
            width = char_width(character)
            if current_width + width > 20:
                lines.append(current_line)
                current_line = ""
                current_width = 0
            current_line += character
            current_width += width
    if current_line or not lines:
        lines.append(current_line)
    content_width = max(sum(char_width(character) for character in line) for line in lines)
    print("_" + "-" * (content_width + 2) + "_")
    for line in lines:
        line_width = sum(char_width(character) for character in line)
        print("| " + line + " " * (content_width - line_width) + " |")
    print("-" + "_" * (content_width + 2) + "-")
    print(" " * (content_width + 3) + "\\")
    print(outlook)
                
class Any:
    """
        可以是任何东西，甚至可以是一个茶壶
        （i don't know because i am a teapot)
    """
    def __init__(self,actls,otlk,name="i_am_nothing"):
        self.name = name
        self.actls = actls
        if "speak" not in actls:
            self.actls.append("speak")
        self.otlk = otlk

    def speak(self, words="Hello"):
        spk(self.otlk, words)

class Cat:
    def __init__(self, name="cat"):
        self.name = name
        self.act_list = ["speak", "meow", "scratch", "sleep"]
        self.fmt_outlook = r"""
             /\     /\
            / |\   /| \
           `   ----    `
         `{ < @ > < @ > }`
          \  == ◯◯ == /               __.
             j       l               ~` __.`>
             (        `E            f  /
             |          `Eo         (  (
              L  \     _   `G_       }  ]
              | \_|   /      `^^_   /  /
              }  /}   E  _--     l`^`_}
              ]  /]   /  (       )=TT~`
            (/|\) (/|\)-(/______>`"""

    def speak(self, words="Meow"):
        spk(self.fmt_outlook, words)


class Dog:
    def __init__(self, name="dog"):
        self.name = name
        self.act_list = ["speak", "bark", "fetch", "wag tail"]
        self.fmt_outlook = r"""
        / \__
       (    @\___
       /         O
      /   (_____/
     /_____/   U"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Fish:
    def __init__(self, name="fish"):
        self.name = name
        self.act_list = ["speak", "swim", "glide", "nibble"]
        self.fmt_outlook = r"""
       ><(((('>"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Goldfish:
    def __init__(self, name="goldfish"):
        self.name = name
        self.act_list = ["speak", "swim", "blow bubbles", "flap fins"]
        self.fmt_outlook = r"""
       ><((o)>"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Cow:
    def __init__(self, name="cow"):
        self.name = name
        self.act_list = ["speak", "moo", "graze", "chew cud"]
        self.fmt_outlook = r"""
       (__)
       (oo)
 /------\/
/ |    ||"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Horse:
    def __init__(self, name="horse"):
        self.name = name
        self.act_list = ["speak", "neigh", "gallop", "trot"]
        self.fmt_outlook = r"""
      >>\.
      /  \
     /|  |\
      /  /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Sheep:
    def __init__(self, name="sheep"):
        self.name = name
        self.act_list = ["speak", "baa", "graze", "bleat"]
        self.fmt_outlook = r"""
      __
   __( oo)
 /|  |  |\
  |__|__|"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Pig:
    def __init__(self, name="pig"):
        self.name = name
        self.act_list = ["speak", "oink", "root", "roll in mud"]
        self.fmt_outlook = r"""
      ^-----^
     ( o   o )
      \  ^  /
      /|___|\ """

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Buffalo:
    def __init__(self, name="buffalo"):
        self.name = name
        self.act_list = ["speak", "bellow", "graze", "charge"]
        self.fmt_outlook = r"""
     \       /
      \_____/
      (o   o)
       \___/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Tiger:
    def __init__(self, name="tiger"):
        self.name = name
        self.act_list = ["speak", "roar", "stalk", "pounce"]
        self.fmt_outlook = r"""
      /\_/\
     ( o.o )
    /|/|||\\|
      /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Lion:
    def __init__(self, name="lion"):
        self.name = name
        self.act_list = ["speak", "roar", "prowl", "rest"]
        self.fmt_outlook = r"""
     .------.
   .'  .--.  '.
  /   (o  o)   \
  \    \__/   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Bear:
    def __init__(self, name="bear"):
        self.name = name
        self.act_list = ["speak", "growl", "forage", "hibernate"]
        self.fmt_outlook = r"""
      (o_o)
     /|   |\
      /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Panda:
    def __init__(self, name="panda"):
        self.name = name
        self.act_list = ["speak", "munch bamboo", "climb", "roll"]
        self.fmt_outlook = r"""
      .--.
     (x  x)
    /( 0 )\
      /  /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Fox:
    def __init__(self, name="fox"):
        self.name = name
        self.act_list = ["speak", "yip", "sprint", "sneak"]
        self.fmt_outlook = r"""
       /\   /\
      (  o o  )
       \  ^  /
        /| |\\
       /_/ \_/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Rabbit:
    def __init__(self, name="rabbit"):
        self.name = name
        self.act_list = ["speak", "hop", "nibble", "thump"]
        self.fmt_outlook = r"""
       (\ /)
       (o.o)
       (   )
       /| |\
        / /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Mouse:
    def __init__(self, name="mouse"):
        self.name = name
        self.act_list = ["speak", "squeak", "scurry", "nibble"]
        self.fmt_outlook = r"""
      ()_()
      (o.o)
      /|_|\
       / /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Bat:
    def __init__(self, name="bat"):
        self.name = name
        self.act_list = ["speak", "screech", "flutter", "hang upside down"]
        self.fmt_outlook = r"""
    /\     /\
   /  \___/  \
  (  o     o  )
   \_/     \_/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Hamster:
    def __init__(self, name="hamster"):
        self.name = name
        self.act_list = ["speak", "run on wheel", "stuff cheeks", "burrow"]
        self.fmt_outlook = r"""
      .-.
     (o.o)
    (  _  )
     /___/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Squirrel:
    def __init__(self, name="squirrel"):
        self.name = name
        self.act_list = ["speak", "scamper", "climb", "bury nuts"]
        self.fmt_outlook = r"""
       __
     _(  )_
    (  o.o )
     /|___|\
      /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Monkey:
    def __init__(self, name="monkey"):
        self.name = name
        self.act_list = ["speak", "chatter", "swing", "climb"]
        self.fmt_outlook = r"""
      .-----.
     (  o o  )
      \  ^  /
      /|   |\
       /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Ox:
    def __init__(self, name="ox"):
        self.name = name
        self.act_list = ["speak", "bellow", "plow", "pull"]
        self.fmt_outlook = r"""
      \     /
       \___/
      (o   o)
      /|___|/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Donkey:
    def __init__(self, name="donkey"):
        self.name = name
        self.act_list = ["speak", "bray", "trot", "carry loads"]
        self.fmt_outlook = r"""
       /\  /\
      (  ..  )
       \ || /
      /|____|\
       /    /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Camel:
    def __init__(self, name="camel"):
        self.name = name
        self.act_list = ["speak", "walk", "kneel", "browse"]
        self.fmt_outlook = r"""
        __
      _(  )_
     /  /\  \
    (  /  \  )
       /  /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Wolf:
    def __init__(self, name="wolf"):
        self.name = name
        self.act_list = ["speak", "howl", "track", "run"]
        self.fmt_outlook = r"""
       / \__
      (    @\___
      /         O
     /   (_____/
    /_____/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Leopard:
    def __init__(self, name="leopard"):
        self.name = name
        self.act_list = ["speak", "stalk", "climb", "pounce"]
        self.fmt_outlook = r"""
       /\_/\
      ( o.o )
    .-o-o-o-o-.
      /     /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Elephant:
    def __init__(self, name="elephant"):
        self.name = name
        self.act_list = ["speak", "trumpet", "spray water", "flap ears"]
        self.fmt_outlook = r"""
      /  \~~~/  \
     (    ..     )
      \__      __/
         \____/
           ||
           ||___"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Rhino:
    def __init__(self, name="rhino"):
        self.name = name
        self.act_list = ["speak", "snort", "charge", "wallow"]
        self.fmt_outlook = r"""
       /\
      /  \___
     (  o    )
      \______/
       /    /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Hippo:
    def __init__(self, name="hippo"):
        self.name = name
        self.act_list = ["speak", "grunt", "wallow", "swim"]
        self.fmt_outlook = r"""
      .------.
     (  o  o  )
     |   __   |
      \______/
       /    /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Giraffe:
    def __init__(self, name="giraffe"):
        self.name = name
        self.act_list = ["speak", "browse leaves", "stride", "chew"]
        self.fmt_outlook = r"""
        .-.
        (o)
         |
      .--|--.
      |  |  |
      |  |  |"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Zebra:
    def __init__(self, name="zebra"):
        self.name = name
        self.act_list = ["speak", "whinny", "gallop", "graze"]
        self.fmt_outlook = r"""
       /\_/\
      ( o.o )
     /|/| |\
       /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Kangaroo:
    def __init__(self, name="kangaroo"):
        self.name = name
        self.act_list = ["speak", "hop", "box", "carry joey"]
        self.fmt_outlook = r"""
        /\
       /  \__
      ( o    )
       \_/\__/
        /  /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Koala:
    def __init__(self, name="koala"):
        self.name = name
        self.act_list = ["speak", "climb", "nap", "eat eucalyptus"]
        self.fmt_outlook = r"""
      .------.
     (  o  o  )
    (   .--.   )
      /|  |\
       /  /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Sloth:
    def __init__(self, name="sloth"):
        self.name = name
        self.act_list = ["speak", "hang", "sleep", "move slowly"]
        self.fmt_outlook = r"""
       .-.
      (o.o)
     _/| |\
    /  | | \
       / /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Otter:
    def __init__(self, name="otter"):
        self.name = name
        self.act_list = ["speak", "swim", "float", "crack shells"]
        self.fmt_outlook = r"""
      __
    _(o )>
   /  ___)
   \_/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Seal:
    def __init__(self, name="seal"):
        self.name = name
        self.act_list = ["speak", "bark", "swim", "balance"]
        self.fmt_outlook = r"""
       .-.
      (o o)
     /  V  \
    (_______)"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Whale:
    def __init__(self, name="whale"):
        self.name = name
        self.act_list = ["speak", "sing", "dive", "spout"]
        self.fmt_outlook = r"""
       __
   ___/  \__
  /  o      \
  \_________/~~"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Dolphin:
    def __init__(self, name="dolphin"):
        self.name = name
        self.act_list = ["speak", "click", "leap", "swim"]
        self.fmt_outlook = r"""
          __
     ____/o \__
    /         /
    \___/\___/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Shark:
    def __init__(self, name="shark"):
        self.name = name
        self.act_list = ["speak", "swim", "circle", "sense vibrations"]
        self.fmt_outlook = r"""
        /\
   ____/  \___
  <   ><      \>
   \__________/"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Penguin:
    def __init__(self, name="penguin"):
        self.name = name
        self.act_list = ["speak", "waddle", "slide", "swim"]
        self.fmt_outlook = r"""
       .---.
      / .-. \
     | (o o) |
     |  \_/  |
      \_____/
       /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Parrot:
    def __init__(self, name="parrot"):
        self.name = name
        self.act_list = ["speak", "squawk", "mimic", "perch"]
        self.fmt_outlook = r"""
        __
      >(o )___
       ( ._> /
        `---'"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Eagle:
    def __init__(self, name="eagle"):
        self.name = name
        self.act_list = ["speak", "soar", "screech", "hunt"]
        self.fmt_outlook = r"""
       \  /
     __ \/ __
    /  \  /  \
       (o )
        /|"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Owl:
    def __init__(self, name="owl"):
        self.name = name
        self.act_list = ["speak", "hoot", "perch", "hunt at night"]
        self.fmt_outlook = r"""
      ,_,
     (O,O)
     (   )
     -"-"-
     /   /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Peacock:
    def __init__(self, name="peacock"):
        self.name = name
        self.act_list = ["speak", "display feathers", "call", "strut"]
        self.fmt_outlook = r"""
       .-.
      (o o)
     / \|/ \
    o-o-o-o-o
       / /"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Chicken:
    def __init__(self, name="chicken"):
        self.name = name
        self.act_list = ["speak", "cluck", "peck", "scratch"]
        self.fmt_outlook = r"""
       ,~.
      (o )
     /)  )
    /(__)"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


class Duck:
    def __init__(self, name="duck"):
        self.name = name
        self.act_list = ["speak", "quack", "paddle", "dabble"]
        self.fmt_outlook = r"""
       __
   __(o )>
  \ <_. )
   `---'"""

    def speak(self, words="Hello"):
        spk(self.fmt_outlook, words)


