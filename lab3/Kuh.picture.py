import graphics as gr
window 	= gr.GraphWin("Window",1000, 600)

sky = gr.Rectangle(gr.Point(0,0),gr.Point(1000,300))
sky.setFill("orange")
sky.draw(window)

grass = gr.Rectangle(gr.Point(0,300),gr.Point(1000,600))
grass.setFill("DarkOliveGreen4")
grass.draw(window)

palatka1 = gr.Polygon(gr.Point(2000/9,300),gr.Point(4000/9,300),gr.Point(3000/9,110))
palatka1.setFill("yellow")
palatka1.draw(window)

door1 = gr.Polygon(gr.Point(3000/9 + 35,300),gr.Point(3000/9 - 35,300),gr.Point(3000/9,150))
door1.setFill("black")
door1.draw(window)

palatka2 = gr.Polygon(gr.Point(500/7,300),gr.Point(2500/7,300),gr.Point(1500/7,150))
palatka2.setFill("yellow")
palatka2.draw(window)

door1 = gr.Polygon(gr.Point(1500/7 + 50,300),gr.Point(1500/7 - 50,300),gr.Point(1500/7,200))
door1.setFill("black")
door1.draw(window)

timber1 = gr.Polygon(gr.Point(450,500-20),gr.Point(425,475-20),gr.Point(550+50,400-20),gr.Point(575+50,425-20))
timber1.setFill("brown")
timber1.draw(window)

timber2 = gr.Polygon(gr.Point(550+50,500-20),gr.Point(575+50,475-20),gr.Point(450,400-20),gr.Point(425,425-20))
timber2.setFill("brown")
timber2.draw(window)

flame1 = gr.Polygon(gr.Point(450+40,400+15),gr.Point(475+40,400+15),gr.Point(475+40,350+15))
flame1.setFill("blue")
flame1.draw(window)

flame2 = gr.Polygon(gr.Point(550+40,400+15),gr.Point(525+40,400+15),gr.Point(525+40,350+15))
flame2.setFill("blue")
flame2.draw(window)

flame3 = gr.Polygon(gr.Point(460+40,425+15),gr.Point(540+40,425+15),gr.Point(500+40,325+15))
flame3.setFill("blue")
flame3.draw(window)

flame4 = gr.Polygon(gr.Point(480+40,415+15),gr.Point(520+40,415+15),gr.Point(500+40,355+15))
flame4.setFill("white")
flame4.draw(window)

sun = gr.Circle(gr.Point(750,150),50)
sun.setFill("yellow")
sun.draw(window)

#ща лучи пойдут

ray1 = gr.Polygon(gr.Point(730,100),gr.Point(770,100),gr.Point(750,80))
ray1.setFill("yellow")
ray1.draw(window)

ray2 = gr.Polygon(gr.Point(730,200),gr.Point(770,200),gr.Point(750,220))
ray2.setFill("yellow")
ray2.draw(window)

ray3 = gr.Polygon(gr.Point(800,130),gr.Point(800,170),gr.Point(820,150))
ray3.setFill("yellow")
ray3.draw(window)

ray4 = gr.Polygon(gr.Point(700,130),gr.Point(700,170),gr.Point(680,150))
ray4.setFill("yellow")
ray4.draw(window)

ray5 = gr.Polygon(gr.Point(750 - 35.5 + 14.2,150 - 35.5 - 14.2),gr.Point(750 - 35.5 - 14.2,150 - 35.5 + 14.2),gr.Point(750 - 35.5 - 14.2,150 - 35.5 - 14.2))
ray5.setFill("yellow")
ray5.draw(window)

ray6 = gr.Polygon(gr.Point(750 + 35.5 + 14.2,150 + 35.5 - 14.2),gr.Point(750 + 35.5 - 14.2,150 + 35.5 + 14.2),gr.Point(750 + 35.5 + 14.2,150 + 35.5 + 14.2))
ray6.setFill("yellow")
ray6.draw(window)

ray7 = gr.Polygon(gr.Point(750 - 35.5 - 14.2,150 + 35.5 - 14.2),gr.Point(750 - 35.5 + 14.2,150 + 35.5 + 14.2),gr.Point(750 - 35.5 - 14.2,150 + 35.5 + 14.2))
ray7.setFill("yellow")
ray7.draw(window)

ray8 = gr.Polygon(gr.Point(750 + 35.5 - 14.2,150 - 35.5 - 14.2),gr.Point(750 + 35.5 + 14.2,150 - 35.5 + 14.2),gr.Point(750 + 35.5 + 14.2,150 - 35.5 - 14.2))
ray8.setFill("yellow")
ray8.draw(window)

#кончились

carpet1 = gr.Polygon(gr.Point(275,420),gr.Point(245,390),gr.Point(305,330),gr.Point(335,360))
carpet1.setFill("orange")
carpet1.draw(window)

carpet2 = gr.Polygon(gr.Point(275,480),gr.Point(245,510),gr.Point(305,580),gr.Point(335,550))
carpet2.setFill("orange")
carpet2.draw(window)

carpet3 = gr.Polygon(gr.Point(725,420),gr.Point(755,390),gr.Point(695,330),gr.Point(665,360))
carpet3.setFill("orange")
carpet3.draw(window)

#ЩА ЕЛКА ПОЙДЕТ СМАРИ

