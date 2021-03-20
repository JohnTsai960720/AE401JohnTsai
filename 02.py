from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
time.sleep(3)

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+100
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
x=x+100
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
z=z+100
mc.player.setTilePos(x,y,z)