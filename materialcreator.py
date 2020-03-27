import os

from jsonmaker.blockitemjson import *
from jsonmaker.blockjson import *
from jsonmaker.blockstatejson import *
from jsonmaker.itemjson import *
from texturemaker.creator import *
from texturemaker.orecreator import *

# modid = input("What is your modid? ")
# resourcelocation = input("What is your resource location? ")
# localized = input("What is your localized name? ")
# rgba = eval(input("What is your desired RGBA? "))
# directory = input("Where is your mod's src folder? ") + "/resources"

modid = "tadas77_materials_mod"
resourcelocation = "jade"
localized = "Jade"
rgba = (0, 255, 0, 128)
directory = "/Users/jayjay/programming/project/test/resources"

assets_dir = directory + "/assets"
data_dir = directory + "/data"

# Item Jsons
itemjsons = ["axe", "chest", "feet", "helm", "hoe", "item", "legs", "pickaxe", "shovel", "sword"]
pitemjsons = [f'{assets_dir}/{modid}/models/item/{resourcelocation}/{name}.json' for name in itemjsons]

os.makedirs(f'{assets_dir}/{modid}/models/item/{resourcelocation}/', exist_ok=True)
for i in range(len(itemjsons)):
    itemJSON(modid, resourcelocation + "/" + itemjsons[i], pitemjsons[i])

# Block Item Jsons
blockitemjsons = ["block", "oreblock"]
pblockitemjsons = [f'{assets_dir}/{modid}/models/item/{resourcelocation}/{name}.json' for name in blockitemjsons]

os.makedirs(f'{assets_dir}/{modid}/models/item/{resourcelocation}/', exist_ok=True)
for i in range(len(blockitemjsons)):
    blockItemJSON(modid, resourcelocation + "/" + blockitemjsons[i], pblockitemjsons[i])

# Block Jsons
blockjsons = ["block", "oreblock"]
pblockjsons = [f'{assets_dir}/{modid}/models/block/{resourcelocation}/{name}.json' for name in blockjsons]

os.makedirs(f'{assets_dir}/{modid}/models/block/{resourcelocation}/', exist_ok=True)
for i in range(len(blockjsons)):
    blockJSON(modid, resourcelocation + "/" + blockjsons[i], pblockjsons[i])

# Block State Jsons
blockstatejsons = ["block", "oreblock"]
pblockstatejsons = [f'{assets_dir}/{modid}/blockstates/{resourcelocation}/{name}.json' for name in blockstatejsons]

os.makedirs(f'{assets_dir}/{modid}/blockstates/{resourcelocation}', exist_ok=True)
for i in range(len(blockstatejsons)):
    blockStateJSON(modid, resourcelocation + "/" + blockstatejsons[i], pblockstatejsons[i])


# Lang
def langfile(localized, resourcelocation, file):
    text = f"""{{
    # {localized}
	"item.tadas77_materials_mod.{resourcelocation}.item": "{localized} Ingot",
	"block.tadas77_materials_mod.{resourcelocation}.block": "{localized} Block",
	"block.tadas77_materials_mod.{resourcelocation}.oreblock": "{localized} Ore",
	
	"item.tadas77_materials_mod.{resourcelocation}.axe": "{localized} Axe",
	"item.tadas77_materials_mod.{resourcelocation}.pickaxe": "{localized} Pickaxe",
	"item.tadas77_materials_mod.{resourcelocation}.shovel": "{localized} Shovel",
	"item.tadas77_materials_mod.{resourcelocation}.hoe": "{localized} Hoe",
	"item.tadas77_materials_mod.{resourcelocation}.sword": "{localized} Sword",
	
	"item.tadas77_materials_mod.{resourcelocation}.helm": "{localized} Helmet",
	"item.tadas77_materials_mod.{resourcelocation}.chest": "{localized} Chestplate",
	"item.tadas77_materials_mod.{resourcelocation}.legs": "{localized} Leggings",
	"item.tadas77_materials_mod.{resourcelocation}.feet": "{localized} Boots"
    }}"""

    with open(file, "w") as f:
        f.write(text)


os.makedirs(f'{assets_dir}/{modid}/lang/', exist_ok=True)
langfile(localized, resourcelocation, f'{assets_dir}/{modid}/lang/en_us.json')

# Block Textures
os.makedirs(f'{assets_dir}/{modid}/textures/block/{resourcelocation}/', exist_ok=True)
stdImage(rgba, "/Users/jayjay/programming/project/Minecraft/forge-tools/texturemaker/textures/blocks/iron_block.png",
         f'{assets_dir}/{modid}/textures/block/{resourcelocation}/block.png')

oreImage(rgba, f'{assets_dir}/{modid}/textures/block/{resourcelocation}/oreblock.png')

# Item Textures
itemtextures = ["axe", "chest", "feet", "helm", "hoe", "item", "legs", "pickaxe", "shovel", "sword"]
aitemtextures = ["axe", "chestplate", "boots", "helmet", "hoe", "ingot", "leggings", "pickaxe", "shovel", "sword"]
pitemtextures = [f'{assets_dir}/{modid}/textures/item/{resourcelocation}/{name}.png' for name in itemtextures]

os.makedirs(f'{assets_dir}/{modid}/textures/item/{resourcelocation}/', exist_ok=True)
for i in range(len(itemtextures)):
    stdImage(rgba,
             f"/Users/jayjay/programming/project/Minecraft/forge-tools/texturemaker/textures/items/iron_{aitemtextures[i]}.png",
             pitemtextures[i])


# Data Files
def process(path, npath):
    content = ""
    with open(path) as f:
        content = f.read()

    content = content.replace("tadas77_materials_mod", modid).replace("copper", resourcelocation)

    with open(npath, "w") as f:
        f.write(content)


## Lootables
block_lootable = ["oreblock", "block"]
pold_block_lootable = [
    f'/Users/jayjay/programming/project/Minecraft/forge-tools/jsonmaker/data/MODID/loot_tables/blocks/RESOURCE_LOCATION/{b}.json'
    for b in block_lootable]
pnew_block_lootable = [f'{data_dir}/{modid}/loot_tables/{resourcelocation}/{b}.json' for b in block_lootable]

os.makedirs(f'{data_dir}/{modid}/loot_tables/{resourcelocation}/', exist_ok=True)
for i in range(len(block_lootable)):
    process(pold_block_lootable[i], pnew_block_lootable[i])

## Recipes
item_recipe = ['axe', 'hoe', 'pickaxe', 'block', 'ingot', 'shovel', 'chest', 'ingot_blasting', 'sword', 'feet',
               'items_from_copper_block', 'helm', 'legs']
pold_item_recipe = [
    f'/Users/jayjay/programming/project/Minecraft/forge-tools/jsonmaker/data/MODID/recipes/RESOURCE_LOCATION/{b}.json'
    for b in item_recipe]
pnew_item_recipe = [f'{data_dir}/{modid}/recipes/{resourcelocation}/{b}.json' for b in item_recipe]

os.makedirs(f'{data_dir}/{modid}/recipes/{resourcelocation}/', exist_ok=True)
for i in range(len(item_recipe)):
    process(pold_item_recipe[i], pnew_item_recipe[i])