stvol = gr.Polygon(gr.Point(500 + 4500/11,480),gr.Point(500+4000/11,480),gr.Point(500+4250/11,200))
stvol.setFill("#654321")
stvol.draw(window)

level1 = gr.Polygon(gr.Point(500 + 5000/11,430),gr.Point(500+3500/11,430),gr.Point(500+4250/11,350))
level1.setFill("forest green")
level1.draw(window)

level2 = gr.Polygon(gr.Point(500 + 4800/11,380),gr.Point(500+3700/11,380),gr.Point(500+4250/11,300))
level2.setFill("forest green")
level2.draw(window)

level3 = gr.Polygon(gr.Point(500 + 4600/11,330),gr.Point(500+3900/11,330),gr.Point(500+4250/11,250))
level3.setFill("forest green")
level3.draw(window)

level4 = gr.Polygon(gr.Point(500 + 4400/11,280),gr.Point(500+4100/11,280),gr.Point(500+4250/11,200))
level4.setFill("forest green")
level4.draw(window)

#Немного изменений

flame1 = gr.Polygon(gr.Point(450+10,400),gr.Point(475+10,400),gr.Point(475+10,350))
flame1.setFill("red")
flame1.draw(window)

flame3 = gr.Polygon(gr.Point(460+10,425),gr.Point(540+10,425),gr.Point(500+10,325))
flame3.setFill("red")
flame3.draw(window)

flame4 = gr.Polygon(gr.Point(480+10,415),gr.Point(520+10,415),gr.Point(500+10,355))
flame4.setFill("yellow")
flame4.draw(window)

sun = gr.Circle(gr.Point(500,150),50)
sun.setFill("red")
sun.draw(window)

#ща лучи пойдут

ray1 = gr.Polygon(gr.Point(480,100),gr.Point(520,100),gr.Point(500,80))
ray1.setFill("red")
ray1.draw(window)

ray2 = gr.Polygon(gr.Point(480,200),gr.Point(520,200),gr.Point(500,220))
ray2.setFill("red")
ray2.draw(window)

ray3 = gr.Polygon(gr.Point(550,130),gr.Point(550,170),gr.Point(570,150))
ray3.setFill("red")
ray3.draw(window)

ray4 = gr.Polygon(gr.Point(450,130),gr.Point(450,170),gr.Point(430,150))
ray4.setFill("red")
ray4.draw(window)

ray5 = gr.Polygon(gr.Point(500 - 35.5 + 14.2,150 - 35.5 - 14.2),gr.Point(500 - 35.5 - 14.2,150 - 35.5 + 14.2),gr.Point(500 - 35.5 - 14.2,150 - 35.5 - 14.2))
ray5.setFill("red")
ray5.draw(window)

ray6 = gr.Polygon(gr.Point(500 + 35.5 + 14.2,150 + 35.5 - 14.2),gr.Point(500 + 35.5 - 14.2,150 + 35.5 + 14.2),gr.Point(500 + 35.5 + 14.2,150 + 35.5 + 14.2))
ray6.setFill("red")
ray6.draw(window)

ray7 = gr.Polygon(gr.Point(500 - 35.5 - 14.2,150 + 35.5 - 14.2),gr.Point(500 - 35.5 + 14.2,150 + 35.5 + 14.2),gr.Point(500 - 35.5 - 14.2,150 + 35.5 + 14.2))
ray7.setFill("red")
ray7.draw(window)

ray8 = gr.Polygon(gr.Point(500 + 35.5 - 14.2,150 - 35.5 - 14.2),gr.Point(500 + 35.5 + 14.2,150 - 35.5 + 14.2),gr.Point(500 + 35.5 + 14.2,150 - 35.5 - 14.2))
ray8.setFill("red")
ray8.draw(window)

#кончились

carpet1 = gr.Polygon(gr.Point(275,420),gr.Point(245,390),gr.Point(305,330),gr.Point(335,360))
carpet1.setFill("orange")
carpet1.draw(window)

carpet2 = gr.Polygon(gr.Point(275,480),gr.Point(245,510),gr.Point(305,580),gr.Point(335,550))
carpet2.setFill("orange")
carpet2.draw(window)

carpet3 = gr.Polygon(gr.Point(725,420),gr.Point(755,390),gr.Point(695,330),gr.Point(665,360))
carpet3.setFill("orange")
carpet3.draw(window)

#ЩА ЕЛКА ПОЙДЕТ СМАРИ

stvol = gr.Polygon(gr.Point(500 + 4500/11,480),gr.Point(500+4000/11,480),gr.Point(500+4250/11,200))
stvol.setFill("#654321")
stvol.draw(window)

level1 = gr.Polygon(gr.Point(500 + 5000/11,430),gr.Point(500+3500/11,430),gr.Point(500+4250/11,350))
level1.setFill("forest green")
level1.draw(window)

level2 = gr.Polygon(gr.Point(500 + 4800/11,380),gr.Point(500+3700/11,380),gr.Point(500+4250/11,300))
level2.setFill("forest green")
level2.draw(window)

level3 = gr.Polygon(gr.Point(500 + 4600/11,330),gr.Point(500+3900/11,330),gr.Point(500+4250/11,250))
level3.setFill("forest green")
level3.draw(window)

level4 = gr.Polygon(gr.Point(500 + 4400/11,280),gr.Point(500+4100/11,280),gr.Point(500+4250/11,200))
level4.setFill("forest green")
level4.draw(window)

window.getMouse()
window.close()